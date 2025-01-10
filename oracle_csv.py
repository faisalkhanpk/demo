import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect('hr/hr@//localhost:1521/oracle')

sql_query = pd.read_sql_query(''' select * from employees''',conn)

sql_query.to_csv(r'E:\PHYTON\EMPLOYEE.CSV', index = False )
## with index column
##sql_query.to_csv(r'E:\PHYTON\EMPLOYEE_22.CSV' )