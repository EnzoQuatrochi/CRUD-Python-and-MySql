import streamlit as st
import pandas as pd

import controller.inserindoDados as inserindoDados

def delete():

    st.title("Delete/Excluir")

    with st.form(key="none3"):

        input_id_Excluir = st.text_input(label=("Id que deseja excluir"))

        input_button_submit1 = st.form_submit_button("Ver")

        if input_button_submit1:

            costumerList = []

            for item in inserindoDados.mostrar(input_id_Excluir): 

                costumerList.append([item.id, item.cidade, item.estado])

            df = pd.DataFrame(

                costumerList,
                columns=['Id', 'Cidade', 'Estado']
            )

            st.table(df)

        input_button_submit2 = st.form_submit_button("Excluir")

        if input_button_submit2:

            st.success("Excluido")

            inserindoDados.excluir(input_id_Excluir)