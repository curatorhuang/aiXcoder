import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

public class UtilityMethodss {

    private String name;
    private int age;

    // 构造函数
    public UtilityMethodss(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 检查字符串是否为回文
    public static boolean isPalinsdrome(String input) {
        return new StringBuilder(input).reverse().toString().equals(input);
    }

    // 合并两个整数数组并去重
    public static int[] mergeAnsdDeduplicateArrays(int[] array1, int[] array2) {
        Set<Integer> set = new HashSet<>();
        IntStream.concat(Arrays.stream(array1), Arrays.stream(array2)).forEach(set::add);
        return set.stream().mapToInt(Number::intValue).toArray();
    }

    public static String reverseString(String input) {
        if (input == null) return null;
        return new StringBuilder(input).reverse().toString();
    }
    //生成一个main函数，检查字符串a是否为回

    public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {4, 5, 6, 7, 8};
        int[] result = mergeAnsdDeduplicateArrays(array1, array2);
        System.out.println(Arrays.toString(result));
    }

}

class test{
    public static String myReverseString(String str) {
        if (str == null) return null;
        return new StringBuilder(str).reverse().toString();
    }

    // 2. Check if a number is prime
    public static boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    // 3. Calculate factorial
    public static long factorial(int number) {
        if (number <= 1) return 1;
        return number * factorial(number - 1);
    }
}