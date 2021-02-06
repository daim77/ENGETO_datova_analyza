SELECT *

FROM covid19_basic_differences
WHERE 1=1

AND country = 'Czechia'
AND date >= '20200901'
AND date <= '20200930'

ORDER BY confirmed DESC;
