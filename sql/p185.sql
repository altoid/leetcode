use leetcode;

with distinct_salaries_by_department as
(
select distinct
departmentId, salary
from p185_employee
),
top_3_salaries_by_dept as
(
select a1.departmentId, a1.salary
from distinct_salaries_by_department a1
inner join distinct_salaries_by_department a2
on a1.salary <= a2.salary
and a1.departmentId = a2.departmentId
group by a1.departmentId, a1.salary
having count(*) <= 3
)
select
d.name Department, e.name Employee, t.salary Salary
from
top_3_salaries_by_dept t
inner join p185_employee e on e.salary = t.salary and e.departmentId = t.departmentId
inner join p185_department d on d.id = e.departmentId
;
