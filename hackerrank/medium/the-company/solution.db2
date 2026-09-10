
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT C.COMPANY_CODE,
       C.FOUNDER,
       COUNT(DISTINCT L.LEAD_MANAGER_CODE),
       COUNT(DISTINCT S.SENIOR_MANAGER_CODE),
       COUNT(DISTINCT M.MANAGER_CODE),
       COUNT(DISTINCT E.EMPLOYEE_CODE)
FROM COMPANY C
LEFT JOIN LEAD_MANAGER L
    ON C.COMPANY_CODE = L.COMPANY_CODE
LEFT JOIN SENIOR_MANAGER S
    ON C.COMPANY_CODE = S.COMPANY_CODE
LEFT JOIN MANAGER M
    ON C.COMPANY_CODE = M.COMPANY_CODE
LEFT JOIN EMPLOYEE E
    ON C.COMPANY_CODE = E.COMPANY_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER
ORDER BY C.COMPANY_CODE;
