# TODO implement jarvis walk/ gift wrapping algorithm for convex hull
# TODO implement find centroid of polygon
# TODO implement find area of polygon


def validate_polygon(points):
    pass


def polygon_area(points):
    # TODO check collinear
    if len(points) < 2 or points[0] != points[-1]:
        raise ValueError

    n = len(points)-1

    area = 0

    for i in range(n):
        x_i, y_i = points[i]
        x_ii, y_ii = points[i+1]

        area += x_i*y_ii - x_ii*y_i

    return 0.5 * area


def polygon_centroid(points):
    n = len(points)-1

    c_x = 0
    c_y = 0

    area = polygon_area(points)

    for i in range(n):
        x_i, y_i = points[i]
        x_ii, y_ii = points[i+1]

        c_x += (x_i + x_ii) * (x_i*y_ii - x_ii*y_i)
        c_y += (y_i + y_ii) * (x_i*y_ii - x_ii*y_i)

    c_x = 1/(6*area) * c_x
    c_y = 1/(6*area) * c_y

    return c_x, c_y


def vector_angle():
    pass


if __name__ == '__main__':
    ccw = [
        (1, 1),
        (3, 1),
        (3, 3),
        (1, 3),
        (1, 1),
    ]
    print(polygon_area(ccw))
    print(polygon_centroid(ccw))
