-- SQLite
-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age=30;
-- SELECT * FROM users WHERE age>=30;

-- SELECT first_name FROM users WHERE age>=30;

-- users에서 age가 30 이상이고 성이 김인 사람의 성과 나이만 가져오면?
-- SELECT age, last_name FROM users
-- WHERE age >= 30 AND last_name='김'
-- LIMIT 10;

-- COUNT
-- SELECT COUNT(*) FROM users;

-- AVG, SUM, MIN, MAX (숫자 컬럼만 가능)
-- 30살 이상인 사람들의 평균나이

-- SELECT AVG(age) FROM users WHERE age >= 30; 

-- user 에서 잔액이 가장 높은 사람의 first_name과 잔액
-- SELECT first_name, MAX(balance) FROM users;

-- users에서 30 이상인 사람의 계좌 평균 잔액
-- SELECT AVG(balance) FROM users WHERE age >= 30;

-- wild cards
-- users에서 20 대인 사람
-- SELECT * FROM users WHERE age LIKE '2_';
-- 지역번호가 02인 사람
-- SELECT * FROM users WHERE phone LIKE '02-%';
-- 이름이 '준'으로 끝나는 사람만
-- SELECT  phone, age FROM users WHERE first_name LIKE '%준';
-- 중간 번호가 5114인 사람은?
-- SELECT first_name FROM users WHERE phone LIKE '_%-5114-_%';

-- ORDER
-- SELECT age, first_name FROM users
-- ORDER BY age ASC LIMIT 10;

-- SELECT age, first_name FROM users
-- ORDER BY age DESC LIMIT 10;

-- SELECT age, balance FROM users
-- ORDER BY age, balance LIMIT 10;

-- SELECT age, last_name FROM users
-- ORDER BY last_name, age LIMIT 10;
-- ORDER BY 앞에 있는 조건을 먼저 정렬하고 그 중에 다음 조건을 정렬

SELECT first_name, last_name FROM users
ORDER BY balance DESC LIMIT 10;