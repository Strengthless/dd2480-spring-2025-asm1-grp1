import numpy as np
from src.modules.types import Comp_Type, Coordinate


def float_compare(a, b, epsilon=0.000001) -> Comp_Type:
    if abs(a - b) < epsilon:
        return Comp_Type.EQ
    elif a < b:
        return Comp_Type.LT
    else:
        return Comp_Type.GT


def float_lte(a, b, epsilon=0.000001) -> bool:
    return float_compare(a, b, epsilon) in [Comp_Type.LT, Comp_Type.EQ]


def float_gte(a, b, epsilon=0.000001) -> bool:
    return float_compare(a, b, epsilon) in [Comp_Type.GT, Comp_Type.EQ]


def convert_to_np_point(point: Coordinate) -> np.ndarray:
    return np.array([point["x"], point["y"]], dtype=float)


def np_points_equal(a: np.ndarray, b: np.ndarray, epsilon=0.000001) -> Comp_Type:
    x_equal = float_compare(a[0], b[0], epsilon)
    y_equal = float_compare(a[1], b[1], epsilon)
    return x_equal == y_equal == Comp_Type.EQ


def get_distance_between_np_points(a: np.ndarray, b: np.ndarray) -> float:
    return np.linalg.norm(a - b)


def get_triangle_area_from_np_points(
    x_point: np.ndarray, y_point: np.ndarray, z_point: np.ndarray
) -> float:
    a = get_distance_between_np_points(x_point, y_point)
    b = get_distance_between_np_points(y_point, z_point)
    c = get_distance_between_np_points(z_point, x_point)
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))


def get_angle_from_np_points(
    x_point: np.ndarray, y_point: np.ndarray, z_point: np.ndarray
) -> float:
    """
    Get the angle between the two lines formed by the three points.

    :param x_point: First point
    :param y_point: Second point (the vertex)
    :param z_point: Third point
    :return: The angle in radians
    """
    a = get_distance_between_np_points(x_point, y_point)
    b = get_distance_between_np_points(y_point, z_point)
    c = get_distance_between_np_points(z_point, x_point)

    if a == 0 or b == 0:
        return 0

    return np.arccos((a**2 + b**2 - c**2) / (2 * a * b))


def can_three_np_points_fit_in_a_circle(
    x_point: np.ndarray, y_point: np.ndarray, z_point: np.ndarray, target_radius: float
) -> bool:
    """
    Check if all three points can fit in a circle with a given radius.

    :param x_point: First point
    :param y_point: Second point
    :param z_point: Third point
    :param target_radius: The radius of the circle
    :return: True if the points can fit in a circle with the given radius, False otherwise
    """
    a_distance = get_distance_between_np_points(x_point, y_point)
    b_distance = get_distance_between_np_points(y_point, z_point)
    c_distance = get_distance_between_np_points(z_point, x_point)
    triangle_area = get_triangle_area_from_np_points(x_point, y_point, z_point)

    # Collinear case
    if triangle_area == 0:
        max_distance = max(a_distance, b_distance, c_distance)
        if float_lte(max_distance / 2, target_radius):
            return True

    sides = sorted([a_distance, b_distance, c_distance])
    a, b, c = sides

    # Acute triangle
    if float_compare(c**2, a**2 + b**2) == Comp_Type.LT:
        circum_radius = (a_distance * b_distance * c_distance) / (4 * triangle_area)
        if float_lte(circum_radius, target_radius):
            return True

    # Right or obtuse triangle
    else:
        if float_lte(c / 2, target_radius):
            return True

    return False
