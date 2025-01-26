# Imports
from modules.types import Connectors, Coordinate, Parameters
from modules.decide import decide
import argparse

# Global variables
num_points: int 
points: list[Coordinate] 
parameters: Parameters # Used to derive CMV
lcm: list[list[Connectors]] # Used with CMV to derive PUM
puv: list[bool] # Used with PUM to derive LAUNCH
verbose: bool = False

# Helper functions
def get_cli_args() -> tuple[str, bool]:
    parser = argparse.ArgumentParser(description='Launch decision maker')
    parser.add_argument('-i', '--input', type=str, help='Name of file stored in the inputs folder', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='Print debug information')
    args = parser.parse_args()
    return args.input, args.verbose

def parse_input(target_file: str) -> tuple[int, list[Coordinate], Parameters, list[list[Connectors]], list[bool]]:
    with open(f'inputs/{target_file}', 'r') as file:
        # Parse number of points
        try: 
            num_points = int(file.readline())
        except:
            raise TypeError("Number of points must be an integer.")
        
        if (num_points < 2 or num_points > 100):
            raise ValueError("Number of points must be [2, 100].")
        
        # Parse points
        points = []
        for _ in range(num_points):
            line_data = file.readline().split()
            if (len(line_data) != 2):
                raise ValueError("Invalid coordinates, or point count mismatch.")
            try:
                x, y = map(float, line_data)
                points.append(Coordinate(x=x, y=y))
            except:
                raise ValueError("Coordinates must be floats.")

        # Parse parameters
        line_data = file.readline().split()
        if (len(line_data) != 19):
            raise ValueError("Parameters count must be 19.")
        try: 
            new_params = Parameters()
            for (key, key_type), data in zip(Parameters.__annotations__.items(), line_data):
                new_params[key] = key_type(data)
            parameters = new_params
        except:
            raise ValueError("Invalid parameter found. Please check whether they are correctly typed as floats or ints.")

        # Parse LCM
        lcm = []
        for _ in range(15):
            line_data = file.readline().split()
            if (len(line_data) != 15):
                raise ValueError("Each LCM row must have 15 connectors.")
            for connector in line_data:
                if (connector not in Connectors.__members__):
                    raise ValueError("Invalid connector. Must be one of ANDD, ORR, NOTUSED.")
            lcm.append(list(map(lambda x: Connectors[x], line_data)))

        # Parse PUV
        line_data = file.readline().split()
        if (len(line_data) != 15):
            raise ValueError("PUV count must be 15.")
        for p in line_data:
            if (p not in ['T', 'F']):
                raise ValueError("PUV values must be either T or F.")
        puv = list(map(lambda x: x == 'T', line_data))

    return num_points, points, parameters, lcm, puv

# Main function
def main():
    global num_points, points, parameters, lcm, puv, verbose
    file_name, verbose = get_cli_args() 
    num_points, points, parameters, lcm, puv = parse_input(file_name)

    launch, cmv, pum, fuv = decide(num_points, points, parameters, lcm, puv)

    print("Launch:", launch)

    if (verbose):
        print("CMV:", cmv)
        print("PUM:", pum)
        print("FUV:", fuv)

if __name__ == "__main__":
    main()