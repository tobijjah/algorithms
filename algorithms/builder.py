from algorithms.container import Token
from abc import (ABCMeta,
                 abstractmethod,)
from string import (digits,
                    whitespace,
                    ascii_letters,)
"""
Token types

WHITESPACE = {\t, \n, \r, \x0b, \x0c}
OPERATOR = {+, -, *, /}
NUMBER(FLOAT, INTEGER) = {[0-9], .}
SYMBOL(VARIABLE, FUNCTION) = {[A-Za-z]}
"""


class TokenBuilder(metaclass=ABCMeta):
    def __init__(self, typ):
        self.chars = []
        self.typ = typ

    def token(self):
        return Token(''.join([c.char for c in self.chars]),
                     self.typ, self.chars[0].row, self.chars[0].column)

    @abstractmethod
    def __iadd__(self, char):
        """Add char and return self"""

    def __repr__(self):
        chars = [c.char for c in self.chars]
        return '<{}(type={}, chars={}) at {:X}>'.format(self.__class__.__name__, self.typ, chars, id(self))

    @classmethod
    @abstractmethod
    def valid(cls, char):
        """If char is valid part of token return true else false"""

    @classmethod
    @abstractmethod
    def identifier(cls, char):
        """If char is token identifier return true else false"""


class WhitespaceTokenBuilder(TokenBuilder):
    # Token grammar
    WHITESPACE = whitespace

    def __init__(self):
        super().__init__('WHITESPACE')

    def __iadd__(self, char):
        self.chars.append(char)
        return self

    @classmethod
    def valid(cls, char):
        return cls.identifier(char)

    @classmethod
    def identifier(cls, char):
        if char.char in cls.WHITESPACE:
            return True
        return False


class NumberTokenBuilder(TokenBuilder):
    # Token grammar
    NUMBER = digits + '.'

    def __init__(self):
        super().__init__('NUMBER')
        self.decimal_point = 0

    def token(self):
        token = super().token()

        if self.decimal_point == 0:
            return Token(token.chars, 'INTEGER', token.row, token.column)

        return Token(token.chars, 'FLOAT', token.row, token.column)

    def __iadd__(self, char):
        if char.char == '.':
            if self.decimal_point < 1:
                self.decimal_point += 1
            else:
                raise ValueError('Illegal number of decimal points')

        self.chars.append(char)
        return self

    @classmethod
    def valid(cls, char):
        return cls.identifier(char)

    @classmethod
    def identifier(cls, char):
        if char.char in cls.NUMBER:
            return True
        return False


class OperatorTokenBuilder(TokenBuilder):
    # Token grammar
    OPERATOR = '+-*/^()'

    def __init__(self):
        super().__init__('OPERATOR')

    def __iadd__(self, char):
        self.chars.append(char)
        return self

    @classmethod
    def valid(cls, char):
        return False

    @classmethod
    def identifier(cls, char):
        if char.char in cls.OPERATOR:
            return True
        return False


class SymbolTokenBuilder(TokenBuilder):
    # Token grammar
    SYMBOL = ascii_letters

    def __init__(self):
        super().__init__('SYMBOL')

    def token(self):
        token = super().token()

        if len(self.chars) > 1:
            return Token(token.chars, 'FUNCTION', token.row, token.column)

        return Token(token.chars, 'VARIABLE', token.row, token.column)

    def __iadd__(self, char):
        self.chars.append(char)
        return self

    @classmethod
    def valid(cls, char):
        return cls.identifier(char)

    @classmethod
    def identifier(cls, char):
        if char.char in cls.SYMBOL:
            return True
        return False


class TokenBuilderFactory:
    BUILDERS = [
        WhitespaceTokenBuilder,
        NumberTokenBuilder,
        OperatorTokenBuilder,
        SymbolTokenBuilder,
    ]

    @classmethod
    def factory(cls, char):
        for builder in cls.BUILDERS:
            if builder.identifier(char):
                obj = builder()
                obj += char
                return obj

        else:
            raise ValueError('Unknown char %s' % char)
