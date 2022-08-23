use leetcode;

select (
SELECT DISTINCT
            Salary
        FROM
 	prob_176_onerow
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1
	) SecondHighestSalary
;
