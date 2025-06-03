select MCDP_CD AS '진료과코드', count(PT_NO) AS '5월예약건수'
from APPOINTMENT
where APNT_YMD BETWEEN '2022-05-01' AND '2022-05-31-23:59:59.999999'
group by MCDP_CD
order by 5월예약건수, 진료과코드