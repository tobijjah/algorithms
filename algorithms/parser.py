import string
from algorithms.builder import TokenBuilderFactory
from algorithms.container import Char

# Shunting yard algorithm
# Recursive descent parser
"""
Token formalization
numbers = int and float; 12 and .0, 0.1, 
operators = + - * / ^ ( )
functions = sin sqrt exp cos ...
variables = letters a-z
"""


class Grammar:
    EOF = '\0'

    EXPONENT_STARTCHAR = '^'
    EXPONENT = string.digits + '.,'

    COEFFICIENT_STARTCHARS = string.digits + '.,'
    COEFFICIENT = COEFFICIENT_STARTCHARS

    WHITESPACE = string.whitespace


class Scanner:
    def __init__(self, expression):
        self.expression = expression
        self.exp_len = len(expression) - 1
        self.current = -1

    def get(self):
        self.current += 1

        if self.current <= self.exp_len:
            return Char(self.expression[self.current], 0, 0, 0)

        return None

    def backward(self, step):
        self.current -= step

    def __call__(self):
        return self.get()


class Lexer:
    def __init__(self, scanner):
        self.scanner = scanner

    def get(self):
        builder = TokenBuilderFactory.factory(self.scanner())
        char = self.scanner()

        while builder.valid(char):
            builder += char
            char = self.scanner()

        self.scanner.backward(1)
        return builder.token()

    def __call__(self):
        return self.get()


if __name__ == '__main__':
    ex = '2.311*y*x^3+sin(x+.3)^2+2x+23'
    scan = Scanner(ex)
    lex = Lexer(scan)
    token = lex.get()
    while token is not None:
        print(token)
        token = lex.get()
