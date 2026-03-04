SELECT 
    c.company_code,
    c.founder,
    COUNT(DISTINCT lm.lead_manager_code)   AS total_lead_managers,
    COUNT(DISTINCT sm.senior_manager_code) AS total_senior_managers,
    COUNT(DISTINCT m.manager_code)         AS total_managers,
    COUNT(DISTINCT e.employee_code)        AS total_employees
FROM COMPANY c
LEFT JOIN LEAD_MANAGER lm
    ON c.company_code = lm.company_code
LEFT JOIN SENIOR_MANAGER sm
    ON c.company_code = sm.company_code
LEFT JOIN MANAGER m
    ON c.company_code = m.company_code
LEFT JOIN EMPLOYEE e
    ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
