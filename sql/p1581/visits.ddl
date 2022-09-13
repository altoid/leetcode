use leetcode_1581;

drop table if exists visits;

create table visits (
visit_id int,
customer_id int
) engine=innodb;

insert into visits values
(1, 23),
(2, 9),
(4, 30),
(5, 54),
(6, 96),
(7, 54),
(8, 54)
;
