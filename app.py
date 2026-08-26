import streamlit as st
import pandas as pd
import urllib.parse

# Configuração da página
st.set_page_config(
    page_title="CAE | Consultoria & Assessoria Econômica",
    page_icon="📈",
    layout="wide"
)

# Estilização Personalizada (Visual Executivo e Formal)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 700;
        color: #0A192F;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4A5568;
        margin-bottom: 25px;
    }
    .card-box {
        background-color: #F8FAFC;
        border-left: 5px solid #0A192F;
        padding: 18px;
        border-radius: 6px;
        margin-bottom: 15px;
    }
    .cta-button {
        background-color: #0A192F;
        color: #FFFFFF !important;
        padding: 14px 28px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Link do WhatsApp
numero_whatsapp = "5584999247550"
mensagem_padrao = "Olá! Gostaria de solicitar informações sobre o pacote de planilhas automáticas e serviços de consultoria econômica."
link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(mensagem_padrao)}"

# Cabeçalho Principal
st.markdown('<p class="main-header">CAE — Consultoria e Assessoria Econômica</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Soluções em Inteligência Financeira, Gestão Estratégica e Análise Mercadológica</p>', unsafe_allow_html=True)
st.divider()

# Navegação por Abas Executivas
aba1, aba2, aba3, aba4 = st.tabs([
    "🏛️ Consultoria & Projetos", 
    "📊 Gestão Financeira & DRE", 
    "🧮 Simulador de Precificação", 
    "📦 Modelos & Planilhas"
])

# ABA 1: CONSULTORIA E PROJETOS
with aba1:
    st.subheader("Soluções Estratégicas para Empresas e Projetos Públicos")
    st.write("A inteligência econômica permite identificar oportunidades de crescimento, mitigar riscos operacionais e otimizar a alocação de recursos.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card-box">
            <h4>Análise de Viabilidade Econômico-Financeira</h4>
            <p>Estudo detalhado de VPL (Valor Presente Líquido), TIR (Taxa Interna de Retorno) e Payback para validação de novos investimentos e projetos expansivos.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-box">
            <h4>Precificação Estratégica & Margem de Lucro</h4>
            <p>Desenvolvimento de modelos rigorosos de formação de preço considerando custos fixos, variáveis, impostos e elasticidade da demanda.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="card-box">
            <h4>Diagnóstico Organizacional e Orçamentário</h4>
            <p>Mapeamento de gargalos financeiros, análise de fluxo de caixa e reestruturação de custos para aumentar a margem operacional.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-box">
            <h4>Projetos e Assessoramento Municipal</h4>
            <p>Suporte em análise de indicadores socioeconômicos, elaboração de pareceres técnicos e planejamento financeiro governamental.</p>
        </div>
        """, unsafe_allow_html=True)

# ABA 2: GESTÃO FINANCEIRA
with aba2:
    st.subheader("Pilares da Gestão Contábil e Financeira")
    st.write("A aplicação contínua de métodos contábeis garante a sustentabilidade e a liquidez de qualquer empreendimento.")
    
    st.markdown("""
    * **Demonstração do Resultado do Exercício (DRE):** Acompanhamento sistemático de Receita Bruta, Deduções, Lucro Bruto, Despesas Operacionais e Lucro Líquido Real.
    * **Conciliação e Gestão do Fluxo de Caixa:** Separação rigorosa entre o regime de caixa e regime de competência para evitar iliquidez técnica.
    * **Indicadores de Desempenho (KPIs):** Monitoramento contínuo da Margem de Contribuição, Ponto de Equilíbrio (Break-Even Point) e Giro de Estoque.
    * **Governança e Separação de Caixas:** Diretrizes para definição do Pró-labore e blindagem do patrimônio pessoal em relação às finanças corporativas.
    """)

# ABA 3: TABELA DE PRECIFICAÇÃO E SIMULAÇÃO
with aba3:
    st.subheader("📊 Simulação Completa de Precificação e Margem de Lucro")
    st.write("Edite os dados dos seus produtos na tabela abaixo para simular o preço final recomendado e a projeção de lucro líquido total.")

    # Tabela com dados iniciais de exemplo que o usuário pode editar na tela
    dados_iniciais = pd.DataFrame([
        {"Produto": "Vestido Floral", "Custo (R$)": 45.0, "Taxas/Impostos (%)": 10.0, "Margem Alvo (%)": 40.0, "Vendas Estimadas (Qtd)": 20},
        {"Produto": "Conjunto Alfaiataria", "Custo (R$)": 80.0, "Taxas/Impostos (%)": 12.0, "Margem Alvo (%)": 45.0, "Vendas Estimadas (Qtd)": 15},
        {"Produto": "Blusa Basic", "Custo (R$)": 25.0, "Taxas/Impostos (%)": 8.0, "Margem Alvo (%)": 35.0, "Vendas Estimadas (Qtd)": 50}
    ])

    # Exibe a tabela editável
    tabela_editada = st.data_editor(dados_iniciais, num_rows="dynamic", use_container_width=True)

    # Processamento dos cálculos
    if not tabela_editada.empty:
        # Fórmulas de Precificação por Markup sobre a venda
        tabela_editada["Preço Sugerido (R$)"] = tabela_editada["Custo (R$)"] / (1 - ((tabela_editada["Taxas/Impostos (%)"] + tabela_editada["Margem Alvo (%)"]) / 100))
        tabela_editada["Lucro Unitário (R$)"] = tabela_editada["Preço Sugerido (R$)"] - tabela_editada["Custo (R$)"] - (tabela_editada["Preço Sugerido (R$)"] * (tabela_editada["Taxas/Impostos (%)"] / 100))
        tabela_editada["Lucro Total Estimado (R$)"] = tabela_editada["Lucro Unitário (R$)"] * tabela_editada["Vendas Estimadas (Qtd)"]

        # Arredondamento para visualização limpa
        tabela_editada["Preço Sugerido (R$)"] = tabela_editada["Preço Sugerido (R$)"].round(2)
        tabela_editada["Lucro Unitário (R$)"] = tabela_editada["Lucro Unitário (R$)"].round(2)
        tabela_editada["Lucro Total Estimado (R$)"] = tabela_editada["Lucro Total Estimado (R$)"].round(2)

        st.markdown("### 📈 Resultado do Diagnóstico de Precificação")
        
        # Resumo Financeiro em Destaque
        faturamento_total = (tabela_editada["Preço Sugerido (R$)"] * tabela_editada["Vendas Estimadas (Qtd)"]).sum()
        lucro_geral = tabela_editada["Lucro Total Estimado (R$)"].sum()

        m1, m2 = st.columns(2)
        m1.metric("Projeção de Faturamento Total", f"R$ {faturamento_total:,.2f}")
        m2.metric("Projeção de Lucro Líquido Total", f"R$ {lucro_geral:,.2f}")

        # Tabela Final Formatada
        st.dataframe(tabela_editada, use_container_width=True)

# ABA 4: MODELOS E PLANILHAS
with aba4:
    st.subheader("Ecossistema Completo de Gestão Financeira")
    st.write("Adquira soluções prontas desenvolvidas para automatizar a operação do seu negócio:")
    
    st.markdown("""
    * **Planilha de Controle Financeiro Integrado:** Fluxo de Caixa, DRE Automático e Dashboard Executivo.
    * **Gerador de Propostas Comerciais:** Automação de orçamentos e cálculo imediato de margem.
    * **Calculadora de Precificação Multiprofissional:** Matriz completa para comércio, serviços e produtos personalizados.
    """)

st.divider()

# Seção CTA Final (Atendimento via WhatsApp)
st.markdown("### 🏛️ Solicite Atendimento ou Adquira os Modelos Automáticos")
st.write("Entre em contato direto para soluções personalizadas de consultoria, assessoria ou envio imediato das ferramentas de gestão.")

st.markdown(f"""
<a href="{link_whatsapp}" target="_blank" class="cta-button">
    📲 Falar com Consultor no WhatsApp
</a>
""", unsafe_allow_html=True)
