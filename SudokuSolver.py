from copy import deepcopy


def print_board(b:list) -> None:
    for i in range(len(b)):
        if(i%3 == 0 and i!=0):
            print("\n", "-"*22, sep="")
        else:
            print()
        for j in range(len(b)):
            if((j+1)%3 == 0):
                print(b[i][j], end=" | ")
            else:
                print(b[i][j], end=" ")


def find_empty(b:list) -> tuple:
    for i in range(len(b)):
        for j in range(len(b)):
            if(b[i][j] == 0):
                return (i,j)
    return None
    


def board_valid(b:list, pos_changed:tuple, val:int) -> bool:
    for i in range(len(b)):
        if(b[i][pos_changed[1]] == val and ((i, pos_changed[1]) != pos_changed)):
            return False
        if(b[pos_changed[0]][i] == val and ((pos_changed[0], i) != pos_changed)):
            return False        
    for i in range(int(len(b)/3)):
        for j in range(int(len(b)/3)):
            if(b[(pos_changed[0]//3)*3+i][(pos_changed[1]//3)*3+j] == val and (((pos_changed[0]//3)*3+i, (pos_changed[1]//3)*3+j) != pos_changed)):
                return False            
    
    return True




def solve_board(b:list, original_pos:tuple):
    pos = find_empty(b)
    if(pos == None):
        return True
    
    for num in range(1,10):
        if(board_valid(b, pos, num)):
            b[pos[0]][pos[1]] = num
            if(solve_board(b, original_pos)):
                if(pos!=original_pos):
                    return True
                else:
                    return b
            b[pos[0]][pos[1]] = 0
            
    return False
        


#Main Script

# board image address: https://miro.medium.com/max/748/1*K7nuelC1TIFlwwGMThdBCA.png
board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]


print("Board:")
print_board(board)
print("\n"*3, "Solved Board:", sep="")
solved = solve_board(deepcopy(board), find_empty(board))
print_board(solved)