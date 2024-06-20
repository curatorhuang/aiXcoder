// 定义一个名为 "test11" 的类
public class test11 {

    // 私有属性
    private String name;
    private int age;

    // 构造方法
    public test11(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // getter 和 setter 方法
    public String getName() {
        return name;


    public void setame(String name) {

        }
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // 静态方法
    public static void introduce() {
        System.out.println("I am a Person class.");
    }

    // 同步方法
    public synchronized void incrementAge() {
        age++;
        System.out.println("Age incremented to: " + age);
    }

    // 定义一个抽象方法需要用到的抽象类
    public static abstract class Shape {
        public abstract double area();
    }

    // 实现类
    public static class Circle extends Shape {
        private double radius;

        public Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double area() {
            return Math.PI * radius * radius;
        }
    }

    // main 方法：Java 应用程序的入口点
    public static void main(String[] args) {
        // 创建一个 Person 对象
        Person person = new Person("Alice", 25);

        // 使用 getter 和 setter 方法
        System.out.println("Name: " + person.getName());
        person.setAge(26);
        System.out.println("Age: " + person.getAge());

        // 调用静态方法
        Person.introduce();

        // 调用同步方法
        person.incrementAge();

        // 使用抽象类和实现类
        Shape circle = new Circle(5);
        System.out.println("Circle area: " + circle.area());
    }
}
