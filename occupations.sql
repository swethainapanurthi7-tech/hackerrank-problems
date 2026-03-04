SELECT 
    COALESCE(MAX(CASE WHEN Occupation = 'Doctor' THEN Name END), 'NULL') AS Doctor,
    COALESCE(MAX(CASE WHEN Occupation = 'Professor' THEN Name END), 'NULL') AS Professor,
    COALESCE(MAX(CASE WHEN Occupation = 'Singer' THEN Name END), 'NULL') AS Singer,
    COALESCE(MAX(CASE WHEN Occupation = 'Actor' THEN Name END), 'NULL') AS Actor
FROM (
    SELECT 
        Name,
        Occupation,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) ranked
GROUP BY rn
ORDER BY rn;
