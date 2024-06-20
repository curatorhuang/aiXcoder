import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void testAdd() {
        assertEquals(5, calculator.add(2, 3));
        assertEquals(-1, calculator.add(-2, 1));
    }

    @Test
    void testMultiply() {
        assertEquals(6, calculator.multiply(2, 3));
        assertEquals(-2, calculator.multiply(-2, 1));
    }

    @Test
    void testDivide() {
        assertEquals(2.0, calculator.divide(4, 2), "Expected result: 2.0");
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(4, 0), "Expected IllegalArgumentException for divider zero");
    }

    @Test
    void testAddWithNegativeNumbers() {
        assertEquals(-5, calculator.add(-2, -3));
    }

    @Test
    void testMultiplyWithNegativeNumbers() {
        assertEquals(6, calculator.multiply(-2, 3));
        assertEquals(2, calculator.multiply(-2, -1));
    }

    @Test
    void testDivideWithZeroDivisor() {
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(4, 0), "Expected IllegalArgumentException for divider zero");
    }
}