# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
# 1. 초기값 [1,1]을 만들고 마지막 수와 마지막 앞 수를 더하면서 그 수를 리스트에 쌓아준다.
# 2. 출력한다.


#s=[1,1]
#for i in range(8):
#    s.append(s[-1] + s[-2])
#print(s)

lis = [1, 1]
# append는 이미 추가시켜버린 것이기 때문에
# 새로 리스트에 배열할 수가 없습니다...!
[lis.append(lis[-1]+lis[-2]) for k in range(0,8)]
print(lis)

