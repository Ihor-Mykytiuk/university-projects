package lab1;

public class Expense {
    private String category;
    private float estimatedAmount;

    public Expense(String category, float estimatedAmount) {
        this.category = category;
        this.estimatedAmount = estimatedAmount;
    }

    public String getCategory() {
        return category;
    }

    public float getEstimatedAmount() {
        return estimatedAmount;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public void setEstimatedAmount(float estimatedAmount) {
        this.estimatedAmount = estimatedAmount;
    }
}
