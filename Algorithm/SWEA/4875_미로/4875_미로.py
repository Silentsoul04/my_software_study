import sys
sys.stdin=open('sample_input.txt','r')

def Goal(y,x):
    global state
    for i in range(len(dxdy)):
        if 0<=y+dxdy[i][0]<=N-1 and 0<= x+dxdy[i][1] <=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]==3:
            print(f'#{tc+1} 1')
            state=True
            break
        elif 0<=y+dxdy[i][0]<=N-1 and 0<= x+dxdy[i][1] <=N-1 and maze[y+dxdy[i][0]][x+dxdy[i][1]]==0:
            maze[y+dxdy[i][0]][x+dxdy[i][1]]='-'
            Goal(y+dxdy[i][0], x+dxdy[i][1])

testcases=int(input())
for tc in range(testcases):
    N=int(input())
    state=False
    maze= [[int(i) for i in input()] for j in range(N)]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==2:
                y=i
                x=j
    dxdy=[(-1,0),(0,1),(1,0),(0,-1)]
    Goal(y,x)
    if state==False:
        print(f'#{tc+1} 0')