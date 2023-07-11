import streamlit as st

import controller.inserindoDados as inserindoDados
import models.data as data

def create():
    
    st.title("Create/Incluir")

    with st.form(key="none"):
            
        input_cidade = st.text_input(label=("Cidade"))
        input_estado = st.selectbox("Estado", options = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RR", "RO", "RJ", "RN", "RS", "SC", "SP", "SE", "TO",])
        input_button_submit = st.form_submit_button("Adicionar")

        if input_button_submit:
            
            data.cidade = input_cidade # type: ignore
            data.estado = input_estado # type: ignore

            st.success("Adicionado")

            inserindoDados.incluir(inserindoDados)