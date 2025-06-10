#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>


double calculate_A(int i) {
    return sqrt(i + 1) / (tan(i + 2) + 3);
}

double find_min_positive(double *arr, int size) {
    double min = -1.0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > 0 && (min == -1.0 || arr[i] < min)) {
            min = arr[i];
        }
    }
    return min;
}

int main(int argc, char** argv) {
    int rank, size;
    long long n;
    double start_time, end_time;
    double min_value, total_sum;
    int done = 0;

    // Ініціалізація MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    while (!done) {
        if (rank == 0) {
            printf("Enter the size of the array (0 quits): ");
            fflush(stdout);

            if (scanf("%lld", &n) != 1) {
                printf("No number entered; quitting\n");
                n = 0;
            }
            start_time = MPI_Wtime();
        }

        MPI_Bcast(&n, 1, MPI_LONG_LONG, 0, MPI_COMM_WORLD);

        if (n == 0) {
            done = 1;
        } else {
            int num_elements_per_process = n / size;
            double *local_array = (double*) malloc(num_elements_per_process * sizeof(double));

            // Генерація фрагмента масиву
            for (int i = 0; i < num_elements_per_process; i++) {
                local_array[i] = calculate_A(rank * num_elements_per_process + i);
            }

            min_value = find_min_positive(local_array, num_elements_per_process);

            // Процес 0 збирає результати
            if (rank == 0) {
                total_sum = min_value;
                for (int i = 1; i < size; i++) {
                    double temp_min;
                    MPI_Recv(&temp_min, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
                    total_sum += temp_min;
                }

                end_time = MPI_Wtime();
                printf("Total sum of minimum positive elements: %f\n", total_sum);
                printf("Time taken: %f seconds\n", end_time - start_time);
            } else {
                // Відправка результатів процесу 0
                MPI_Send(&min_value, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
            }

            free(local_array);
        }

        MPI_Barrier(MPI_COMM_WORLD);
    }

    // Завершення роботи MPI
    MPI_Finalize();
    return 0;
}
