from modules.types import Coordinate, Parameters
import numpy as np

from utils import (
    can_three_np_points_fit_in_a_circle,
    convert_to_np_point,
    get_angle_from_np_points,
    get_distance_between_np_points,
    get_triangle_area_from_np_points,
    np_points_equal,
)


# Helper functions
def check_lic_0(num_points, points: list[Coordinate], parameters: Parameters) -> bool:
    if num_points < 2 or parameters["length1"] <= 0:
        return False

    for i in range(num_points - 1):
        point_1 = convert_to_np_point(points[i])
        point_2 = convert_to_np_point(points[i + 1])

        distance = get_distance_between_np_points(point_1, point_2)

        if distance > parameters["length1"]:
            return True
    return False


def check_lic_1() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_2() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_3() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_4() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_5(points: list[Coordinate]) -> bool:
    return any(p2["x"] - p1["x"] < 0 for p1, p2 in zip(points, points[1:]))


def check_lic_6(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    n_pts = parameters["n_pts"]
    dist = parameters["dist"]

    if num_points < 3 or not (3 <= n_pts <= num_points) or dist < 0:
        return False

    for i in range(len(points) - n_pts + 1):
        stripped_points = points[i : i + n_pts]
        first_point = convert_to_np_point(stripped_points[0])
        last_point = convert_to_np_point(stripped_points[-1])

        for j in range(1, n_pts):
            current_point = convert_to_np_point(stripped_points[j])

            if np_points_equal(first_point, last_point):
                curr_dist = get_distance_between_np_points(current_point, first_point)
                if curr_dist > dist:
                    return True

            else:
                # Calculate the shortest distance between the current point
                # and the line formed by the first and last points.
                ax, ay = last_point - first_point
                bx, by = first_point - current_point
                cross_value = ax * by - ay * bx
                curr_pt_dist_to_line = np.abs(cross_value) / np.linalg.norm([ax, ay])

                if curr_pt_dist_to_line > dist:
                    return True

    return False


def check_lic_7(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]

    if num_points < 3:
        return False
    if not (1 <= k_pts <= (num_points - 2)):
        return False
    if length1 < 0:
        return False

    for i in range(num_points - k_pts - 1):
        first_point = convert_to_np_point(points[i])
        last_point = convert_to_np_point(points[i + k_pts + 1])

        dist = get_distance_between_np_points(first_point, last_point)

        if dist > length1:
            return True

    return False


def check_lic_8(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]

    if a_pts + b_pts > num_points - 3:
        return False
    if (a_pts < 1) or (b_pts < 1):
        return False
    if radius1 < 0:
        return False
    if num_points < 5:
        return False

    for i in range(num_points - a_pts - b_pts - 2):
        # Using properties of a circumcirle for 3 points creating a triangle.
        x_point = convert_to_np_point(points[i])
        y_point = convert_to_np_point(points[i + a_pts + 1])
        z_point = convert_to_np_point(points[i + a_pts + b_pts + 2])

        fit = can_three_np_points_fit_in_a_circle(x_point, y_point, z_point, radius1)

        if not fit:
            return True

    return False


def check_lic_9(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    c_pts = parameters["c_pts"]
    d_pts = parameters["d_pts"]
    epsilon = parameters["epsilon"]

    if (
        (c_pts + d_pts > num_points - 3)
        or (1 > c_pts)
        or (1 > d_pts)
        or (epsilon < 0)
        or (num_points < 5)
    ):
        return False

    for i in range(num_points - c_pts - d_pts - 2):
        first_vertex = convert_to_np_point(points[i])
        angle_vertex = convert_to_np_point(points[i + c_pts + 1])
        last_vertex = convert_to_np_point(points[i + c_pts + d_pts + 2])

        if np_points_equal(first_vertex, angle_vertex):
            continue
        if np_points_equal(last_vertex, angle_vertex):
            continue

        angle = get_angle_from_np_points(first_vertex, angle_vertex, last_vertex)

        if angle < (np.pi - epsilon):
            return True
        if angle > (np.pi + epsilon):
            return True
    return False


def check_lic_10(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    area1 = parameters["area1"]
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]

    if num_points < 5:
        return False
    if e_pts < 1:
        return False
    if f_pts < 1:
        return False
    if e_pts + f_pts > num_points - 3:
        return False

    for i in range(num_points - e_pts - f_pts - 2):
        point_i = convert_to_np_point(points[i])
        point_j = convert_to_np_point(points[i + e_pts + 1])
        point_k = convert_to_np_point(points[i + e_pts + f_pts + 2])

        area = get_triangle_area_from_np_points(point_i, point_j, point_k)

        if area > area1:
            return True

    return False


def check_lic_11(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    g_pts = parameters["g_pts"]

    if num_points < 3:
        return False

    if not (1 <= g_pts <= num_points - 2):
        return False

    for i in range(num_points - g_pts - 1):
        point_1 = points[i]
        point_2 = points[i + g_pts + 1]
        x_difference = point_2["x"] - point_1["x"]

        if x_difference < 0:
            return True

    return False


def check_lic_12(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]
    length2 = parameters["length2"]

    if num_points < 3:
        return False
    if length2 < 0:
        return False

    flag_1 = False
    flag_2 = False

    for i in range(num_points - k_pts - 1):
        point_1 = convert_to_np_point(points[i])
        point_2 = convert_to_np_point(points[i + k_pts + 1])

        length = get_distance_between_np_points(point_1, point_2)

        if length > length1:
            flag_1 = True

        if length < length2:
            flag_2 = True

        if flag_1 and flag_2:
            return True

    return False


def check_lic_13(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]
    radius2 = parameters["radius2"]

    if (radius2 < 0) or (num_points < 5):
        return False

    flag_1 = False
    flag_2 = False

    for i in range(len(points) - a_pts - b_pts - 2):
        point_i = convert_to_np_point(points[i])
        point_j = convert_to_np_point(points[i + a_pts + 1])
        point_k = convert_to_np_point(points[i + a_pts + b_pts + 2])

        fit_1 = can_three_np_points_fit_in_a_circle(point_i, point_j, point_k, radius1)
        fit_2 = can_three_np_points_fit_in_a_circle(point_i, point_j, point_k, radius2)

        if not fit_1:
            flag_1 = True

        if fit_2:
            flag_2 = True

        if flag_1 and flag_2:
            return True

    return False


def check_lic_14(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    area1 = parameters["area1"]
    area2 = parameters["area2"]
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]

    if (num_points < 5) or (area2 < 0):
        return False

    flag_1 = False
    flag_2 = False

    for i in range(len(points) - e_pts - f_pts - 2):
        point_i = convert_to_np_point(points[i])
        point_j = convert_to_np_point(points[i + e_pts + 1])
        point_k = convert_to_np_point(points[i + e_pts + f_pts + 2])

        area = get_triangle_area_from_np_points(point_i, point_j, point_k)

        if area > area1:
            flag_1 = True

        if area < area2:
            flag_2 = True

        if flag_1 and flag_2:
            return True

    return False


# Main function
def get_cmv(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> list[bool]:
    return [
        check_lic_0(num_points, points, parameters),
        check_lic_1(),
        check_lic_2(),
        check_lic_3(),
        check_lic_4(),
        check_lic_5(points),
        check_lic_6(num_points, points, parameters),
        check_lic_7(num_points, points, parameters),
        check_lic_8(num_points, points, parameters),
        check_lic_9(num_points, points, parameters),
        check_lic_10(num_points, points, parameters),
        check_lic_11(num_points, points, parameters),
        check_lic_12(),
        check_lic_13(num_points, points, parameters),
        check_lic_14(num_points, points, parameters),
    ]
