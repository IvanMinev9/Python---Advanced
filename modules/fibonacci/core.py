def create(n):
    seq = [0, 1]
    
    for num in range(n -2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(num, seuq):
    try:
        return seuq.index(num)
    except ValueError as err:
        return f"No such number - {err}"