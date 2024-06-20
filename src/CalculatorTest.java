import aliba.Calculator;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        Assertions.assertEquals(5, result);
    }

    @Test
    public void testMultiply() {
        Calculator calculator = new Calculator();
        int result = calculator.multiply(2, 3);
        Assertions.assertEquals(6, result);
    }

    @Test
    public void testDividePositive() {
        Calculator calculator = new Calculator();
        double result = calculator.divide(6, 2);
        Assertions.assertEquals(3.0, result, 0.0);
    }

    @Test
    public void testDivideNegative() {
        Calculator calculator = new Calculator();
        double result = calculator.divide(-6, 2);
        Assertions.assertEquals(-3.0, result, 0.0);
    }

    @Test
    public void testDivideByZero() {
        Calculator calculator = new Calculator();
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            calculator.divide(6, 0);
        });
    }
}
