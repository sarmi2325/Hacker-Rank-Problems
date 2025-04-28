 N = int(input())
    l=[]
    for i in range(N):
        comd=input().split()
        if comd[0]=='insert':
            l.insert(int(comd[1]),int(comd[2]))
        elif comd[0]=='print':
            print(l)
        elif comd[0]=='remove':
            l.remove(int(comd[1]))
        elif comd[0]=='append':
            l.append(int(comd[1]))
        elif comd[0]=='sort':
            l.sort()
        elif comd[0]=='pop':
            l.pop()
        elif comd[0]=='reverse':
            l.reverse()
