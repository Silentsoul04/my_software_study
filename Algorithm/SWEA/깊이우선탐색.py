def DFS(x):
    global result
    visited[x]=True
    for _ in range(len(mat)):
        if mat[x][_]==1 and visited[_]==False:
            result+=[_]
            DFS(_)
    else:
        return


inp=[1,2,2,3,3,4,4,5,4,7,5,6]
mat=[[0 for i in range(10)] for j in range(10)]
for i in range(0,len(inp),2):
    mat[inp[i]][inp[i+1]]=1
    mat[inp[i+1]][inp[i]]=1
stack=[0 for i in range(10)]
visited=[False for k in range(10)]
result=[]
result+=[1]
DFS(1)
print(result)

def DFS(u):
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            P[v] = u
            DFS(v)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))
D = [0xfffff] * (V+1) # D[s] 는 충분히 큰 값
P = [i for i in range(V+1)]
D[1] =0
DFS(1)















# top=-1
# v=1
# visited[1]=True
# result='1'
#
# while True:
#     for i in range(len(mat[v])):
#         if mat[v][i]==1 and visited[i]==False:
#             top+=1
#             visited[i] = True
#             stack[top]=i
#             v=i
#             result+='-'+str(i)
#             break
#     else:
#         # v=stack[top]
#         # stack[top]=0
#         # top-=1 #여기 틀림
#         stack[top]=0
#         top-=1
#         v=stack[top]
#     if top == -1:
#         print(result)
#         break
