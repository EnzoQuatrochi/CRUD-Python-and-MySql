import mysql.connector

conexao = mysql.connector.connect(
    host='add here your sql host',
    user='add here your sql user',
    password='Add here your sql password',
    database='projetoext',
)

cursor = conexao.cursor()
