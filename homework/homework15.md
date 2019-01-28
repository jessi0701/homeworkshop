```python
1.관계형 데이터베이스를 생성,수정,관리한다.
```

```python
2. True False
2.1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [ True ]
2.2. SQL 에서 명령어는 대문자로 써야만 동작한다. [False ]
2.3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [True ]
2.4. SQLite 에서 dot(.) 으로 시작하는 명령어는 SQL 이 아니다.[True ]
2.5. 한 개의 DB 에는 한개의 테이블만 존재한다. [False ]
```

```python
3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.
sqlite> .nullvalue “NULL”
sqlite> CREATE TABLE ssafy (
...> id INTEGER,
...> location TEXT,
...> class INTEGER
...> );
sqlite> INSERT INTO ssafy (id, location)
...> VALUES (1, ‘JEJU’);
sqlite> SELECT class FROM ssafy WHERE id=1;

A) NULL
```

