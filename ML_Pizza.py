import streamlit as st  # Importa a biblioteca Streamlit para criar a interface
import pandas as pd  # Importa o pandas para manipulação de dados
from sklearn.linear_model import LinearRegression  # Importa o modelo de regressão linear do Scikit-Learn

# Carrega os dados do arquivo CSV
df = pd.read_csv("dados/pizzas.csv")

# Inicializa o modelo de regressão linear
modelo = LinearRegression()

# Define as variáveis independentes (X) e dependentes (y) para o treinamento do modelo
x = df[["diametro"]]  # Característica usada para previsão
y = df[["preco"]]  # Valor que queremos prever

# Treina o modelo com os dados disponíveis
modelo.fit(x, y)

# Configuração da interface do usuário com Streamlit
st.title("🍕 Prevendo o valor de uma pizza")  # Título do aplicativo
st.divider()  # Linha divisória para organização visual

# Entrada do usuário para inserir o diâmetro da pizza
diametro = st.number_input("Digite o tamanho do diâmetro da pizza:")

# Verifica se o usuário digitou um valor válido para fazer a previsão
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]  # Faz a previsão com base no diâmetro inserido
    st.success(f"O valor estimado para uma pizza de {diametro:.2f} cm é R${preco_previsto:.2f}.")  # Exibe o resultado
    st.balloons()  # Animação com balões para melhor experiência do usuário