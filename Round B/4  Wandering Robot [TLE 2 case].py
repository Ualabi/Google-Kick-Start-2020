T = int(input())
for i in range(T):
    W, H, L, U, R, D = map(int,input().split())
    
    if H == 1 or W == 1 or (L == 1 and U == 1):
        print('Case #{}: 0.0'.format(i+1))
        continue
    
    new = []
    for x in range(H):
        pst, new = new, []
        for y in range(W):
            if U-1<=x and x<D and L-1<=y and y<R:   new.append(0)
            else:                                   new.append(True)
                
        for y in range(W):
            if new[y]:
                if x == 0:
                    if y == 0:      new[y] = 1
                    else:           new[y] = new[y-1]/2
                elif x == H-1:
                    if y == 0:      new[y] = pst[y]/2
                    elif y == W-1:  new[y] = new[y-1] + pst[y]
                    else:           new[y] = new[y-1] + pst[y]/2
                else:
                    if y == 0:      new[y] = pst[y]/2
                    elif y == W-1:  new[y] = new[y-1]/2 + pst[y]
                    else:           new[y] = new[y-1]/2 + pst[y]/2
            else:
                continue
    
    print('Case #{}: {}'.format(i+1,new[-1]))
