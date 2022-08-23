use leetcode;

-- rank is a reserved work in mysql

with unique_scores as
(
select distinct score from p178_scores
order by score desc
),
ranked_scores as
(
select x.`rank`, x.score
from
(select @n := 0) init
join
(
select distinct @n := @n + 1 `rank`,
unique_scores.score
from unique_scores
order by score desc
) x
)
select
p.score, ranked_scores.`rank`
from ranked_scores
inner join
p178_scores p on p.score = ranked_scores.score
order by p.score desc
;
