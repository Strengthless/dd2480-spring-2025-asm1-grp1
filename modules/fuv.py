def get_fuv(pum: list[list[bool]], puv: list[bool]) -> list[bool]:
    # check if inputs have correct size
    assert(len(pum) == 15)
    assert(len(pum[0]) == 15)
    assert(len(puv) == 15)
    
    # initialize fuv with as all False
    fuv = [False] * 15

    for i in range(15):
        # fuv is True if puv[i] is false or the entire row of pum[i] is True
        fuv[i] = (not puv[i]) or (pum[i] == [True] * 15) 

    return fuv