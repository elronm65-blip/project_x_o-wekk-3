

matrix = [1,2,3,4,5,6,7,8,9]

def print_matrix(matrix):
    count =1
    for num in matrix:
        print (num , end = "      ")
        if count % 3 == 0:
            print("\n---------------")
        count += 1   


def check_victory(matrix):
    if matrix[0] == matrix[1] == matrix[2] and matrix[0] in ("o", "x"):
        return 'game over'
    if matrix[3] == matrix[4] == matrix[5] and matrix[3] in ("o", "x"):
        return 'game over'
    if matrix[6] == matrix[7] == matrix[8] and matrix[6] in ("o", "x"):
        return 'game over'
    if matrix[2] == matrix[5] == matrix[8] and matrix[2] in ("o", "x"):
        return 'game over'
    if matrix[0] == matrix[3] == matrix[6] and matrix[0] in ("o", "x"):
        return 'game over'
    if matrix[2] == matrix[4] == matrix[7] and matrix[2] in ("o", "x"):
        return 'game over'
    if matrix[0] == matrix[4] == matrix[8] and matrix[0] in ("o", "x"):
         return 'game over'
    if matrix[1] == matrix[4] == matrix[7] and matrix[1] in ("o", "x"):
         return 'game over'
    return ' no win yet!'









# place = int(input("choose place"))
# if matrix[place-1] == "x":
#     print('the place taken')
# if matrix[place-1] == "0": 
#     print('the place taken')   
# matrix[place-1] = "x"



# print_matrix(matrix)
  
# print(matrix)
   
    
    


            
