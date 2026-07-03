#include <stdio.h>
#include <stdio.h>
#include <unistd.h> // в Linux
//#include <windows.h> // в Windows
#include <omp.h>
int main(int argc, char* argv[])
{
    double start_time, end_time, tick;
    start_time = omp_get_wtime();
    sleep(1.20); // cекунди
    end_time = omp_get_wtime();
    tick = omp_get_wtick();
    printf("Time %lf\n", end_time - start_time);
    printf("Timer %.12lf\n", tick);
}