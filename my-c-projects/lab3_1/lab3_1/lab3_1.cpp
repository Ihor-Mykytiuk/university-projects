#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>
#define N 10

using namespace std;

void print_array(int arr[]) {
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
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - i - 1; j++) {          
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
        cout << i + 1 << " ітерація: " << endl;
        print_array(arr);
    }
}
void first_improve(int arr[]) {
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
        cout << i + 1 << " ітерація: " << endl;
        print_array(arr);
    }
}
void second_improve(int arr[]) {
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
        cout << i + 1 << " ітерація: " << endl;
        print_array(arr);
    }
}
void third_improve(int arr[]) {
    int high = 0, low = N - 1;
    while (high < low)
    {
        cout << high + 1 << " ітерація: " << endl;
        for (int i = high; i < low; i++) 
        {
            if (arr[i] > arr[i + 1]) 
            {
                swap(arr[i], arr[i + 1]);
            }
        }
        print_array(arr);
        low--; 
        for (int j = low; j > high; j--) 
        {
            if (arr[j] < arr[j - 1]) 
            {
                swap(arr[j], arr[j - 1]);
            }
        }
        print_array(arr);
        high++;
    }
}
void all_improve(int arr[]) {
    bool swapped;
    int lastSwap = N - 1;
    int high = 0, low = N - 1;
    int iteration = 0;
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
        iteration++;
        cout << "Ітерація " << iteration << " (зліва направо): ";
        print_array(arr); // виведення масиву після кожного проходу зліва направо
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
        iteration++;
        cout << "Ітерація " << iteration << " (справа наліво): ";
        print_array(arr); // виведення масиву після кожного проходу справа наліво
        if (!swapped) {
            break;
        }
    }
}
int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    int arr[N];
    generate_array(arr);
    cout << "Початковий масив: " << endl;
    print_array(arr);
    //cout << "Впорядкування бульбашкою" << endl;
    //bubble_sort(arr);
    //cout << "Впорядкування бульбашкою (перший варіант покращення)" << endl;
    //first_improve(arr);
    //cout << "Впорядкування бульбашкою (другий варіант покращення)" << endl;
    //second_improve(arr);
    //cout << "Впорядкування бульбашкою (третій варіант покращення)" << endl;
    //third_improve(arr);
    cout << "Шейкер-впорядкування(повна модифікація бульбашки)" << endl;
    all_improve(arr);
    return 0;
}