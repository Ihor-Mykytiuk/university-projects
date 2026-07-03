package lab1;

import java.util.ArrayList;
import java.time.LocalDate;
public class Form {
    private static int count = 0;
    private int id;
    private String fullName;
    private LocalDate date;
    private ArrayList<Language> languages;
    private ArrayList<Hobby> hobbies;
    private Contact contact;
    private ArrayList<Expense> expenses;
    private float monthlyExpense;
    public Form(String fullName) {
        this.id = count++;
        this.fullName = fullName;
        this.date = LocalDate.now();
        this.languages = new ArrayList<>();
        this.hobbies = new ArrayList<>();
        this.contact = new Contact();
        this.expenses = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getFullName() {
        return fullName;
    }

    public LocalDate getDate() {
        return date;
    }

    public ArrayList<Language> getLanguages() {
        return languages;
    }

    public ArrayList<Hobby> getHobbies() {
        return hobbies;
    }

    public Contact getContact() {
        return contact;
    }

    public ArrayList<Expense> getExpenses() {
        return expenses;
    }

    public float getMonthlyExpense() {
        return monthlyExpense;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public void setLanguages(ArrayList<Language> languages) {
        this.languages = languages;
    }

    public void setHobbies(ArrayList<Hobby> hobbies) {
        this.hobbies = hobbies;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

    public void setExpenses(ArrayList<Expense> expenses) {
        this.expenses = expenses;
    }

    public void setMonthlyExpense(float monthlyExpense) {
        this.monthlyExpense = monthlyExpense;
    }

    public void addLanguage(Language language) {
        languages.add(language);
    }

    public void addHobby(Hobby hobby) {
        hobbies.add(hobby);
    }
    private float calculateMonthlyExpense() {
        float sum = 0;
        for (Expense expense : expenses) {
            sum += expense.getEstimatedAmount();
        }
        return sum;
    }
    public void addExpense(Expense expense) {
        expenses.add(expense);
        this.monthlyExpense = calculateMonthlyExpense();

    }
    public void addEmail(String email) {
        contact.addEmail(email);
    }

    public void addPhoneNumber(PhoneNumber phoneNumber) {
        contact.addPhoneNumber(phoneNumber);
    }
}
