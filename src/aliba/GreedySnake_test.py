from src.GreedySnake import Snake
import unittest
# 导入可能需要用的包
import unittest.mock

class TestSnake(unittest.TestCase):

    def setUp(self):
        """
        # 测试场景：创建蛇实例
        # 预期结果：返回蛇实例
        """
        self.snake = Snake()

    def test_move_right(self):
        """
        # 测试场景：蛇向右移动
        # 预期结果：蛇的头部向右移动
        """
        self.snake.direction = 'right'
        self.snake.body = [(0, 0), (0, 0)]
        self.snake.move()
        self.assertEqual(self.snake.body[0], (BLOCK_SIZE, 0))

    def test_move_left(self):
        """
        # 测试场景：蛇向左移动
        # 预期结果：蛇的头部向左移动
        """
        self.snake.direction = 'left'
        self.snake.body = [(0, 0), (0, 0)]
        self.snake.move()
        self.assertEqual(self.snake.body[0], (-BLOCK_SIZE, 0))

    def test_move_up(self):
        """
        # 测试场景：蛇向上移动
        # 预期结果：蛇的头部向上移动
        """
        self.snake.direction = 'up'
        self.snake.body = [(0, 0), (0, 0)]
        self.snake.move()
        self.assertEqual(self.snake.body[0], (0, -BLOCK_SIZE))

    def test_move_down(self):
        """
        # 测试场景：蛇向下移动
        # 预期结果：蛇的头部向下移动
        """
        self.snake.direction = 'down'
        self.snake.body = [(0, 0), (0, 0)]
        self.snake.move()
        self.assertEqual(self.snake.body[0], (0, BLOCK_SIZE))

    def test_move_invalid_direction(self):
        """
        # 测试场景：蛇移动无效方向
        # 预期结果：抛出ValueError
        """
        self.snake.direction = 'invalid'
        with self.assertRaises(ValueError):
            self.snake.move()

if __name__ == '__main__':
    unittest.main()