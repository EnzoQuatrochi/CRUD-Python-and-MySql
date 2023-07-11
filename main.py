from os import write
from numpy.core.fromnumeric import size

import streamlit as st

import screens.Create as create
import screens.Update as update
import screens.Delete as delete
import screens.Read as read

st.sidebar.title("Menu")
opção = st.sidebar.selectbox('Opções', ['Create/Incluir', 'Read/Consultar', 'Update/Alterar', 'Delete/Excluir'])

if opção == 'Create/Incluir':

    create.create()

if opção == 'Read/Consultar':

    read.read()

if opção == 'Update/Alterar':

    update.update()

if opção == 'Delete/Excluir':

    delete.delete()