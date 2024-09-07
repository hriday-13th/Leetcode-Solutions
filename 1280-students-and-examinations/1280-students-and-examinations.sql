# Write your MySQL query statement below
select s.student_id, s.student_name, b.subject_name, (case when (select count(*) from examinations e where e.student_id = s.student_id and e.subject_name = b.subject_name) > 0 then (select count(*) from examinations e where e.student_id = s.student_id and e.subject_name = b.subject_name) else 0 end) attended_exams
from students s, subjects b
order by s.student_id, b.subject_name;

# select s.student_id, s.student_name, e.subject_name, count(select count())
# from students s
# left join examinations e
# on e.student_id = s.student_id
# order by s.student_id, e.subject_name;