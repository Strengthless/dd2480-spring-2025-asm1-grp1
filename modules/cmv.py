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


def check_lic_7(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]

    if num_points < 3 or not (1 <= k_pts <= (num_points - 2)) or length1 < 0:
        return False

    for i in range(num_points - k_pts - 1):
        first_point = np.array([points[i]["x"], points[i]["y"]], dtype=float)
        last_point = np.array(
            [points[i + k_pts + 1]["x"], points[i + k_pts + 1]["y"]], dtype=float
        )

        first_last_distance = np.linalg.norm(first_point - last_point)

        if first_last_distance > length1:
            return True

    return False


def check_lic_8() -> bool:
    # TODO: Update the function signature and implementation
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
        return False
    if f_pts < 1:
        return False
    if e_pts + f_pts > num_points - 3:
        return False

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
        return False

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
        check_lic_7(num_points, points, parameters),
        check_lic_8(),
        check_lic_9(),
        check_lic_10(num_points, points, parameters),
        check_lic_11(num_points, points, parameters),
        check_lic_12(),
        check_lic_13(),
        check_lic_14(),
    ]
