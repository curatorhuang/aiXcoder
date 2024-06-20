import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class test11Test {

    private test11 t11;

    @Before
    public void setUp() {
        t11 = new test11();
    }

    @Test
    public void testGetName() {
        // 首先设置名字
        String expectedName = "John Doe";
        t11.setName(expectedName);
        
        // 然后验证 getName 是否返回正确的名字
        Assert.assertEquals(expectedName, t11.getName());
    }

    @Test
    public void testSetName() {
        // 设置一个新的名字并验证是否成功设置
        String newName = "Jane Smith";
        t11.setName(newName);
        
        // 验证 getName 是否返回新的名字
        Assert.assertEquals(newName, t11.getName());
    }
}
