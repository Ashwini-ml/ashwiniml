theboard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}
def printboard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['low-l']+'|'+board['low-m']+'|'+board['low-r'])
turn='x'
for i in range (9):
    printboard(theboard)
    print('turn for'+turn+'.move on which space?')
    move=input()
    theboard[move] =turn
    if turn=='x':
        turn='o'
    else:
        turn='x'
printboard(theboard)
