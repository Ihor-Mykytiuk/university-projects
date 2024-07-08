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

void bubble_sort(int arr[], int &comp, int &swaps) {
    int temp;
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N-i - 1; j++) {
            comp++;
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
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
    //cout << "Original array: " <<endl;;
    //print_array(arr);
    bubble_sort(arr, comp, swap);
    t1 = Th();
    T = (t1 - t0);
    //cout << "Sorted array: " << endl;
    //print_array(arr);
    cout << "Кількість елементів, що сортуються: " << N << endl;
    cout << "Час роботи алгоритму: " << T << endl;
    cout << "Кількість порівнянь:" << endl;
    cout << "Фактична: " << comp << " " << "Розрахункова: " << int(0.5 * N * (N - 1)) << endl;
    cout << "Кількість перестановок:" << endl;
    cout << "Фактична: " << swap << " " << "Розрахункова (max): " << int(3/2. * (N*N - N)) << endl;
    return 0;
}
