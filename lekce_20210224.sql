# lekce 20210224

# INNER JOIN

# LEFT JOIN

# RIGHT JOIN

# OUTER JOIN

# CROSS JOIN


SELECT
    covid19_basic_differences.date,
    covid19_basic_differences.country,
    covid19_basic_differences.confirmed,
    covid19_basic.confirmed
FROM covid19_basic
LEFT OUTER JOIN covid19_basic_differences
    on covid19_basic.country = covid19_basic_differences.country
    AND covid19_basic.date = covid19_basic_differences.date;


SELECT
    base.*,
    diff.confirmed AS confirmed_diff
FROM covid19_detail_us AS base
LEFT OUTER JOIN covid19_detail_us_differences AS diff
    ON base.date = diff.date
    AND base.country = diff.country
    AND base.admin2 = diff.admin2;


CREATE TABLE address (
    id serial PRIMARY KEY,
    street varchar(255),
    street_number int,
    city varchar(255),
    zip_code varchar(6)
) ENGINE  = InnoDB;
INSERT INTO address(street, street_number, city, zip_code) values ('Do', 1, 'Engetov', '12300');


CREATE TABLE  doctor (
    id serial PRIMARY KEY,
    name varchar(255),
    surname varchar(255),
    address_id bigint UNSIGNED,

)

