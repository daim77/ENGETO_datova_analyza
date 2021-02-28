# === UKOL JOIN covid and weather via max temp, CZE and confirmed =====
# lekce 5 JOIN s covid2 ukol 3

DESCRIBE covid19_basic;
DESCRIBE weather;

SELECT
    w.date,
    w.city,
    MAX(w.temp)
FROM weather AS w
WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime)
AND w.city = 'Prague'
GROUP BY w.date;

SELECT
    cb.date,
    cb.confirmed
FROM covid19_basic AS cb
WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime )
AND cb.country = 'Czechia';


WITH max_temp AS (
        SELECT
            w.date,
            MAX(w.temp) AS mt
        FROM weather AS w
        WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime)
        AND w.city = 'Prague'
        GROUP BY w.date
        ),
    czech_covid AS (
        SELECT
            cb.date,
            cb.confirmed
        FROM covid19_basic AS cb
        WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime )
        AND cb.country = 'Czechia'
        )
SELECT
    *
FROM max_temp
LEFT OUTER JOIN czech_covid ON max_temp.date = czech_covid.date;


# odstraneni duplicitniho datumu a celkove hodnoty
SELECT
    MAX(wm.max_temp),
    SUM(cb.diff)
FROM (
         SELECT w.date,
                MAX(w.temp) AS max_temp
         FROM weather AS w
         WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime)
           AND w.city = 'Prague'
         GROUP BY w.date
     ) AS wm
LEFT OUTER JOIN (
        SELECT
            cb.date,
            cb.confirmed - LAG(cb.confirmed) over (PARTITION BY cb.country ORDER BY cb.date) AS diff
        FROM covid19_basic AS cb
        WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime )
        AND cb.country = 'Czechia'
    ) AS cb ON cb.date = wm.date;


# odstraneni duplicitniho datumu a hodnoty pro jednotlive dny
SELECT
    cb.date,
    wm.max_temp,
    cb.diff
FROM (
         SELECT w.date,
                MAX(w.temp) AS max_temp
         FROM weather AS w
         WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime)
           AND w.city = 'Prague'
         GROUP BY w.date
     ) AS wm
LEFT OUTER JOIN (
        SELECT
            cb.date,
            cb.confirmed - LAG(cb.confirmed) over (PARTITION BY cb.country ORDER BY cb.date) AS diff
        FROM covid19_basic AS cb
        WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime )
        AND cb.country = 'Czechia'
    ) AS cb ON cb.date = wm.date;


# odstraneni duplicitniho datumu a celkove hodnoty pro jednotlive dny
SELECT
    cb.date,
    wm.max_temp,
    cb.confirmed
FROM (
         SELECT w.date,
                MAX(w.temp) AS max_temp
         FROM weather AS w
         WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime)
           AND w.city = 'Prague'
         GROUP BY w.date
     ) AS wm
LEFT OUTER JOIN (
        SELECT
            cb.date,
            cb.confirmed
        FROM covid19_basic AS cb
        WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201031' AS datetime )
        AND cb.country = 'Czechia'
    ) AS cb ON cb.date = wm.date;


# odstraneni duplicitniho datumu a hodnoty pro jednotlive dny a posun max teploty = FINAL
WITH result AS (
    SELECT cb.date,
           LAG(wm.max_temp, 1) OVER (ORDER BY cb.date) AS max_temp,
           cb.diff
    FROM (
             SELECT w.date,
                    MAX(w.temp) AS max_temp
             FROM weather AS w
             WHERE w.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201101' AS datetime)
               AND w.city = 'Prague'
             GROUP BY w.date
         ) AS wm
    LEFT OUTER JOIN (
            SELECT cb.date,
                   cb.confirmed - LAG(cb.confirmed) over (PARTITION BY cb.country ORDER BY cb.date) AS diff
            FROM covid19_basic AS cb
            WHERE cb.date BETWEEN CAST('20201001' AS datetime) AND CAST('20201101' AS datetime)
              AND cb.country = 'Czechia'
    ) AS cb ON cb.date = wm.date
    WHERE cb.date > CAST('20200930' AS datetime)
)
SELECT
*
FROM result
WHERE result.date > CAST('20201001' AS datetime);