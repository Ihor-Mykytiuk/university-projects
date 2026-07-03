#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 13

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Визначення кількості сусідів для кожної вершини
    int neighbors_count[N] = {3, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    
    // Визначення сусідів для кожної вершини
    int neighbors[N][4] = {
        {1, 2, 3, -1},
        {0, 4, 5, 6}, 
        {0, 7, 8, 9},
        {0, 10, 11, 12},
        {1, -1, -1, -1},
        {1, -1, -1, -1},
        {1, -1, -1, -1},
        {2, -1, -1, -1},
        {2, -1, -1, -1},
        {2, -1, -1, -1},
        {3, -1, -1, -1},
        {3, -1, -1, -1},
        {3, -1, -1, -1}
    };

    MPI_Comm graph_comm;
    int* index = (int*)malloc(N * sizeof(int));
    int total_neighbors = 0;
    
    for (int i = 0; i < N; i++) {
        total_neighbors += neighbors_count[i];
        index[i] = total_neighbors;
    }
    
    int* edges = (int*)malloc(total_neighbors * sizeof(int));
    int edge_index = 0;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < neighbors_count[i]; j++) {
            edges[edge_index++] = neighbors[i][j];
        }
    }
    
    MPI_Graph_create(MPI_COMM_WORLD, N, index, edges, 0, &graph_comm);
    
    int num_neighbors;
    MPI_Graph_neighbors_count(graph_comm, rank, &num_neighbors);
    
    int* my_neighbors = (int*)malloc(num_neighbors * sizeof(int));
    MPI_Graph_neighbors(graph_comm, rank, num_neighbors, my_neighbors);
    
    printf("Process %d has %d neighbors: ", rank, num_neighbors);
    for (int i = 0; i < num_neighbors; i++) {
        printf("%d ", my_neighbors[i]);
    }
    printf("\n");
    
    free(index);
    free(edges);
    free(my_neighbors);
    MPI_Finalize();
    
    return 0;
}