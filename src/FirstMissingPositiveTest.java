import static org.junit.Assert.*;
import org.junit.Test;

public class FirstMissingPositiveTest {

    @Test
    public void testEmptyArray() {
        assertEquals(1, new firstMissingPositive().firstMissingPositive(new int[] {}));
    }

    @Test
    public void testAllNegativeOrZero() {
        assertEquals(1, new firstMissingPositive().firstMissingPositive(new int[] {-1, -2, 0}));
    }

    @Test
    public void testContinuousPositiveStartingAtOne() {
        assertEquals(4, new firstMissingPositive().firstMissingPositive(new int[] {1, 2, 3}));
    }

    @Test
    public void testNonContinuousPositive() {
        assertEquals(2, new firstMissingPositive().firstMissingPositive(new int[] {3, 4, -1, 1}));
    }

    @Test
    public void testArrayWithDuplicates() {
        assertEquals(3, new firstMissingPositive().firstMissingPositive(new int[] {1, 2, 2}));
    }

    @Test
    public void testMissingPositiveAtEnd() {
        assertEquals(3, new firstMissingPositive().firstMissingPositive(new int[] {1, 2}));
    }

    @Test
    public void testAllPositivesIncluded() {
        assertEquals(4, new firstMissingPositive().firstMissingPositive(new int[] {1, 2, 3}));
    }
}
