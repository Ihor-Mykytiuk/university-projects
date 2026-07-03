#include <iostream>
using namespace std;

int num_comparisons = 0;
int num_swaps = 0;

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void quickSort(int arr[], int left, int right) {
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];
   
    while (i <= j) {
        while (arr[i] < pivot) {
            i++;
            num_comparisons++;
        }

        while (arr[j] > pivot) {
            j--;
            num_comparisons++;
        }

        if (i <= j) {
            swap(arr[i], arr[j]);
            i++;
            j--;
            num_swaps += 2;
            cout << "Swap: " << endl;
            printArray(arr, 10);
        }
    }

    if (left < j) {
        quickSort(arr, left, j);
    }

    if (i < right) {
        quickSort(arr, i, right);
    }
}

int main() {
    int arr[] = { 60,43,41,44,55,30,29,40,80,19 };
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    cout << "Sorted array: "<<endl;
    printArray(arr, n);

    cout << "Number of comparisons: " << num_comparisons << endl;
    cout << "Number of swaps: " << num_swaps << endl;

    return 0;
}
