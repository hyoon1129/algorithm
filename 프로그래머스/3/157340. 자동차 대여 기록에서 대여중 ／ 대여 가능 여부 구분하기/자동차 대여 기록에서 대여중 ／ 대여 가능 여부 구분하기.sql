-- 코드를 입력하세요
SELECT CAR_ID, 
    CASE
        WHEN EXISTS (
            select *
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY h2
            where h2.CAR_ID = h1.CAR_ID AND
            '2022-10-16' BETWEEN h2.START_DATE AND h2.END_DATE
        )
        THEN '대여중'
        ELSE '대여 가능'
    END AS 'AVAILABILITY'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h1
GROUP BY CAR_ID
ORDER BY CAR_ID DESC