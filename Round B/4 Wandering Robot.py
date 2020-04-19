# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565

T = int(input())
for i in range(T):
    W, H, L, U, R, D = map(int,input().split())
    
    if H == 1 or W == 1 or (L == 1 and U == 1):
        print('Case #{}: 0.0'.format(i+1))
        continue
    
    field = [[True for x in range(W)] for y in range(H)]
    
    for x in range(U-1,D):
        for y in range(L-1,R):
            field[x][y] = 0
    
    for x in range(H):
        for y in range(W):
            if field[x][y]:
                if x == 0:
                    if y == 0:      field[x][y] = 1
                    else:           field[x][y] = field[x][y-1]/2
                elif x == H-1:
                    if y == 0:      field[x][y] = field[x-1][y]/2
                    elif y == W-1:  field[x][y] = field[x][y-1] + field[x-1][y]
                    else:           field[x][y] = field[x][y-1] + field[x-1][y]/2
                else:
                    if y == 0:      field[x][y] = field[x-1][y]/2
                    elif y == W-1:  field[x][y] = field[x][y-1]/2 + field[x-1][y]
                    else:           field[x][y] = field[x][y-1]/2 + field[x-1][y]/2
            else:
                continue
    
    print('Case #{}: {}'.format(i+1,field[H-1][W-1]))
