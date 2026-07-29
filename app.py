
import streamlit as st
import datetime
from functions import *
from mensagens import *


#empresas = ['ALOS3', 'ASAI3', 'AURE3', 'AXIA3' , 'AZZA3', 'B3SA3', 'BBSE3', 'BBDC3', 'BBDC4', 'BRAP4', 'BBAS3', 'BRKM5',
#             'BRAV3', 'BPAC11', 'CXSE3', 'CEAB3', 'CMIG4', 'COGN3', 'CSMG3', 'CPLE3', 'CSAN3', 'CPFE3', 'CMIN3', 'CURY3',
#            'CYRE3', 'DIRR3', 'EMBJ3', 'ENGI11', 'ENEV3', 'EGIE3', 'EQTL3', 'FLRY3', 'GGBR4', 'GOAU4', 'HAPV3', 'HYPE3',
#            'IGTI11', 'ISAE4', 'ITSA4', 'ITUB4', 'KLBN11', 'RENT3', 'LREN3', 'MGLU3', 'POMO4', 'MBRF3', 'BEEF3', 'MOTV3',
#            'MRVE3', 'MULT3', 'NATU3', 'PETR3', 'PETR4', 'RECV3', 'PSSA3', 'PRIO3', 'RADL3', 'RDOR3', 'RAIL3', 'SBSP3',
#             'SANB11', 'CSNA3', 'SLCE3', 'SMFT3', 'SUZB3', 'TAEE11', 'VIVT3', 'TIMS3', 'TOTS3', 'UGPA3', 'USIM5', 'VALE3',
#              'VAMO3', 'VBBR3', 'VIVA3', 'WEGE3', 'YDUQ3']"

empresas = criar_lista_b3()
st.set_page_config(page_icon=':chart_with_upwards_trend:', page_title='MoneyMagic', layout='centered' )

st.sidebar.header('Bem vindo(a) :nerd_face:')

def seleciona_pagina():
    option = st.sidebar.selectbox('Slecione a uma página', ['Inicial', 'Disclaimer', 'Quem é JBrutus?', 'Gráfico', 'Tabela', 'Estatístico', 'Explorador Estatístico',
                                                             'Previsão', 'Portifólio' ])
    if option == 'Inicial':
        pagina_inicial()
    elif option == 'Disclaimer':
        pagina_disclaimer()
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
    
def pagina_disclaimer():
    criar_pagina_disclaimer()

def pagina_apresentacao():
    criar_pagina_apresentacao()

def data_frame():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Cotação do ativo {ativo} por {periodo} anos')
    df, ativo, anos = baixar_dados(ativo, periodo)
    mensagem_tabela()
    st.dataframe(df)
    st.info('Fim dos dados da tabela. :tada: :tada: :tada:')
    
def grafico():
    ativo = st.sidebar.selectbox(f'Selecione um dos {len(empresas)} ativos do IBOV', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Gráfico do ativo {ativo} por {periodo} anos. :chart_with_upwards_trend: :chart_with_downwards_trend:')
    df, ativo, anos = baixar_dados(ativo, periodo)
    option = st.sidebar.radio('Selecione um dos dois tipos de gráficos', ['Gráfico Simples', 'Gráfico Iterativo'])
    if option == 'Gráfico Simples':
        mensagem_graficos()
        criar_grafico(df, ativo, anos)
        st.sidebar.info('Em breve gráfico interativo com plotly :hugs:')
        st.success('Em breve, também, vou postas os melhores indicadores de preço e volume mais usados por traders de todo o mundo. :crown:')

    else:
        try:
            st.error('Vou postar em breve os gráficos iterativos de candlestick e volume, mas por enquanto, vou deixar o gráfico simples por um curto periodo :hugs:')
        except:
            st.error('Ocorreu um problema com o pacote do python que cria gráficos iterativos')

def estatistico():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    mensagem_legislacao_curta()
    st.header(f'Estudo estatístico para o ativo {ativo} :bar_chart:')
    btn_estatistico = st.button('RODAR O ESTUDO ESTATÍSTICO')
    st.info(':point_up_2: Clique aqui após selecionar o ativo e o período')
    if btn_estatistico:
        with st.spinner('Gerando gráfico estatístico, por favor aguarde...'):
            criar_estatistico(ativo, periodo)
    
def explorador_estatistico():
    st.header('Explorador Estatístico :male_detective: :chart_with_downwards_trend: :chart_with_upwards_trend:')
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.sidebar.write('Role a tela para baixo e leia o texto após os gráficos')
    mensagem_explorador_estatistico()
    mensagem_legislacao_curta()
    st.subheader('Clique no botão para avaliar todas as empresas da B3 utilizando a técnica estatística de variação do preço.')
    btn = st.button('RODAR O EXPLORADOR')
    st.info(':point_up_2: Clique aqui para gerar um estudo estatistico de todas as empresas da B3. Esse estudo é baseado na variação do preço de fechamento do ativo, e não é recomendação de compra ou venda de ativos. :hugs:')
    if btn:
        st.header(':fire:'*15)
        #executar_explorador_estatistico(periodo)
        mensagem_legislacao_estatistico()
        mensagem_fim_pagina()
        
def previsao():
    ativo = st.sidebar.selectbox('Selecione uma empresa', empresas)
    periodo = st.sidebar.slider('Selecione a quantidade de anos', value=5, min_value=1, max_value=20)
    st.header(f'Previsão do ativo {ativo} por {periodo} anos :dollar: :money_with_wings:')
    mensagem_previsao()
    df, ativo, anos = baixar_dados(ativo, periodo)
    df, ativo, anos, ultima_cotacao = tratar_dados(df, ativo, anos)
    btn_prev = st.button('RODAR O MODELO DE PREVISÃO')
    st.success(':point_up_2: Clique aqui após selecionar o ativo e o período')
    if btn_prev:
        modelar_dados(df, ativo, anos, ultima_cotacao)
    

def portifolio():
    st.header('Otimizador de portifólio. Sharpe Rátio :male_detective:')
    mensagem_portifolio()
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
    mensagem_legislacao_curta()
    
    if botao:
        with st.spinner('Calculando a melhor combinação das empresas selecionadas...'):
            plota_grafico_Sharper(ativos, data_inicial, data_final, valor_investido)

if __name__ == '__main__':
    seleciona_pagina()

