import mysql.connector
conn = mysql.connector.connect(user = 'root',password = 'zlxs',database = 'test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['1','MA'])
cursor.rowcount()
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',['1'])
values = cursor.fetchall()
values
cursor.close()
conn.close()