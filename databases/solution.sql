use leetcode;

select k1.salary, k1.departmentid from
(
select distinct salary, departmentid
from employee
)
k1
inner join
(
select distinct salary, departmentid
from employee
)
k2
on k1.salary <= k2.salary
and k1.departmentid = k2.departmentid
group by k1.salary, k1.departmentid
having count(*) <= 3
;

select d.name Department, e.name Employee, result.salary Salary
from 
(
select k1.salary, k1.departmentid from
(
select distinct salary, departmentid
from employee
)
k1
inner join
(
select distinct salary, departmentid
from employee
)
k2
on k1.salary <= k2.salary
and k1.departmentid = k2.departmentid
group by k1.salary, k1.departmentid
having count(*) <= 3
) result
inner join department d on result.departmentid = d.id
inner join employee e on result.salary = e.salary and e.departmentid = d.id
;
