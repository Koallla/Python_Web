# 1
'5 студентов с наибольшим средним баллом по всем предметам.'
SELECT Students.name, ROUND(AVG(grade), 2) AS avg_grade
FROM "Grades"
JOIN "Students" AS Students ON Students.id = users_id
GROUP BY Students.name
ORDER BY avg_grade DESC
LIMIT 5

# 2
'1 студент с наивысшим средним баллом по одному предмету.'
SELECT Students.name, ROUND(AVG(grade), 2) AS avg_grade
FROM "Grades"
JOIN "Students" AS Students ON Students.id = users_id
WHERE course_id = 5
GROUP BY Students.name
ORDER BY avg_grade DESC
LIMIT 1


# 3
'Cредний балл в группе по одному предмету.'
SELECT "Groups".name, ROUND(AVG(grade), 2) AS avg_grade
FROM "Grades"
JOIN "Students" ON "Students".id = users_id
JOIN "Groups" ON "Groups".id = "Students".group_id
WHERE course_id = 1
GROUP BY "Groups".name


# 4
'Средний балл в потоке.'
SELECT ROUND(AVG(grade), 2) AS avg_grade
FROM "Grades"

# 5
'Какие курсы читает преподаватель.'
SELECT course, "Teatchers".name
FROM public."Courses"
JOIN "Teatchers" ON "Teatchers".id = teatcher_id
WHERE teatcher_id = 2


# 6
'Список студентов в группе.'
SELECT "Students".name, surname, "Groups".name AS group_name, group_id
FROM public."Students"
JOIN "Groups" ON "Groups".id = group_id
WHERE group_id = 2



# 7
'Оценки студентов в группе по предмету.'
SELECT grade, "Courses".course AS course_name, "Groups".name AS group_name
FROM public."Grades"
JOIN "Students" ON "Students".id = users_id
JOIN "Groups" ON "Groups".id = "Students".group_id
JOIN "Courses" ON "Courses".id = course_id
WHERE "Groups".id = 3 and "Courses".id = 2

# 8
'Оценки студентов в группе по предмету на последнем занятии.'
SELECT grade, "Courses".course AS course_name, "Groups".name AS group_name, created_at
FROM public."Grades"
JOIN "Students" ON "Students".id = users_id
JOIN "Groups" ON "Groups".id = "Students".group_id
JOIN "Courses" ON "Courses".id = course_id
WHERE "Groups".id = 1 and "Courses".id = 3 and created_at = (SELECT MAX(created_at) FROM public."Grades" )
ORDER BY created_at DESC


# 9
'Список курсов, которые посещает студент.'
SELECT DISTINCT "Students".name, "Students".surname, "Courses".course
FROM public."Grades"
JOIN "Students" ON users_id = "Students".id
JOIN "Courses" ON "Courses".id = course_id
WHERE "Students".id > 0 
ORDER BY "Students".name

# 10
'Список курсов, которые студенту читает преподаватель.'
SELECT DISTINCT "Students".name, "Students".surname, "Teatchers".name, "Courses".course
FROM public."Grades"
JOIN "Students" ON users_id = "Students".id
JOIN "Courses" ON "Courses".id = course_id
JOIN "Teatchers" ON "Teatchers".id = "Grades".teatcher_id
WHERE "Students".id > 0 
ORDER BY "Students".name

# 11
'Средний балл, который преподаватель ставит студенту.'
SELECT s.name, t.name, ROUND(AVG(grade), 2) AS avg_grade
FROM public."Grades"
JOIN "Students" AS s ON s.id = users_id
JOIN "Teatchers" AS t ON t.id = teatcher_id
GROUP BY s.name, t.name
ORDER BY s.name


# 12
'Средний балл, который ставит преподаватель.'
SELECT t.name, ROUND(AVG(grade), 2) AS avg_grade
FROM public."Grades"
JOIN "Teatchers" AS t ON t.id = teatcher_id
GROUP BY t.name