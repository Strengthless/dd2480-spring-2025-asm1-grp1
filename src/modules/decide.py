# Imports
from typing import NamedTuple
from src.modules.types import Connectors, Coordinate, Parameters
from src.modules.cmv import get_cmv
from src.modules.fuv import get_fuv
from src.modules.pum import get_pum


# Type declarations
class Decision(NamedTuple):
    launch: bool
    cmv: list[int]
    pum: list[list[bool]]
    fuv: list[bool]


# Helper functions
def determine_launch(fuv: list[bool]) -> bool:
    return all(fuv)


# Main function
def decide(
    num_points: int,
    points: list[Coordinate],
    parameters: Parameters,
    lcm: list[list[Connectors]],
    puv: list[bool],
) -> Decision:
    cmv = get_cmv(num_points, points, parameters)
    pum = get_pum(cmv, lcm)
    fuv = get_fuv(pum, puv)
    launch = determine_launch(fuv)
    return Decision(launch, cmv, pum, fuv)
