# from itertools import combinations

# def combinations(idx,temp):
#     global cnt, result
#     if temp != [] and sum(temp)==S:
#         cnt+=1
#         return
#     elif idx==N:
#         return
#     else:
#         combinations(idx+1,temp[:])
#         temp.append(lis[idx])
#         combinations(idx+1,temp[:])

# 상태 공간 트리, 백트래킹 씨발 좆같네, 여기서 순열 만드는 법 씨발, 여기서 조합 만드는 법


# 라이브러리 사용
# N,S = list(map(int,input().split()))
# lis=list(map(int,input().split()))
# cnt=0
# for _ in range(1,N+1):
#     result=combinations(lis, _)
#     for __ in result:
#         if sum(__) == S:
#             cnt+=1
# print(cnt)