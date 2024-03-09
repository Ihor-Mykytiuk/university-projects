package lab2;

public class CircleArea implements Area{
    private final double radius;

    public CircleArea(double radius) {
        this.radius = radius;
    }

    public double getArea() {
        return Math.PI * radius * radius;
    }

    public String getType() {
        return "Circle";
    }
}
