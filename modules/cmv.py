import math
from modules.types import Coordinate, Parameters
import numpy as np


# Helper functions
def check_lic_0(num_points, points: list[Coordinate], parameters: Parameters) -> bool:
    if num_points < 2 or parameters["length1"] <= 0:
        return False

    for i in range(num_points - 1):
        point_1 = points[i]
        point_2 = points[i + 1]

        distance_points = math.sqrt(
            (point_1["x"] - point_2["x"]) ** 2 + (point_1["y"] - point_2["y"]) ** 2
        )

        if distance_points > parameters["length1"]:
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


def check_lic_5() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_6() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_7() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_8(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]

    if (
        (a_pts + b_pts > num_points - 3)
        or (1 > a_pts)
        or (1 > b_pts)
        or (radius1 < 0)
        or (num_points < 5)
    ):
        return False

    for i in range(num_points - a_pts - b_pts - 2):
        # Using properties of a circumcirle for 3 points creating a triangle.
        x_point = np.array([points[i]["x"], points[i]["y"]], dtype=float)
        y_point = np.array(
            [points[i + a_pts + 1]["x"], points[i + a_pts + 1]["y"]], dtype=float
        )
        z_point = np.array(
            [points[i + a_pts + b_pts + 2]["x"], points[i + a_pts + b_pts + 2]["y"]],
            dtype=float,
        )

        a_distance = np.linalg.norm(x_point - y_point)

        b_distance = np.linalg.norm(y_point - z_point)

        c_distance = np.linalg.norm(z_point - x_point)

        triangle_area = (
            abs(
                x_point[0] * (y_point[1] - z_point[1])
                + y_point[0] * (z_point[1] - x_point[1])
                + z_point[0] * (x_point[1] - y_point[1])
            )
            / 2
        )

        if triangle_area == 0:
            max_distance = max(a_distance, b_distance, c_distance)

            # Identical points are skipped
            if max_distance == 0:
                continue

            # Collinear case
            if max_distance / 2 > radius1:
                return True

            # Skip, check other points
            continue

        circumcircle_radius = (a_distance * b_distance * c_distance) / (
            4 * triangle_area
        )

        if circumcircle_radius > radius1:
            return True

    return False


def check_lic_9() -> bool:
    # TODO: Update the function signature and implementation
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
        raise ValueError("e_pts must be greater than or equal to 1")
    if f_pts < 1:
        raise ValueError("f_pts must be greater than or equal to 1")
    if e_pts + f_pts > num_points - 3:
        raise ValueError("e_pts + f_pts must be less than or equal to num_points - 3")

    for i in range(num_points - e_pts - f_pts - 2):
        # Calculate the area of the triangle that is defined by the two
        # vectors formed by the point i to the point j and k respectively
        point_i = points[i]
        point_j = points[i + e_pts + 1]
        point_k = points[i + e_pts + f_pts + 2]

        vector_1 = [point_j["x"] - point_i["x"], point_j["y"] - point_i["y"]]
        vector_2 = [point_k["x"] - point_i["x"], point_k["y"] - point_i["y"]]

        calc_area = abs((1 / 2) * np.cross(vector_1, vector_2))

        if calc_area > area1:
            return True

    return False


def check_lic_11(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    g_pts = parameters["g_pts"]

    if num_points < 3:
        return False

    if not (1 <= g_pts <= num_points - 2):
        raise ValueError

    for i in range(num_points - g_pts - 1):
        if points[i + g_pts + 1]["x"] - points[i]["x"] < 0:
            return True

    return False


def check_lic_12() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_13() -> bool:
    # TODO: Update the function signature and implementation
    return False


def check_lic_14() -> bool:
    # TODO: Update the function signature and implementation
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
        check_lic_5(),
        check_lic_6(),
        check_lic_7(),
        check_lic_8(num_points, points, parameters),
        check_lic_9(),
        check_lic_10(num_points, points, parameters),
        check_lic_11(num_points, points, parameters),
        check_lic_12(),
        check_lic_13(),
        check_lic_14(),
    ]
