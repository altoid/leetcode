use leetcode_1393;

/*
they make it easy:

- there is a 1:1 correspondence for buys and sales of each stock:  no buy without a sell and vice versa
- buys precede sales
*/

with purchases as
(
select stock_name, sum(price) price
from stocks
where operation = 'buy'
group by stock_name
),
sales as
(
select stock_name, sum(price) price
from stocks
where operation = 'sell'
group by stock_name
)
select
p.stock_name,
s.price - p.price as capital_gain_loss
from purchases p
join sales s on p.stock_name = s.stock_name
;
