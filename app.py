import streamlit as st
#configuração da pagina

st.set_page_config(
    page_title="Projeto de estilizção",
    page_icon="❤️",
    layout="wide"
)
#titulo e subtitulo
st.title("Projeto de Estilização Streamlit")
st.subheader("Exemplo de como organizar e estilizar um app")

#Barra lateral
st.sidebar.header("Filtros")
st.sidebar.checkbox("Ativar tema escuro", key="tema")
st.sidebar.slider("Selecionar valor", 0, 100, 25)

# métricas
st.metric("Vendas", "R$ 50.000", "+5%")
st.metric("Usuários", "1.200", "-2%")

#colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.header("coluna 1")
    st.success("Tudo certo!")
    st.button("Clique aqui")

with col2:
    st.header("Coluna 2")
    st.warning("Atenção!")
    st.radio("Escolha uma opção", ["Opção A", "Opção B", "Opção C"])

with col3:
    st.header("Coluna 3")
    st.info("Informação últil")
    st.selectbox("escolha um intem", ["Item 1", "Item 2", "Item 3"])

    #Expamder

with st.expander("Clique para ver mais detalhes"):
    st.write("Aqui dentro você pode colocar informações adicionais, gráficos ou tabelas.")
    st.checkbox("Ativar detalhe extra")
    st.text_input("Digite algo interessante")

#core e markdown
st.markdown(
    """
    <div style='background-color: #F9F9F9; padding: 10px; border-radius: 10px'>
    <h4 stylle='color: #FF5733;' >texto colorido em estilo personalizado</h4>
    </div>
    """,
    unsafe_allow_html= True
)

#Rodapé
st.markdown("---")
st.markdown("💡 Exemplo simples de estilização no Streamlit sem lógica complexa")