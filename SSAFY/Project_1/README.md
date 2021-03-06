# Python을 통한 데이터 수집 및 파일 저장

## 1. 목표

- 기초 Python에 대한 이해
- Python을 통한 데이터 수집 및 파일 저장
- 웹 크롤러 및 API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
- 영화평점사이트(예-watcha)에 필요한 데이터를 프로그래밍을 통해 수집한다.

## 2. 준비 사항

1. Python 환경 설정
   - python 3.6 이상
2. 필수 라이브러리 활용
   - requests
3. 필수 API
   - 영화진흥위원회 오픈 API
     - 주간/주말 박스오피스 API 서비스
     - 영화 상세정보 API 서비스
   - 네이버 영화 검색 API

## 3. 제작 단계

### 1. 영화진흥위원회 오픈 API (주간/주말 박스오피스 데이터)

1. 조건
   1. 주간(월~일)까지 기간의 데이터를 조회
   2. 조회 기간은 총 10주, 기준일(마지막 일자)은 2019년 1월 13일
   3. 다양한 영화/상업 영화를 모두 포함
   4. 한국/외국 영화를 모두 포함
   5. 모든 상영지역 포함

2. 결과

   1. 데이터는 `영화 대표코드`, `영화명`, `해당일 누적관객수`, `해당일`을 기록한다.
   2. `해당일 누적관객수`는 중복시 최신 정보를 반영한다.

3. 코드 (주석참고)

   ```python
   import requests #요청을 위한 requests import
   import json #json 형식을 파싱하기 위한 import
   import os
   import bs4
   import csv
   from pprint import pprint as pp #정보를 보다 간편하게 보기 위한 pprint
   import datetime #10주간의 시간을 알기위한 datetime import
   import urllib.request #이미지를 저장하기위한 코드
   
   token = os.getenv('MOVIE_TOKEN') #환경변수로 지정한 API키를 불러왔다.
   
   url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
   Movie_boxoffice_data = [] #영화 주간/주말 박스오피스 데이터
   fixed_crds=[] #영화 상세정보를 위한 코드 담는 곳
   movie_names=[] #중복된 영화 이름 확인하기위한 장소
   for h in range(10): #10주간 순회
       d=datetime.date(2019,1,13)
       dd=d+datetime.timedelta(-7*h) #일주일 * 10회 ==> 10주
       dd=dd.strftime('%Y%m%d')
       params = {
       'key':token,
       'targetDt':dd,
       'weekGb':'0' #주간(월~일)까지 기간의 데이터를 조회합니다.
       } #요청을 위해서 파라미터 내부에 내가 넘길 정보를 담았다.
       
       response = json.loads(requests.get(url,params=params).text) #파라미터를 포함하여 특정 url에 요청을 보내었다.
   
       Movie_cords=[] #영화 대표 코드를 정리하기 위한 리스트
       Movie_names=[] #영화명을 정리하기 위한 리스트
       Movie_audiAcc=[] #누적관객수를 정리하기 위한 리스트
       Movie_yearWeekTime = response['boxOfficeResult']['yearWeekTime'] #해당일 몇 주인지 알려주는 코드
   
       
       for i in range(10): #영화 대표코드
           Movie_cords.append(response['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'])
       
       for j in range(10): #영화명
           Movie_names.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieNm'])
       
       for k in range(10): #해당일 누적관객수
           Movie_audiAcc.append(response['boxOfficeResult']['weeklyBoxOfficeList'][k]['audiAcc'])
           
       for z in range(10):
           if Movie_names[z] in movie_names:
               continue
           else:
               movie_names.append(Movie_names[z])
               fixed_crds.append(Movie_cords[z])
               Movie_boxoffice = {
               'movie_code':Movie_cords[z],
               'title':Movie_names[z],
               'audience':Movie_audiAcc[z],
               'recorded_at':params['targetDt']
           }
               Movie_boxoffice_data.append(Movie_boxoffice) #CSV 파일을 위해서 딕셔너리 형태로 만들고 그 딕셔너리 정보를 하나의 리스트로 만들었다.
   
   with open('boxoffice.csv','a',encoding='utf-8') as o: #영진위에서 영화 정보 받아서 csv 파일 만드는 코드
       filed = ('movie_code','title','audience','recorded_at')
       writer = csv.DictWriter(o, fieldnames=filed)
       writer.writeheader()
       for l in Movie_boxoffice_data:
           writer.writerow(l)
   ```

### 2. 영화진흥위원회 오픈 API(영화 상세정보)

1. 앞서 수집한 영화 대표코드를 활용하여 상세 정보를 수집, 해당 데이터는 향후 영화평점서비스에서 영화 정보로 활용될 것이다.

2. 결과

   1. 영화별로 다음과 같은 내용을 저장한다.

      `영화 대표코드`, `영화명(국명)`, `영화명(영문)`, `영화명(원문)`, `개봉연도`, `상영시간`, `장르`, `감독명`, `관람등급`, `배우1`, `배우2`, `배우3`

      - 배우의 경우 최대 3명이며, 영화에 따라 1~2명일 수도 있다.

3. 코드 (주석참고)

   ```python
   details=[] #최종 상세정보들을 담을 딕셔너리
   for crd in fixed_crds:
       url2 = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
       params2 = {
           'key':token,
           'movieCd':crd
       } #url에 보낼 파라미터 정보를 담아서 변수로 만들었다.
       response2 = json.loads(requests.get(url2,params=params2).text) #url에다 파라미터 정보를 담아서 요청을 보내었다.
       
       detail={} #for문 돌면서 넣을 임시 딕셔너리
       
       moviecrd=crd #영화코드
       movieNm=response2['movieInfoResult']['movieInfo']['movieNm'] #영화이름
       movieNmEn=response2['movieInfoResult']['movieInfo']['movieNmEn'] #영화영어이름
       movieNmOg=response2['movieInfoResult']['movieInfo']['movieNmOg'] #영화원문이름
       openDt=response2['movieInfoResult']['movieInfo']['openDt'] #개봉연도
       showTm=response2['movieInfoResult']['movieInfo']['showTm'] #상영시간
       
       genres=response2['movieInfoResult']['movieInfo']['genres'] #장르이름
       genress=[]
       for genre in range(0,len(genres)):
           genress.append(genres[genre]['genreNm'])
       final_genres='/'.join(genress) #장르 다 합치기
       
       directors=response2['movieInfoResult']['movieInfo']['directors'] #감독이름
       directorss=[]
       for director in range(0,len(directors)):
           directorss.append(directors[director]['peopleNm'])
       final_directors='/'.join(directorss) #감독 다 합치기
       
       grades=response2['movieInfoResult']['movieInfo']['audits'] #시청등급
       gradess=[]
       for grade in range(0,len(grades)):
           gradess.append(grades[grade]['watchGradeNm'])
       final_grades='/'.join(gradess) #시청 다 합치기
       
       actors=response2['movieInfoResult']['movieInfo']['actors'] #배우
       actorss=['-','-','-'] #3명의 배우가 모자라면 -가 출력하도록 만들었다.
       for actor in range(0,len(actors)): #3명 초과되면 안됨
           if actor == 3: #그래서 3명의 기준에서 break
               break
           # actorss.append(actors['peopleNm'])
           actorss[actor]=actors[actor]['peopleNm'] #배우 다 합치기
       
       detail={
           'movie_code':moviecrd,
           'movie_name_ko':movieNm,
           'movie_name_en':movieNmEn,
           'movie_name_og':movieNmOg,
           'prdt_year':openDt,
           'genres':final_genres,
           'directors':final_directors,
           'watch_grade_nm':final_grades,
           'actor1':actorss[0],
           'actor2':actorss[1],
           'actor3':actorss[2]
       } #요청한 정보를 모아서
       
       details.append(detail) #details의 리스트에 담도록 하자
   
   with open('movie.csv','a',encoding='utf-8') as f:
       filed = ('movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3')
       writer = csv.DictWriter(f, fieldnames=filed)
       writer.writeheader()
       for l in details:
           writer.writerow(l)
   ```

### 3. 네이버 영화 검색 API

1. 앞서 영진위에서 얻은 영화명(국문)을 바탕으로 네이버 영화 검색 API를 통해 추가적인 데이터를 수집한다. 해당 데이터는 향후 영화평점서비스에서 기준 평점 및 영화 포스터 썸네일로 활용될 것이다.

2. 결과

   - 영화별로 `영진위 영화 대표코드`, `영화 썸네일 이미지의 URL`, `하이퍼텍스트 link`, `유저 평점`

3. 코드 (주석참고)

   ```python
   naver_url = 'https://openapi.naver.com/v1/search/movie.json' #네이버 URL
   
   id = os.getenv('naver_id') #네이버 아이디 환경변수
   secret = os.getenv('naver_secret') #네이버 비번 환경변수
   
   headers = {
       'X-Naver-Client-Id' : id,
       'X-Naver-Client-Secret' : secret
   } #요청하기 위해 박스에 담았다.
   
   naver_movies=[] #영진위 영화 대표코드, 영화 썸네일 이미지의 URL, 하이퍼텍스트 link, 유저 평점 담은 리스트
   for i in details:
       params = {
           'query' : i['movie_name_ko']
       }
       
       res=json.loads(requests.get(naver_url, headers=headers, params=params).text) #get 방식은 params post는 data로 보냄
       
       thumb_url = res['items'][0]['image']
       link_url = res['items'][0]['link']
       user_rating = res['items'][0]['userRating']
       
       naver_movie={
           'movie_code':i['movie_code'],
           'thumb_url':thumb_url,
           'link_url':link_url,
           'user_rating':user_rating
       } #movie_code, thumb_url, link_url, user_rating을 딕셔너리로 만들어서
       
       naver_movies.append(naver_movie) #리스트 형식의 naver_movies에 넣어주도록 하자
   
   with open('movie_naver.csv','a',encoding='utf-8') as z: #movie_naver.csv 만드는 코드
       filed = ('movie_code','thumb_url','link_url','user_rating')
       writer = csv.DictWriter(z, fieldnames=filed)
       writer.writeheader()
       for l in naver_movies:
           writer.writerow(l)
   ```

### 4. 영화 포스터 이미지 저장

1. 앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장한다. 해당 데이터는 향후 영화 목록에서 포스터 이미지로 사용된다.

2. 결과

   1. 응답받은 결과를 파일로 저장, 반드시 `wb`옵션으로 저장한다.
   2. 저장되는 파일명은 images 폴더 내에 `영진위 영화 대표코드.jpg`이다.

3. 코드 (주석참고)

   ```python
   for k in naver_movies: #naver_movies에 저장해놓은 자료를 돌면서 코드와 썸네일 이미지를 저장하자.
       image_url = k['thumb_url']
       movie_code = k['movie_code']
       file = urllib.request.urlretrieve(image_url,'images/'+str(movie_code)+'.jpg') #for문을 돌면서 image 폴더 내부에다가 jpg 파일로 저장하도록하자.
   ```

## 4.프로젝트 후기

- python을 이용한 웹 크롤링 이해도를 높일 수 있었다.
- 다양한 메서드를 활용을 하면서 클래스에 대한 이해도를 높일 수 있었다.
- 요청 받은 정보에서 원하는 정보만 골라서 나만의 것으로 만드는 방법을 알게되었다.