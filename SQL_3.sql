SELECT
    country,
    date,
    confirmed
FROM covid19_basic
WHERE country ='Austria'
ORDER BY date DESC;

SELECT
    deaths
FROM covid19_basic
WHERE country = 'Czechia'
ORDER BY date DESC;

SELECT
    SUM(confirmed)
FROM covid19_basic
WHERE date < CAST('2020-08-31' AS  datetime);

SELECT
    DISTINCT province
FROM covid19_detail_us
order by province ASC;

SELECT
    *,
    covid19_basic.confirmed - covid19_basic.recovered AS ill
FROM covid19_basic
ORDER BY date DESC
LIMIT 10;

SELECT
    country,
    confirmed
FROM covid19_basic_differences
WHERE date = CAST('2020-07-01' AS datetime )
ORDER BY confirmed DESC
LIMIT 10;

SELECT
    country AS 'state',
    CASE
        WHEN confirmed > 10000 THEN '1' ELSE '0'
    END AS more_than_10000
FROM covid19_basic_differences
WHERE date = CAST('2020-07-01' AS datetime )
ORDER BY confirmed DESC;

SELECT
    MIN(date) AS 'oldest',
    MAX(date) AS 'youngest'
FROM covid19_detail_us;

SELECT
    DISTINCT country,
    CASE
        WHEN country = 'France'
                OR country = 'Germany'
                OR country = 'Spain'
            THEN 'EU'
            ELSE 'other'
    END AS flag
FROM covid19_basic
ORDER BY flag;

SELECT
    DISTINCT country,
    CASE
        WHEN country IN ('France', 'Germany', 'Spain')
        THEN 'EU'
        ELSE 'other'
    END AS flag
FROM covid19_basic
ORDER BY flag;

SELECT
    DISTINCT country,
    CASE WHEN country like 'Ge%' THEN 'Ge state' ELSE 'other'
    END AS flag_ge
FROM covid19_basic
ORDER BY flag_ge;

SELECT
       country,
    CASE
        WHEN confirmed <= 1000 THEN 'k'
        WHEN confirmed <= 10000 THEN  'kk'
        WHEN confirmed > 10000 THEN  'kkk'
        ELSE 'error'
    END AS category
FROM covid19_basic
ORDER BY date DESC;

SELECT
    country,
    CASE
        WHEN country in ('US', 'India', 'China') AND confirmed >= 10000 THEN 1
        ELSE 0
    END AS flag
FROM covid19_basic_differences
ORDER BY flag DESC;

SELECT
    country,
    CASE
        WHEN country like '%a' THEN '-a'
        ELSE '--'
    END AS flag
FROM covid19_basic_differences;

CREATE VIEW v_martin_danek_cumul AS
SELECT
    date,
    confirmed,
    country
FROM covid19_basic_differences
WHERE country IN ('China', 'US', 'India');

SELECT
    distinct country
FROM covid19_basic
WHERE country IN
    (
        SELECT
            country
        FROM countries
        WHERE population >= 100000000
        );

SELECT
    country
FROM covid19_basic
WHERE country IN
    (
        SELECT
            DISTINCT country
        FROM covid19_detail_us
        );

SELECT
    confirmed - COALESCE(LAG(confirmed) over (PARTITION BY country ORDER BY date), 0) AS diff
FROM  covid19_basic
WHERE country = 'Czechia';

WITH diff_table AS
(
    SELECT
        country,
        confirmed - LAG(confirmed) OVER (PARTITION BY country ORDER BY date) AS diff
    FROM covid19_basic
)
SELECT
    DISTINCT country
FROM diff_table
WHERE diff > 10000;

SELECT
    country,
    abbreviation,
    domain_tld
FROM countries
WHERE LOWER(abbreviation) != SUBSTRING(LOWER(domain_tld), 2, 2);

SELECT
    country,
    capital_city
FROM countries
WHERE capital_city like '% %';
