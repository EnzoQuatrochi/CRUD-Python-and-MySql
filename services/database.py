import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0709',
    database='projetoext',
)

cursor = conexao.cursor()