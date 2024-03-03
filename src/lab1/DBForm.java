package lab1;
import java.util.ArrayList;

public class DBForm {
    private ArrayList<Form> forms;

        public DBForm() {
            forms = new ArrayList<Form>();
        }

        public void addForm(Form form) {
            forms.add(form);
        }

        public ArrayList<Form> getForms() {
            return forms;
        }

        public void setForms(ArrayList<Form> forms) {
            this.forms = forms;
        }
}
