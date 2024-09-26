gamelist = [' ' for i in range(9)]
def tic_tac_toe():
    for i in range(1,10):
        print(f'{gamelist[i-1]}',end=' ')
        if i%3!=0:
            print(f'|',end=' ')
        if i%3==0 and i<9:
            print()
            for j in range(5):
                print('-',end=' ')
            print()
    print('\n\n')

def check_answer_P1():
    if gamelist[0:3]==['O','O','O']:
        return True
    elif gamelist[3:6]==['O','O','O']:
        return True
    elif gamelist[6:9]==['O','O','O']:
        return True
    elif gamelist[0]=='O' and gamelist[1]=='O' and gamelist[2]=='O':
        return True
    elif gamelist[3]=='O' and gamelist[4]=='O' and gamelist[5]=='O':
        return True
    elif gamelist[6]=='O' and gamelist[7]=='O' and gamelist[8]=='O':
        return True
    elif gamelist[0]=='O' and gamelist[4]=='O' and gamelist[8]=='O':
        return True
    elif gamelist[2]=='O' and gamelist[4]=='O' and gamelist[6]=='O':
        return True
    else:
        return False
def check_answer_P2():
    if gamelist[0:3]==['X','X','X']:
        return True
    elif gamelist[3:6]==['X','X','X']:
        return True
    elif gamelist[6:9]==['X','X','X']:
        return True
    elif gamelist[0]=='X' and gamelist[1]=='X' and gamelist[2]=='X':
        return True
    elif gamelist[3]=='X' and gamelist[4]=='X' and gamelist[5]=='X':
        return True
    elif gamelist[6]=='X' and gamelist[7]=='X' and gamelist[8]=='X':
        return True
    elif gamelist[0]=='X' and gamelist[4]=='X' and gamelist[8]=='X':
        return True
    elif gamelist[2]=='X' and gamelist[4]=='X' and gamelist[6]=='X':
        return True
    else:
        return False
list1=[i for i in range(1,10)]
def game():
    
    print('lets begin the game of Tic tac toe')
    player1=input('P1 write your name')
    player2=input('P2 write your name')
    flag=True
    flag1=True
    while flag:
        
        while True:
            pos1=input('{player1} write position:1 to 9')
            if pos1.isdigit() and int(pos1) in list1:
                list1.remove(int(pos1))
                gamelist[int(pos1)-1]='O'
                tic_tac_toe()
                if check_answer_P1():
                    print(f'congratulation!{player1} you are a winner')
                    flag=False
                    flag1=False
                    break
                    
                    
                else:
                   break
            else:
                print(f'invalid option')
            
        while flag1:
            if len(list1)==0:
                print(f'Draw')
                flag1=False
                flag=False

            pos2=input('{player2} write position:1 to 9')
            if pos2.isdigit() and int(pos2) in list1:
                list1.remove(int(pos2))
                gamelist[int(pos2)-1]='X'
                tic_tac_toe()
                if check_answer_P2():
                    print(f'congratulation!{player2} you are a winner')
                    flag=False
                    break

                else:
                    break
            else:
                print('invalid option')
                       
game()
