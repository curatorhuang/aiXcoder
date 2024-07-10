package main

import (
	"fmt"
	"strconv"
	"strings"
)

// TokenType 定义 token 的类型
type TokenType int

const (
	NUMBER TokenType = iota
	PLUS
	MINUS
	MULTIPLY
	DIVIDE
	LPAREN
	RPAREN
)

// Token 表示一个解析后的标记
type Token struct {
	Type  TokenType
	Value string
}

// Tokenize 将输入字符串分割为标记
func Tokenize(expression string) ([]Token, error) {
	var tokens []Token
	i := 0
	for i < len(expression) {
		switch expression[i] {
		case '+':
            tokens = append(tokens, Token{Type: PLUS, Value: "+"})
            i++
        case '-':
            tokens = append(tokens, Token{Type: MINUS, Value: "-"})
            i++
        case '*':
            tokens = append(tokens, Token{Type: MULTIPLY, Value: "*"})
            i++
        case '/':
            tokens = append(tokens, Token{Type: DIVIDE, Value: "/"})
            i++
        case '(':
            tokens = append(tokens, Token{Type: LPAREN, Value: "("})
            i++
        case ')':
            tokens = append(tokens, Token{Type: RPAREN, Value: ")"})
            i++
        default:
            if isDigit(expression[i]) {
                j := i
                for j < len(expression) && isDigit(expression[j]) {
                    j++
                }
                tokens = append(tokens, Token{Type: NUMBER, Value: expression[i:j]})
                i = j
            } else {
                return nil, fmt.Errorf("invalid character: %c", expression[i])
            }
		}
	}
	return tokens, nil
}

// isDigit 判断字符是否为数字
func isDigit(ch byte) bool {
	return ch >= '0' && ch <= '9'
}

// Parse 解析标记列表为语法树
func Parse(tokens []Token) (float64, error) {
	return parseExpression(tokens, 0)
}

func parseExpression(tokens []Token, pos int) (float64, error) {
	left, newPos, err := parseTerm(tokens, pos)
	if err != nil {
		return 0, err
	}
	for newPos < len(tokens) && (tokens[newPos].Type == PLUS || tokens[newPos].Type == MINUS) {
		op := tokens[newPos]
		right, nextPos, err := parseTerm(tokens, newPos+1)
		if err != nil {
			return 0, err
		}
		if op.Type == PLUS {
			left += right
		} else {
			left -= right
		}
		newPos = nextPos
	}
	return left, nil
}

func parseTerm(tokens []Token, pos int) (float64, int, error) {
	left, newPos, err := parseFactor(tokens, pos)
	if err != nil {
		return 0, pos, err
	}
	for newPos < len(tokens) && (tokens[newPos].Type == MULTIPLY || tokens[newPos].Type == DIVIDE) {
		op := tokens[newPos]
		right, nextPos, err := parseFactor(tokens, newPos+1)
		if err != nil {
			return 0, pos, err
		}
		if op.Type == MULTIPLY {
			left *= right
		} else {
			left /= right
		}
		newPos = nextPos
	}
	return left, newPos, nil
}

func parseFactor(tokens []Token, pos int) (float64, int, error) {
	if tokens[pos].Type == NUMBER {
		value, err := strconv.ParseFloat(tokens[pos].Value, 64)
		if err != nil {
			return 0, pos, err
		}
		return value, pos + 1, nil
	}
	if tokens[pos].Type == LPAREN {
		value, newPos, err := parseExpression(tokens, pos+1)
		if err != nil {
			return 0, pos, err
		}
		if tokens[newPos].Type != RPAREN {
			return 0, pos, fmt.Errorf("missing closing parenthesis")
		}
		return value, newPos + 1, nil
	}
	return 0, pos, fmt.Errorf("unexpected token: %s", tokens[pos].Value)
}

func main() {
	var expression string
	fmt.Println("请输入一个四则运算表达式（例如：3 + 5 * (2 - 4)）：")
	fmt.Scanln(&expression)

	tokens, err := Tokenize(strings.ReplaceAll(expression, " ", ""))
	if err != nil {
		fmt.Println("解析表达式时出错:", err)
		return
	}

	result, err := Parse(tokens)
	if err != nil {
		fmt.Println("计算表达式时出错:", err)
		return
	}

	fmt.Printf("表达式 %s 的计算结果是: %f\n", expression, result)
}
