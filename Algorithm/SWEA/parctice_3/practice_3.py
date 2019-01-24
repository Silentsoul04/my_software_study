li=[[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def my_sort(li):
    nums=99999  # 이렇게 겸손치 못한 친구가 있다.
    lis=[]  # 숫자를 받을 바가지를 준비해놓자
    for a in range(25):  # 총 숫자가 25개니까 25번 반복
        for i in range(len(li)):  # 행
            for j in range(len(li[i])):  # 열
                if nums>li[i][j]:  # 대소비교
                    nums=li[i][j]  # nums의 값이 크면 겸손하게 만들어주자
                    a=i  # 그 위치를 기록해놓자
                    b=j
        lis.append(nums)
        nums=99999  # 겸손해진 줄 알았지만 쉽게 변하지 않는다.
        li[a][b]=999999  # 그 마음의 빈자리를 사랑으로 가득 채워주자
    return lis

def snail(li):
    x, y = len(result)//2,len(result)//2  # 중심역에 도착하였습니다.
    n = 1  # 달팽이의 처음 이동거리는 1
    a, b = (n, n)  # 얘들이 둘 다 0이 되면 달팽이가 강해진다. n이 달팽이의 이동거리가 1 증가함
    q = 1  # 직진만 아는 친구에게 방향을 알려주도록 하자
    result[x][y] = li[-1]  # 중심역에 달팽이를 살포시 놓도록하자
    for i in li[::-1][1:]:  # 24 ~ 1까지 순회
        if a != 0:  # a!=0이면 달팽이는 왼쪽 오른쪽 둘 중 하나로 향한다.
            y -= 1 * q # y 시작은 -1이라서 -=했다.
            result[x][y] = i  # 달팽이의 흔적을 남기도록 하자. 비록 느리지만 노력하는 달팽이
            a -= 1  # 달팽이생이 순탄치만은 않다.
            continue
        elif b != 0:  # b!=0이면 달팽이는 위 아래 위위 아래 둘 중 하나로 향한다.
            x += 1 * q  # x 시작은 +1이라서 +=했다.
            result[x][y] = i  # 달팽이의 흔적을 남기도록 하자. 비록 느리지만 노력하는 달팽이
            b -= 1  # 달팽이생이 순탄치만은 않다.
        else:
            q *= -1  # a,b가 전부 0,0 이 되면 방향을 꺾어야한다.
            y -= 1 * q  # 근데 a,b에게 새로운 값을 줄 때 하나의 값이 무시당하니 얘를 추가한다.
            result[x][y] = i  # 무시당하는 친구에게 i 선물 준다.
            n += 1  # 달팽이의 이동거리 1 증가
            a, b = (n, n)  # 달팽이에게 먹이를 주자.
            a -= 1  # 미리 움직인 y값 만큼 뒤로 빼준다.
    return result

li=my_sort(li)
print(snail(li))