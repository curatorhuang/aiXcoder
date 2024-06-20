import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class UtilityMethodssTest {

    @Test
    public void testIsPalinsdrome() {
        assertTrue(UtilityMethodss.isPalinsdrome("racecar"));
        assertFalse(UtilityMethodss.isPalinsdrome("hello"));
    }

    @Test
    public void testMergeAnsdDeduplicateArrays() {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {4, 5, 6, 7, 8};
        int[] expectedResult = {1, 2, 3, 4, 5, 6, 7, 8};
        assertArrayEquals(expectedResult, UtilityMethodss.mergeAnsdDeduplicateArrays(array1, array2));
    }

    @Test
    public void testReverseString() {
        assertEquals("dcba", UtilityMethodss.reverseString("abcd"));
        assertEquals(null, UtilityMethodss.reverseString(null));
    }

    @Test
    public void testMyReverseString() {
        assertEquals("dcba", test.myReverseString("abcd"));
        assertEquals(null, test.myReverseString(null));
    }

    @Test
    public void testIsPrime() {
        assertTrue(test.isPrime(2));
        assertFalse(test.isPrime(1));
        assertTrue(test.isPrime(3));
        assertFalse(test.isPrime(4));
    }

    @Test
    public void testFactorial() throws Exception {
        assertEquals(1, test.factorial(0));
        assertEquals(1, test.factorial(1));
        assertEquals(2, test.factorial(2));
        assertEquals(6, test.factorial(3));
        assertEquals(24, test.factorial(4));
    }
}