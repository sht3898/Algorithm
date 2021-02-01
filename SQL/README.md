# [JOIN](https://coding-factory.tistory.com/87)

* 컬럼끼리의 결합(열의 확장)

## INNER JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/99799F3E5A8148D703)

```SQL
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
INNER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키....

--예제--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A
INNER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```



## LEFT OUTER JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/997E7F415A81490507)

```SQL
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
LEFT OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키 .....

--예제--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A
LEFT OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT

```



## RIGHT OUTER JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/9984CE355A8149180A)

```SQL
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
RIGHT OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키 .....

--예제--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A
RIGHT OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT

```



## FULL OUTER JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/99195F345A8149391B)

```SQL
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
FULL OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키 .....

--예제--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A
FULL OUTER JOIN JOIN_TABLE B ON A.NO_EMP = B.NO_EMP AND A.DEPT = B.DEPT
```



## CROSS JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/993F4E445A8A2D281A)

```SQL
--문법(첫번째방식)--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭
CROSS JOIN 조인테이블 별칭

--예제(첫번째방식)--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A
CROSS JOIN JOIN_TABLE B

=====================================================================================

--문법(두번째방식)--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 기준테이블 별칭,조인테이블 별칭

--예제(두번째방식)--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A,JOIN_TABLE B
```



## SELF JOIN

![JOIN](https://t1.daumcdn.net/cfile/tistory/99341D335A8A363D06)

```SQL
--문법--
SELECT
테이블별칭.조회할칼럼,
테이블별칭.조회할칼럼
FROM 테이블 별칭,테이블 별칭2

--예제--
SELECT
A.NAME, --A테이블의 NAME조회
B.AGE --B테이블의 AGE조회
FROM EX_TABLE A,EX_TABLE B
```







# [집합연산자(UNION)](https://webstudynote.tistory.com/74) [참고2](https://keep-cool.tistory.com/45)

![img](https://t1.daumcdn.net/cfile/tistory/99934B335A2D099E12)

| 종류      | 내용                               |
| --------- | ---------------------------------- |
| UNION     | 두 집합의 합집합. 중복제거O, 정렬O |
| UNION ALL | 두 집합의 합집합. 중복제거X, 정렬X |
| INTERSECT | 두 집합의 교집합                   |
| MINUS     | 두 집합의 차집합                   |

* 기존 행에 밑으로 추가(행의 확장)
* 두 집합의 SELECT절에 오는 컬럼의 개수 같아야함
* 두 집합의 SELECT절에 오는 컬럼의 데이터형 같아야함
* 두 집합의 컬럼명을 달라도 괜찮음

## 기본구조

```SQL
SELECT ……

[UNION | UNION ALL | INTERSECT | MINUS]



SELECT ……

[ORDER BY 컬럼 [ASC/DESC]];
```

## UNION

```SQL
select employee_id, job_id

from employees

union

select employee_id, job_id

from job_history;
```

![img](https://t1.daumcdn.net/cfile/tistory/994E7E335A2D0B9A12)



## INTERSECT

```SQL
select employee_id, job_id

from employees

intersect

select employee_id, job_id

from job_history;
```

![img](https://t1.daumcdn.net/cfile/tistory/99A642335A2D0C7725)

## MINUS

```SQL
select employee_id, job_id

from employees

minus

select employee_id, job_id

from job_history;
```

![img](https://t1.daumcdn.net/cfile/tistory/99E638335A2D0CDD37)



# 함수 선언

```SQL
SET @함수 := "이름";
```

* SQL에서는 `=`이 비교연산자로 인식되어 혼동을 피하고자 `:=`와 같은 형태로 사용
* SET에서는 `=` 만 써도 되긴함
* 끝에 세미콜론을 붙여야함