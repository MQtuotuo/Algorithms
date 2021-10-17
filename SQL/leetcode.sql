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

--184
with tmp as (
select Id, Name, Salary, DepartmentId,
MAX(Salary) over (partition by DepartmentId) as maxSalary
from Employee
)
select Department.Name as Department, tmp.Name as Employee,
Salary
from tmp left join Department on tmp.DepartmentId = Department.Id
where Salary = maxSalary

--185
with tmp as (
select *,
dense_rank() over (partition by DepartmentId order by Salary desc) as rk
from Employee
)
select Department.Name as Department, tmp.Name as Employee, Salary
from tmp left join Department on tmp.DepartmentId = Department.Id
where rk<=3;

--196
DELETE FROM Person
WHERE Id NOT IN
(SELECT *
 FROM (SELECT MIN(Id) AS Id
     FROM Person
     GROUP BY Email) P
);

--197
SELECT
    w1.Id
FROM weather w1, weather w2
WHERE DATEDIFF(day, w1.RecordDate, w2.RecordDate)=1   --w2 - w1 = 1
AND w1.Temperature > w2.Temperature;

--262
select
Request_at as Day,
round(sum(case
when Status !='completed' then 1 else 0
end)/count(*),2) as "Cancellation Rate"
from Trips
where
request_at between "2013-10-01" and "2013-10-03" and
client_ID not in (
select users_id from users u
where u.banned = 'Yes')
AND
driver_Id not in ((
select users_id from users u
where u.banned = 'Yes')
)
group by Request_at;

--620
SELECT *
FROM Cinema
WHERE id % 2 <> 0 AND description <> 'boring'
ORDER BY rating DESC;

--626 medium
select s1.id,
       case when s1.id %2 = 0 then s3.student
       when s2.id is not null then s2.student
       else s1.student end as student
from seat s1
left join seat s2 on s1.id = s2.id - 1
left join seat s3 on s3.id = s1.id - 1;

--627
Update Salary
SET sex=CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;

--601 hard
--Cte1 creates a rank group that is unique for each consecutive >=100 row in the table.
with cte1  as (
select id, visit_date, people,
id - row_number() over(order by id) rk
from stadium where people>=100)
--Whenever the rank’s count is greater than or equal to 3
--we know that the partition has more than three >=100 rows consecutively.
select id, visit_date, people
from cte1
where rk in (select rk from cte1 group by rk having count(1)>=3)
order by id
