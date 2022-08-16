\W

use leetcode;

create table if not exists department
(
id int not null auto_increment primary key,
`name` varchar(16) not null
) engine=innodb;

create table if not exists employee
(
id int not null auto_increment primary key,
`name` varchar(16) not null,
salary int not null,
departmentid int not null,
foreign key (departmentid) references department(id) on delete cascade
) engine=innodb;


insert into department values
(1, 'IT'),
(2, 'Sales')
;

insert into employee
(`name`, salary, departmentid)
values
('Joe'   ,85000  ,1),
('Henry' ,80000  ,2),
('Sam'   ,60000  ,2),
('Max'   ,90000  ,1),
('Janet' ,69000  ,1),
('Randy' ,85000  ,1),
('Will'  ,70000  ,1)
;
