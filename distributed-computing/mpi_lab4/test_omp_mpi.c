#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <omp.h>
#include <time.h>

int main(int argc, char *argv[]) {
    int rank, size;
    long long int total_points = 10000000000; // 1 млрд точок
    long long int points_per_process;
    long long int local_hits = 0, global_hits = 0;
    int num_threads = 1;

    double t_start, t_end;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    points_per_process = total_points / size;

    // Ініціалізація генератора випадкових чисел
    unsigned int seed = time(NULL) + rank * 100;

    // Дізнаємося кількість потоків (тільки один раз)
    #pragma omp parallel
    {
        #pragma omp master
        num_threads = omp_get_num_threads();
    }

    if (rank == 0) {
        printf("Running with %d MPI processes, each using %d OpenMP threads.\n", size, num_threads);
        t_start = MPI_Wtime(); // Початок таймера
    }

    // Паралельне обчислення методом Монте-Карло
    #pragma omp parallel reduction(+:local_hits)
    {
        unsigned int tid = omp_get_thread_num();
        unsigned int local_seed = seed + tid;
        #pragma omp for
        for (long long int i = 0; i < points_per_process; i++) {
            double x = rand_r(&local_seed) / (double)RAND_MAX;
            double y = rand_r(&local_seed) / (double)RAND_MAX;
            if (x * x + y * y <= 1.0)
                local_hits++;
        }
    }

    // Збір результатів
    MPI_Reduce(&local_hits, &global_hits, 1, MPI_LONG_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        double pi = 4.0 * global_hits / total_points;
        t_end = MPI_Wtime(); // Кінець таймера
        printf("Estimated Pi = %.10f\n", pi);
        printf("Total execution time: %.3f seconds\n", t_end - t_start);
    }

    MPI_Finalize();
    return 0;
}
