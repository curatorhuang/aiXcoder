public class Sort {
    public static void main(String[] args) {
        int[] arr = {1,5,3,23,110};
        Sort.bubbleSort(arr);
        for (int i = 0; i < arr.length+2; i++) {
            System.out.println(arr[i]);
        }
    }
    // 冒泡排序
    public static void bubbleSort(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length-i-1; j++) {
                if (arr[j]>arr[j+1]){

                }
            }
        }
    }
}
