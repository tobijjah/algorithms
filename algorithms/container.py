class Char:
    __slots__ = 'row', 'column', 'idx', 'char'

    def __init__(self, char, idx, row, column):
        self.idx = idx
        self.row = row
        self.char = char
        self.column = column

    def __str__(self):
        return '{} at line {} column {}'.format(self.char, self.row, self.column)

    def __repr__(self):
        return '<{}(char={}, idx={}, row={}, column={}) at {:x}>'.format(self.__class__.__name__,
                                                                         self.char,
                                                                         self.idx,
                                                                         self.row,
                                                                         self.column,
                                                                         id(self))


class Token:
    def __init__(self, chars, typ, row, column):
        self.chars = chars
        self.typ = typ
        self.row = row
        self.column = column

    def __repr__(self):
        return '({}, {})'.format(self.typ, self.chars)


