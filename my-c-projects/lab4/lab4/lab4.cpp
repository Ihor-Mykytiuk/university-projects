#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <Windows.h>

using namespace std;
#define SIZE 10
// Структура для дати
struct Date {
    int day;
    int month;
    int year;
};

// Структура для подорожнього
struct Passenger {
    int ticketCode;
    string lastName;
    int luggageCount;
    int luggageWeight;
    Date date;
};

// Функція для читання даних з файлу та запису їх у масив структур
void readPassengersData(Passenger passengers[]) {
    ifstream inputFile("passengers_data.txt");

    if (!inputFile.is_open()) {
        cout << "Помилка відкриття файлу" << endl;
        return;
    }

    for (int i = 0; i < SIZE; i++) {
        Date date;

        inputFile >> passengers[i].ticketCode >> passengers[i].lastName >> passengers[i].luggageCount >> passengers[i].luggageWeight;
        inputFile >> date.year >> date.month >> date.day;
        passengers[i].date = date;
    }

    inputFile.close();
}


void printPassengersData(Passenger passengers[]) {
    for (int i = 0; i < SIZE; i++) {
        cout << "Код білета: " << passengers[i].ticketCode << endl;
        cout << "Прізвище пасажира: " << passengers[i].lastName << endl;
        cout << "Кількість речей багажу: " << passengers[i].luggageCount << endl;
        cout << "Загальна вага багажу: " << passengers[i].luggageWeight << "кг" << endl;
        cout << "Дата: " << passengers[i].date.day << "." << passengers[i].date.month << "." << passengers[i].date.year << endl;
        cout << endl;
    }
}
//void printPassengersData(Passenger passengers[]) {
//    cout << left << setw(10) << "Ticket #" << setw(20) << "Surname"
//        << setw(10) << "Weight" << setw(10) << "Count"
//        << setw(12) << "Birth date" << endl;
//    for (int i = 0; i < SIZE; i++) {
//        cout << left << setw(10) << passengers[i].ticketCode
//            << setw(20) << passengers[i].lastName
//            << setw(10) << passengers[i].luggageWeight
//            << setw(10) << passengers[i].luggageCount
//            << setw(2) << passengers[i].date.day << "."
//            << setw(2) << passengers[i].date.month << "."
//            << setw(6) << passengers[i].date.year << "  "
//            << endl;
//    }
//}
void sortByTicket(Passenger passenger[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (passenger[j].ticketCode > passenger[j + 1].ticketCode) {
                swap(passenger[j], passenger[j + 1]);
            }
        }
    }
}
void sortByDate(Passenger passengers[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            // Порівнюємо дати двох подорожніх
            if (passengers[j].date.year < passengers[i].date.year ||
                (passengers[j].date.year == passengers[i].date.year && passengers[j].date.month < passengers[i].date.month) ||
                (passengers[j].date.year == passengers[i].date.year && passengers[j].date.month == passengers[i].date.month && passengers[j].date.day < passengers[i].date.day)) {
                // Якщо дата другого подорожнього менша за дату першого, то міняємо місцями
                Passenger temp = passengers[i];
                passengers[i] = passengers[j];
                passengers[j] = temp;
            }
        }
    }
}
void sortByLuggageWeightAndCount(Passenger passengers[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            // Порівнюємо вагу багажу двох подорожніх
            if (passengers[j].luggageWeight < passengers[i].luggageWeight ||
                (passengers[j].luggageWeight == passengers[i].luggageWeight && passengers[j].luggageCount < passengers[i].luggageCount)) {
                // Якщо вага багажу другого менша за вагу багажу першого, то міняємо місцями
                Passenger temp = passengers[i];
                passengers[i] = passengers[j];
                passengers[j] = temp;
            }
        }
    }
}
// Головна функція
int main() {
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
    Passenger passengers[SIZE];
    readPassengersData(passengers);
    int choice;

    do {      
        // Виводимо меню
        cout << "Виберіть тип сортування:" << endl;
        cout << "1. Сортування за кодом білета" << endl;
        cout << "2. Сортування за датою приїзду" << endl;
        cout << "3. Сортування за вагою та кількістю багажу" << endl;
        cout << "4. Вийти" << endl;
        // Зчитуємо вибір користувача
       
        cin >> choice;  

        switch (choice) {
        case 1:
            system("cls");
            sortByTicket(passengers);
            printPassengersData(passengers);
            break;
        case 2:
            system("cls");
            sortByDate(passengers);
            printPassengersData(passengers);
            break;
        case 3:
            system("cls");
            sortByLuggageWeightAndCount(passengers);
            printPassengersData(passengers);
            break;
        case 4:
            cout << "Вихід..." << endl;
            break;
        default:
            cout << "Невірний вибір. Спробуйте знову." << endl;
            break;
        }
    } while (choice != 4);
    

    return 0;
} 
