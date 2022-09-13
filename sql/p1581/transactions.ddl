use leetcode_1581;

drop table if exists transactions;

create table transactions (
transaction_id int,
visit_id int,
amount int
) engine=innodb;

insert into transactions values
(2, 5, 310),
(3, 5, 300),
(9, 5, 200),
(12, 1, 910),
(13, 2, 970)
;
