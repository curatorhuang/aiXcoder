public class LinearSearch {
    public static int linearSearch(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] a = {90, 10, 23, 45, 78, 88, 80};
        int key = 45;
        System.out.println(key + " 的位置是: " + linearSearch(a, key));
    }
}

