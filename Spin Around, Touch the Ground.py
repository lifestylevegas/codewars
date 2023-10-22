def spin_around(lst: list):
    spin=0
    for item in lst:
        if item=='right':
            spin+=90
        elif item=='left':
            spin-=90
    return abs(spin)//360
