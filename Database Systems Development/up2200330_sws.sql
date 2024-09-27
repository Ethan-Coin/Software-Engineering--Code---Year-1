-- Query 1
 WITH AverageModuleGradeL4 AS
        (SELECT m.mod_name AS mod_name,
                sm.staff_id,
                ROUND(AVG(mr.submission_mark)) AS sub_mark
         FROM modules m
         JOIN modules_results mr ON m.mod_id = mr.mod_id
         JOIN staff_modules sm ON m.mod_id = sm.module_id
         GROUP BY m.mod_id,
                  sm.staff_id
         HAVING m.acc_level = 'Level 4')
SELECT CONCAT_WS(' ', s.staff_name, s.staff_mid_name, s.staff_last_name) AS "Staff Full Name",
       s.staff_role AS "Staff Role",
       mod_name AS "Module Name",
       sub_mark AS "Average Student Mark"
FROM staff s
JOIN AverageModuleGradeL4 amg ON s.staff_id = amg.staff_id
ORDER BY "Average Student Mark" DESC;

-- Query 2
 WITH staffTeachingHours AS
        (SELECT st.staff_id,
                SUM(EXTRACT(HOUR
                            FROM ts.session_end_time) - EXTRACT(HOUR
                                                                FROM ts.session_start_time)) AS total_dur
         FROM teaching_sessions ts
         JOIN staff_teaching st ON ts.session_id = st.session_id
         GROUP BY st.staff_id)
SELECT CONCAT_WS(' ', s.staff_name, s.staff_mid_name, s.staff_last_name) AS "Staff Full Name",
       s.staff_role AS "Staff Role",
       s.staff_position AS "Staff Position",
       total_dur AS "Teaching Hours"
FROM staff s
JOIN staffTeachingHours sth ON s.staff_id = sth.staff_id;

--Query 3

SELECT ts.session_id AS "Session ID",
       r.room_capacity AS "Room Capacity",
       COUNT(st.stu_id) AS "Total Students"
FROM teaching_sessions ts
JOIN rooms r ON ts.room_id = r.room_id
JOIN students_teaching st ON ts.session_id = st.session_id
GROUP BY ts.session_id,
         r.room_id
HAVING COUNT(st.stu_id) > r.room_capacity
ORDER BY ts.session_id;

--Query 4

SELECT c.course_name AS "Course Name",
       COUNT(s.stu_id) AS "Total Students"
FROM courses c
JOIN students s ON c.course_id = s.course_id
WHERE s.acc_level = 'Level 4'
GROUP BY c.course_id
ORDER BY "Total Students" DESC;

