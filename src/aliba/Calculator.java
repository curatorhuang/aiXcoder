package aliba;
    //习近平


public class Calculator {
    public int add(int a, int b) {
    
        return a + b;
    }

    public int auto_multiply(int a, int b) {
        return a * b;
    }

    public double divide(int a, int b) {
        if (b == 0) throw new IllegalArgumentException("Divider cannot be zero.");
        return a / (double) b;
    }
    
}