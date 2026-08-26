import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal de Economia & Gestão", layout="wide")

# Título Principal do Site
st.title("💡 Portal de Economia & Gestão para Empreendedores")
st.caption("Aprenda conceitos práticos de negócios e aplique ferramentas de gestão no seu dia a dia.")

# Organização do Portal em Abas Educativas
aba1, aba2, aba3 = st.tabs(["📊 Economia Aplicada", "📑 Contabilidade Prática", "⏱️ Rotina do Negócio"])

with aba1:
    st.header("Economia para Micro e Pequenos Negócios")
    st.write("""
    * **Margem de Contribuição:** O valor que sobra da venda de um produto após descontar os custos e despesas variáveis. É o que vai pagar os custos fixos da sua empresa.
    * **Ponto de Equilíbrio (Break-Even):** O volume exato de vendas necessário para que sua empresa não tenha nem lucro nem prejuízo.
    * **Impacto da Inflação no Estoque:** Como ajustar sua tabela de preços à medida que a matéria-prima e os insumos sobem.
    """)

with aba2:
    st.header("Finanças e Contabilidade Simplificada")
    st.write("""
    * **Fluxo de Caixa vs. Lucro:** Entenda por que uma empresa pode ser lucrativa no papel, mas ficar sem dinheiro no caixa para pagar contas no dia a dia.
    * **DRE Simplificado:** Como organizar Receitas, Custos Variáveis, Margem Bruta, Despesas Fixas e Resultado Líquido em uma estrutura lógica.
    * **Separação de Caixas:** A importância de definir um pró-labore e nunca misturar as finanças pessoais com as da empresa.
    """)

with aba3:
    st.header("Rotina e Protocolos de Gestão Operacional")
    st.write("""
    * **Fechamento Diário:** Protocolo de verificação do caixa físico e conciliação das taxas de maquininhas de cartão.
    * **Controle de Estoque Giro/Curva ABC:** Identificação dos produtos de alta rotação que não podem faltar nas vendas.
    * **Revisão Semanal de Metas:** Como analisar indicadores de desempenho (KPIs) rápidos para tomar decisões informadas.
    """)

st.divider()

# Ferramenta Interativa de Demonstração (Calculadora de Precificação)
st.subheader("🛠️ Ferramenta Prática: Calculadora de Precificação")
st.write("Insira os dados do seu produto abaixo para calcular a margem real de lucro.")

col1, col2 = st.columns(2)

with col1:
    custo_direto = st.number_input("Custo da Matéria-Prima / Aquisição (R$):", min_value=0.0, value=25.0)
    taxa_cartao = st.number_input("Taxas de Cartão / Venda (%):", min_value=0.0, value=5.0)

with col2:
    margem_desejada = st.slider("Margem de Lucro Desejada (%):", min_value=5, max_value=150, value=40)

if st.button("Calcular Preço Sugerido"):
    # Lógica simples de precificação sobre o custo
    preco_base = custo_direto * (1 + (margem_desejada / 100))
    preco_final = preco_base / (1 - (taxa_cartao / 100))
    lucro_liquido = preco_final - custo_direto - (preco_final * (taxa_cartao / 100))
    
    st.success(f"**Preço de Venda Recomendado:** R$ {preco_final:.2f}")
    st.info(f"**Lucro Líquido Estimado:** R$ {lucro_liquido:.2f} por unidade")

st.divider()

# Chamada de Ação (CTA) para Venda das Planilhas/Modelos Completos
st.subheader("📦 Leve a Gestão Completa para o seu Negócio")
st.write("Quer automatizar todo o seu controle de caixa, emissão de propostas e precificação em planilhas prontas?")

st.markdown("""
<a href="https://kiwify.com.br" target="_blank">
    <button style="background-color:#0284c7; color:white; border:none; padding:12px 24px; border-radius:6px; font-size:16px; cursor:pointer;">
        🛒 Adquirir Modelo Completo de Planilhas
    </button>
</a>
""", unsafe_allow_html=True)
