use leetcode;

with highest_salary_by_dept as
(
select max(salary) maxsal, departmentId
from employee
group by departmentId
)
select distinct
d.name Department, e.name Employee, e.salary Salary
from employee e
inner join highest_salary_by_dept h
on h.maxsal = e.salary
and h.departmentId = e.departmentId
inner join department d
on d.id = e.departmentId
;
