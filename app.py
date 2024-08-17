import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def analise():
    st.title("Análise de Dados")
    st.write("Carregue um arquivo CSV para começar")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Dados carregados com sucesso!")
        
        st.write("Visualização dos dados:")
        st.dataframe(df)
        
        st.write("Estatísticas descritivas:")
        st.write(df.describe())
        
        st.write("Gráfico de barras:")
        columns = st.multiselect("Escolha as colunas para o gráfico de barras", df.columns)
        if columns:
            st.bar_chart(df[columns])
        
        st.write("Gráfico de dispersão:")
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_columns) > 1:
            x_axis = st.selectbox("Escolha a coluna para o eixo X", numeric_columns)
            y_axis = st.selectbox("Escolha a coluna para o eixo Y", numeric_columns)
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis])
            st.pyplot(fig)
        else:
            st.write("Não há colunas numéricas suficientes para criar um gráfico de dispersão.")

if __name__ == "__main__":
    analise()