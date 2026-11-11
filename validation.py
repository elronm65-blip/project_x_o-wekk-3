from function import print_matrix

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
def aaa(victor , matrix , gamer):       
    if victor  ==  'game over':
        print(f'{victor} the winner is {gamer}! ')
        print_matrix(matrix)
        return 1
    elif  victor  == "draw!!!":
        print(victor)
        print_matrix(matrix)
        return 1

    print(victor) 