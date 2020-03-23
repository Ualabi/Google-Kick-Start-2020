T = int(input())

for x in range(T):
    [n,k] = list(map(int,input().split()))
    arr = sorted(list(map(int,input().split())))
    y = 0
    while y<len(arr) and arr[y] <= k:
        k -= arr[y]
        y += 1    
    print('Case #{}: {}'.format(x+1,y))
