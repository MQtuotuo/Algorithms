--175
select p.FirstName, p.LastName, a.City, a.State
from Person p
left join Address a
on p.PersonId = a.PersonId;

--176
select max(salary) as SecondHighestSalary
from employee
where salary <> (select max(salary) from employee);

WITH cte AS
(
SELECT salary, rank() over(ORDER BY salary DESC) as rk
FROM Employee
)
SELECT IF(max(cte.rk)<2, null, salary)  as SecondHighestSalary
FROM cte
WHERE cte.rk = 2;

select
(select distinct Salary
from Employee
order by Salary desc limit 1 offset 1) as SecondHighestSalary;

--177
SELECT DISTINCT salary FROM employee ORDER BY salary DESC LIMIT 1 offset N-1;

select distinct salary
      from (
      select Salary,
      dense_rank() over (order by Salary desc) as rk
      from Employee
          ) tmp where rk = N;
/*
RANK gives you the ranking within your ordered partition.
Ties are assigned the same rank, with the next ranking(s) skipped.
So, if you have 3 items at rank 2, the next rank listed would be ranked 5.

DENSE_RANK again gives you the ranking within your ordered partition, but the ranks are consecutive.
*/

--178
select score,
	   dense_rank() over (order by score desc) as `rank`
from scores;

--180
select  distinct first as consecutiveNums
from(
-- identify 3 consecutive ids in a row and their corresponding num
select  A.num as first
       ,B.num as second
       ,C.num as third
from logs A
inner join logs B on A.id = B.id-1
inner join logs C on A.id = C.id-2
) tmp
-- display num that appears at least three times consecutively
where first = second and second = third and first = third

--181
SELECT e1.Name as Employee
FROM Employee as e1
JOIN Employee as e2
ON  e1.ManagerId = e2.Id AND e1.Salary > e2.Salary;

-- 182
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;

--183
select Customers.Name as Customers
from Customers
left join Orders
on Customers.Id = Orders.CustomerId
where Orders.CustomerId is null;

--