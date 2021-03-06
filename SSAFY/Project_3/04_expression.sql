-- 모든 영화의 총 누적관객수
SELECT SUM(누적관객수) FROM movies;

-- 가장 많은 누적관객수인 영화이름과 누적관객수를 출력
SELECT 영화이름, MAX(누적관객수) FROM movies;

-- 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력
SELECT 장르, MIN(상영시간) FROM movies;

-- 제작국가가 한국인 영화의 평균 누적관객수를 출력
SELECT ROUND(AVG(누적관객수),2) FROM movies WHERE 제작국가 = '한국';

-- 관람등급이 청소년관람불가인 영화의 개수를 출력
SELECT COUNT(*) FROM movies WHERE 관람등급 = '청소년관람불가';

-- 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력
SELECT COUNT(*) FROM movies WHERE 상영시간 >=100 AND 장르 = '애니메이션';