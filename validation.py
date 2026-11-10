def chek_place():
    place = input("choose a place!")
    if not place.isdigit():
        raise ValueError("only numbers not a str !")
    if not (1 <= int(place) <= 9):
        raise ValueError("only num between 1 - 9  !") 
    return int(place)


def updet_gamer(counter):
    if counter % 2 == 0:
        return  "o"
    else:
        return  "x"    
        
