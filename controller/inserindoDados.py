import services.database as db 
import models.data as data

def incluir(city):

    cursor = db.conexao.cursor()

    add_cidade = ("INSERT INTO projetoext (cidade, estado) VALUES (%s, %s)")
    data_cidade = (data.cidade, data.estado) # type: ignore

    cursor.execute(add_cidade, data_cidade)
    
    db.conexao.commit()


def consultar():

    db.cursor.execute("SELECT * FROM projetoext")

    costumerList = []

    for row in db.cursor.fetchall(): # type: ignore

        costumerList.append(data.city(row[0], row[1], row[2]))
    
    return costumerList


def alterar(input_id_Alterar, input_cidade_Alterar, input_estado_Alterar):

    cursor = db.conexao.cursor()

    alterar = ("UPDATE projetoext SET cidade = %s, estado = %s WHERE ID = %s")
    
    valores = (input_cidade_Alterar, input_estado_Alterar, input_id_Alterar)

    cursor.execute(alterar,valores)

    db.conexao.commit()


def excluir(input_id_Excluir):

    cursor = db.conexao.cursor()

    excluir = (f"DELETE FROM projetoext WHERE ID = {input_id_Excluir}")

    cursor.execute(excluir)
    
    db.conexao.commit()

def mostrar(input_id_Excluir):

    costumerList = []

    mostrar = db.cursor.execute(f'SELECT * FROM projetoext WHERE ID = {input_id_Excluir}')

    for row in db.cursor.fetchall():  

        costumerList.append(data.city(row[0], row[1], row[2]))  

    return costumerList