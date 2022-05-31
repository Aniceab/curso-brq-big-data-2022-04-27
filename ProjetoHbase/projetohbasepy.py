from sqlite3 import Cursor
import csv
import mysql.connector 
from pandas import DataFrame
db = mysql.connector.connect(host='177.104.61.65',user='fgv', password='fgv', port=3306)

select_my=db.cursor()
select_my.execute("use stockfgv")
select_my.execute("select s.date_ as 'date',p.shares,p.symbol,s.close,ROUND(s.close * p.shares, 2) total from stockfgv.stocks s INNER JOIN stockfgv.portfolio p ON p.symbol = s.symbol 	WHERE s.date_ = '2020-06-12';")
df=DataFrame(select_my.fetchmany(20))
csv=df.to_csv('tabela.csv',index= False)
#print(df)
#db.commit()
if (db.connected()):
    db.close()
Cursor.close()
print("Conexão encerrada")