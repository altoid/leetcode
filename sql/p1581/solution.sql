use leetcode_1581;

-- 3 different solutions:  left join, NOT IN, NOT EXISTS

/*
select customer_id, count(*) count_no_trans
from visits v
left join transactions t on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id
;
*/

/*
with freeloaders as
(
select customer_id from visits v where not exists (select * from transactions t where t.visit_id = v.visit_id)
)
select customer_id, count(*) count_no_trans
from freeloaders
group by customer_id
;
*/

with freeloaders as
(
select *
from visits
where visit_id not in (
      select visit_id
      from transactions
      )
)
select customer_id, count(*) count_no_trans
from freeloaders
group by customer_id
;
