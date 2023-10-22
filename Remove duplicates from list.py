def distinct(seq: list):
    lst=[]
    for x in seq:
        if x not in lst:
            lst.append(x)
    seq=lst
    return seq
