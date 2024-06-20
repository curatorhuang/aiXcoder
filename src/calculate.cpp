#include <iostream>

// 函数声明
double calculate(double x, double y, char operation);

int main() {
    double num1, num2;
    char operation;

    // 获取用户输入
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    std::cout << "Enter an operator (+, -, *, /): ";
    std::cin >> operation;

    // 调用函数并显示结果
    std::cout << "Result: " << calculate(num1, num2, operation) << std::endl;

    return 0;
}

// 计算函数定义
double calculate(double x, double y, char operation) {
    // 根据不同的运算符执行计算
    switch (operation) {
        case '+':
            return x + y  // 加法运算
        case '-':
            return x - y;  // 减法运算
        case '*':
            return x * y;  // 乘法运算
        case '/':
            // 检查除数是否为0
            if (y != 0) {
                return x / y;  // 除法运算
            } else {
                std::cout << "Error: Division by zero" << std::endl;
                return 0;  // 当除数为0时返回0，并提示错误
            }
        default:
            std::cout << "Invalid operation" << std::endl;
            return 0;  // 非法运算符错误
    }
}
