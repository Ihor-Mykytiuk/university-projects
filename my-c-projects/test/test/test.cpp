#include <iostream>
#include <Windows.h>

using namespace std;
struct Node {
	int item;
	Node* next;
};
Node* head = nullptr;


struct Node2 {
	int item;
	Node2* next;
	Node2* prev;
};
Node2* head2 = nullptr;
Node2* tail2 = nullptr;
void display() {
	Node2* current = head2;
	while (current != nullptr) {
		cout << current->item << " -> ";
		current = current->next;
	}
	cout << "null" << endl;
}
void displayR() {
	Node2* current = tail2;
	while (current != nullptr) {
		cout << current->item << " -> ";
		current = current->prev;
	}
	cout << "null" << endl;
}
void addElement(int data) {
	Node* newNode = new Node;
	newNode->item = data;
	newNode->next = nullptr;
	if (head == nullptr) {
		head = newNode;
	}
	else {
		Node* current = head;
		while (current->next != nullptr) {
			current = current->next;
		}
		current->next = newNode;
	}
}


void addElement2(int data) {
	Node2* newNode = new Node2;
	newNode->item = data;
	newNode->next = nullptr;
	newNode->prev = nullptr;

	if (head2 == nullptr) {
		head2 = newNode;
		tail2 = newNode;

	}
	else {
		tail2->next = newNode;
		newNode->prev = tail2;
		tail2 = newNode;
	}
}

void addByPos(int pos, int data) {
		
	Node* newNode = new Node;
	newNode->item = data;
	if (pos == 0) {
		newNode->next = head;
		head = newNode;
	}
	else {
		Node* current = head;
		for (int i = 1; i < pos; i++) {
			current = current->next;
		}
		newNode->next = current->next;
		current->next = newNode;
	}
}
void addElement2(int pos, int data) {
	Node2* newNode = new Node2;
	newNode->item = data;
	Node2* current = head2;
	pos--;
	for (int i = 1; i < pos; i++) {
		current = current->next;
	}
	newNode->next = current->next;
	current->next->prev = newNode; // Додали рядок для оновлення посилання на попередній елемент
	newNode->prev = current; // Додали рядок для оновлення посилання на попередній елемент
	current->next = newNode;
}
void addElement2_upd(int pos, int data) {
	Node2* newNode = new Node2;
	newNode->item = data;
	Node2* current = head2;
	newNode->next = nullptr;
	newNode->prev = nullptr;

	pos--;
	for (int i = 1; i < pos; i++) {
		current = current->next;
	}
	if (pos == 0) {
		if (head2 == nullptr) {
			head2 = newNode;
			tail2 = newNode;
		}
		else {
			newNode->next = head2;
			head2->prev = newNode;
			head2 = newNode;
		}
	}
	else if (current->next == nullptr) {
		addElement2(data);
	}
	else {
		newNode->next = current->next;
		current->next->prev = newNode; // Додали рядок для оновлення посилання на попередній елемент
		newNode->prev = current; // Додали рядок для оновлення посилання на попередній елемент
		current->next = newNode;
	}
}
void addElement2R(int pos, int data) {
	Node2* newNode = new Node2;
	newNode->item = data;
	Node2* current = tail2;
	for (int i = 1; i < pos - 1; i++) {
		current = current->prev;
	}
	newNode->prev = current->prev;
	current->prev->next = newNode; 
	newNode->next = current; 
	current->prev = newNode;
}
void addElementBeforeK(int k, int data) {
	Node2* newNode = new Node2;
	newNode->item = data;
	newNode->next = nullptr;
	newNode->prev = nullptr;

	if (head2 == nullptr) {
		head2 = newNode;
		tail2 = newNode;
	}
	else {
		Node2* current = head2;
		int pos = 1;
		while (current != nullptr && pos < k-1) {
			current = current->next;
			pos++;
		}
		if (current != nullptr) {
			if (current == head2) {
				newNode->next = head2;
				head2->prev = newNode;
				head2 = newNode;
			}
			else {
				newNode->next = current;
				newNode->prev = current->prev;
				current->prev->next = newNode;
				current->prev = newNode;
			}
		}
		else {
			tail2->next = newNode;
			newNode->prev = tail2;
			tail2 = newNode;
		}
	}
}
int main() {
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	int size;
	int data;

	cout << "Введіть кількість елементів для списку: "<<endl;
	cin >> size;
	for (int i = 0; i < size; i++) {
		cout << "Введіть " << i << " елемент: ";
		cin >> data;
		addElement2(data);
	}
	display();
	cout << "Reverse: " << endl;
	displayR();
	cout << "Введіть позицію для вставки: " << endl;
	int pos;
	cin >> pos;
	cout << "Введіть елемент: ";
	cin >> data;
	addElement2_upd(pos, data);
	display();

	displayR();
}