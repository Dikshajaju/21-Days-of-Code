create database users;
use users;

CREATE TABLE employees(
  emp_id INT,
  name VARCHAR(50),
  department VARCHAR(50),
  salary INT
);

INSERT INTO employees VALUES
(1, 'Amit','IT',23000),
(2, 'sumit','HR',35000),
(3, 'Diyaa','IT',50000),
(4, 'Anisha','Comp',30000);


SELECT *  
FROM employees;
where salary > 30000;

SELECT *  
FROM employees;
where department = 'IT';

SELECT MAX(salary) FROM employees;
