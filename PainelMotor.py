import streamlit as st
from motorrcOperacional import pageOperacional
from motorrctransp import pageTransporte


##############################################################################################################################################
#CHAMANDO O MOTOR POR PRODUTO
with st.sidebar:
   st.title("Motor de Cálculo")
   pageProduto = st.selectbox('Selecione o Produto',['RC Ambiental Transporte', 'RC Ambiental Operacional'],index=None, placeholder="Produtos")
   
if pageProduto =='RC Ambiental Operacional':
     pageOperacional()

if pageProduto =='RC Ambiental Transporte':
     pageTransporte()