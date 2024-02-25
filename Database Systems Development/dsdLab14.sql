--Question 1

SELECT a.auth_name AS "Author Name",
       a.auth_last_name AS "Author Last Name",
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
JOIN books b ON ba.book_id = b.book_id
WHERE b.book_id IN
        (SELECT book_id
         FROM books
         WHERE book_pub_year > 2020 );

--Question 2

SELECT a.auth_name AS "Author Name",
       a.auth_last_name AS "Author Last Name",
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
JOIN books b ON ba.book_id = b.book_id
WHERE EXISTS
        (SELECT 1
         FROM books_editions be
         WHERE be.book_id = b.book_id
             AND be.ed_year> 2020 );

--Question 3

SELECT CONCAT_WS(' ',a.auth_name, a.auth_last_name) AS "Author Name",
       b.book_title AS "Book Title",
       b.book_pub_year AS "Orginal Publication Year",

    (SELECT max(be.ed_year)
     FROM books_editions be
     WHERE be.book_id = b.book_id) AS "Latest Edition Year"
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
JOIN books b ON ba.book_id = b.book_id
WHERE EXISTS
        (SELECT 1
         FROM books_editions be
         WHERE be.book_id = b.book_id
             AND be.ed_year> 2020 );

--Question 4

SELECT a.auth_name AS "Author Name",
       a.auth_last_name AS "Author Last Name"
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
JOIN books b ON ba.book_id = b.book_id
WHERE b.genre_id IN
        (SELECT genre_id
         FROM genres
         WHERE genre_name != 'Science Fiction' );

--Question 5

SELECT g.genre_name AS "Genre Name",
       COUNT(b.book_id) AS "Number of Books"
FROM genres g
JOIN books b ON g.genre_id = b.genre_id
GROUP BY g.genre_name
HAVING COUNT(b.book_id) =
    (SELECT MAX(book_count)
     FROM
         (SELECT COUNT(b.book_id) AS book_count
          FROM genres g
          JOIN books b ON g.genre_id = b.genre_id
          GROUP BY g.genre_id) AS book_counts);

-- Question 6

SELECT sld."Student",
       sld."Loan Date",
       sld."Due Date",
       sld."Inventory ID"
FROM student_loan_details sld
WHERE sld."Loan ID" IN
        (SELECT sld."Loan ID"
         FROM student_loan_details sld
         WHERE sld."Book Title" = 'PostgreSQL up and running'
             AND sld."Due Date" < CURRENT_DATE );

-- Question 7

SELECT bd."Book Title"
FROM books_details bd
WHERE bd."Book Title" NOT IN
        (SELECT sld."Book Title"
         FROM student_loan_details sld);

-- Question 8

SELECT bd."Book Title",
       ROUND(AVG(sld_subquery."Loan Duration")) AS "Average Loan Duration"
FROM books_details bd
JOIN
    (SELECT "Book Title",
            "Due Date" - "Loan Date" AS "Loan Duration"
     FROM student_loan_details) sld_subquery ON bd."Book Title" = sld_subquery."Book Title"
GROUP BY bd."Book Title"
ORDER BY "Average Loan Duration" ASC;

-- Question 9

SELECT b.book_title AS "Book Title"
FROM books b
WHERE b.book_id NOT IN
        ( SELECT bl.book_id
         FROM books_languages bl
         JOIN languages l ON bl.lang_id = l.lang_id
         WHERE l.lang_name = 'English' );

-- Question 10

SELECT c.course_name AS "Course Name",
       COUNT(s.stu_id) AS "Number of Students"
FROM courses c
JOIN students s ON c.course_id = s.stu_course
GROUP BY c.course_name
HAVING COUNT(s.stu_id) =
    (SELECT MAX(student_count)
     FROM
         (SELECT COUNT(s.stu_id) AS student_count
          FROM courses c
          JOIN students s ON c.course_id = s.stu_course
          GROUP BY c.course_id) AS student_counts);

-- Question 11

SELECT CONCAT_WS(' ',a.auth_name, a.auth_last_name) AS "Author Name",
       COUNT(DISTINCT ba.book_id) AS "Number of Books"
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
GROUP BY a.auth_id
HAVING COUNT(DISTINCT ba.book_id) >
    (SELECT COUNT(*) / COUNT(DISTINCT auth_id) AS "Average Number of Books per Author"
     FROM books_authors)
ORDER BY "Number of Books" DESC;