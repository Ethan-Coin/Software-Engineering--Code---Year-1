--Question 1
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    customer_email VARCHAR(150) NOT NULL UNIQUE,
    customer_phone VARCHAR(15) NOT NULL UNIQUE
);
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (total_amount > 0)
);
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    CHECK (price > 0)
);
CREATE TABLE order_items (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (quantity > 0)
);
--Valid data
--Insert into Customers
INSERT INTO customers (customer_name, customer_email, customer_phone)
VALUES ('John Smith', 'John.Smith@yahoo.com', '0123456789'),
       ('Jane Doe', 'Jane.Doe@yahoo.com', '0123456788');
--Insert into Orders
INSERT INTO orders (customer_id, order_date, total_amount)
VALUES (1, '2020-01-01', 100),
       (2, '2020-01-02', 200),
       (1, '2020-01-03', 300);
--Insert into Products
INSERT INTO products (product_name, price)
VALUES ('Product A', 100),
       ('Product B', 200);
--Insert into Order Items
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1, 1, 1),
       (1, 2, 2),
       (2, 1, 3),
       (3, 2, 4),
       (3, 1, 5);
--Verify constraints
--Insert into Customers
INSERT INTO customers (customer_name, customer_email, customer_phone)
VALUES ('John Doe', 'Jane.Doe@yahoo.com', '0123456789');
--Insert into Orders
INSERT INTO orders (customer_id, order_date, total_amount)
VALUES (1, '2020-01-04', 0);
--Insert into Products
INSERT INTO products (product_name, price)
VALUES ('Product C', 0);
--Insert into Order Items
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (4, 1, 0);


--Question 2
CREATE TABLE cinemas (
    cinema_id SERIAL PRIMARY KEY,
    cinema_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(100) NOT NULL
);
CREATE TABLE screens (
    screen_id SERIAL PRIMARY KEY,
    cinema_id INT NOT NULL,
    screen_date DATE NOT NULL,
    screen_time TIME NOT NULL,
    FOREIGN KEY (cinema_id) REFERENCES cinemas(cinema_id),
    CHECK (screen_time BETWEEN '08:00:00' AND '23:00:00')
);
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_time VARCHAR(150) NOT NULL,
    movie_genre VARCHAR(50) NOT NULL
);
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    screen_id INT NOT NULL,
    movie_id INT NOT NULL,
    seat_number INT NOT NULL,
    tickect_price DECIMAL(4,2) NOT NULL,
    CHECK (tickect_price >= 4.99),
    UNIQUE (screen_id, movie_id, seat_number)
);
--Valid data
--Insert into Cinemas
INSERT INTO cinemas (cinema_name, location)
VALUES ('Cinema A', 'Location A'),
       ('Cinema B', 'Location B');
--Insert into Screens
INSERT INTO screens (cinema_id, screen_date, screen_time)
VALUES (1, '2020-01-01', '08:00:00'),
       (2, '2020-01-02', '09:00:00'),
       (1, '2020-01-03', '10:00:00'),
       (2, '2020-01-04', '11:00:00');
--Insert into Movies
INSERT INTO movies (movie_time, movie_genre)
VALUES ('Movie A', 'Genre A'),
       ('Movie B', 'Genre B'),
       ('Movie C', 'Genre C');
--Insert into Tickets
INSERT INTO tickets (screen_id, movie_id, seat_number, tickect_price)
VALUES (1, 1, 1, 4.99),
       (1, 2, 2, 5.99),
       (2, 1, 1, 6.99),
       (2, 2, 2, 7.99),
       (2, 3, 3, 8.99); 
--Verify constraints
--Insert into Cinemas
INSERT INTO cinemas (cinema_name, location)
VALUES ('Cinema A', 'Location B');
--Insert into Screens
INSERT INTO screens (cinema_id, screen_date, screen_time)
VALUES (1, '2020-01-01', '05:00:00');
--Insert into tickets
INSERT INTO tickets (screen_id, movie_id, seat_number, tickect_price)
VALUES  (1, 1, 2, 3.99);
--Insert into tickets
INSERT INTO tickets (screen_id, movie_id, seat_number, tickect_price)
VALUES  (1, 1, 1, 5.99);

--Question 3
CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    car_make VARCHAR(50) NOT NULL,
    car_model VARCHAR(50) NOT NULL,
    car_year INT NOT NULL,
    car_price DECIMAL(10,2) NOT NULL,
    CHECK (car_price >= 19.99)
);
CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(50) NOT NULL,
    cust_last_name VARCHAR(50) NOT NULL,
    cust_email VARCHAR(150) NOT NULL UNIQUE,
    cust_phone VARCHAR(15) NOT NULL UNIQUE
);
CREATE TABLE rentals (
    rental_id SERIAL PRIMARY KEY,
    car_id INT NOT NULL,
    cust_id INT NOT NULL,
    rental_start_date DATE NOT NULL,
    rental_end_date DATE NOT NULL,
    FOREIGN KEY (car_id) REFERENCES cars(car_id),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
    CHECK (rental_start_date < rental_end_date)
);
CREATE TABLE rental_payments (
    payment_id SERIAL PRIMARY KEY,
    rental_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(7,2) NOT NULL,
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id),
    CHECK (payment_amount >= 19.99)
);
CREATE TABLE rental_reviews (
    review_id SERIAL PRIMARY KEY,
    rental_id INT NOT NULL,
    rating SMALLINT NOT NULL,
    comment VARCHAR(500) NOT NULL,
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id),
    CHECK(rating BETWEEN 1 AND 5)
);
--Valid data
--Insert into Cars
INSERT INTO cars (car_make, car_model, car_year, car_price)
VALUES ('Car A', 'Model A', 2015, 19.99),
       ('Car B', 'Model B', 2017, 29.99),
       ('Car C', 'Model C', 2018, 39.99),
       ('Car D', 'Model D', 2020, 49.99),
       ('Car E', 'Model E', 2021, 59.99);
--Insert into Customers
INSERT INTO customers (cust_name, cust_last_name, cust_email, cust_phone)
VALUES ('John', 'Smith', 'John.Smith@yahoo.com', '0123456789'),
       ('Jane', 'Doe', 'Jane.Doe@yahoo.com', '0123456788'),
       ('John', 'Doe', 'John.Doe@yahoo.com', '0123456787');
--Insert into Rentals
INSERT INTO rentals (car_id, cust_id, rental_start_date, rental_end_date)
VALUES (1, 1, '2020-01-01', '2020-01-05'),
       (2, 1, '2020-01-02', '2020-01-03'),
       (3, 2, '2020-01-03', '2020-01-12'),
       (4, 2, '2020-01-04', '2020-01-09'),
       (5, 3, '2020-01-05', '2020-01-08');
--Insert into Rental Payments
INSERT INTO rental_payments (rental_id, payment_date, payment_amount)
VALUES (1, '2020-01-01', 19.99),
       (2, '2020-01-02', 29.99),
       (3, '2020-01-03', 39.99),
       (4, '2020-01-04', 49.99),
       (5, '2020-01-05', 59.99);
--Insert into Rental Reviews
INSERT INTO rental_reviews (rental_id, rating, comment)
VALUES (1, 1, 'Comment A'),
       (2, 2, 'Comment B'),
       (3, 3, 'Comment C'),
       (4, 4, 'Comment D'),
       (5, 5, 'Comment E');
--Verify constraints
--Insert into Cars
INSERT INTO cars (car_make, car_model, car_year, car_price)
VALUES ('Car A', 'Model A', 2015, 10);
--Insert into Customers
INSERT INTO customers (cust_name, cust_last_name, cust_email, cust_phone)
VALUES ('Dan','John','Dan.John@yahoo.com','0123456789');
--Insert into Rentals
INSERT INTO rentals (car_id, cust_id, rental_start_date, rental_end_date)
VALUES (1, 1, '2023-12-01','2023-09-01');
--Insewr into Rental Payments
INSERT INTO rental_payments (rental_id, payment_date, payment_amount)
VALUES (1, '2023-12-01', 1);
--Insert into Rental Reviews
INSERT INTO rental_reviews (rental_id, rating, comment)
VALUES (1, 0, 'Comment F');