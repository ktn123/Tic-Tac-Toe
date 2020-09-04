winner = ''
dicc = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
win = [[1,2,3],[1,4,7],[3,6,9],[7,8,9],[2,5,8],[4,5,6],[1,5,9],[3,5,7]]
def want_to_play():
    play = input('Do you want to play Tic Tac Toe?')
    if play.lower()=='yes':
        start_game()
    else:
        print("Thank You!!")

def print_board():
    print(f" {dicc['1']} | {dicc['2']} | {dicc['3']} ")
    print("__|__|__")
    print(f" {dicc['4']} | {dicc['5']} | {dicc['6']} ")
    print("__|__|__")
    print(f" {dicc['7']} | {dicc['8']} | {dicc['9']} ")

def player_input(position,i):
    if i%2==0:
        dicc[str(position)] = 'x'
    else:
        dicc[str(position)] = 'o'
    if i>2:
        for i in win:
            arr = i
            if dicc[str(arr[0])] == dicc[str(arr[1])]==dicc[str(arr[2])] =='x' or dicc[str(arr[0])] == dicc[str(arr[1])]==dicc[str(arr[2])] =='o':
                global winner
                winner = str(dicc[str(arr[0])])
                 
def start_game():
    i=0
    ask_pat1 = ask_pat2 = False
    player1 = input("You want x or o ?")
    if player1=='x':
        player2 = 'o'
    else:
        player2 = 'x'
    while i<9:
        position = input("Where do you want to enter (1-9)?")
        
        player_input(position,i)
        print_board()
        if winner =="x":
            print("Player x won!!")
            break
        elif winner == "o":
            print("Player o won!!")
            break
        i = i+1
    if winner == '':
        print("It's a Tie!!")
want_to_play()
        
    
    
