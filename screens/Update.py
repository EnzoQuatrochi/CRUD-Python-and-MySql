import streamlit as st
import pandas as pd

import controller.inserindoDados as inserindoDados
import screens.Read as rd
import models.data as data

def update():

    st.title("Update/Alterar")

    with st.form(key="none2"):

        input_id_Alterar = st.text_input(label=("Id que deseja alterar"))

        botaoConsultar = st.form_submit_button("Consultar esse Id")

        if botaoConsultar:

            costumerList = []

            for item in inserindoDados.mostrar(input_id_Alterar): 

                costumerList.append([item.id, item.cidade, item.estado])

            df = pd.DataFrame(

                costumerList,
                columns=['Id', 'Cidade', 'Estado']
            )

            st.table(df)

        input_cidade_Alterar = st.text_input(label=("Nova cidade"))
        input_estado_Alterar = st.selectbox("Novo Estado", options = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", 
        "PB", "PR", "PE", "PI", "RR", "RO", "RJ", "RN", "RS", "SC", "SP", "SE", "TO",])

        input_button_submit_Alterar = st.form_submit_button("Alterar")

        if input_button_submit_Alterar:

            st.success("Alterado")

            inserindoDados.alterar(input_id_Alterar, input_cidade_Alterar, input_estado_Alterar)