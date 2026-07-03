#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

double calculate_Aij(int i, int j) {
    double numerator = fabs(sin(i) + pow(cos(i), 2));
    double denominator = 6.5 + atan(i);
    return numerator / denominator;
}

double calculate_Bij(int i, int j) {
    if (i <= 0) {
        return 0.0;
    } else {
        return log10(i) + 0.78 * tan(j);
    }
}

double calculate_testij(int i, int j) {
    return (double)(i + j);
}

void print_matrix(const char* name, double* matrix, int size) {
    printf("Матриця %s (%dx%d):\n", name, size, size);
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%8.4f ", matrix[i * size + j]);
        }
        printf("\n");
    }
    printf("\n");
}

void initialize_matrix_zeros(double* matrix, int size) {
    for (int i = 0; i < size * size; i++) {
        matrix[i] = 0.0;
    }
}

void multiply_blocks(double* A, double* B, double* C, int block_size) {
    for (int i = 0; i < block_size; i++) {
        for (int j = 0; j < block_size; j++) {
            for (int k = 0; k < block_size; k++) {
                C[i * block_size + j] += A[i * block_size + k] * B[k * block_size + j];
            }
        }
    }
}

void copy_block(double* full_matrix, double* block, int N, int block_size, int row_block, int col_block) {
    for (int i = 0; i < block_size; i++) {
        for (int j = 0; j < block_size; j++) {
            int global_row = row_block * block_size + i;
            int global_col = col_block * block_size + j;
            block[i * block_size + j] = full_matrix[global_row * N + global_col];
        }
    }
}

void print_matrix_parts(const char* name, double* matrix, int size, int subsize) {
    printf("Матриця %s — кути (%dx%d):\n", name, subsize, subsize);

    printf("\nЛівий верхній кут:\n");
    for (int i = 0; i < subsize; i++) {
        for (int j = 0; j < subsize; j++) {
            printf("%8.4f ", matrix[i * size + j]);
        }
        printf("\n");
    }

    printf("\nПравий нижній кут:\n");
    for (int i = size - subsize; i < size; i++) {
        for (int j = size - subsize; j < size; j++) {
            printf("%8.4f ", matrix[i * size + j]);
        }
        printf("\n");
    }

    printf("\n");
}


int main(int argc, char **argv) {
    int rank, size;
    double start_time, end_time;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Розмір матриці (N x N)
    int N = 1200;

    
    int grid_size = (int)sqrt(size);
    if (grid_size * grid_size != size) {
        if (rank == 0) {
            printf("Кількість процесів повинна бути квадратом цілого числа\n");
        }
        MPI_Finalize();
        return 1;
    }

    if (N % grid_size != 0) {
        if (rank == 0) {
            printf("Розмір матриці (%d) повинен бути кратним розміру сітки (%d)\n", N, grid_size);
        }
        MPI_Finalize();
        return 1;
    }

    // Розмір локального блоку матриці
    int block_size = N / grid_size;

    if (rank == 0) {
        printf("Параметри програми:\n");
        printf("- Розмір матриці: %d x %d\n", N, N);
        printf("- Кількість процесів: %d\n", size);
        printf("- Розмір сітки: %d x %d\n", grid_size, grid_size);
        printf("- Розмір локального блоку: %d x %d\n", block_size, block_size);
    }

    // Топологія сітки
    int ndims = 2;
    int dims[2] = {grid_size, grid_size};
    int periods[2] = {1, 1};
    int reorder = 0;
    MPI_Comm cart_comm;
    MPI_Cart_create(MPI_COMM_WORLD, ndims, dims, periods, reorder, &cart_comm);

    // Визначення координат процесу в сітці
    int coords[2];
    MPI_Cart_coords(cart_comm, rank, 2, coords);
    
    // Локальні блоки матриць
    double* A_block = NULL;
    double* B_block = NULL;

    start_time = MPI_Wtime();
    if (rank == 0) {
        double* A = malloc(N * N * sizeof(double));
        double* B = malloc(N * N * sizeof(double));
    
        // Заповнення матриць
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i * N + j] = calculate_Aij(i, j);
                B[i * N + j] = calculate_Bij(i, j);
            }
        }
    
        
        
        // Розсилка блоків
        for (int proc = 0; proc < size; proc++) {
            int coords[2];
            MPI_Cart_coords(cart_comm, proc, ndims, coords);
            int i = coords[0], j = coords[1];
    
            double* tempA = malloc(block_size * block_size * sizeof(double));
            double* tempB = malloc(block_size * block_size * sizeof(double));
            copy_block(A, tempA, N, block_size, i, j);
            copy_block(B, tempB, N, block_size, i, j);
    
            if (proc == 0) {
                A_block = tempA;
                B_block = tempB;
            } else {
                MPI_Send(tempA, block_size * block_size, MPI_DOUBLE, proc, 0, cart_comm);
                MPI_Send(tempB, block_size * block_size, MPI_DOUBLE, proc, 1, cart_comm);
                free(tempA);
                free(tempB);
            }
        }
        free(A);
        free(B);
    } else {
        A_block = malloc(block_size * block_size * sizeof(double));
        B_block = malloc(block_size * block_size * sizeof(double));
        MPI_Recv(A_block, block_size * block_size, MPI_DOUBLE, 0, 0, cart_comm, MPI_STATUS_IGNORE);
        MPI_Recv(B_block, block_size * block_size, MPI_DOUBLE, 0, 1, cart_comm, MPI_STATUS_IGNORE);
    }

    // Комунікатори для рядків і стовпців
    MPI_Comm row_comm, col_comm;

    int remain_dims_row[2] = {0, 1}; // залишаємо тільки стовпці (процеси в рядку)
    MPI_Cart_sub(cart_comm, remain_dims_row, &row_comm);

    int remain_dims_col[2] = {1, 0}; // залишаємо тільки рядки (тобто процеси в стовпці)
    MPI_Cart_sub(cart_comm, remain_dims_col, &col_comm);

    double* C_block = malloc(block_size * block_size * sizeof(double));
    initialize_matrix_zeros(C_block, block_size);

    double* A_temp = malloc(block_size * block_size * sizeof(double));
    for (int k = 0; k < grid_size; k++) {
        int root = (coords[0] + k) % grid_size;

        if (coords[1] == root) {
            for (int i = 0; i < block_size * block_size; i++) {
                A_temp[i] = A_block[i];
            }
        }

        MPI_Bcast(A_temp, block_size * block_size, MPI_DOUBLE, root, row_comm);

        multiply_blocks(A_temp, B_block, C_block, block_size);

        // Зсув B вгору
        int src, dst;
        MPI_Cart_shift(col_comm, 0, -1, &src, &dst);
        MPI_Sendrecv_replace(B_block, block_size * block_size, MPI_DOUBLE, dst, 0, src, 0, col_comm, MPI_STATUS_IGNORE);
    }

    free(A_temp);

    // Збір результатів
    if (rank == 0) {
        double* C = malloc(N * N * sizeof(double));
        for (int proc = 0; proc < size; proc++) {
            int coords[2];
            MPI_Cart_coords(cart_comm, proc, ndims, coords);
            int i = coords[0], j = coords[1];
            if (proc == 0) {
                for (int ii = 0; ii < block_size; ii++) {
                    for (int jj = 0; jj < block_size; jj++) {
                        int global_i = i * block_size + ii;
                        int global_j = j * block_size + jj;
                        C[global_i * N + global_j] = C_block[ii * block_size + jj];
                    }
                }
            } else {
                double* temp = malloc(block_size * block_size * sizeof(double));
                MPI_Recv(temp, block_size * block_size, MPI_DOUBLE, proc, 2, cart_comm, MPI_STATUS_IGNORE);
                for (int ii = 0; ii < block_size; ii++) {
                    for (int jj = 0; jj < block_size; jj++) {
                        int global_i = i * block_size + ii;
                        int global_j = j * block_size + jj;
                        C[global_i * N + global_j] = temp[ii * block_size + jj];
                    }
                }
                free(temp);
            }
        }
    
        free(C);
    } else {
        MPI_Send(C_block, block_size * block_size, MPI_DOUBLE, 0, 2, cart_comm);
    }
    end_time = MPI_Wtime();
    if (rank == 0) {
        printf("\n----------------------------------------\n");
        printf("Загальний час виконання: %.6f секунд\n", end_time - start_time);
        printf("----------------------------------------\n");
    }
    
    MPI_Finalize();
    return 0;
}