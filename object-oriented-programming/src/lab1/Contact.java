package lab1;

import java.util.ArrayList;

public class Contact {
    private ArrayList<String> emails;
    private ArrayList<PhoneNumber> phoneNumbers;

    public Contact() {
        this.emails = new ArrayList<>();
        this.phoneNumbers = new ArrayList<>();
    }

    public ArrayList<String> getEmails() {
        return emails;
    }

    public ArrayList<PhoneNumber> getPhoneNumbers() {
        return phoneNumbers;
    }

    public void setEmails(ArrayList<String> emails) {
        this.emails = emails;
    }

    public void setPhoneNumbers(ArrayList<PhoneNumber> phoneNumbers) {
        this.phoneNumbers = phoneNumbers;
    }

    public void addEmail(String email) {
        this.emails.add(email);
    }

    public void addPhoneNumber(PhoneNumber phoneNumber) {
        this.phoneNumbers.add(phoneNumber);
    }
}
