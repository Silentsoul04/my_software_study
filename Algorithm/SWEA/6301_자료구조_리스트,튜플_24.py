# 항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.
# 1. 0 4개를 가지는 리스트를 만든다.
# 2. 0 4개를 리스트를 3개를 가진 리스트를 만든다.
# 3. 2번 리스트를 2번을 가진 리스트를 만든다.
lis = [list(list(0 for a in range(0, 4)) for b in range(0, 3)) for c in range(0,2)]
print(lis)
