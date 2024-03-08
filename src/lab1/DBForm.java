package lab1;
import java.util.ArrayList;
import java.util.Collections;

public class DBForm {
    private ArrayList<Form> forms;
    public DBForm() {
        this.forms = new ArrayList<>();
    }

    public void addForm(Form form) {
        this.forms.add(form);
    }

    public ArrayList<Form> getForms() {
        return forms;
    }
    public void setForms(ArrayList<Form> forms) {
        this.forms = forms;
    }

    public ArrayList<String> getAllLanguages() {
        ArrayList<String> languages = new ArrayList<>();
        for (Form form : forms) {
            for (Language language : form.getLanguages()) {
                if (!languages.contains(language.getName())) {
                    languages.add(language.getName());
                }
            }
        }
        return languages;
    }
    public int getStudentsKnowingLanguage(String language) {
        int count = 0;
        for (Form form : forms) {
            for (Language lang : form.getLanguages()) {
                if (lang.getName().equals(language)) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
    public int getStudentsKnowingLanguage(String language, String proficiencyLevel) {
        int count = 0;
        for (Form form : forms) {
            for (Language lang : form.getLanguages()) {
                if (lang.getName().equals(language) && lang.getProficiencyLevel().equals(proficiencyLevel)) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
    public float getTotalPhoneFee(int id) {
        float sum = 0;
        Form form = null;
        for (Form f : forms) {
            if (f.getId() == id) {
                form = f;
            }
        }
        if (form == null) {
            return 0;
        }
        for (PhoneNumber phone : form.getContact().getPhoneNumbers()) {
            sum += phone.getMonthlyFee();
        }
        return sum;
    }
    private void sortByPhoneFee() {
        for (int i = 0; i < forms.size(); i++) {
            for (int j = 0; j < forms.size(); j++) {
                if (getTotalPhoneFee(forms.get(i).getId()) < getTotalPhoneFee(forms.get(j).getId())) {
                    Collections.swap(forms, i, j);
                }
            }
        }
    }
    public ArrayList<String> getMaxSubscribers(int N) {
        ArrayList<String> maxSubscribers = new ArrayList<>();
        sortByPhoneFee();
        for (int i = forms.size() - 1; i > forms.size() - 1 - N; i--) {
            maxSubscribers.add(forms.get(i).getFullName());
        }
        return maxSubscribers;
    }
    public ArrayList<String> getMinSubscribers(int N) {
        ArrayList<String> minSubscribers = new ArrayList<>();
        sortByPhoneFee();
        for (int i = 0; i < N; i++) {
            minSubscribers.add(forms.get(i).getFullName());
        }
        return minSubscribers;
    }
    public ArrayList<String> getNameWithMinMaxExpense() {
        String nameWithMaxExpense = "";
        String nameWithMinExpense = "";
        float max = 0;
        float min = Float.MAX_VALUE;
        for (Form form : forms) {
            if (form.getMonthlyExpense() > max) {
                max = form.getMonthlyExpense();
                nameWithMaxExpense = form.getFullName();
            }
            if (form.getMonthlyExpense() < min) {
                min = form.getMonthlyExpense();
                nameWithMinExpense = form.getFullName();
            }
        }
        ArrayList<String> result = new ArrayList<>();
        result.add(nameWithMinExpense);
        result.add(nameWithMaxExpense);
        return result;
    }
}
