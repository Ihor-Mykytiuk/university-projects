#include <stdio.h>
#include <omp.h>
int main()
{
    int rank, size;
    #pragma omp parallel
    {
        rank = omp_get_thread_num();
        size = omp_get_num_threads();
        printf("Thread %d of %d threads\n", rank, size);
    }
}