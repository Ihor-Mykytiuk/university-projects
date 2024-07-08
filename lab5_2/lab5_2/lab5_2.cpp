#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#define N 100*8

using namespace std;

int num_swaps = 0;
int num_comparisons = 0;

double Th()
{
    SYSTEMTIME time;
    GetSystemTime(&time);
    double chas;
    chas = time.wHour * 60 * 60 * 1000 + time.wMinute * 60 * 1000 + time.wSecond * 1000 + time.wMilliseconds;
    return chas;
}

void generate_array(int arr[]) {
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        arr[i] = rand() % 100;  
    }
}
void print_array(int arr[]) {
    for (int i = 0; i < N; i++) {
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
            num_swaps+=2;
        }
    }
    if (left < j) {
        quickSort(arr, left, j);
    }
    if (i < right) {
        quickSort(arr, i, right);
    }
}

void merge(int a[], long left, long split, long right)
{
    long pos1 = left; 
    long pos2 = split + 1; 
    long pos3 = 0; 
    int* temp;
    temp = new int[right - left + 1];
    while (pos1 <= split && pos2 <= right)
    {
        if (a[pos1] < a[pos2]) {
            temp[pos3] = a[pos1];
            pos3++; pos1++;
        }
        else {
            temp[pos3] = a[pos2]; pos3 = pos3++; pos2++;
        }

        num_comparisons++;
    }
    while (pos1 <= split) 
    {
        temp[pos3] = a[pos1]; pos3++; pos1++;
        num_comparisons++;
    }
    while (pos2 <= right) 
    {
        temp[pos3] = a[pos2]; pos3++; pos2++;
        num_comparisons++;
    }
    for (pos3 = 0; pos3 < right - left + 1; pos3++) {
        a[left + pos3] = temp[pos3];

        num_swaps+=2;
    }
    delete[] temp;
}

void mergeSort(int a[], long left, long right) {
    long split; 
    if (left < right) 
    {
        split = (left + right) / 2;
        mergeSort(a, left, split); 
        mergeSort(a, split + 1, right); 
        merge(a, left, split, right); 
    }
}
int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    double t0, t1, T;
    int arr[N];
    generate_array(arr);
    t0 = Th();
    //quickSort(arr, 0, N - 1);
    mergeSort(arr, 0, N - 1);
    //print_array(arr);
    t1 = Th();
    T = (t1 - t0);
    cout << "Кількість елементів, що сортуються: " << N << endl;
    cout << "Час роботи алгоритму: " << T << endl;
    cout << "Кількість порівнянь: " << num_comparisons << endl;
    cout << "Кількість перестановок:"<< num_swaps << endl;

}