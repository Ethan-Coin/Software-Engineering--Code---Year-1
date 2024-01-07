--Question 1
SELECT
    book_title AS "Book Title",
    book_pub_year AS "Publication Year"
FROM books
WHERE book_pages > 500;
--Question 2
SELECT
    CONCAT(auth_name, ' ', auth_mid_name, ' ', auth_last_name) AS "Author Full Name"
FROM authors
WHERE auth_name = 'Michael';
--Question 3
SELECT
    CONCAT_WS(' ', stu_name,stu_mid_name,stu_last_name) AS "Student Full Name",
    CONCAT_WS(' ', stu_addr1,stu_addr2,stu_city,stu_postcode) AS "Student Full Name",
    stu_email AS "Student Email",
    stu_phone AS "Student Phone",
    stu_enroll AS "Student Enrolment Date"
FROM students
WHERE stu_enroll >'2021-09-01'
    AND stu_city = 'Portsmouth';
--Question 4
SELECT
    book_title AS "Book Title"
FROM books
WHERE book_pub_year BETWEEN 2000 AND 2005
ORDER BY book_pub_year ASC;
--Question 5
SELECT
    CONCAT(auth_name, ' ', auth_mid_name, ' ', auth_last_name) AS "Author Full Name"
FROM authors
WHERE auth_name LIKE 'M%' OR auth_mid_name LIKE 'M%' OR auth_last_name LIKE 'M%';
--Question 6
SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN genres g ON b.genre_id = g.genre_id
WHERE g.genre_name in ('Sci-Fi','Action');
--Question 7
SELECT
    CONCAT_WS(' ',s.stu_name,s.stu_last_name) AS "Student Name",
    c.course_name AS "Course Name",
    c.course_code AS "Course Code"
FROM students s
    JOIN courses c ON s.stu_course = c.course_id
WHERE c.course_code = 'C006'
ORDER BY s.stu_name ASC;
--Question 8
SELECT
    book_title AS "Book Title"
FROM books
ORDER BY book_pub_year DESC, book_title ASC
LIMIT 10;
--Question 9
SELECT
    DISTINCT g.genre_name AS "Genre Name"
FROM genres g 
    JOIN books b 
        ON g.genre_id = b.genre_id
    JOIN books_inventory bi 
        ON b.book_id = bi.book_id
    JOIN loans l
        ON bi.inv_id = l.inv_id
    JOIN students s
        ON l.stu_id = s.stu_id
    JOIN courses c
        ON s.stu_course = c.course_id
WHERE c.course_name = 'Web Development';
--Question 10
SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN publishers p 
        ON b.pub_id = p.pub_id
WHERE p.pub_name = 'Elsevier' AND b.book_pub_year = 2015;
--Question 11
SELECT
    CONCAT(a.auth_name, ' ', a.auth_mid_name, ' ', a.auth_last_name) AS "Author Full Name",
    b.book_title AS "Book Title"
FROM authors a
    JOIN books_authors ba 
        ON a.auth_id = ba.auth_id
    JOIN books b
        ON ba.book_id = b.book_id
WHERE b.book_pages >= 800
ORDER BY b.book_pages ASC;
--Question 12
SELECT
    CONCAT_WS(' ',s.stu_name,s.stu_mid_name,s.stu_last_name) AS "Student Full Name",
FROM students s
    JOIN courses c
        ON s.stu_course = c.course_id
WHERE c.course_name = 'Software Engineering' AND s.stu_city = 'Portsmouth';
--Question 13
SELECT
    b.book_title AS "Book Title"
FROM books b
    JOIN genres g
        ON b.genre_id = g.genre_id
    JOIN books_authors ba
        ON b.book_id = ba.book_id
    JOIN authors a
        ON ba.auth_id = a.auth_id
WHERE g.genre_name = 'Science' 
    AND a.auth_name = 'Ayato' 
    AND a.auth_last_name = 'Murphy';
--Question 14
SELECT
    b.book_isbn AS "Book ISBN",
    b.book_title AS "Book Title",
    b.book_pub_year AS "Book Publication Year",
    b.book_pages AS "Number Of Pages"
FROM books b
    JOIN books_languages bl
        ON b.book_id = bl.book_id
    JOIN languages l
        ON bl.lang_id = l.lang_id
    JOIN publishers p
        ON b.pub_id = p.pub_id
WHERE l.lang_name = 'German'
    AND p.pub_name = 'Wiley'
ORDER BY b.book_pub_year;
--Question 15
SELECT
    CONCAT_WS(' ', s.stu_name, s.stu_mid_name, s.stu_last_name) AS "Student Full Name",
    l.loan_date AS "Loan Date",
    l.due_date AS "Due Date"
FROM students s
    JOIN loans l
        ON s.stu_id = l.stu_id
    JOIN books_inventory bi
        ON l.inv_id = bi.inv_id
    JOIN books b
        ON bi.book_id = b.book_id
WHERE b.book_title = 'Database Systems' 
    AND l.status = 'Borrowed';