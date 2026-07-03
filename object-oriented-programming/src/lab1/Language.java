package lab1;

public class Language {
    private String name;
    private String proficiencyLevel;
    private String status;

    public Language(String name, String proficiencyLevel, String status) {
        this.name = name;
        this.proficiencyLevel = proficiencyLevel;
        this.status = status;
    }

    public String getName() {
        return name;
    }

    public String getProficiencyLevel() {
        return proficiencyLevel;
    }

    public String getStatus() {
        return status;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setProficiencyLevel(String proficiencyLevel) {
        this.proficiencyLevel = proficiencyLevel;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
