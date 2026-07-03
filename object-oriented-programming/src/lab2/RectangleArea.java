package lab2;

public class RectangleArea implements Area{
    private final double width;
    private final double height;

    public RectangleArea(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getArea() {
        return width * height;
    }

    public String getType() {
        return "Rectangle";
    }
}
