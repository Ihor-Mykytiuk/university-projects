package lab1;

public class Hobby {
    private String name;
    private String duration;
    private int usefulnessScore;

    public Hobby(String name, String duration, int usefulnessScore) {
        this.name = name;
        this.duration = duration;
        this.usefulnessScore = usefulnessScore;
    }

    public String getName() {
        return name;
    }

    public String getDuration() {
        return duration;
    }

    public int getUsefulnessScore() {
        return usefulnessScore;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public void setUsefulnessScore(int usefulnessScore) {
        this.usefulnessScore = usefulnessScore;
    }
}
