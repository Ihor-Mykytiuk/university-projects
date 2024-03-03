package lab1;

public class PhoneNumber {
    private String number;
    private String mobileOperator;
    private float monthlyFee;

    public PhoneNumber(String number, String mobileOperator, float monthlyFee) {
        this.number = number;
        this.mobileOperator = mobileOperator;
        this.monthlyFee = monthlyFee;
    }

    public String getNumber() {
        return number;
    }

    public String getMobileOperator() {
        return mobileOperator;
    }

    public float getMonthlyFee() {
        return monthlyFee;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public void setMobileOperator(String mobileOperator) {
        this.mobileOperator = mobileOperator;
    }

    public void setMonthlyFee(float monthlyFee) {
        this.monthlyFee = monthlyFee;
    }
}
