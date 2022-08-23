/*
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+


{"headers": {"Employee": ["id", "name", "salary", "departmentId"],
"Department": ["id", "name"]}, "rows":
{"Employee": [[1, "Joe", 60000, 1], [2, "Sam", 50000, 1], [4, "Max", 50000, 2]],
"Department": [[1,"IT"], [2, "HR"]]}}

*/

use leetcode;

drop table if exists department;

create table department
(
id int not null auto_increment primary key,
name varchar(15) not null
) engine = innodb;

drop table if exists employee;

create table employee
(
id int not null auto_increment primary key,
name varchar(15) not null,
salary int not null,
departmentId int not null
) engine = innodb;

/*
insert into department
values
(1, 'IT'),
(2, 'Sales')
;

insert into employee
values
(1  , 'Joe'   , 60000  , 1)            ,
(2  , 'Sam'   , 50000  , 1)            ,
(4  , 'Max'   , 50000  , 2)
;

*/

insert into department
values
(1, 'IT'),
(2, 'Sales')
;


insert into employee
values
(1  , 'Joe'   , 70000  , 1)            ,
(2  , 'Jim'   , 90000  , 1)            ,
(3  , 'Henry' , 80000  , 2)            ,
(4  , 'Sam'   , 60000  , 2)            ,
(5  , 'Max'   , 90000  , 1)
;
