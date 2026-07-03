#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>
#include <string.h>
#define N 4  // розмір глобальної матриці

void init_matrix(double *mat, int n) {
    for (int i = 0; i < n * n; ++i) {
        mat[i] = (double)(i + 1);
    }
}

void print_matrix(double *mat, int n, const char *name) {
    printf("%s:\n", name);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            printf("%6.1f ", mat[i * n + j]);
        }
        printf("\n");
    }
    printf("\n");
}

void multiply_block(double *A, double *B, double *C, int block_size) {
    for (int i = 0; i < block_size; ++i)
        for (int j = 0; j < block_size; ++j)
            for (int k = 0; k < block_size; ++k)
                C[i * block_size + j] += A[i * block_size + k] * B[k * block_size + j];
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int q = (int)sqrt(size);
    if (q * q != size || N % q != 0) {
        if (rank == 0)
            printf("Кількість процесів має бути квадратом і ділити N націло.\n");
        MPI_Finalize();
        return -1;
    }

    int block_size = N / q;
    int dims[2] = {q, q}, periods[2] = {1, 1};
    MPI_Comm grid_comm, row_comm;
    int coords[2];

    MPI_Cart_create(MPI_COMM_WORLD, 2, dims, periods, 1, &grid_comm);
    MPI_Cart_coords(grid_comm, rank, 2, coords);
    MPI_Comm_split(grid_comm, coords[0], coords[1], &row_comm);

    double *A_full = NULL, *B_full = NULL, *C_full = NULL;
    if (rank == 0) {
        A_full = malloc(N * N * sizeof(double));
        B_full = malloc(N * N * sizeof(double));
        C_full = calloc(N * N, sizeof(double));
        init_matrix(A_full, N);
        init_matrix(B_full, N);
    }

    double *A_block = malloc(block_size * block_size * sizeof(double));
    double *B_block = malloc(block_size * block_size * sizeof(double));
    double *C_block = calloc(block_size * block_size, sizeof(double));
    double *A_temp = malloc(block_size * block_size * sizeof(double));

    // Розсилка блоків вручну
    if (rank == 0) {
        for (int p = 0; p < size; ++p) {
            int proc_coords[2] = {p / q, p % q};
            double *a_buf = malloc(block_size * block_size * sizeof(double));
            double *b_buf = malloc(block_size * block_size * sizeof(double));
            for (int i = 0; i < block_size; ++i)
                for (int j = 0; j < block_size; ++j) {
                    int gi = proc_coords[0] * block_size + i;
                    int gj = proc_coords[1] * block_size + j;
                    a_buf[i * block_size + j] = A_full[gi * N + gj];
                    b_buf[i * block_size + j] = B_full[gi * N + gj];
                }

            if (p == 0) {
                memcpy(A_block, a_buf, block_size * block_size * sizeof(double));
                memcpy(B_block, b_buf, block_size * block_size * sizeof(double));
            } else {
                MPI_Send(a_buf, block_size * block_size, MPI_DOUBLE, p, 0, MPI_COMM_WORLD);
                MPI_Send(b_buf, block_size * block_size, MPI_DOUBLE, p, 1, MPI_COMM_WORLD);
            }
            free(a_buf); free(b_buf);
        }
    } else {
        MPI_Recv(A_block, block_size * block_size, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        MPI_Recv(B_block, block_size * block_size, MPI_DOUBLE, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }

    // Алгоритм Фокса
    for (int stage = 0; stage < q; ++stage) {
        int bcast_root = (coords[0] + stage) % q;
        if (bcast_root == coords[1]) {
            memcpy(A_temp, A_block, block_size * block_size * sizeof(double));
        }
        MPI_Bcast(A_temp, block_size * block_size, MPI_DOUBLE, bcast_root, row_comm);
        multiply_block(A_temp, B_block, C_block, block_size);

        int src, dst;
        MPI_Cart_shift(grid_comm, 1, -1, &src, &dst);
        MPI_Sendrecv_replace(B_block, block_size * block_size, MPI_DOUBLE, dst, 0, src, 0, grid_comm, MPI_STATUS_IGNORE);
    }

    // Збір результату
    if (rank == 0) {
        for (int p = 0; p < size; ++p) {
            int proc_coords[2] = {p / q, p % q};
            double *recv_buf = (p == 0) ? C_block : malloc(block_size * block_size * sizeof(double));
            if (p != 0)
                MPI_Recv(recv_buf, block_size * block_size, MPI_DOUBLE, p, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            for (int i = 0; i < block_size; ++i)
                for (int j = 0; j < block_size; ++j) {
                    int gi = proc_coords[0] * block_size + i;
                    int gj = proc_coords[1] * block_size + j;
                    C_full[gi * N + gj] = recv_buf[i * block_size + j];
                }
            if (p != 0) free(recv_buf);
        }

        print_matrix(A_full, N, "Matrix A");
        print_matrix(B_full, N, "Matrix B");
        print_matrix(C_full, N, "Matrix C = A x B");
        free(A_full); free(B_full); free(C_full);
    } else {
        MPI_Send(C_block, block_size * block_size, MPI_DOUBLE, 0, 2, MPI_COMM_WORLD);
    }

    free(A_block); free(B_block); free(C_block); free(A_temp);
    MPI_Comm_free(&row_comm);
    MPI_Comm_free(&grid_comm);
    MPI_Finalize();
    return 0;
}
