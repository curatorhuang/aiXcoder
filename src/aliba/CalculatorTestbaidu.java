import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CalculatorTestbaidu {

    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();

        // Test with positive numbers
        int result = calculator.add(5, 3);
        assertEquals(8, result, "Adding 5 and 3 should equal 8");

        // Test with negative numbers
        result = calculator.add(-2, -4);
        assertEquals(-6, result, "Adding -2 and -4 should equal -6");

        // Test with zero
        result = calculator.add(0, 0);
        assertEquals(0, result, "Adding 0 and 0 should equal 0");

        // Test with one number being zero
        result = calculator.add(0, 5);
        assertEquals(5, result, "Adding 0 and 5 should equal 5");

        result = calculator.add(5, 0);
        assertEquals(5, result, "Adding 5 and 0 should equal 5");
    }
}
