import streamlit as st


def mensagen_inicial():
    st.header('Bem-vindo ao universo da Inteligência Artificial aplicada ao Mercado de Ações! 🚀')
    st.subheader("Se você já testou dezenas de estratégias, acompanhou recomendações de especialistas e percebeu que seus " \
             "resultados mal superam investimentos conservadores, como um CDB, este espaço foi criado para você.")
    st.write('Quero mostrara para você as várias técnicas sendo algumas antigas e outras das mais atuais possíveis envolvendo LLMs para operação de compra e venda de ativos financeiros.')
    st.write('Eu me comprometo com você que aqui você verá as técnicas mais modernas possíveis e vou usar a máxima transparência com você em todas as operações que faremos.')
    st.write('Vou postar até notas de corretagem para provar a efetividade dessas técnicas :facepunch:.')
    st.write('By JBruts.')
    st.warning(':heart_eyes_cat:     Navegue pelas páginas pelo menu dropdown à sua esquerda')
    st.sidebar.success('Previsão de preços com IA')
    st.sidebar.error('Ganho com estatística')
    st.sidebar.warning('Melhores indicadores gráficos')
    st.sidebar.info('Técnicas fundamentalista')

def mensagem_apresentacao():
    st.header('Um pouco sobre quem vos fala :nerd_face:')
    st.write("""
        Meu nome é João Marcos. Sou economista, engenheiro de software e especialista em Engenharia de Inteligência Artificial. Nos últimos anos, dediquei meu tempo ao desenvolvimento e à validação de modelos quantitativos utilizando Inteligência Artificial, Machine Learning e análise de dados para identificar oportunidades no mercado financeiro.

        Ao longo dessa jornada, descobri uma verdade que poucos comentam: o maior inimigo do investidor raramente é o mercado. Na maioria das vezes, são as próprias emoções — especialmente a ganância, a ansiedade e a falta de disciplina para seguir um método consistente.

        O mercado financeiro está em constante transformação. Estratégias que funcionavam ontem podem perder eficiência amanhã. Por isso, adaptação, estudo contínuo e gestão de risco são tão importantes quanto encontrar boas oportunidades.

        O que você encontrará aqui

        Você não encontrará promessas de enriquecimento rápido, "fórmulas mágicas" ou o famoso "Santo Graal" dos investimentos.

        O que encontrará é um método baseado em:

            -> Inteligência Artificial e Machine Learning;
            -> Análise quantitativa e fundamentalista;
            -> Gestão de risco;
            -> Disciplina operacional;
            -> Transparência em todas as operações.

        Mais do que ensinar uma estratégia, quero mostrar como ela é aplicada na prática.

        Operarei utilizando meu próprio capital e compartilharei minhas análises, critérios de seleção, pontos de entrada e saída, além das notas de corretagem sempre que possível. Assim, você poderá acompanhar como as decisões são tomadas e entender a lógica por trás de cada operação.

        Meu objetivo é construir uma comunidade de investidores que tomam decisões fundamentadas em dados, estatística e tecnologia, reduzindo a influência das emoções e aumentando a consistência dos resultados ao longo do tempo.

        Seja muito bem-vindo(a)! Vamos explorar juntos como a Inteligência Artificial pode se tornar uma poderosa aliada na busca por melhores decisões no mercado de ações.
        """)
    st.write('JBrutus')
    st.sidebar.success(':blush: :open_hands: Sobre mim')


def mensagem_graficos():
    st.write("""
            Aqui temos um gráfico simples e também você poderá selecionar outro tipo iterativo, de candles, que você pode selecionar ao lado esquerdo.
                
            Com ese grárico podemos ver como o preço do ativo selecionado se comportou durante o tempo, também selecionado, e tentaremos enxergar alguma oportunidade para ganhar com essa variação.
                
            Ainda estou em fases de teste para ver qual gráfico será melhor, talvez da próxima vez que você entrar aqui, eu possa ter implementado algumas mudanças.
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