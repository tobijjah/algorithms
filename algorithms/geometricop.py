# TODO implement jarvis walk/ gift wrapping algorithm for convex hull
# TODO implement find centroid of polygon
# TODO implement find area of polygon


def validate_polygon(points):
    pass


def polygon_area(points):
    # TODO check collinear
    if len(points) < 2 or points[0] != points[-1]:
        raise ValueError

    area = 0

    for idx, point in enumerate(points):
        x_i, y_i = point
        x_ii, y_ii = points[idx + 1]

        area += x_i*y_ii - x_ii*y_i

        if idx == len(points)-2:
            break

    return abs(0.5 * area)


def polygon_centroid(points):
    pass


if __name__ == '__main__':
    ccw = [
        (1, 1),
        (1, 3),
        (3, 3),
        (3, 1),
        (1, 1),
    ]
    print(polygon_area(ccw))

