#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int size, rank;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Топологія гіперкуба 2-го порядку, неперіодичний
    int ndims = 2;
    int dims[2] = {2, 2};  
    int periods[2] = {0, 0};
    int reorder = 0;  

    MPI_Comm cart_comm;
    MPI_Cart_create(MPI_COMM_WORLD, ndims, dims, periods, reorder, &cart_comm);

    // Координати кожного процесу
    int coords[2];
    MPI_Cart_coords(cart_comm, rank, ndims, coords);
    printf("Процес %d має координати (%d, %d)\n", rank, coords[0], coords[1]);
    int rank_check;
    MPI_Cart_rank(cart_comm, coords, &rank_check);

    // Перевірка правильності номера процесу
    if (rank != rank_check) {
        printf("Помилка: координаті не відповідає номер процесу (%d, %d)\n", coords[0], coords[1]);
    }

    srand(time(NULL) + rank);  
    int data[10];
    for (int i = 0; i < 10; i++) {
        data[i] = rand() % 100;  
    }

    printf("Процес %d, початковий масив: ", rank);
    for (int i = 0; i < 10; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    // Зсув збільшення координат по X
    int source, dest;
    MPI_Cart_shift(cart_comm, 0, 1, &source, &dest); 

    int recv_data[10];

    if (dest != MPI_PROC_NULL) {
        MPI_Send(data, 10, MPI_INT, dest, 0, cart_comm);
    }
    if (source != MPI_PROC_NULL) {
        MPI_Recv(recv_data, 10, MPI_INT, source, 0, cart_comm, MPI_STATUS_IGNORE);

        printf("Процес %d отримав від процесу %d: ", rank, source);
        for (int i = 0; i < 10; i++) {
            printf("%d ", recv_data[i]);
        }
        printf("\n");
    }

    MPI_Finalize();
    return 0;
}
