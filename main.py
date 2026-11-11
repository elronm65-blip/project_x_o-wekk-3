from function import print_matrix , check_victory
from validation import  chek_place ,updet_gamer ,aaa

matrix = [1,2,3,4,5,6,7,8,9]
counter  = 1
flag =2
while flag == 2:

    gamer = updet_gamer(counter)
    print_matrix(matrix)

    try:
        place = chek_place()
    except ValueError as e:
        print (e)
        continue
            
    
    if isinstance (matrix[place-1]  , str):
        print('the place taken')
        continue
  
    matrix[place-1] = gamer

    
    victor = check_victory(matrix)
    old = aaa(victor ,matrix ,gamer) 
    if  old  == 1:
        flag  = old    

    counter += 1
    


    
