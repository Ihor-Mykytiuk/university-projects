package lab1;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        DBForm db = new DBForm();
        Form form1 = new Form("Ivanchuk Ivan Ivanovych");
        form1.addLanguage(new Language("Ukrainian", "С2", "Native"));
        form1.addLanguage(new Language("English", "B2", "Active learning"));
        form1.addHobby(new Hobby("Football", "5 years", 3));
        form1.addHobby(new Hobby("Learning English", "1 years", 5 ));
        form1.addEmail("ivan@gmail.com");
        form1.addPhoneNumber(new PhoneNumber("380123456789", "Kyivstar", 150));
        form1.addPhoneNumber(new PhoneNumber("380987654321", "Vodafone", 100));
        form1.addExpense(new Expense("Phone", 250));
        form1.addExpense(new Expense("Internet", 150));
        db.addForm(form1);

        Form form2 = new Form("Petrenko Petro Petrovych");
        form2.addLanguage(new Language("Ukrainian", "С2", "Native"));
        form2.addLanguage(new Language("German", "A1", "Active learning"));
        form2.addHobby(new Hobby("Watching series", "3 years", 1));
        form2.addHobby(new Hobby("Learning German", "1 moth", 5 ));
        form2.addEmail("petro@gmail.com");
        form2.addPhoneNumber(new PhoneNumber("380111111111", "Kyivstar", 175));
        form2.addExpense(new Expense("Phone", 175));
        form2.addExpense(new Expense("Restaurant", 500));
        db.addForm(form2);

        Form form3 = new Form("Vasilenko Vasyl Vasylovych");
        form3.addLanguage(new Language("Ukrainian", "С2", "Native"));
        form3.addLanguage(new Language("English", "С1", "Stopped learning"));
        form3.addLanguage(new Language("Spanish", "A2", "Active learning"));
        form3.addHobby(new Hobby("Playing guitar", "2 years", 3));
        form3.addHobby(new Hobby("Learning Spanish", "4 moth", 5 ));
        form3.addEmail("vasyl@gmail.com");
        form3.addPhoneNumber(new PhoneNumber("380222222222", "Kyivstar", 200));
        form3.addPhoneNumber(new PhoneNumber("380333333333", "Kyivstar", 150));
        form3.addExpense(new Expense("Phone", 350));
        form3.addExpense(new Expense("Food", 300));
        form3.addExpense(new Expense("Rent", 1000));
        db.addForm(form3);

        Form form4 = new Form("Pavlenko Pavlo Pavlovych");
        form4.addLanguage(new Language("Ukrainian", "С2", "Native"));
        form4.addEmail("pavlo@gmail.com");
        form4.addPhoneNumber(new PhoneNumber("380444444444", "Kyivstar", 100));
        form4.addExpense(new Expense("Phone", 100));
        db.addForm(form4);

        System.out.println("All languages: " + db.getAllLanguages());
        System.out.println("Students knowing English: " + db.getStudentsKnowingLanguage("English"));
        System.out.println("Students knowing English at B2 level: " + db.getStudentsKnowingLanguage("English", "B2"));
        System.out.println("Total phone fee for id2: " + db.getTotalPhoneFee(2));
        System.out.println("Get 2 subscribers with the highest phone fee: " + db.getMaxSubscribers(2));
        System.out.println("Get 2 subscribers with the lowest phone fee: " + db.getMinSubscribers(2));
        System.out.println("Get names of students with the highest and lowest expenses: " + db.getNameWithMinMaxExpense());
    }
}
