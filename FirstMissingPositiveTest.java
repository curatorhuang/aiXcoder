import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
//本次修改
public class FirstMissingPositiveTest {

    @Test
    public void testFirstMissingPositiveNormal() {
        int[] nums = {3, 4, -1, 1};
        int result = firstMissingPositive(nums);
        assertEquals(2, result);
    }

    @Test
    public void testFirstMissingPositiveCombination() {
        int[] nums = {1, 2, 0};
        int result = firstMissingPositive(nums);
        assertEquals(3, result);
    }

    @Test
    public void testFirstMissingPositiveAllOne() {
        int[] nums = {1, 2, 3};
        int result = firstMissingPositive(nums);
        assertEquals(4, result);
    }

    @Test
    public void testFirstMissingPositiveAllNegative() {
        int[] nums = {-3, -4, -1};
        int result = firstMissingPositive(nums);
        assertEquals(2, result);
    }

    @Test
    public void testFirstMissingPositiveAllZero() {
        int[] nums = {0, 0, 0};
        int result = firstMissingPositive(nums);
        assertEquals(1, result);
    }

    @Test
    public void testFirstMissingPositiveNullInput() {
        int[] nums = null;
        int result = firstMissingPositive(nums);
        assertEquals(1, result);
    }
}ls(1, result);
    }
}