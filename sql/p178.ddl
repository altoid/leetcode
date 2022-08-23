use leetcode;

drop table  if exists p178_scores;

Create table p178_scores (id int, score DECIMAL(3,2)) engine=innodb;

insert into p178_scores values
(1, 3.5),
(2, 3.65),
(3, 4.0),
(4, 3.85),
(5, 4.0),
(6, 3.65)
;
