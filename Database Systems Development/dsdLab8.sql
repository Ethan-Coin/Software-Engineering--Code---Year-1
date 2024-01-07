--Question 1
SELECT 
    s.stu_name AS "Student First Name",
    s.stu_last_name AS "Student Last Name",
    s.stu_email AS "Student Email",
    c.course_name AS "Course Name",
    c.course_code AS "Course Code"
FROM students s
    JOIN courses c ON s.stu_course = c.course_id;

--Question 2
SELECT
    b.book_title AS "Book Title",
    b.book_pub_year AS "Book Publication Year",
    b.book_pages AS "Number Of Pages",
    g.genre_name AS "Genre Name"
FROM books b 
    JOIN genres g ON b.genre_id = g.genre_id;

--Question 3
SELECT
    a.auth_name AS "Author First Name",
    a.auth_mid_name AS "Author Middle Name",
    a.auth_last_name AS "Author Last Name",
    b.book_title AS "Book Title",
    b.book_pub_year AS "Publication Year"
FROM books b
    JOIN books_authors ba ON b.book_id = ba.book_id
    JOIN authors a ON ba.auth_id = a.auth_id;

--Question 4
SELECT
    b.book_title AS "Book Title",
    be.ed_year AS "Edition Publication Year",
    be.ed_no AS "Edition Number",
    p.pub_name AS "Publisher Name"
FROM books b 
    JOIN books_editions be ON b.book_id = be.book_id
    JOIN publishers p ON b.pub_id = p.pub_id;

--Question 5
SELECT
    b.book_title AS "Book Title",
    b.book_pub_year AS "Publication Year",
    l.lang_name AS "Language Name",
    be.ed_no AS "Edition Number"
FROM books b 
    JOIN books_languages bl ON b.book_id = bl.book_id
    JOIN languages l ON bl.lang_id = l.lang_id
    JOIN books_editions be ON b.book_id = be.book_id;

--Question 6
SELECT
    b.book_title AS "Book Title",
    s.stu_name AS "Student First Name",
    s.stu_mid_name AS "Student Middle Name",
    s.stu_last_name AS "Student Last Name",
    li.lib_name AS "Librarian Name",
    li.lib_last_name AS "Librarian Last Name"
FROM books b 
    JOIN books_inventory bi ON b.book_id = bi.book_id
    JOIN loans lo ON bi.inv_id = lo.inv_id
    JOIN students s ON s.stu_id = lo.stu_id
    JOIN librarians li ON li.lib_id = lo.lib_id; 

--Question 7
SELECT
    b.book_title AS "Book Title",
    s.stu_name AS "Student First Name",
    s.stu_last_name AS "Student Last Name",
    lo.loan_date AS "Loan Date",
    lo.due_date AS "Due Date",
    lo.return_date AS "Return Date"
FROM books b 
    JOIN books_inventory bi ON b.book_id = bi.book_id
    JOIN loans lo ON bi.inv_id = lo.inv_id
    JOIN students s ON s.stu_id = lo.stu_id
WHERE s.stu_name = 'Hana';

--Question 8
SELECT
    b.book_title AS "Book Name",
    g.genre_name AS "Genre Name",
    be.ed_no AS "Edition Number",
    bi.total_copies AS "Number Of Copies"
FROM books b 
    JOIN genres g ON b.genre_id = g.genre_id
    JOIN books_editions be ON b.book_id = be.book_id
    JOIN books_inventory bi ON b.book_id = bi.book_id;