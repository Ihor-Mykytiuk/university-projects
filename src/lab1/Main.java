package lab1;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        DBForm db = new DBForm();
        Form form1 = new Form("Микитюк Ігор Вікторович");
        form1.addLanguage(new Language("English", "Native", "Active"));
        form1.addLanguage(new Language("Ukrainian", "Native", "Active"));

        form1.addExpense(new Expense("Food", 1000));
        form1.addExpense(new Expense("Transport", 500));

        form1.addEmail("igor14vn@gmail.com");
        form1.addEmail("adsdsa");

        form1.addPhoneNumber(new PhoneNumber("0682538722", "Kyivstar", 150));
        db.addForm(form1);

        Form form2 = new Form("Петренко Олександр Вікторович");
        form2.addLanguage(new Language("English", "Intermediate", "Active"));
        form2.addLanguage(new Language("Ukrainian", "Intermediate", "Active"));

        form2.addExpense(new Expense("Food", 1000));
        form2.addExpense(new Expense("Transport", 500));

        form2.addEmail("dssd");
        form2.addEmail("adsdsa");

        form2.addPhoneNumber(new PhoneNumber("0682538722", "Kyivstar", 49));
        form2.addPhoneNumber(new PhoneNumber("0682538722", "Kyivstar", 100));

        db.addForm(form2);

        Form form3 = new Form("Іванчук Іван Іванович");
        form3.addLanguage(new Language("French", "Intermediate", "Active"));
        form3.addLanguage(new Language("German", "Native", "Active"));

        form3.addExpense(new Expense("Clothes", 1000));
        form3.addExpense(new Expense("Car", 3000));
        form3.addExpense(new Expense("Restourant", 300));

        form3.addEmail("ivan@gmail.com");

        form3.addPhoneNumber(new PhoneNumber("0682538722", "Kyivstar", 100));
        form3.addPhoneNumber(new PhoneNumber("0682538722", "Kyivstar", 500));
        db.addForm(form3);


    }
}
