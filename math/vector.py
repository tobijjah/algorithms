from matplotlib.patches import FancyArrow


class VectorBaseException(Exception):
    """Base exception"""


class VectorDimensionError(VectorBaseException):
    """Diverging dimensions of start and end point"""


class VectorAdditionError(VectorBaseException):
    """Vector addition error"""


class VectorBase:
    def __init__(self, start=(0, 0), end=(1, 1)):
        if len(start) != len(end):
            raise VectorDimensionError(
                'Start length and end length must be similar (%s != %s).' % (len(start), len(end))
            )

        self.start = list(start)
        self.end = list(end)
        self.distances = [v1 - v2 for v1, v2 in zip(end, start)]

    def scale(self, scalar):
        end = [scalar * val for val in self.end]

        return __class__(self.start, end)

    def __add__(self, other):
        if not isinstance(other, __class__):
            raise VectorAdditionError('Wrong type {}, only supported for {}'.format(type(other), __class__.__name__))

        elif len(self) != len(other):
            raise VectorDimensionError('Vectors need the same base to be added.')

        end = [sum(vals) for vals in zip(self.end, other.end)]

        return __class__(self.start, end)

    def __repr__(self):
        return '<Vector({}, {}) at {}>'.format(self.start, self.end, hex(id(self)))

    def __len__(self):
        return len(self.start)


class Vector2D(VectorBase):
    DEFAULT = {
        'width': 0.05,
        'color': 'black',
        'shape': 'right',
        'length_includes_head': True,
    }

    def __init__(self, end, start=None, **kwargs):
        if len(end) > 2:
            raise VectorDimensionError('2D-Vectors allow only a 2 dimensional vector space.')

        if start is None:
            start = [0] * len(end)

        super().__init__(start, end)

        if kwargs:
            self.graphic_attrs = __class__.DEFAULT.copy()
            self.graphic_attrs.update(kwargs)

        else:
            self.graphic_attrs = __class__.DEFAULT.copy()

        self.graphic = FancyArrow(*self.start, *self.distances, **self.graphic_attrs)

    def scale(self, scalar):
        vec = super().scale(scalar)

        return __class__(vec.end, vec.start, **self.graphic_attrs)

    def __add__(self, other):
        vec = super().__add__(other)

        return __class__(vec.end, vec.start)


if __name__ == '__main__':
    pass
