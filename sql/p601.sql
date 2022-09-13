use leetcode;

select * from
(select @n := 0, @expected_id := 0) init
join
(
select
row_number() over w,
s.visit_date, s.people,
@n := if(people >= 100, @n + 1, 0) counter,
@expected_id := if(@n = 1, id, if(@n > 1, @expected_id + 1, id)) expected_id,
s.id
from p601_stadium s
window w as (order by id)
) x
;
