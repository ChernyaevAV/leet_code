def is_triangle(sides):
    side_1, side_2, side_3 = sides
    return (
            sum((side_1, side_2)) >= side_3 > 0 and
            sum((side_1, side_3)) >= side_2 > 0 and
            sum((side_2, side_3)) >= side_1 > 0
    )


def equilateral(sides):
    side_1, side_2, side_3 = sides
    return is_triangle(sides) and side_1 == side_2 == side_3


def isosceles(sides):
    side_1, side_2, side_3 = sides
    return is_triangle(sides) and (
        side_1 == side_2 or side_1 == side_3 or side_2 == side_3
    )


def scalene(sides):
    side_1, side_2, side_3 = sides
    return is_triangle(sides) and side_1 != side_2 and side_1 != side_3 and side_2 != side_3


assert equilateral([2, 2, 2]) == True
assert equilateral([0.5, 0.5, 0.5]) == True
