--Question 1
--Authors inserts
INSERT INTO
    authors (
        auth_name,
        auth_last_name,
        auth_phone,
        auth_country
    )
VALUES
    ('Lemuel', 'Darnborough', '6307841875', 'China'),
    ('Christoffer', 'Frangione', '4853415743', NULL),
    ('Melvin', 'Quesne', NULL, 'Malaysia');

--publishers inserts
INSERT INTO
    publishers (pub_name, pub_city)
VALUES
    ('Stillman', 'Štěnovice'),
    ('Bernetta', NULL);

--books inserts
INSERT INTO
    books (pub_id, book_title, book_pub_year)
VALUES
    (1, 'Boys from Brazil, The', 1803),
    (
        1,
        'Gentle Breeze in the Village, A (Tennen kokekkô) ',
        2010
    ),
    (2, 'Deceit', 1993),
    (1, 'Thoroughbreds Don''t Cry', 2012),
    (2, 'Dorian Gray', 2009),
    (2, 'Ravenous', 1865),
    (1, 'Goldene Zeiten', 1965),
    (2, 'Secrets & Lies', 2023),
    (1, 'Kahaani', 1976),
    (2, 'Super Hero Party Clown', 1992);

--genres inserts
INSERT INTO
    genres (genre_name)
VALUES
    ('Action'),
    ('Documentary'),
    ('Comedy');

--books_genres inserts
INSERT INTO
    books_genres (book_id, genre_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (5, 1),
    (5, 3),
    (6, 1),
    (6, 2),
    (6, 3),
    (7, 1),
    (7, 2),
    (7, 3),
    (8, 1),
    (8, 2),
    (8, 3),
    (9, 1),
    (9, 2),
    (9, 3),
    (10, 1),
    (10, 2),
    (10, 3);

--books_authors inserts
INSERT INTO
    books_authors (book_id, auth_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 3),
    (8, 3),
    (9, 3),
    (10, 3),
    (3, 3),
    (4, 3),
    (6, 3);

--Question 2
CREATE VIEW books_details AS
SELECT
    b.book_id AS "Book ID",
    b.book_title AS "Book Title",
    g.genre_name AS "Genre Name",
    p.pub_name AS "Publisher Name",
    b.book_pub_year AS "Book Publication Year"
FROM
    books b
    JOIN genres g ON b.genre_id = g.genre_id
    JOIN publishers p ON p.pub_id = b.pub_id
ORDER BY
    g.genre_name ASC;

--Question 3
SELECT
    CONCAT_WS(
        ' ',
        a.auth_name,
        a.auth_mid_name,
        a.auth_last_name
    ) AS "Author Full Name",
    bd."Book Title",
    bd."Genre Name"
FROM
    authors a
    JOIN books_authors ba ON a.auth_id = ba.auth_id
    JOIN books_details bd ON bd."Book ID" = ba.book_id
WHERE
    bd."Book Publication Year" >= 2020
ORDER BY
    bd."Book Publication Year" DESC;

--Question 4
CREATE VIEW student_loan_details AS
SELECT
    s.stu_id AS "Student ID",
    CONCAT_WS(' ', s.stu_name, s.stu_mid_name, s.stu_last_name) AS "Student",
    l.loan_id AS "Loan ID",
    l.loan_date AS "Loan Date",
    l.due_date AS "Due Date",
    l.status AS "Loan Status",
    bi.inv_id AS "Inventory ID",
    bd."Book Title"
FROM
    students s
    JOIN loans l ON s.stu_id = l.stu_id
    JOIN books_inventory bi ON l.inv_id = bi.inv_id
    JOIN books_details bd ON bd."Book ID" = bi.book_id;

--Question 5----------------------------------------------------------------------------------------
SELECT
    sld."Book Title",
    sld."Loan ID",
    sld."Loan Date",
    sld."Due Date",
    sld."Loan Status",
    c.course_name AS "Course Name"
FROM
    student_loan_details sld
    JOIN students s ON sld."Student ID" = s.stu_id
    JOIN courses c ON s.stu_course = c.course_id
WHERE
    sld."Due Date" < CURRENT_DATE;

--Question 6
SELECT
    *
FROM
    books_details bd
WHERE
    bd."Book Title" ILIKE '%Science%';

--Question 7
SELECT
    *
FROM
    books_details bd
WHERE
    bd."Publisher Name" ILIKE 'penguin%';

--Question 8
SELECT
    *
FROM
    books_details bd
WHERE
    bd."Book Title" SIMILAR TO 'The % of %';

--Question 9
EXPLAIN ANALYZE
SELECT
    b.book_id AS "Book ID",
    b.book_title AS "Title",
    CONCAT(
        a.auth_name,
        ' ',
        COALESCE(a.auth_mid_name, ''),
        ' ',
        a.auth_last_name
    ) AS "Author Full Name",
    b.book_pub_year AS "Publication Year",
    g.genre_name AS "Genre"
FROM
    books b
    JOIN genres g ON b.genre_id = g.genre_id
    JOIN books_authors ba ON b.book_id = ba.book_id
    JOIN authors a ON ba.auth_id = a.auth_id
WHERE
    b.book_pub_year > 2000
    AND g.genre_name = 'Science';

CREATE INDEX ind_genre_name ON genres (genre_name);

--Question 10
SELECT
    bd."Book Title"
FROM
    books_details bd
    JOIN books_languages bl ON bd."Book ID" = bl.book_id
    JOIN languages l ON l.lang_id = bl.lang_id
WHERE
    l.lang_name IN ('Chinese', 'German')
GROUP BY
    bd."Book ID",
    bd."Book Title"
HAVING
    COUNT(DISTINCT l.lang_name) = 2
ORDER BY
    bd."Book Title" ASC;

--Question 11
SELECT
    c.course_name AS "Course Name",
    c.course_code AS "Course Code"
FROM
    students s
    RIGHT JOIN courses c ON s.stu_course = c.course_id
WHERE
    s.stu_course IS NULL;

--Question 12 
SELECT
    b.book_title AS "Book Title"
FROM
    books b
WHERE
    b.book_pub_year BETWEEN 2000
    AND 2020
    AND (
        b.book_pages BETWEEN 200
        AND 300
        OR b.book_pages BETWEEN 400
        AND 500
    );