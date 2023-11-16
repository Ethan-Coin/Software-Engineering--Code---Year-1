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