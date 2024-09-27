--Question 1

SELECT b.book_title AS "Book Title",
       g.genre_name AS "Genre",
       p.pub_name AS "Publisher"
FROM books b
JOIN genres g ON b.genre_id = g.genre_id
JOIN publishers p ON b.pub_id = p.pub_id;

--Question 2

SELECT CONCAT_WS(' ',a.auth_name,a.auth_mid_name, a.auth_last_name) AS "Author",
       COUNT(b.book_id) AS "Number of Books"
FROM books b
JOIN books_authors ba ON b.book_id = ba.book_id
JOIN authors a ON ba.auth_id = a.auth_id
GROUP BY a.auth_id
HAVING COUNT(b.book_id) > 1;

--Question 3

SELECT b.book_title AS "Book Title",
       b.book_pub_year AS "Publication Year"
FROM books b
WHERE b.book_pub_year BETWEEN 2000 AND 2010;

--Question 4

SELECT g.genre_name AS "Genre",
       COUNT(b.book_id) AS "Number of Books"
FROM books b
JOIN genres g ON b.genre_id = g.genre_id
GROUP BY g.genre_id;

--Question 5

SELECT CONCAT_WS(' ', s.stu_name, s.stu_mid_name, s.stu_last_name) AS "Student",
       COUNT(l.loan_id) AS "Total Books Borrowed"
FROM students s
JOIN loans l ON s.stu_id = l.stu_id
GROUP BY s.stu_id;

--Question 6

SELECT b.book_title AS "Book Title"
FROM books b
LEFT JOIN books_inventory bi ON b.book_id = bi.book_id
LEFT JOIN loans l ON bi.inv_id = l.inv_id
WHERE l.inv_id IS NULL;

--Question 7

SELECT *
FROM loans;


SELECT DISTINCT CONCAT_WS(' ', s.stu_name, s.stu_mid_name, s.stu_last_name) AS "Student"
FROM students s
JOIN loans l ON s.stu_id = l.stu_id
WHERE CURRENT_DATE > l.due_date
    AND l.status = 'Borrowed';

--Question 8

SELECT b.book_title AS "Book Title",
       CONCAT_WS(' ', a.auth_name, a.auth_mid_name, a.auth_last_name) AS "Author Name",
       l.lang_name AS "Language name"
FROM books b
JOIN books_authors ba ON b.book_id = ba.book_id
JOIN authors a ON a.auth_id = ba.auth_id
JOIN books_languages bl ON b.book_id = bl.book_id
JOIN languages l ON l.lang_id = bl.lang_id;

--Question 9

SELECT g.genre_name AS "Genre Name",
       ROUND(AVG(b.book_pages)) AS "Average Pages"
FROM books b
JOIN genres g ON b.genre_id = g.genre_id
GROUP BY g.genre_id;

--Question 10

SELECT a.auth_name AS "Author Name",
       COUNT(DISTINCT b.genre_id) AS "Genres"
FROM authors a
JOIN books_authors ba ON a.auth_id = ba.auth_id
JOIN books b ON ba.book_id = b.book_id
GROUP BY a.auth_id
HAVING COUNT(DISTINCT b.genre_id) > 1;

--Question 11

SELECT b.book_title AS "Book Title",
       COUNT(be.ed_id) AS "Book Editions"
FROM books b
JOIN books_editions be ON b.book_id = be.book_id
GROUP BY b.book_id;

--Question 12

SELECT DISTINCT p.pub_name AS "Publisher"
FROM publishers p
LEFT JOIN books b ON b.pub_id = p.pub_id
AND b.book_pub_year = 2015
WHERE b.book_id IS NULL;

--Question 13

SELECT g.genre_name as "Genre name",
       ROUND(AVG(b.book_pages)) AS "Average Pages"
FROM books b
JOIN genres g ON g.genre_id = b.genre_id
JOIN books_editions be ON b.book_id = be.book_id
GROUP BY g.genre_id
HAVING COUNT(be.ed_no) >= 2;


SELECT g.genre_name AS "Genre",
       ROUND(AVG(b.book_pages)) AS "Avg Pages"
FROM genres g
JOIN books b ON g.genre_id = b.genre_id
WHERE b.book_id IN
        (SELECT be.book_id
         FROM books_editions be
         GROUP BY be.book_id
         HAVING COUNT(be.ed_no) >= 2)
GROUP BY g.genre_name;

--Question 14
 WITH GenreLoans2023 AS
    (SELECT b.genre_id,
            COUNT(l.loan_id) AS total_loans
     FROM loans l
     JOIN books_inventory bi ON l.inv_id = bi.inv_id
     JOIN books_editions be ON bi.ed_id = be.ed_id
     JOIN books b ON be.book_id = b.book_id
     WHERE EXTRACT(YEAR
                   FROM l.loan_date) = 2023
     GROUP BY b.genre_id)
SELECT g.genre_name AS "Genre",
       COALESCE(gl.total_loans, 0) AS "Total Loans"
FROM genres g
LEFT JOIN GenreLoans2023 gl ON g.genre_id = gl.genre_id
ORDER BY "Total Loans" DESC;

--Question 15
 WITH BorrowedBooks AS
    ( SELECT g.genre_name,
             b.book_title,
             COUNT(l.loan_id) AS borrow_count
     FROM loans l
     JOIN books_inventory bi ON l.inv_id = bi.inv_id
     JOIN books_editions be ON bi.ed_id = be.ed_id
     JOIN books b ON bi.book_id = b.book_id
     JOIN genres g ON b.genre_id = g.genre_id
     GROUP BY g.genre_name,
              b.book_title),
      RankedBooks AS
    ( SELECT genre_name,
             book_title,
             borrow_count,
             RANK() OVER (PARTITION BY genre_name
                          ORDER BY borrow_count DESC) as rank
     FROM BorrowedBooks)
SELECT genre_name AS "Genre",
       book_title AS "Book Title",
       borrow_count AS "Times Borrowed"
FROM RankedBooks
WHERE rank = 1;

--V2 - Using Subqueries

SELECT g.genre_name AS "Genre",
       b.book_title AS "Most Borrowed Book",
       COUNT(l.loan_id) AS "Times Borrowed"
FROM genres g
JOIN books b ON g.genre_id = b.genre_id
JOIN books_inventory bi ON b.book_id = bi.book_id
JOIN loans l ON bi.inv_id = l.inv_id
GROUP BY g.genre_id,
         b.book_id
HAVING COUNT(l.loan_id) =
    ( SELECT MAX(BorrowCount)
     FROM
         ( SELECT b2.book_id,
                  COUNT(l2.loan_id) AS BorrowCount
          FROM books b2
          JOIN books_inventory bi2 ON b2.book_id = bi2.book_id
          JOIN loans l2 ON bi2.inv_id = l2.inv_id
          WHERE b2.genre_id = g.genre_id
          GROUP BY b2.book_id ) AS SubQuery)
ORDER BY "Genre",
         "Times Borrowed" DESC;