import streamlit as st


def mensagen_inicial():
    st.header('Bem-vindo ao universo da Inteligência Artificial aplicada ao Mercado de Ações! 🚀')
    st.subheader("Se você já testou dezenas de estratégias, acompanhou recomendações de especialistas e percebeu que seus " \
             "resultados mal superam investimentos conservadores, como um CDB, este espaço foi criado para você.")
    st.write('Quero mostrara para você as várias técnicas sendo algumas antigas e outras das mais atuais possíveis envolvendo LLMs para operação de compra e venda de ativos financeiros.')
    st.write('Eu me comprometo com você que aqui você verá as técnicas mais modernas possíveis e vou usar a máxima transparência com você em todas as operações que faremos.')
    st.write('Vou postar até notas de corretagem para provar a efetividade dessas técnicas :facepunch:.')
    st.write('By JBruts.')
    st.warning(':heart_eyes_cat: Navegue pelas páginas pelo menu dropdown à sua esquerda')
    st.sidebar.success('Previsão de preços com IA')
    st.sidebar.error('Ganho com estatística')
    st.sidebar.warning('Melhores indicadores gráficos')
    st.sidebar.info('Técnicas fundamentalista')

def mensagem_apresentacao():
    st.header('Um pouco sobre minha história até aqui :hugs:')
    st.subheader('Estou em processo de certfificação CNPI-p, então não posso recomendar investimentos, por isso terão várias mensagenns ressaltando essa situação!')
    st.write("""
            Meu nome é João Marcos. Sou economista, engenheiro de software e especialista em Engenharia de Inteligência Artificial, com especialização em Desenvolvimento de Sistemas com Python e em Finanças voltadas ao Mercado Financeiro e atualmente trabalho em uma distribuidora de energia elétrica como operador em tempo real. Ao longo da minha trajetória, também realizei diversos cursos na área de Ciência de Dados e participei de vários projetos envolvendo análise e modelagem de dados.

            Nos últimos anos, dediquei meu tempo ao desenvolvimento e à validação de modelos quantitativos utilizando Inteligência Artificial, Machine Learning e Análise de Dados para identificar oportunidades no mercado financeiro.

            Ao longo dessa jornada, descobri uma verdade que poucos comentam: o maior inimigo do investidor raramente é o mercado. Na maioria das vezes, são as próprias emoções — especialmente a ganância, a ansiedade e a falta de disciplina para seguir um método consistente.

            O mercado financeiro está em constante transformação. Estratégias que funcionam hoje podem perder eficiência amanhã. Por isso, adaptação, estudo contínuo e gestão de risco são tão importantes quanto encontrar boas oportunidades.

            O que você encontrará aqui

            Você não encontrará promessas de enriquecimento rápido, "fórmulas mágicas" ou o famoso "Santo Graal" dos investimentos.

            O que encontrará é um método baseado em:

            Inteligência Artificial e Machine Learning;
            Análise quantitativa e fundamentalista;
            Gestão de risco;
            Disciplina operacional;
            Transparência em todas as operações.

            Mais do que apresentar uma estratégia, quero mostrar como ela é aplicada na prática.

            Operarei utilizando meu próprio capital e compartilharei minhas análises, critérios de seleção, pontos de entrada e saída, além das notas de corretagem, sempre que possível. Assim, você poderá acompanhar como as decisões são tomadas e compreender a lógica por trás de cada operação.

            Meu objetivo é construir uma comunidade de investidores que tomam decisões fundamentadas em dados, estatística e tecnologia, reduzindo a influência das emoções e buscando maior consistência nos resultados ao longo do tempo.

            Seja muito bem-vindo(a)! Vamos explorar juntos como a Inteligência Artificial pode se tornar uma poderosa aliada na busca por decisões mais inteligentes no mercado financeiro.

            :rotating_light: :rotating_light: :rotating_light: Aviso Legal: Todo o conteúdo disponibilizado possui caráter exclusivamente educacional e informativo. As análises apresentadas não constituem recomendação de investimento, oferta de compra ou venda de ativos ou consultoria financeira. Toda decisão de investimento é de responsabilidade exclusiva do investidor.
                    
                    """)
    st.sidebar.image('WhatsApp Image 2026-07-26 at 02.41.47 (1).jpeg', 
             caption='João Marcos - Economista, Engenheiro de Software e Especialista em Inteligência Artificial :brazil:')

def mensagem_graficos():
    st.write("""
            Aqui teremos gráficos de preços e volume do ativo selecionado. A ideia é que você consiga identificar padrões de comportamento do preço e volume para que possamos criar estratégias de compra e venda.
            """)

def mensagem_estatistico1():
    st.write("""
            Nesse gráfico visualizaremos a variação percentual do preço em relação ao tempo. Observe o primeiro gráfico inferior desse plot e veja como o preço trabalhaou em um intervalo.
            
            Uma da estratégia que usaremos é comprar quando o preço estiver próximo a esse percentual, isto é, abaixo do preço mínimo identificado pela linha azul e vender próximo a linha vermelha de preço máximo.

                        """)
    
def mensagem_estatistico2():
    st.write("""
            Aqui teremos, teoricamente, os preços de compra e venda de acordo com alguns parâmetros.
            Alguns ativos se mostraram uma excelente estratégia, outros nem tanto, porém faremos alguns filtros antes de colocar nosso dinheiro nessa estratégia. Esses filtros serão vários sendo alguns o comportamento de volume e até avaliaremos indicadores fundamentalistas para fugir de ciladas aos quais poderão nos custar algumas cifras.
            """)   

def mensagem_tabela():
    st.write('Aqui temos as cotações nua e crua do ativo selecionado a qual você poderá conseguir em qualquer corretora, site da B3 ou até mesmo pelo Google.')

def mensagem_explorador_estatistico():
    st.write("""
            Vamos analisar todos os ativos da B3 em busca das melhores oportunidades sendo que cada ativo passará por filtros e apenas os que apresentarem maior potencial entrarão no radar de investimento.

            Essa é uma estratégia baseada em dados, diferente dos métodos tradicionais, com diversificação e gestão inteligente do capital.
            """)

def mensagem_legislacao():
    st.markdown("<h1 style='text-align: center;'>ALERTA MUITOIMPORTANTE</h1>", unsafe_allow_html=True)
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
            Aqui teremos uma ferramenta que nos ajudará a encontrar a melhor combinação de ativos para obter o maior retorno possível com o menor risco possível.
            A ideia é que você consiga identificar padrões de comportamento do preço e volume para que possamos criar estratégias de compra e venda.
            """)