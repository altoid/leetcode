use leetcode;

drop table if exists p601_stadium;

create table p601_stadium (
id int,
visit_date varchar(10),
people int
) engine=innodb;

insert into p601_stadium values
(1, '2017-01-01', 10),
(2, '2017-01-02', 109),
(3, '2017-01-03', 150),
(4, '2017-01-04', 99),
(5, '2017-01-05', 145),
(6, '2017-01-06', 1455),
(7, '2017-01-07', 199),
(8, '2017-01-09', 188),
(10, '2017-01-09', 111),
(11, '2017-01-09', 111),
(12, '2017-01-09', 111),
(13, '2017-01-09', 111)
;