#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#define N 10

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

void insertion_sort(int arr[], int& comp, int& swap) {
    for (int i = 1; i < N; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            comp++;
            swap++;
            arr[j + 1] = arr[j];
            j--;
        }
        swap++;
        arr[j + 1] = key;
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
    //cout << "Original array: " << endl;;
    //print_array(arr);
    insertion_sort(arr, comp, swap);
   
    t1 = Th();
    T = (t1 - t0);
    //cout << "Sorted array: " << endl;
    //print_array(arr);
    cout << "Кількість елементів, що сортуються: " << N << endl;
    cout << "Час роботи алгоритму: " << T << endl;
    cout << "Кількість порівнянь:" << endl;
    cout << "Фактична: " << comp << " " << "Розрахункова (max): " << int(0.5 * (N * N + N)) << endl;
    cout << "Кількість перестановок:" << endl;
    cout << "Фактична: " << swap << " " << "Розрахункова (max): " << int(0.5 * (N * N + N)) << endl;
    return 0;
}
