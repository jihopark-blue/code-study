select DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
from DOCTOR
WHERE MCDP_CD like 'CS' or MCDP_CD like 'GS'
order by HIRE_YMD DESC, DR_NAME;