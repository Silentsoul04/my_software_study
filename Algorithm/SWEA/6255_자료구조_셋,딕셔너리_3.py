#아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
#"TV":2000000
#"냉장고":1500000,
#"책상":350000
#"노트북":1200000
#"가스레인지":200000
#"세탁기":1000000

#1. 전자제품 딕셔너리를 만든다.
#2. for문을 돌리면 value 값들을 정렬한다.
#3. 출력한다.

mers = {"TV":2000000,"냉장고":1500000,"책상":350000,"노트북":1200000,"가스레인지":200000,"세탁기":1000000}
result = sorted(mers.items(), key = lambda t : t [1])
result.reverse()
for i in result:
    print("{}: {}".format(i[0],i[1]))
