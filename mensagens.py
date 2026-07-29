import streamlit as st


def mensagen_inicial():
    st.header('Bem-vindo ao universo da Inteligência Artificial aplicada ao Mercado de Ações! 🚀')
    st.warning(':point_left: Navegue pelas páginas pelo menu dropdown à sua esquerda')
    st.info(
    ":loudspeaker: Este projeto tem como objetivo exclusivamente demonstrar, de forma didática, como diferentes metodologias de análise de ativos financeiros podem ser desenvolvidas e avaliadas. \n\nAo longo do conteúdo, exploraremos desde conceitos clássicos da análise quantitativa e fundamentalista até abordagens modernas baseadas em Inteligência Artificial, Machine Learning e Grandes Modelos de Linguagem (LLMs). \n\nTodo o material possui caráter EDUCACIONAL e experimental, buscando apresentar exemplos práticos, estudos de caso e resultados reproduzíveis para facilitar o aprendizado, sem QUALQUER PROMESSA de RENTABILIDADE ou RECOMENDAÇÃO de investimento. O foco é compartilhar conhecimento, incentivar o pensamento crítico e mostrar, com total transparência, como essas técnicas podem ser implementadas e analisadas na prática. 📚"
)
    st.warning(':point_left: Navegue pelas páginas pelo menu dropdown à sua esquerda')
    st.sidebar.success('Previsão de preços com IA')
    st.sidebar.error('Ganho com estatística')
    st.sidebar.warning('Melhores indicadores gráficos')
    st.sidebar.info('Técnicas fundamentalista')
    mensagem_legislacao_curta()

def mensagem_apresentacao():
    st.header('Um pouco sobre minha história até aqui :hugs:')
    st.warning('Estou em processo de certfificação CNPI-p, então reformulei todo o conteúdo, inicialmente criado, para não caracterizar recomendação de compra ou venda de ativos.')
    st.write("""
Meu nome é João Marcos. Sou economista, engenheiro de software e especialista em Engenharia de Inteligência Artificial, com especialização em Desenvolvimento de Sistemas com Python e também em Finanças voltadas ao Mercado Financeiro. 

Atualmente, trabalho em uma distribuidora de energia elétrica como operador em tempo real e ao longo da minha trajetória, também realizei diversos cursos na área de Ciência de Dados e participei de vários projetos envolvendo análise e modelagem de dados.

Nos últimos anos, dediquei meu tempo ao desenvolvimento e à validação de modelos quantitativos utilizando Inteligência Artificial, Machine Learning e Análise de Dados para identificar oportunidades no mercado financeiro.

Ao longo dessa jornada, descobri uma verdade que poucos comentam: o maior inimigo do investidor raramente é o mercado. Na maioria das vezes, são as próprias emoções — especialmente a ganância, a ansiedade e a falta de disciplina para seguir um método consistente.

O mercado financeiro está em constante transformação. Estratégias que funcionam hoje podem perder eficiência amanhã. Por isso, adaptação, estudo contínuo e gestão de risco são tão importantes quanto encontrar boas oportunidades.

📌 O que você encontrará aqui?

Você não encontrará promessas de enriquecimento rápido, "fórmulas mágicas" ou o famoso "Santo Graal" dos investimentos.

O que encontrará é um método baseado em:

    • Inteligência Artificial e Machine Learning;
    • Análise quantitativa e fundamentalista;
    • Gestão de risco;
    • Disciplina operacional;
    • Transparência em todas as operações.

Mais do que apresentar uma estratégia, quero mostrar como ela foi aplicada na prática.

Neste momento eu uso o meu proprío dinheiro e gostaria de compartilhar minhas análises, critérios de seleção, pontos de entrada e saída, além das notas de corretagem, sempre que possível. Assim, você poderá acompanhar como as decisões são tomadas e compreender a lógica por trás de cada operação.

Meu objetivo é, APÓS EU CONSEGUIR MINHA CERTIFICAÇÃO CNPI-p, construir uma comunidade de investidores que tomem decisões fundamentadas em dados, estatística e tecnologia, reduzindo a influência das emoções e buscando maior consistência nos resultados ao longo do tempo.

Seja muito bem-vindo(a)! Vamos explorar juntos como a Inteligência Artificial pode se tornar uma poderosa aliada na busca por decisões mais inteligentes no mercado financeiro.

🚨🚨🚨 AVISO LEGAL 🚨🚨🚨

Todo o conteúdo disponibilizado possui caráter exclusivamente educacional e informativo. As análises apresentadas não constituem recomendação de investimento, oferta de compra ou venda de ativos, nem consultoria financeira. Toda decisão de investimento é de responsabilidade exclusiva do investidor.

            """)
    st.sidebar.image('WhatsApp Image 2026-07-26 at 02.41.47 (1).jpeg', 
             caption='João Marcos - Economista, Engenheiro de Software e Especialista em Inteligência Artificial :brazil:')
    st.info('Fim da minha apresentação. :tada: :tada: :tada:')

def mensagem_graficos():
    st.write("""
            Aqui teremos gráficos de preços e volume do ativo selecionado. A ideia é que você consiga identificar padrões de comportamento do preço e volume para que possamos criar estratégias de compra e venda.
            """)

def mensagem_final_grafico():
    st.info('Além dos gráficos iterativos, tembém vou trazer os indicadores de preço e volume mais usado por trades atualmente :crown:')

def mensagem_estatistico1():
    st.write("""
            Nesse gráfico visualizaremos a variação percentual do preço em relação ao tempo. Observe o primeiro gráfico inferior desse plot e veja como o preço trabalhou em um intervalo que é delimitado pelas linhas vermelha e azul. A linha vermelha representa o preço máximo e a linha azul representa o preço mínimo. O preço do ativo tende a oscilar dentro desse intervalo, e quando ele se aproxima da linha azul, há uma maior probabilidade de ocorrer uma reversão para cima, enquanto que quando ele se aproxima da linha vermelha, há uma maior probabilidade de ocorrer uma reversão para baixo.
            
            Uma da estratégia que usamos é comprar quando o preço estiver próximo a esse percentual, isto é, abaixo ou próximo do preço mínimo identificado pela linha azul e vender próximo a linha vermelha de preço máximo. Perceba que estatisticamente, o preço tende a oscilar dentro desse intervalo, e quando ele se aproxima da linha azul, há uma maior probabilidade de ocorrer uma reversão para cima, enquanto que quando ele se aproxima da linha vermelha, há uma maior probabilidade de ocorrer uma reversão para baixo.

                        """)
    
def mensagem_estatistico2():
    st.write("""
Nesta seção serão apresentados, de forma didática, os pontos teóricos de compra e venda dos ativos com base nos critérios definidos pela estratégia. Embora alguns ativos apresentem desempenho superior a outros, nenhuma decisão será considerada sem antes passar por um conjunto de filtros adicionais. Entre eles estão a análise do comportamento do volume negociado, indicadores técnicos e indicadores fundamentalistas, que ajudam a identificar possíveis riscos e evitar ativos com maior probabilidade de comprometer o desempenho da estratégia. O objetivo é demonstrar como a combinação de diferentes critérios pode contribuir para uma seleção de ativos mais consistente e criteriosa.
""")  

def mensagem_tabela():
    st.write('Aqui temos as cotações nua e crua do ativo selecionado a qual você poderá conseguir em qualquer corretora, site da B3 ou até mesmo pelo Google.')

def mensagem_explorador_estatistico():
   st.write("""
        Nossa objetivo é analisar todo o universo de ativos da B3 em busca das oportunidades mais promissoras. Cada ativo será submetido a esse filtro estatístico de variação do preço. Apenas aqueles que atenderem a esses requisitos definidos pela metodologia serão incluídos no radar de acompanhamento de curtíssimo prazo.

        A proposta é demonstrar uma abordagem sistemática e orientada por dados, reduzindo a influência das emoções na tomada de decisão. Em vez de depender exclusivamente de opiniões ou análises subjetivas, utilizamos critérios objetivos para selecionar ativos com características que historicamente apresentaram maior probabilidade de gerar bons resultados, sempre com foco em diversificação, gestão de risco e disciplina operacional.
        """)

def mensagem_para_pagina_legislacao():
    st.markdown("<h1 style='text-align: center;'>ALERTA MUITO IMPORTANTE</h1>", unsafe_allow_html=True)
    st.warning(""" :rotating_light: :rotating_light: :rotating_light:
        Disclaimer: Este material foi elaborado exclusivamente para fins educacionais e informativos. As análises, opiniões e exemplos apresentados não devem ser interpretados como recomendação
        de investimento, relatório de análise, oferta ou solicitação para compra ou venda de valores mobiliários, nos termos da regulamentação 
        aplicável da Comissão de Valores Mobiliários (CVM). Rentabilidade passada não representa garantia de resultados futuros. Os investimentos envolvem riscos, inclusive de perda do capital investido. Antes de 
        investir, avalie seu perfil de investidor e consulte profissionais devidamente habilitados, quando necessário. :rotating_light: :rotating_light: :rotating_light:
        """)
    st.markdown("<h1 style='text-align: center;'>Para cumprimento da legislação!</h1>", unsafe_allow_html=True)
    st.sidebar.warning(""" :rotating_light: :rotating_light: :rotating_light:
        Este conteúdo é exclusivamente educacional e não constitui recomendação de investimento, consultoria financeira ou oferta de compra e venda de ativos.
        Toda decisão de investimento é de responsabilidade do investidor. :rotating_light: :rotating_light: :rotating_light:
                        """)

def mensagem_legislacao_curta():
    st.sidebar.warning(""" :rotating_light: :rotating_light: :rotating_light: 
        Este conteúdo é exclusivamente educacional e não constitui recomendação de investimento, consultoria financeira ou oferta de compra e venda de ativos.
        Toda decisão de investimento é de responsabilidade do investidor. :rotating_light: :rotating_light: :rotating_light:
               """)

def mensagem_portifolio():
    st.write("""
            Aqui teremos uma ferramenta desenvolvida para análise histórica de dados do mercado, com o objetivo de identificar como determinados ativos se comportaram no passado em diferentes cenários. Através da avaliação de preços, volumes negociados e outros indicadores, poderemos estudar padrões e combinações de ativos que apresentaram, historicamente, uma relação interessante entre retorno e risco.

            É importante destacar que essas informações representam apenas comportamentos passados e não garantem resultados futuros. O objetivo desta ferramenta é exclusivamente educacional: demonstrar como dados históricos podem ser analisados para a criação e avaliação de estratégias de compra e venda, sempre considerando que o mercado financeiro envolve incertezas e riscos.
            """)
    st.info(':dart: Resumindo:\n\nSe você tivesse escolhido com base em seu $: (Valor do portifólio)\n\nAs ações: (Selecione as empresas)\n\nNo período: (data inicial e data final)\n\nÉ só clicar :point_up_2: no botão para saber qual rentabilidade você teria de acordo com suas escolhas no período selecionado!')
    st.error(':rotating_light: :rotating_light: :rotating_light: Nesse momento eu tive que limitar muito o código para não configurar recomendação!')
def mensagem_legislacao_estatistico():
    st.markdown("<h1 style='text-align: center;'>ALERTA MUITO IMPORTANTE</h1>", unsafe_allow_html=True)
    st.info("""
        :mega: :mega: Por questões regulatórias e em respeito à legislação vigente, não posso divulgar publicamente todos os critérios utilizados no processo de seleção dos ativos do índice B3, uma vez que isso poderia ser interpretado como recomendação de compra ou venda de valores mobiliários.

        :mega: :mega: Atualmente, estou em processo de certificação e de formalização de parceria com uma instituição do mercado financeiro. A expectativa é que, nos próximos meses, eu tenha maior liberdade para apresentar essa metodologia de forma completa e em conformidade com as normas aplicáveis.

        :mega: :mega: Enquanto isso, todo o conteúdo disponibilizado neste projeto terá caráter exclusivamente educacional e demonstrativo, com o objetivo de explicar os conceitos, os métodos de análise e os fundamentos matemáticos utilizados na construção da estratégia, sem constituir recomendação de investimento.
        
        
        :hugs: Agradeço a compreensão de todos e reforço que o foco deste projeto é compartilhar conhecimento, incentivar o pensamento crítico e mostrar, com total transparência, como essas técnicas podem ser implementadas e analisadas na prática.""")

def mensagem_previsao():

    st.write("""
            Aqui teremos uma ferramenta desenvolvida para previsão de preços de ativos do mercado financeiro utilizando técnicas de Inteligência Artificial e Machine Learning. Através da análise de dados históricos, padrões de comportamento do mercado e algoritmos avançados, o modelo busca identificar tendências e fornecer estimativas para os preços futuros dos ativos.

            É importante destacar que essas previsões são baseadas em dados passados e não garantem resultados futuros. O objetivo desta ferramenta é exclusivamente educacional: demonstrar como técnicas de IA podem ser aplicadas na análise financeira, sempre considerando que o mercado envolve incertezas e riscos.
            """)
    st.info(':point_left: Selecione o ativo e o período de análise para gerar a previsão do preço de fechamento do próximo pregão. :chart_with_upwards_trend:')

def mensagem_fim_pagina():
    st.info('Fim da página. :tada: :tada: :tada:')