
import streamlit as st
import datetime
from functions import *
from mensagens import *

empresas = criar_lista_b3()
st.set_page_config(page_icon=':alien:', page_title='MoneyMagic', layout='centered' )

st.sidebar.header('Bem vindo(a) :nerd_face:')

def seleciona_pagina():
    option = st.sidebar.selectbox('Slecione a uma página', ['Inicial', 'Quem é JBrutus?', 'Gráfico', 'Tabela', 'Estatístico', 'Explorador Estatístico',
                                                             'Previsão', 'Portifólio' ])
    if option == 'Inicial':
        pagina_inicial()
    elif option == 'Quem é JBrutus?':
        pagina_apresentacao()    
    elif option == 'Gráfico':
        grafico()
    elif option == 'Tabela':
        data_frame()
    elif option == 'Estatístico':
        estatistico()
    elif option == 'Explorador Estatístico':
        explorador_estatistico()
    elif option == 'Previsão':
        previsao()
    else:
        portifolio()

def pagina_inicial():
    cria_pagina_inicial()

def pagina_apresentacao():
    criar_pagina_apresentacao()

def data_frame():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Cotação do ativo {ativo} por {periodo} anos')
    df, ativo, anos = baixar_dados(ativo, periodo)
    mensagem_tabela()
    st.dataframe(df)
    

def grafico():
    ativo = st.sidebar.selectbox(f'Selecione um dos {len(empresas)} ativos do IBOV', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Gráfico do ativo {ativo} por {periodo} anos :office:')
    df, ativo, anos = baixar_dados(ativo, periodo)
    option = st.sidebar.radio('Selecione um dos dois tipos de gráficos', ['Gráfico Simples', 'Gráfico Iterativo'])
    if option == 'Gráfico Simples':
        mensagem_graficos()
        criar_grafico(df, ativo, anos)
    else:
        try:
            st.write('Aqui secriará um gráfico iterativo com plotly em breve')
        except:
            st.error('Ocorreu um problema com o pacote do python que cria gráficos iterativos')

def estatistico():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Estudo estatístico para o ativo {ativo} :fire:')
    with st.spinner('Gerando gráfico estatístico, por favor aguarde...'):
        criar_estatistico(ativo, periodo)
    
def explorador_estatistico():
    st.header('Explorador Estatístico :male_detective:')
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.sidebar.write('Role a tela para baixo e leia o texto após os gráficos')
    mensagem_explorador_estatistico()
    st.subheader('Clique no botão para avaliar todas as empresas da B3 utilizando a técnica estatística de variação do preço.')
    btn = st.button('RODAR O EXPLORADOR')
    if btn:
        st.header(':fire:'*7)
        executar_explorador_estatistico(periodo)
        
def previsao():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Previsão do ativo {ativo} por {periodo} anos :money_mouth_face:')
    st.write(f'Nessa parte famos usar aprendizado de máquina para prever o preço de fechamento futuro do ativo {ativo} utilizando dados de aprendizado de {periodo} anos')
    df, ativo, anos = baixar_dados(ativo, periodo)
    df, ativo, anos, ultima_cotacao = tratar_dados(df, ativo, anos)
    modelar_dados(df, ativo, anos, ultima_cotacao)

def portifolio():
    st.header('OTIMIZADRO DE AÇÕES :male_detective:')
    st.write("""Selecione uma ou mais empresas e clique no botão para calcular a melhor combinação para obter o maior rendimento.""")
    st.sidebar.success('OTIMIZADOR DE PORTIFÓLIO')
    # valor
    valor_investido = st.sidebar.number_input('Valor do Portifólio', min_value=1000, max_value=1000000, value=10000)
    #empresas = ['NVDA','AMZN', 'GOOGL','AMD','MSFT', 'AAPL', 'TSLA', 'SONY', 'META','NFLX']
    empresa2 = []
    for empresa in empresas:
        empresa2.append(f'{empresa}.SA')

    ativos = st.sidebar.multiselect('Selecione as empresas', empresa2)
    data_inicial = st.sidebar.date_input('Insira a data inicial', datetime(2026, 1, 1))
    data_final = st.sidebar.date_input("Insira da data final", datetime.today())
    botao = st.sidebar.button('CALCULAR')
    
    if botao:
        with st.spinner('Calculando a melhor combinação das empresas selecionadas...'):
            plota_grafico_Sharper(ativos, data_inicial, data_final, valor_investido)

if __name__ == '__main__':
    seleciona_pagina()

