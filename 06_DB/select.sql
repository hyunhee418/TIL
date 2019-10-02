-- SQLite
-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;

-- SELECT * FROM classmates;
-- SELECT * FROM classmates LIMIT 2;  -- 앞에 두 개만
-- SELECT * FROM classmates LIMIT 1 OFFSET 2;  -- 앞의 두 개 띄고 한 개 보기

-- WHERE
-- SELECT * FROM classmates WHERE name='하다다연';
-- SELECT * FROM classmates WHERE address='대구';

-- DISTINCT
SELECT DISTINCT age FROM classmates;

