from os import write
from numpy.core.fromnumeric import size

import streamlit as st
import pandas as pd

import controller.inserindoDados as inserindoDados

def read():

    st.title("Read/Consultar")

    costumerList = []

    for item in inserindoDados.consultar():

        costumerList.append([item.id, item.cidade, item.estado])

    df = pd.DataFrame(

        costumerList,
        columns=['Id', 'Cidade', 'Estado']
    )

    st.table(df)