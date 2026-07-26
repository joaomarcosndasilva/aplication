import pandas as pd
import datetime as dt
from datetime import datetime
import yfinance as yf
import warnings
import streamlit as st
from time import sleep
warnings.filterwarnings('ignore')
from mensagens import *

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ -> ícones

def cria_pagina_inicial():
    mensagen_inicial()
    mensagem_legislacao_curta()

def criar_pagina_disclaimer():
    mensagem_para_pagina_legislacao()

def criar_pagina_apresentacao():
    mensagem_apresentacao()

def criar_lista_b3():
    acoes = pd.read_excel('ibov.xls')
    acoes = acoes['IBOV - Carteira do Dia 27/07/26']
    acoes = acoes.values[1:-3].tolist()

    return acoes

def baixar_dados(ativo, anos):
    """Baixa os dados utilizando o yahoo finance."""
    ticket = yf.Ticker(f'{ativo.upper()}.SA')
    df = ticket.history(f'{anos}y')

    return df, ativo, anos

def tratar_dados(df, ativo, anos):
    """Trata os dados recebendo a df após baixar com os dados do yahoo finance..."""
    df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    df['Tomorrow'] = df['Close'].shift(-1)
    ultima_cotacao = df[-1:]
    ultima_cotacao = ultima_cotacao.drop('Tomorrow', axis=1)
    df = df.dropna()

    return df, ativo, anos, ultima_cotacao

def criar_grafico(df, ativo, anos):
    """Cria o gráfico após utilizar as funções"""
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    fig, ax = plt.subplots(figsize=(14,7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=90))
    ax.xaxis.set_tick_params(rotation=30)

    ax.set_title(f'Cotação de ativo {ativo.upper()} por {anos} anos', fontsize=25)
    ax.set_ylabel('Valor em $', fontsize=18)
    ax.plot(df.index, df.Close, label='Fechamento', color='k')
    
    plt.grid()
    plt.legend()

    st.pyplot(fig)

def criar_estatistico(ativo, periodo, grafico=True):
    #"""Calcula indicadores estatísticos para tomada de decisão e retorna ou não um gráfico"""
    with st.spinner('Importando os pacotes necessários... aguarde....'):
        import matplotlib.pyplot as plt
        import matplotlib.gridspec as grid

    df, ativo, anos = baixar_dados(ativo, periodo)
    df['close_change'] = df['Close'].pct_change()
    ultima_cotacao = df.iloc[-1:]
    df = df.dropna()
    p25, p75 = df['close_change'].describe()[['25%', '75%']]
    pmin = max(min(df['close_change']), p25 - 1.5 * (p75 - p25))
    pmax = min(max(df['close_change']), p75 + 1.5 * (p75 - p25))

    if grafico:
        mensagem_estatistico1()
        fig = plt.figure(figsize=(12, 8))
        gs = grid.GridSpec(2, 2)

        ax = fig.add_subplot(gs[0, :])
        ax.plot(df.index, df['Close'], label='Fechamento', color='k')
        ax.set_title(f'Cotação de {ativo.upper()} por {periodo} ano(s)', fontsize=24)
        ax.set_ylabel('Preço em R$', fontsize=16)
        ax.legend()

        ax = fig.add_subplot(gs[1, 0])
        ax.plot(df.index, df.close_change, color='k', label='Variação (%)')
        ax.set_title('Variação (%) do preço', color='k', fontsize=14)
        ax.axhline(pmin, linestyle='--', label='Preço Mínimo')
        ax.axhline(pmax, color='red', linestyle='--', label='Preço Máximo')
        ax.scatter(ultima_cotacao.index, ultima_cotacao.close_change, color='purple', label='Último preço')
        ax.legend()

        ax = fig.add_subplot(gs[1, 1])
        ax.boxplot(df['close_change'])
        ax.axhline(pmin, linestyle='--', label='Preço mínimo')
        ax.axhline(pmax, linestyle='--', color='red', label='Preço máximo')
        ax.set_title(f'Variação de {ativo.upper()} por {periodo} ano(s)', fontsize=14)
        ax.set_ylabel('Variação %', fontsize=16)
        ax.legend()

        st.pyplot(fig)

        data = df[-1000:]
        gatilhos_compra = data[data['close_change'] < pmin]
        gatilhos_venda = data[data['close_change'] > pmax]

        
        # Pontos de compra
        st.subheader("""\n\nPontos de compra de acordo com essa estratégia :dart:\n\n""")
        mensagem_estatistico2()
        fig, ax = plt.subplots(figsize=(16, 8))

        ax.plot(data['Close'])
        ax.set_title(f'Ponto de compra de {ativo.upper()} dos ultimos 1000 períodos', fontsize=24)
        ax.set_ylabel('Preço em R$', fontsize=18)

        for i, c in gatilhos_compra.iterrows():
            ax.annotate('Compra', xy=(i, c.Close), xytext=(i, c.Close - 0.6),
                        arrowprops=dict(facecolor='blue', shrink=0.05))
        for i, c in gatilhos_venda.iterrows():
            ax.annotate('Venda', xy=(i, c.Close), xytext=(i, c.Close + 0.6),
                        arrowprops=dict(facecolor='red', shrink=0.05))
        st.pyplot(fig)

    return df, pmin, pmax
    
def executar_explorador_estatistico(anos_estudo=5):
    #""" Faz um loop e compara todas as empresas do ibovespa, filtrando as que se encaixarem na estratégia estatística """
    filtro = []
    empresas = criar_lista_b3()
    st.write('Agora aguarde... vamos estudar todas as ações que compõe o índice do IBOVESPA e verificar qual se encaixa na estratégia!')
    st.info('Buscando todas as ultimas cotações da B3 e valiando qual se encaixa no gatilho...')
    try:
        for empresa in empresas:
            with st.spinner(f'Analisando o ativo: {empresa}'):
                df, pmin, pmax = criar_estatistico(empresa, anos_estudo, grafico=False)
                if df.iloc[-1:, :]['close_change'].values < pmin:
                    filtro.append(empresa)
                    sleep(2)

        st.error(f'\n\nHoje tem apenas {len(filtro)} empresa(s) com oportunidade de lucro por esse método')
        for cia in filtro:
            st.warning(f'Análisando dados de {cia}')
            df, pmin, pmax = criar_estatistico(cia, anos_estudo)
            st.success(f'Fim da análise de {cia}')
            st.header('\n\n')
        st.write('\n\nO ídeal é rodar esse método todos os dias, muitas vezes temos oportunidades de ganhos diáriamente')
    except:
        st.error('Ocorreu um problema ao rodar o explorador de ações. Tente mais uma vez, por favor ')

def modelar_dados(df, ativo, anos, ultima_cotacao):
    """Importa as bibliotecas necessárias para fazer modelar os dados e assim executar a previsão..."""
    with st.spinner('Importando os pacotes necessários...'):
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import StandardScaler
        from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error
    
    # separando as ultimas 15 cotações para testar o modelo com as previsões passadas
    ultimas_15_prev = df[-15:]
    df = df[:-15]
        
    # separando em x e y
    x, y = df.drop('Tomorrow', axis=1), df['Tomorrow']
    x_validation, y_validation = ultimas_15_prev.drop('Tomorrow', axis=1), ultimas_15_prev.Tomorrow

    # embaralhando os dados para o modelo aprender
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Utilizando a padronização dos dados
    with st.spinner('Padronizando os dados...'):
        scaler = StandardScaler()
        scaler.fit_transform(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        x_validation_scaled = scaler.transform(x_validation)
        ultima_cotacao_scaled = scaler.transform(ultima_cotacao)

    # criando o modelo
    with st.spinner(f'Aprendendo com os dados de {ativo} por {anos} anos...'):
        sleep(1)
        model = LinearRegression()
        model.fit(x_train_scaled, y_train)
        y_pred = model.predict(x_test_scaled)
        y_pred_validation = model.predict(x_validation_scaled)
        preco_fechamento_futuro = model.predict(ultima_cotacao_scaled) 
    
    with st.spinner('Indicadores'):
        sleep(0.2)
        # calculando os indicadores
        st.write('\nIndicadores de eficiência do modelo:');sleep(1)
        st.write(f'R2 Score: {r2_score(y_test, y_pred)}');sleep(1)
        st.write(f'MSE: {root_mean_squared_error(y_test, y_pred)}');sleep(1)
        st.write(f'MAE: {mean_absolute_error(y_test, y_pred)}');sleep(1)

    st.write('\nTestes do modelo')
    data = pd.DataFrame({'Y Teste': y_validation, 'Modelo':y_pred_validation, 'Diferença':round((y_validation-y_pred_validation), 2)}) 

    with st.spinner('Plotando o resultado do modelo...'):
        sleep(1)
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        fig, ax = plt.subplots(figsize=(12,4))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_tick_params(rotation=60)
        ax.set_title(f'Teste do ativo {ativo.upper()} dos ultimos 15 dias de pregão...', fontsize=18)
        ax.set_ylabel('Valor em R$', fontsize=14)
        ax.plot(data.index, data['Y Teste'], label='Real', color='blue', marker='o')
        ax.plot(data.index, data['Modelo'], label='Previsão', color='red', marker='o')
        ax.scatter(ultima_cotacao.index, preco_fechamento_futuro, label=f'Previsão R$ {round(preco_fechamento_futuro[0], 2)}', 
                   color='purple', marker='^')
        plt.grid()
        plt.legend()

        st.pyplot(fig)
        st.success(f'Previsão para preço de fechamento do próximo pregão: R$ {round(preco_fechamento_futuro[0], 2):.2f}')

#################### PARTE DO PORTIFÓLIO ######################################

def baixar_dados_portifolio(lista_empresas, data_inicio, data_fim):
    df = yf.download(lista_empresas, data_inicio, data_fim)
    df = df['Close']
    retornos = df.pct_change().dropna()
    media_retornos = retornos.mean()

    return df, retornos, media_retornos

def calcula_pesos_ret_vol_sharpe(lista_empresas, data_inicio, data_fim, valor_investido=10000):
    import numpy as np
    """ Inicializa os pesos, ret, vol e sharper e simula os pesos e calcula o melhor Sharper Rátio"""
    df, retornos, media_retornos = baixar_dados_portifolio(lista_empresas, data_inicio, data_fim)
    # Parâmetros
    np.random.seed(42)
    empresas = lista_empresas[:]
    num_ports = valor_investido
    all_pesos = np.zeros((num_ports, len(empresas)))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sharper_arr = np.zeros(num_ports)
    cov_matrix = retornos.cov()

    # Simulando os pesos de acordo com o número de portifólio
    for x in range(num_ports):
        pesos = np.array(np.random.random(len(empresas)))
        pesos = pesos/np.sum(pesos)
        all_pesos[x, :] = pesos

        ret_arr[x] = np.sum(media_retornos * pesos * len(retornos))

        vol_arr[x] = np.sqrt(np.dot(pesos.T, np.dot(cov_matrix * len(retornos), pesos)))

        sharper_arr[x] = ret_arr[x]/vol_arr[x]

    print('Melhor Sharper Rátio', sharper_arr.max())

    return all_pesos, ret_arr, vol_arr, sharper_arr, cov_matrix

def plota_grafico_Sharper(lista_empresas, data_inicio, data_fim, valor_investido=10000):
    """ Baixa os dados selecionando a empresa, calcula pesos, volatilidade e sharper rátido e gera o gráfico """
    import matplotlib.pyplot as plt

    empresas, inicio, fim = lista_empresas, data_inicio, data_fim
  
    all_pesos, ret_arr, vol_arr, sharper_arr, cov_matrix = calcula_pesos_ret_vol_sharpe(lista_empresas, data_inicio, data_fim, valor_investido)
    
    indice = sharper_arr.argmax()
    max_vol = vol_arr[indice]
    max_ret = ret_arr[indice]
    """ Cria um gráfico dos portifólios simulados e o sharper rátio """
    fig, ax = plt.subplots(figsize=(12,6))
    ax.set_title('Melhor Combinação com empresas selecionadas', fontsize=22)
    ax.set_ylabel('Retornos', fontsize=18)
    ax.set_xlabel('Volatilidade', fontsize=18)
    ax.scatter(vol_arr, ret_arr, color='k', label='Possibilidades')
    ax.scatter(max_vol, max_ret, color='red', label=f'Melhor Sharper Ratio {round(sharper_arr.max(), 2)}')

    plt.legend()
    plt.grid()
    st.pyplot(fig)

    print('Melhor porcentagem investida devido ao Risco X Retorno')
    contador = 0
    investimentos = dict()
    lista_investimentos = list()
    for i in empresas:
        investimentos['empresa'] = i
        investimentos['porcentagem'] = all_pesos[indice][contador]*100
        lista_investimentos.append(investimentos.copy())
        contador += 1
    ordenada = sorted(lista_investimentos, key=lambda x: x['porcentagem'], reverse=True)
    st.info('De acordo com as empresas selecionadas, para ter o mair retorno, invista as seguintes porcentagem nos ativos:')
    for c, v in enumerate(ordenada):
        st.write(f" Invista: {round(v['porcentagem'],2)}% no ativo: {v['empresa']}")
        
    return lista_investimentos
