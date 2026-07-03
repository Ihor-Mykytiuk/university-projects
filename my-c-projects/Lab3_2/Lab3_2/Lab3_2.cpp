#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#define N 10000*8

using namespace std;
double Th()
{
    SYSTEMTIME time;
    GetSystemTime(&time);
    double chas;
    chas = time.wHour * 60 * 60 * 1000 + time.wMinute * 60 * 1000 + time.wSecond * 1000 + time.wMilliseconds;
    return chas;
}
void printArray(int arr[]) {
    for (int i = 0; i < N; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
void generate_array(int arr[]) {
    for (int i = 0; i < N; i++) {
        arr[i] = rand() % 160 + 1;
    }
}
void bubble_sort(int arr[]) {
    double t0, t1, T;
    t0 = Th();
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    t1 = Th();
    T = (t1 - t0);
    cout << "Час роботи алгоритму: " << T << endl;
}
void first_improve(int arr[]) {
    double t0, t1, T;
    t0 = Th();
    bool swapped;
    for (int i = 0; i < N - 1; i++) {
        swapped = false;
        for (int j = 0; j < N - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
    t1 = Th();
    T = (t1 - t0);
    cout << "Час роботи алгоритму: " << T << endl;
}
void second_improve(int arr[]) {
    double t0, t1, T;
    t0 = Th();
    int limit = N - 1;
    int lastSwap = N - 1;
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < limit; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                lastSwap = j;
            }
        }
        limit = lastSwap;
    }
    t1 = Th();
    T = (t1 - t0);
    cout << "Час роботи алгоритму: " << T << endl;
}
void third_improve(int arr[]) {
    double t0, t1, T;
    t0 = Th();
    int high = 0, low = N - 1;
    while (high < low)
    {
        for (int i = high; i < low; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                swap(arr[i], arr[i + 1]);
            }
        }
        low--;
        for (int j = low; j > high; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                swap(arr[j], arr[j - 1]);
            }
        }
        high++;
    }
    t1 = Th();
    T = (t1 - t0);
    cout << "Час роботи алгоритму: " << T << endl;
}

void all_improve(int arr[]) {
    double t0, t1, T;
    t0 = Th();
    bool swapped;
    int lastSwap = N - 1;
    int high = 0;
    int low = N - 1;
    while (high < low) {
        swapped = false;
        for (int i = high; i < low; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
                lastSwap = i;
            }
        }
        low = lastSwap;
        if (!swapped) {
            break;
        }
        swapped = false;
        for (int j = low; j > high; j--) {
            if (arr[j] < arr[j - 1]) {
                swap(arr[j], arr[j - 1]);
                swapped = true;
                lastSwap = j;
            }
        }
        high = lastSwap;
        if (!swapped) {
            break;
        }
    }
    t1 = Th();
    T = (t1 - t0);
    cout << "Час роботи алгоритму: " << T << endl;
}
int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    int arr[N];
    int a;
    generate_array(arr);
    cout << "Кількість елементів масиву: " << N << endl;
    cout << "Виберіть метод сортування: " << endl;
    cout << "1. Впорядкування бульбашкою" << endl;
    cout << "2. Впорядкування бульбашкою (перший варіант покращення)" << endl;
    cout << "3. Впорядкування бульбашкою (другий варіант покращення)" << endl;
    cout << "4. Впорядкування бульбашкою (третій варіант покращення)" << endl;
    cout << "5. Шейкер-впорядкування (повна модифікація бульбашки)" << endl;
    cin >> a;
    switch (a)
    {
    case 1:
        bubble_sort(arr);
        break;
    case 2:
        first_improve(arr);
        break;
    case 3:
        second_improve(arr);
        break;
    case 4:
        third_improve(arr);
        break;
    case 5:
        all_improve(arr);
        break;
    }
    return 0;
}