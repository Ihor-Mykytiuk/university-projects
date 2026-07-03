#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <Windows.h>

using namespace std;
#define SIZE 10

struct Date {
    int day;
    int month;
    int year;
};


struct Passenger {
    int ticketCode;
    string lastName;
    int luggageCount;
    int luggageWeight;
    Date date;
};


void readPassengersData(Passenger passengers[]) {
    ifstream inputFile("passengers_data.txt");

    if (!inputFile.is_open()) {
        cout << "Помилка відкриття файлу" << endl;
        return;
    }

    for (int i = 0; i < SIZE; i++) {
        Date date;

        inputFile >> passengers[i].ticketCode 
            >> passengers[i].lastName 
            >> passengers[i].luggageCount 
            >> passengers[i].luggageWeight;
        inputFile >> date.year >> date.month >> date.day;
        passengers[i].date = date;
    }

    inputFile.close();
}

void printPassengersData(Passenger passengers[]) {
    cout << left << setw(13) << "Код білета" 
        << setw(20) << "Прізвище"
        << setw(18) << "Кількість багажу" 
        << setw(18) << "Вага багажу"
        << setw(12) << "Дата приїзду" << endl << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << left << setw(13) << passengers[i].ticketCode
            << setw(20) << passengers[i].lastName
            << setw(18) << passengers[i].luggageCount
            << setw(18) << passengers[i].luggageWeight;
        cout << right << setw(2) << setfill('0') << passengers[i].date.day << "."
            << setw(2) << setfill('0') << passengers[i].date.month << "." << setfill(' ')
            << left << setw(6) << passengers[i].date.year  << endl;
    }
}
void sortByTicket(Passenger passengers[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (passengers[j].ticketCode >= passengers[j + 1].ticketCode) {
                swap(passengers[j], passengers[j + 1]);
            }
        }
    }
}

void sortByDate(Passenger passengers[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            if (passengers[j].date.year < passengers[i].date.year ||
                (passengers[j].date.year == passengers[i].date.year && passengers[j].date.month < passengers[i].date.month) ||
                (passengers[j].date.year == passengers[i].date.year && passengers[j].date.month == passengers[i].date.month && passengers[j].date.day < passengers[i].date.day)) {
                swap(passengers[i], passengers[j]);
            }
        }
    }
}
void sortByLuggageWeightAndCount(Passenger passengers[]) {
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            if (passengers[j].luggageWeight < passengers[i].luggageWeight ||
                (passengers[j].luggageWeight == passengers[i].luggageWeight && passengers[j].luggageCount < passengers[i].luggageCount)) {
                swap(passengers[i], passengers[j]);
            }
        }
    }
}

int main() {
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);
    Passenger passengers[SIZE];
    readPassengersData(passengers);
    int choice;
    cout << "Дані в порядку створення: " << endl;
    printPassengersData(passengers);
    do {
        cout << "Виберіть тип впорядкування:" << endl;
        cout << "1. Впорядкування за кодом білета" << endl;
        cout << "2. Впорядкування за датою приїзду" << endl;
        cout << "3. Впорядкування за вагою та кількістю багажу" << endl;
        cout << "4. Вийти" << endl;

        cin >> choice;

        switch (choice) {
        case 0:
            system("cls");
            break;
        case 1:
            system("cls");
            cout << "1. Впорядкування за кодом білета" << endl;
            sortByTicket(passengers);
            printPassengersData(passengers);
            break;
        case 2:
            system("cls");
            cout << "2. Впорядкування за датою приїзду" << endl;
            sortByDate(passengers);
            printPassengersData(passengers);
            break;
        case 3:
            system("cls");
            cout << "3. Впорядкування за вагою та кількістю багажу" << endl;
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
