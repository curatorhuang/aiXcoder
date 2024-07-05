package org.example.user;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.mockito.*;
import static org.mockito.Mockito.*;
import static org.testng.Assert.*;

import java.util.*;

// 测试类定义
public class UserServiceTest {

    // 注入要测试的服务
    @InjectMocks
    private UserService userService;

    // 模拟依赖的用户仓库
    @Mock
    private UserRepository userRepository;

    // 在每个测试方法之前初始化模拟对象
    @BeforeMethod
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * 测试正常场景：用户存在
     * 预期结果：返回用户名称
     */
    @Test
    public void testGetUserName_NormalScenario() {
        // 模拟用户仓库返回用户对象
        User user = new User("1", "John");
        when(userRepository.findUserById("1")).thenReturn(user);

        // 调用测试方法并断言结果
        String result = userService.getUserName("1");
        assertEquals(result, "John", "用户名称应正确");
    }

    /**
     * 测试正常场景：用户不存在
     * 预期结果：返回"Unknown"
     */
    @Test
    public void testGetUserName_UserNotFound() {
        // 模拟用户仓库返回null
        when(userRepository.findUserById("2")).thenReturn(null);

        // 调用测试方法并断言结果
        String result = userService.getUserName("2");
        assertEquals(result, "Unknown", "用户名称应为Unknown");
    }

    /**
     * 测试边界场景：用户ID为null
     * 预期结果：抛出NullPointerException
     */
    @Test
    public void testGetUserName_UserIDIsNull() {
        try {
            // 调用测试方法
            userService.getUserName(null);
            fail("应抛出NullPointerException");
        } catch (NullPointerException e) {
            // 验证抛出NullPointerException
            assertNotNull(e);
        }
    }
}