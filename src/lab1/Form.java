package lab1;

import java.util.ArrayList;
import java.time.LocalDate;
public class Form {
    private int id;
    private String fullName;
    private LocalDate date;
    private ArrayList<Language> languages;
    private ArrayList<Hobby> hobbies;
    private Contact contact;
    private ArrayList<Expense> expenses;
    private float monthlyExpense;

    public Form(int id, String fullName, LocalDate date, ArrayList<Language> languages, ArrayList<Hobby> hobbies, Contact contact, ArrayList<Expense> expenses, float monthlyExpense) {
        this.id = id;
        this.fullName = fullName;
        this.date = date;
        this.languages = languages;
        this.hobbies = hobbies;
        this.contact = contact;
        this.expenses = expenses;
        this.monthlyExpense = monthlyExpense;
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

    public void addExpense(Expense expense) {
        expenses.add(expense);
    }

}
