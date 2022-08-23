use leetcode;

drop table if exists p185_department;

create table p185_department
(
id int not null auto_increment primary key,
name varchar(15) not null
) engine = innodb;

drop table if exists p185_employee;

create table p185_employee
(
id int not null auto_increment primary key,
name varchar(15) not null,
salary int not null,
departmentId int not null
) engine = innodb;


insert into p185_department
values
(1, 'IT'),
(2, 'Sales')
;


insert into p185_employee
values
(1  , 'Joe'   , 85000  , 1),
(2  , 'Henry' , 80000  , 2),
(3  , 'Sam'   , 60000  , 2),
(4  , 'Max'   , 90000  , 1),
(5  , 'Janet' , 69000  , 1),
(6  , 'Randy' , 85000  , 1),
(7  , 'Will'  , 70000  , 1)
;
