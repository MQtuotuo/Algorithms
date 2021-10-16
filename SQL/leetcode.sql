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

--