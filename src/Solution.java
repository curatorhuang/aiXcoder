import org.junit.Test;
import static org.junit.Assert.*;

public class Solution {
  /*n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
  你需要按照以下要求，给这些孩子分发糖果：
  每个孩子至少分配到 1 个糖果。
  相邻两个孩子评分更高的孩子会获得更多的糖果。
  请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目。*/
  public int candy(int[] ratings) {
    int n = ratings.length;
    int[] candy = new int[n];
    for (int i = 0; i < n; i++) {
      candy[i] = 1;
    }
    for (int i = 1; i < n; i++) {
      if (ratings[i] > ratings[i - 1]) {
        candy[i] = candy[i - 1] + 1;
      }
    }
    for (int i = n - 2; i >= 0; i--) {
      if (ratings[i] > ratings[i + 1]) {
        candy[i] = Math.max(candy[i], candy[i + 1] + 1);
      }
    }
    int sum = 0;
    for (int i = 0; i < n; i++) {
      sum += candy[i];
    }
    return sum;
  }

    @Test
    public void testCandy() {
      Solution solution = new Solution();
      int[] ratings1 = {1, 0, 2};
      int[] ratings2 = {1, 2, 2};
      int[] ratings3 = {};
      int[] ratings4 = {5};
      int[] ratings5 = {4,4,4};
      int[] ratings6 = {1, 2, 3,4};
      int[] ratings7 = {4,3,2,1};

      assertEquals(5, solution.candy(ratings1));
      assertEquals(4, solution.candy(ratings2));
      assertEquals(0, solution.candy(ratings3));
      assertEquals(1, solution.candy(ratings4));
      assertEquals(3, solution.candy(ratings5));
      assertEquals(10, solution.candy(ratings6));
      assertEquals(10, solution.candy(ratings7));
    }
}
