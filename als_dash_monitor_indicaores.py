import streamlit as st
import datetime
from monitor_indicadores_dolfut import (
    get_ewz_xpath, get_vxbr_xpath, get_petax_xpath,
    get_eua2_xpath, get_eua5_xpath, get_eua10_xpath, get_eua30_xpath
)

# Configuração visual
st.set_page_config(page_title="Monitor de Indicadores • ALS CENTURY", layout="centered")

# LOGO e TÍTULO CENTRALIZADO
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image("Logo-mei.jpg", width=180)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#ffffff;'>Monitor de Indicadores Financeiros</h1>", unsafe_allow_html=True)
st.caption("Fonte: br.investing.com")

t_atual = datetime.datetime.now().strftime('%H:%M:%S')

if st.button('🔄 Atualizar agora'):
    st.rerun()

# Função de formatação com cor e setas
def format_percent(val):
    if not val or val.strip() in ['-', '(', ')', '()']:
        return '-'
    try:
        vlimpo = val.replace('(', '').replace(')', '').replace('%', '').replace(',', '.').strip()
        v = float(vlimpo)
        val_formatado = val
        if not val.strip().startswith('(') and not val.strip().endswith(')'):
            val_formatado = f'({val.strip()})'
        if v < 0:
            return f'<span style="color:red;font-weight:bold;">&#8595; {val_formatado}</span>'
        else:
            return f'<span style="color:lightgreen;font-weight:bold;">&#8593; {val_formatado}</span>'
    except:
        return '-'

# Buscar dados
ewz_valor, ewz_perc = get_ewz_xpath()
vxbr_valor, vxbr_perc = get_vxbr_xpath()
petax_valor, petax_perc = get_petax_xpath()
eua2_valor, eua2_perc = get_eua2_xpath()
eua5_valor, eua5_perc = get_eua5_xpath()
eua10_valor, eua10_perc = get_eua10_xpath()
eua30_valor, eua30_perc = get_eua30_xpath()

# Indicadores principais
st.markdown("---")
st.subheader("🇧🇷 Indicadores Brasil")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('EWZ', ewz_valor or '-')
    st.markdown(f"Variação: {format_percent(ewz_perc)}", unsafe_allow_html=True)
with col2:
    st.metric('VXBR', vxbr_valor or '-')
    st.markdown(f"Variação: {format_percent(vxbr_perc)}", unsafe_allow_html=True)
with col3:
    st.metric('PETAX', petax_valor or '-')
    st.markdown(f"Variação: {format_percent(petax_perc)}", unsafe_allow_html=True)

# Títulos dos EUA
st.markdown("---")
st.subheader("🇺🇸 Títulos do Tesouro Americano")
col4, col5, col6, col7 = st.columns(4)
with col4:
    st.metric('2 anos', eua2_valor or '-')
    st.markdown(f"Variação: {format_percent(eua2_perc)}", unsafe_allow_html=True)
with col5:
    st.metric('5 anos', eua5_valor or '-')
    st.markdown(f"Variação: {format_percent(eua5_perc)}", unsafe_allow_html=True)
with col6:
    st.metric('10 anos', eua10_valor or '-')
    st.markdown(f"Variação: {format_percent(eua10_perc)}", unsafe_allow_html=True)
with col7:
    st.metric('30 anos', eua30_valor or '-')
    st.markdown(f"Variação: {format_percent(eua30_perc)}", unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.caption(f"🕓 Última atualização: {t_atual}")