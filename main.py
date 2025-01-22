# Imports
from modules.types import Connectors, Coordinate, Parameters
from modules.decide import decide

# Inputs
num_points: int 
points: list[Coordinate] 
parameters: Parameters # Used to derive CMV
lcm: list[list[Connectors]] # Used with CMV to derive PUM
puv: list[bool] # Used with PUM to derive LAUNCH

debug: bool = False

# Main function
def main():
    global num_points, points, parameters, lcm, puv, debug
    # TODO: Finish implementation
    # num_points, points, parameters, lcm, puv = read_input()
    # debug = check_for_debug_flag()

    launch, cmv, pum, fuv = decide(num_points, points, parameters, lcm, puv)

    print("Launch: ", launch)

    if (debug):
        print("CMV: ", cmv)
        print("PUM: ", pum)
        print("FUV: ", fuv)

if __name__ == "__main__":
    main()