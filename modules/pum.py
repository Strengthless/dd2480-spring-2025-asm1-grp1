from modules.types import Connectors

def get_pum(cmv: list[int], lcm: list[list[Connectors]]) -> list[list[bool]]:
    # create pum matrix with true as default
    n = len(cmv) 
    pum = [[True] * n] * n

    # go over matrix (only half because symmetric)
    for i in range(n):
        for j in range(i):
            # set pum according to operation in lcm
            if lcm[i,j] == Connectors.ANDD:
                pum[i,j] = cmv[i] and cmv[j]
            elif lcm[i,j] == Connectors.ORR:
                pum[i,j] = cmv[i] or cmv[j]
            
            # mirror values to other side
            pum[j,i] = pum[i,j]

    return pum