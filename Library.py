from re import M

def Comma_Sep_List(List):
    Sentence = ''
    for i,M in enumerate(List):
        Sentence += M
        if i == len(List) - 2:
            Sentence += ', and '
        elif i < len(List) - 2:
            Sentence += ', '
    return Sentence