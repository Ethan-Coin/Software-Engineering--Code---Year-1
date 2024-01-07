--Question 1
SELECT
    g.genre_name AS "Genre",
    COUNT(b.book_id) AS "Total Number Of Books In Genre"
FROM books b
    JOIN genres g ON b.genre_id = g.genre_id
GROUP BY g.genre_name;

--Question 2
SELECT
    CONCAT_WS(' ',a.auth_name,a.auth_mid_name,a.auth_last_name) AS "Author Full Name",
    COUNT(b.book_id) AS "Total Books Authored"
FROM authors a 
    JOIN books_authors ba ON a.auth_id = ba.auth_id
    JOIN books b ON b.book_id = ba.book_id
GROUP BY a.auth_id
ORDER BY COUNT(b.book_id) DESC;

--Question 3
SELECT
    p.pub_name AS "Publisher Name",
    COUNT(book_id) AS "Total Books Published"
FROM books b
    JOIN publishers p  ON b.pub_id = p.pub_id
GROUP BY p.pub_id
HAVING COUNT(book_id) >= 5;

SELECT
    p.pub_name AS "Publisher Name",
    b.book_id AS "Book ID"
FROM books b
    JOIN publishers p  ON b.pub_id = p.pub_id
WHERE p.pub_id = 5; 

--Question 4
SELECT
    l.lang_name AS "Language Name",
    COUNT(b.book_id) AS "Total Number Of Books"
FROM books b
    JOIN books_languages bl ON b.book_id = bl.book_id
    JOIN languages l ON l.lang_id = bl.lang_id
GROUP BY l.lang_id
ORDER BY COUNT(b.book_id) DESC
LIMIT 2;

--Question 5
SELECT
    b.book_title AS "Book Title",
    l.lang_name AS "Language Written In"
FROM books b
    JOIN books_languages bl 
        ON b.book_id = bl.book_id
    JOIN languages l 
        ON l.lang_id = bl.lang_id
WHERE l.lang_name = 'English' OR l.lang_name = 'Spanish';

--Question 6 
SELECT
    CONCAT_WS(' ',a.auth_name,a.auth_mid_name,a.auth_last_name) AS "Author Full Name",
    COUNT(b.book_id) AS "Total Books Authored"
FROM authors a 
    JOIN books_authors ba ON a.auth_id = ba.auth_id
    JOIN books b ON b.book_id = ba.book_id
GROUP BY a.auth_id
HAVING COUNT(b.book_id) > 9
ORDER BY COUNT(b.book_id) DESC;

--Question 7
SELECT
    g.genre_name AS "Genre Name",
    COUNT(b.book_id) AS "Number Of Books" 
FROM authors a 
    JOIN books_authors ba ON a.auth_id = ba.auth_id
    JOIN books b ON b.book_id = ba.book_id
    JOIN genres g ON b.genre_id = g.genre_id
WHERE a.auth_id = 4
GROUP BY g.genre_id;

SELECT 
    g.genre_name AS "Genre Name",
    a.auth_id AS "Author ID",
    b.book_id AS "Book ID"
FROM authors a 
    JOIN books_authors ba ON a.auth_id = ba.auth_id
    JOIN books b ON b.book_id = ba.book_id
    JOIN genres g ON b.genre_id = g.genre_id
WHERE a.auth_id = 4;

--Question 8 
SELECT
    CONCAT_WS(' ',a.auth_name,a.auth_mid_name,a.auth_last_name) AS "Author Full Name",
    COUNT(b.book_id) AS "Total Books Authored"
FROM books b 
    JOIN genres g 
        ON b.genre_id = g.genre_id
    JOIN books_authors ba 
        ON ba.book_id = b.book_id
    JOIN authors a 
        ON a.auth_id = ba.auth_id
WHERE g.genre_name = 'Programming'
GROUP BY a.auth_id;

--Question 9
SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN books_authors ba 
        ON b.book_id = ba.book_id
    JOIN authors a 
        ON ba.auth_id = a.auth_id
 WHERE a.auth_id = 3
 UNION
 SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN books_authors ba 
        ON b.book_id = ba.book_id
    JOIN authors a 
        ON ba.auth_id = a.auth_id
 WHERE a.auth_id = 4;
 --Question 10
 SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN books_authors ba 
        ON b.book_id = ba.book_id
    JOIN authors a 
        ON ba.auth_id = a.auth_id
 WHERE a.auth_id = 3
 INTERSECT
 SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN books_authors ba 
        ON b.book_id = ba.book_id
    JOIN authors a 
        ON ba.auth_id = a.auth_id
 WHERE a.auth_id = 4;
 --Question 11
SELECT
    CONCAT_WS(' ',s.stu_name,s.stu_mid_name,s.stu_last_name) AS "Student Full Name",
    COUNT(b.book_id) AS "Total Books Borrowed"
FROM books b
    JOIN books_inventory bi 
        ON b.book_id = bi.book_id
    JOIN loans l 
        ON bi.inv_id = l.inv_id
    JOIN students s
        ON l.stu_id = s.stu_id
WHERE l.status = 'Borrowed'
GROUP BY s.stu_id
ORDER BY s.stu_last_name;
--Question 12
SELECT
    c.course_name AS "Course Name",
    MAX(s.stu_enroll) AS "Last Enroll"
FROM students s 
    JOIN courses c ON c.course_id = s.stu_course
GROUP BY c.course_id;

SELECT
    c.course_name AS "Course Name",
    s.stu_enroll AS "Last Enroll"
FROM students s 
    JOIN courses c ON c.course_id = s.stu_course
WHERE c.course_id = 5;

--Question 13
SELECT
    CONCAT_WS(' ',li.lib_name,li.lib_last_name) AS "Librarian Name",
    MIN(lo.loan_date) AS "Earliest Loan Date"
FROM librarians li
    JOIN loans lo ON li.lib_id = lo.lib_id
GROUP BY li.lib_id;

--Question 14
SELECT
    g.genre_name AS "Genre Name",
    ROUND(AVG(b.book_pages)) AS "Average Number Of Pages"
FROM books b
    JOIN genres g 
        ON g.genre_id = b.genre_id
GROUP BY g.genre_id;

--Question 15
SELECT
    



