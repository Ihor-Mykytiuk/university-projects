#include <stdio.h>
#include <omp.h>

double f(double i) {
    return (i*i*i - i*i + 2) / (i + 0.5);
}

int main() {
    double a = 0.5;
    double b = 70.0;
    long long n = 950000000; // 9.5E8
    double h = (b - a) / n;
    double sum_seq = 0.0;
    double sum_omp = 0.0;

    // Послідовна версія
    double start_seq = omp_get_wtime();
    for (long long i = 0; i < n; i++) {
        double x = a + h * (i + 0.5);
        sum_seq += f(x);
    }
    double result_seq = h * sum_seq;
    double end_seq = omp_get_wtime();

    //  Паралельна версія (OpenMP)
    double start_omp = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum_omp)
    for (long long i = 0; i < n; i++) {
        double x = a + h * (i + 0.5);
        sum_omp += f(x);
    }
    double result_omp = h * sum_omp;
    double end_omp = omp_get_wtime();

    printf("Sequential Result:     %.10f\n", result_seq);
    printf("Sequential Time:       %.6f sec\n\n", end_seq - start_seq);

    printf("OpenMP Result:         %.10f\n", result_omp);
    printf("OpenMP Time:           %.6f sec\n\n", end_omp - start_omp);


    return 0;
}
