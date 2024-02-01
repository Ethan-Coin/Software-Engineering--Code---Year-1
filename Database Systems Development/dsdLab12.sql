--Question 1

INSERT INTO genres (genre_id, genre_name)
VALUES (9,
        'Short Story');


SELECT g.genre_name AS "Genre Name",
       COUNT(b.book_id) AS "Total Number of Books In Genre"
FROM genres g
LEFT JOIN books b ON g.genre_id = b.genre_id
GROUP BY g.genre_id
ORDER BY g.genre_name ASC;

--Question 2

SELECT CONCAT_WS(' ',a.auth_name, auth_mid_name, auth_last_name) AS "Author Full Name",
       COALESCE(b.book_title, 'N/A') AS "Book Title"
FROM authors a
LEFT JOIN books_authors ba ON a.auth_id = ba.auth_id
LEFT JOIN books b ON ba.book_id = b.book_id
ORDER BY a.auth_name ASC;

--Question 3

SELECT bi.inv_id AS "Inventory ID",
       b.book_title AS "Book Name",
       COALESCE(l.loan_id, 'N/A') AS "Loan ID"
FROM loans l
FULL JOIN books_inventory bi ON l.inv_id = bi.inv_id
JOIN books b ON bi.book_id = b.book_id
WHERE l.loan_id IS NULL
ORDER BY b.book_title ASC;

--Question 4

SELECT l.loan_id AS "Loan ID",
       CONCAT_WS(' ',stu_name, stu_mid_name, stu_last_name) AS "Student Name",
       bi.inv_id AS "Inventory ID",
       b.book_title AS "Book Title",
       l.loan_date AS "Loan Date",
       l.due_date AS "Due Date",
       l.return_date AS "Return Date"
FROM loans l
JOIN students s ON l.stu_id = s.stu_id
JOIN books_inventory bi ON bi.inv_id = l.inv_id
JOIN books b ON b.book_id = bi.book_id
WHERE l.return_date > l.due_date
ORDER BY s.stu_name;

--Question 5

SELECT c.course_name AS "Course Name",
       COUNT(s.stu_id) AS "Total Number of Students"
FROM students s
RIGHT JOIN courses c ON s.stu_course = c.course_id
GROUP BY c.course_id
ORDER BY COUNT(s.stu_id) DESC;

--Question 6

SELECT b.book_title AS "Book Title",
       SUM(bi.total_copies) AS "Total Copies"
FROM books b
INNER JOIN books_inventory bi ON b.book_id = bi.book_id
GROUP BY b.book_title
ORDER BY SUM(bi.total_copies) DESC;

--Question 7

SELECT CONCAT_WS(' ', s.stu_name, s.stu_mid_name, s.stu_last_name) AS "Student Full Name",
       CONCAT('Email: ', s.stu_email, ' Phone Number: ', s.stu_phone) AS "Contact Details"
FROM students s
WHERE stu_course is NULL;

--Question 8

SELECT b.book_id AS "Book ID",
       b.book_title AS "Book Title"
FROM books b
LEFT JOIN books_languages bl ON bl.book_id = b.book_id
LEFT JOIN languages l ON l.lang_id = bl.lang_id
WHERE l.lang_name is NULL;

--Question 9

SELECT CONCAT_WS(' ',a.auth_name, auth_mid_name, auth_last_name) AS "Author Full Name",
       COUNT(b.book_id) AS "Number of Books Published"
FROM books b
JOIN books_authors ba ON ba.book_id = b.book_id
JOIN authors a ON a.auth_id = ba.auth_id
GROUP BY a.auth_id
ORDER BY COUNT(b.book_title) DESC;

--Question 10

SELECT b.book_pub_year AS "Publication Year",
       COUNT(b.book_id) AS "Total Books",
       CONCAT(round((COUNT(b.book_id) * 1.0 / SUM(COUNT(b.book_id)) OVER () * 100),2), ' %') AS "Percentage of Total"
FROM books b
GROUP BY b.book_pub_year
ORDER BY b.book_pub_year ASC;

--Question 11