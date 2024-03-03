package lab1;

import java.util.ArrayList;

public class Contact {
    private ArrayList<String> emails;
    private ArrayList<PhoneNumber> phoneNumbers;

    public Contact(ArrayList<String> emails, ArrayList<PhoneNumber> phoneNumbers) {
        this.emails = emails;
        this.phoneNumbers = phoneNumbers;
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


}
