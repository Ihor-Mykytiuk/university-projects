#include "mpi.h"
#include <iostream>
#include <cmath>
#include <limits> 
#include <chrono> 

int main(int argc, char *argv[]) {
    int procNum, procRank;
    double startTime = 0.0, endTime = 0.0;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &procNum);
    MPI_Comm_rank(MPI_COMM_WORLD, &procRank);

    if (procRank == 0) {
        startTime = MPI_Wtime();
    }

    int totalElements = 500000000LL;
    int elementsPerProcess = totalElements / procNum;
    
    double* localArray = new double[elementsPerProcess];

    for (int i = 0; i < elementsPerProcess; ++i) {
        int globalIndex = procRank * elementsPerProcess + i;
        localArray[i] = (globalIndex * cos(globalIndex * 2.0)) / 3.0;
    }

    
    double minPositive = std::numeric_limits<double>::max();
    double maxNegative = std::numeric_limits<double>::lowest();
    bool foundPositive = false;
    bool foundNegative = false;

    for (int i = 0; i < elementsPerProcess; ++i) {
        double val = localArray[i];
        if (val > 0 && val < minPositive) {
            minPositive = val;
            foundPositive = true;
        }
        if (val < 0 && val > maxNegative) {
            maxNegative = val;
            foundNegative = true;
        }
    }

    double localProduct = 1.0;
    if (foundPositive && foundNegative) {
        localProduct = minPositive * maxNegative;
    } else {
        if (!foundPositive) {
            std::cout << "Process " << procRank << ": No positive elements found in its fragment." << std::endl;
        }
        if (!foundNegative) {
            std::cout << "Process " << procRank << ": No negative elements found in its fragment." << std::endl;
        }
        localProduct = 0.0;
    }

    
    if (procRank != 0) {
        MPI_Send(&localProduct, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
    } else {
        double totalSum = localProduct;
        for (int i = 1; i < procNum; ++i) {
            double receivedProduct;
            MPI_Recv(&receivedProduct, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            totalSum += receivedProduct;
        }
        std::cout << "Сума добутків (Z2): " << totalSum << std::endl;
        endTime = MPI_Wtime();
        std::cout << "Час виконання: " << endTime - startTime << " секунд" << std::endl;
    }

    delete[] localArray;
    MPI_Finalize();
    return 0;
}
