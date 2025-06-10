#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

double f(double i) {
    return (i * i * i - i * i + 2) / (i + 0.5);
}

int main(int argc, char* argv[]) {
    int rank, size;
    double a = 0.5;
    double b = 70.0;
    long long n = 950000000; // 9.5E8
    double h = (b - a) / n;
    double local_sum = 0.0, total_sum = 0.0;
    double start_time, end_time;

    // Ініціалізація MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank); // номер процесу
    MPI_Comm_size(MPI_COMM_WORLD, &size); // кількість процесів


    if (rank == 0)
        start_time = MPI_Wtime();

    // Розрахунок діапазону ітерацій для кожного процесу
    long long chunk = n / size;
    long long start = rank * chunk;
    long long end = (rank == size - 1) ? n : start + chunk;


    for (long long i = start; i < end; i++) {
        double x = a + h * (i + 0.5);
        local_sum += f(x);
    }


    MPI_Reduce(&local_sum, &total_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        double result = h * total_sum;
        end_time = MPI_Wtime();

        printf("MPI Result:            %.10f\n", result);
        printf("MPI Time:              %.6f sec\n", end_time - start_time);
    }

    MPI_Finalize();
    return 0;
}
