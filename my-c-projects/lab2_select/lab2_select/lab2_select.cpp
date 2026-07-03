#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#define N 10000

using namespace std;

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

void selection_sort(int arr[], int& comp, int& swap) {
    for (int i = 0; i < N - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < N; j++) {
            comp++;
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap++;
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    double t0, t1, T;
    int comp = 0, swap = 0;
    int arr[N];
    generate_array(arr);
    t0 = Th();
    //cout << "Original Array:" << endl;
    //print_array(arr);
    selection_sort(arr, comp, swap);
    t1 = Th();
    T = (t1 - t0);
    //cout << "Sorted Array:" << endl;
    //print_array(arr);
    cout << "Кількість елементів, що сортуються: " << N << endl;
    cout << "Час роботи алгоритму: " << T << endl;
    cout << "Кількість порівнянь:" << endl;
    cout << "Фактична: " << comp << " " << "Розрахункова: " << int(0.5 * N * (N - 1)) << endl;
    cout << "Кількість перестановок:" << endl;
    cout << "Фактична: " << swap << " " << "Розрахункова (max): " << int(N - 1) << endl;
    return 0;
}
