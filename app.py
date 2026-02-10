import streamlit as st

st.set_page_config(
    page_title="Minerador de estrategia",
    page_icon="M",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stSidebar"] {display: none;}

    .center-note {
      text-align: center;
      opacity: 0.78;
      margin: 0.25rem 0 0.9rem 0;
    }

    /* Moldura (st.container(border=True)) */
    [data-testid="stVerticalBlockBorderWrapper"]{
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.10);
      border-radius: 16px;
      padding: 1.0rem 1.0rem 0.6rem 1.0rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.28);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "etapa" not in st.session_state:
    st.session_state.etapa = 1

if "nome_robo" not in st.session_state:
    st.session_state.nome_robo = ""

if "nome_input" not in st.session_state:
    st.session_state.nome_input = ""

if "operar_compra" not in st.session_state:
    st.session_state.operar_compra = "Sim"

if "operar_venda" not in st.session_state:
    st.session_state.operar_venda = "Sim"

if "mercado" not in st.session_state:
    st.session_state.mercado = "B3"

if "tipo_operacional" not in st.session_state:
    st.session_state.tipo_operacional = "Swing Trade"

if "modo_processamento" not in st.session_state:
    st.session_state.modo_processamento = "A cada tick"

if "final_operar_compra" not in st.session_state:
    st.session_state.final_operar_compra = "Nao usar"

if "final_operar_venda" not in st.session_state:
    st.session_state.final_operar_venda = "Nao usar"

if "final_modo_processamento" not in st.session_state:
    st.session_state.final_modo_processamento = "Nao usar"

if "config_inicial_salva" not in st.session_state:
    st.session_state.config_inicial_salva = False

if "tempo_grafico_principal" not in st.session_state:
    st.session_state.tempo_grafico_principal = "Corrente"

if "tempo_grafico_finalizar" not in st.session_state:
    st.session_state.tempo_grafico_finalizar = "Nao usar"

if "volume_inicial" not in st.session_state:
    st.session_state.volume_inicial = 1

if "spread_maximo" not in st.session_state:
    st.session_state.spread_maximo = 0

if "volume_passe" not in st.session_state:
    st.session_state.volume_passe = 0

if "volume_finalizar" not in st.session_state:
    st.session_state.volume_finalizar = 0

if "spread_passe" not in st.session_state:
    st.session_state.spread_passe = 0

if "spread_finalizar" not in st.session_state:
    st.session_state.spread_finalizar = 0

if "parametros_execucao_salvos" not in st.session_state:
    st.session_state.parametros_execucao_salvos = False

if "tipo_calculo_distancias" not in st.session_state:
    st.session_state.tipo_calculo_distancias = "Em pontos"

if "final_tipo_calculo_distancias" not in st.session_state:
    st.session_state.final_tipo_calculo_distancias = "Nao usar"

if "ordem_entrada" not in st.session_state:
    st.session_state.ordem_entrada = "A mercado"

if "final_ordem_entrada" not in st.session_state:
    st.session_state.final_ordem_entrada = "Nao usar"

if "ordem_saida" not in st.session_state:
    st.session_state.ordem_saida = "A mercado"

if "final_ordem_saida" not in st.session_state:
    st.session_state.final_ordem_saida = "Nao usar"

if "tipo_ordens_salvas" not in st.session_state:
    st.session_state.tipo_ordens_salvas = False

if "tipo_calculo_alvos" not in st.session_state:
    st.session_state.tipo_calculo_alvos = "Em pontos"

if "final_tipo_calculo_alvos" not in st.session_state:
    st.session_state.final_tipo_calculo_alvos = "Nao usar"

if "usar_stoploss_personalizado" not in st.session_state:
    st.session_state.usar_stoploss_personalizado = "Nao"

if "final_usar_stoploss_personalizado" not in st.session_state:
    st.session_state.final_usar_stoploss_personalizado = "Nao usar"

if "usar_takeprofit_personalizado" not in st.session_state:
    st.session_state.usar_takeprofit_personalizado = "Nao"

if "final_usar_takeprofit_personalizado" not in st.session_state:
    st.session_state.final_usar_takeprofit_personalizado = "Nao usar"

if "alvos_personalizados_salvos" not in st.session_state:
    st.session_state.alvos_personalizados_salvos = False

if "tipo_calculo_stoploss" not in st.session_state:
    st.session_state.tipo_calculo_stoploss = "Em pontos"

if "final_tipo_calculo_stoploss" not in st.session_state:
    st.session_state.final_tipo_calculo_stoploss = "Nao usar"

if "stoploss_inicial" not in st.session_state:
    st.session_state.stoploss_inicial = 0

if "stoploss_passe" not in st.session_state:
    st.session_state.stoploss_passe = 0

if "final_stoploss_inicial" not in st.session_state:
    st.session_state.final_stoploss_inicial = 0

if "inicio_break_even_sl" not in st.session_state:
    st.session_state.inicio_break_even_sl = 0

if "inicio_break_even_sl_passe" not in st.session_state:
    st.session_state.inicio_break_even_sl_passe = 0

if "final_inicio_break_even_sl" not in st.session_state:
    st.session_state.final_inicio_break_even_sl = 0

if "distancia_break_even_sl" not in st.session_state:
    st.session_state.distancia_break_even_sl = 0

if "distancia_break_even_sl_passe" not in st.session_state:
    st.session_state.distancia_break_even_sl_passe = 0

if "final_distancia_break_even_sl" not in st.session_state:
    st.session_state.final_distancia_break_even_sl = 0

if "inicio_trailing_stop" not in st.session_state:
    st.session_state.inicio_trailing_stop = 0

if "inicio_trailing_stop_passe" not in st.session_state:
    st.session_state.inicio_trailing_stop_passe = 0

if "final_inicio_trailing_stop" not in st.session_state:
    st.session_state.final_inicio_trailing_stop = 0

if "passo_trailing_stop" not in st.session_state:
    st.session_state.passo_trailing_stop = 0

if "passo_trailing_stop_passe" not in st.session_state:
    st.session_state.passo_trailing_stop_passe = 0

if "final_passo_trailing_stop" not in st.session_state:
    st.session_state.final_passo_trailing_stop = 0

if "stoploss_salvo" not in st.session_state:
    st.session_state.stoploss_salvo = False

if "tipo_calculo_takeprofit" not in st.session_state:
    st.session_state.tipo_calculo_takeprofit = "Em pontos"

if "final_tipo_calculo_takeprofit" not in st.session_state:
    st.session_state.final_tipo_calculo_takeprofit = "Nao usar"

if "takeprofit_inicial" not in st.session_state:
    st.session_state.takeprofit_inicial = 0

if "takeprofit_passe" not in st.session_state:
    st.session_state.takeprofit_passe = 0

if "final_takeprofit_inicial" not in st.session_state:
    st.session_state.final_takeprofit_inicial = 0

if "inicio_break_even_tp" not in st.session_state:
    st.session_state.inicio_break_even_tp = 0

if "inicio_break_even_tp_passe" not in st.session_state:
    st.session_state.inicio_break_even_tp_passe = 0

if "final_inicio_break_even_tp" not in st.session_state:
    st.session_state.final_inicio_break_even_tp = 0

if "distancia_break_even_tp" not in st.session_state:
    st.session_state.distancia_break_even_tp = 0

if "distancia_break_even_tp_passe" not in st.session_state:
    st.session_state.distancia_break_even_tp_passe = 0

if "final_distancia_break_even_tp" not in st.session_state:
    st.session_state.final_distancia_break_even_tp = 0

if "inicio_trailing_profit" not in st.session_state:
    st.session_state.inicio_trailing_profit = 0

if "inicio_trailing_profit_passe" not in st.session_state:
    st.session_state.inicio_trailing_profit_passe = 0

if "final_inicio_trailing_profit" not in st.session_state:
    st.session_state.final_inicio_trailing_profit = 0

if "passo_trailing_profit" not in st.session_state:
    st.session_state.passo_trailing_profit = 0

if "passo_trailing_profit_passe" not in st.session_state:
    st.session_state.passo_trailing_profit_passe = 0

if "final_passo_trailing_profit" not in st.session_state:
    st.session_state.final_passo_trailing_profit = 0

if "takeprofit_salvo" not in st.session_state:
    st.session_state.takeprofit_salvo = False

if "referencia_tempo_saida" not in st.session_state:
    st.session_state.referencia_tempo_saida = "Segundos"

if "final_referencia_tempo_saida" not in st.session_state:
    st.session_state.final_referencia_tempo_saida = "Nao usar"

if "tempo_saida_operacoes_positivas" not in st.session_state:
    st.session_state.tempo_saida_operacoes_positivas = 0

if "tempo_saida_operacoes_positivas_passe" not in st.session_state:
    st.session_state.tempo_saida_operacoes_positivas_passe = 0

if "final_tempo_saida_operacoes_positivas" not in st.session_state:
    st.session_state.final_tempo_saida_operacoes_positivas = 0

if "saldo_maximo_operacoes_positivas" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_positivas = 0

if "saldo_maximo_operacoes_positivas_passe" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_positivas_passe = 0

if "final_saldo_maximo_operacoes_positivas" not in st.session_state:
    st.session_state.final_saldo_maximo_operacoes_positivas = 0

if "saldo_minimo_operacoes_positivas" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_positivas = 0

if "saldo_minimo_operacoes_positivas_passe" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_positivas_passe = 0

if "final_saldo_minimo_operacoes_positivas" not in st.session_state:
    st.session_state.final_saldo_minimo_operacoes_positivas = 0

if "tempo_saida_operacoes_negativas" not in st.session_state:
    st.session_state.tempo_saida_operacoes_negativas = 0

if "tempo_saida_operacoes_negativas_passe" not in st.session_state:
    st.session_state.tempo_saida_operacoes_negativas_passe = 0

if "final_tempo_saida_operacoes_negativas" not in st.session_state:
    st.session_state.final_tempo_saida_operacoes_negativas = 0

if "saldo_maximo_operacoes_negativas" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_negativas = 0

if "saldo_maximo_operacoes_negativas_passe" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_negativas_passe = 0

if "final_saldo_maximo_operacoes_negativas" not in st.session_state:
    st.session_state.final_saldo_maximo_operacoes_negativas = 0

if "saldo_minimo_operacoes_negativas" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_negativas = 0

if "saldo_minimo_operacoes_negativas_passe" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_negativas_passe = 0

if "final_saldo_minimo_operacoes_negativas" not in st.session_state:
    st.session_state.final_saldo_minimo_operacoes_negativas = 0

if "saida_temporal_salva" not in st.session_state:
    st.session_state.saida_temporal_salva = False

if "tipo_calculo_gradiente_linear" not in st.session_state:
    st.session_state.tipo_calculo_gradiente_linear = "Em pontos"

if "final_tipo_calculo_gradiente_linear" not in st.session_state:
    st.session_state.final_tipo_calculo_gradiente_linear = "Nao usar"

if "quantidade_niveis_gradiente_linear" not in st.session_state:
    st.session_state.quantidade_niveis_gradiente_linear = 0

if "quantidade_niveis_gradiente_linear_passe" not in st.session_state:
    st.session_state.quantidade_niveis_gradiente_linear_passe = 0

if "final_quantidade_niveis_gradiente_linear" not in st.session_state:
    st.session_state.final_quantidade_niveis_gradiente_linear = 0

if "distancia_niveis_gradiente_linear" not in st.session_state:
    st.session_state.distancia_niveis_gradiente_linear = 0

if "distancia_niveis_gradiente_linear_passe" not in st.session_state:
    st.session_state.distancia_niveis_gradiente_linear_passe = 0

if "final_distancia_niveis_gradiente_linear" not in st.session_state:
    st.session_state.final_distancia_niveis_gradiente_linear = 0

if "volume_ordens_gradiente_linear" not in st.session_state:
    st.session_state.volume_ordens_gradiente_linear = 0

if "volume_ordens_gradiente_linear_passe" not in st.session_state:
    st.session_state.volume_ordens_gradiente_linear_passe = 0

if "final_volume_ordens_gradiente_linear" not in st.session_state:
    st.session_state.final_volume_ordens_gradiente_linear = 0

if "alvo_parcial_gradiente_linear" not in st.session_state:
    st.session_state.alvo_parcial_gradiente_linear = 0

if "alvo_parcial_gradiente_linear_passe" not in st.session_state:
    st.session_state.alvo_parcial_gradiente_linear_passe = 0

if "final_alvo_parcial_gradiente_linear" not in st.session_state:
    st.session_state.final_alvo_parcial_gradiente_linear = 0

if "limite_entradas_gradiente_linear" not in st.session_state:
    st.session_state.limite_entradas_gradiente_linear = 0

if "limite_entradas_gradiente_linear_passe" not in st.session_state:
    st.session_state.limite_entradas_gradiente_linear_passe = 0

if "final_limite_entradas_gradiente_linear" not in st.session_state:
    st.session_state.final_limite_entradas_gradiente_linear = 0

if "reposicionar_ordem_gradiente_linear" not in st.session_state:
    st.session_state.reposicionar_ordem_gradiente_linear = 0

if "reposicionar_ordem_gradiente_linear_passe" not in st.session_state:
    st.session_state.reposicionar_ordem_gradiente_linear_passe = 0

if "final_reposicionar_ordem_gradiente_linear" not in st.session_state:
    st.session_state.final_reposicionar_ordem_gradiente_linear = 0

if "gradiente_linear_salvo" not in st.session_state:
    st.session_state.gradiente_linear_salvo = False

if "tempo_grafico_vela_filtro" not in st.session_state:
    st.session_state.tempo_grafico_vela_filtro = "Corrente"

if "final_tempo_grafico_vela_filtro" not in st.session_state:
    st.session_state.final_tempo_grafico_vela_filtro = "Nao usar"

if "tamanho_minimo_vela_filtro" not in st.session_state:
    st.session_state.tamanho_minimo_vela_filtro = 0

if "tamanho_minimo_vela_filtro_passe" not in st.session_state:
    st.session_state.tamanho_minimo_vela_filtro_passe = 0

if "final_tamanho_minimo_vela_filtro" not in st.session_state:
    st.session_state.final_tamanho_minimo_vela_filtro = 0

if "tamanho_maximo_vela_filtro" not in st.session_state:
    st.session_state.tamanho_maximo_vela_filtro = 0

if "tamanho_maximo_vela_filtro_passe" not in st.session_state:
    st.session_state.tamanho_maximo_vela_filtro_passe = 0

if "final_tamanho_maximo_vela_filtro" not in st.session_state:
    st.session_state.final_tamanho_maximo_vela_filtro = 0

if "minimo_corpo_vela_filtro" not in st.session_state:
    st.session_state.minimo_corpo_vela_filtro = 0

if "minimo_corpo_vela_filtro_passe" not in st.session_state:
    st.session_state.minimo_corpo_vela_filtro_passe = 0

if "final_minimo_corpo_vela_filtro" not in st.session_state:
    st.session_state.final_minimo_corpo_vela_filtro = 0

if "maximo_corpo_vela_filtro" not in st.session_state:
    st.session_state.maximo_corpo_vela_filtro = 0

if "maximo_corpo_vela_filtro_passe" not in st.session_state:
    st.session_state.maximo_corpo_vela_filtro_passe = 0

if "final_maximo_corpo_vela_filtro" not in st.session_state:
    st.session_state.final_maximo_corpo_vela_filtro = 0

if "vela_filtro_salvo" not in st.session_state:
    st.session_state.vela_filtro_salvo = False

if "canal_bandas_indicador" not in st.session_state:
    st.session_state.canal_bandas_indicador = "Nao usar"

if "canal_bandas_entrada" not in st.session_state:
    st.session_state.canal_bandas_entrada = "Nao usar"

if "canal_bandas_sentido" not in st.session_state:
    st.session_state.canal_bandas_sentido = "Tendencia"

if "canal_bandas_saida" not in st.session_state:
    st.session_state.canal_bandas_saida = "Nao usar"

if "cruzamento_sinal_rapido" not in st.session_state:
    st.session_state.cruzamento_sinal_rapido = "Nao usar"

if "cruzamento_sinal_lento" not in st.session_state:
    st.session_state.cruzamento_sinal_lento = "Nao usar"

if "cruzamento_entrada" not in st.session_state:
    st.session_state.cruzamento_entrada = "Nao usar"

if "cruzamento_sentido" not in st.session_state:
    st.session_state.cruzamento_sentido = "Tendencia"

if "cruzamento_saida" not in st.session_state:
    st.session_state.cruzamento_saida = "Nao usar"

if "sobrecompra_venda_indicador" not in st.session_state:
    st.session_state.sobrecompra_venda_indicador = "Nao usar"

if "sobrecompra_venda_entrada" not in st.session_state:
    st.session_state.sobrecompra_venda_entrada = "Nao usar"

if "sobrecompra_nivel" not in st.session_state:
    st.session_state.sobrecompra_nivel = 2

if "sobrecompra_nivel_passe" not in st.session_state:
    st.session_state.sobrecompra_nivel_passe = 2

if "final_sobrecompra_nivel" not in st.session_state:
    st.session_state.final_sobrecompra_nivel = 2

if "sobrevenda_nivel" not in st.session_state:
    st.session_state.sobrevenda_nivel = 2

if "sobrevenda_nivel_passe" not in st.session_state:
    st.session_state.sobrevenda_nivel_passe = 2

if "final_sobrevenda_nivel" not in st.session_state:
    st.session_state.final_sobrevenda_nivel = 2

if "sobrecompra_venda_sentido" not in st.session_state:
    st.session_state.sobrecompra_venda_sentido = "Tendencia"

if "sobrecompra_venda_saida" not in st.session_state:
    st.session_state.sobrecompra_venda_saida = "Nao usar"

if "sinais_prontos_salvo" not in st.session_state:
    st.session_state.sinais_prontos_salvo = False

if "indicador_escolha_1" not in st.session_state:
    st.session_state.indicador_escolha_1 = "Não usar"

if "indicador_escolha_2" not in st.session_state:
    st.session_state.indicador_escolha_2 = "Não usar"

if "indicador_escolha_3" not in st.session_state:
    st.session_state.indicador_escolha_3 = "Não usar"

if "indicador_escolha_4" not in st.session_state:
    st.session_state.indicador_escolha_4 = "Não usar"

_migracao_indicadores = {
    "Nao usar": "Não usar",
    "**Regressao": "**Regressão",
    "**Afastamento da media": "**Afastamento da média",
    "**Desvio Medio": "**Desvio Médio",
    "Media Movel": "Média Móvel",
    "Estocastico": "Estocástico",
    "Desvio Padrao": "Desvio Padrão",
    "Acumulacao/Distribuicao (A/D)": "Acumulação/Distribuição (A/D)",
}
for _k in ("indicador_escolha_1", "indicador_escolha_2", "indicador_escolha_3", "indicador_escolha_4"):
    _v = st.session_state.get(_k)
    if _v in _migracao_indicadores:
        st.session_state[_k] = _migracao_indicadores[_v]

if "escolher_indicadores_salvo" not in st.session_state:
    st.session_state.escolher_indicadores_salvo = False

if "sec_modo_edicao" not in st.session_state:
    st.session_state.sec_modo_edicao = "Avançado"

if "sec_tipo_vela" not in st.session_state:
    st.session_state.sec_tipo_vela = "Completas"

if "sec_estrategia" not in st.session_state:
    st.session_state.sec_estrategia = "Entrada compra (1)"

for _i in range(1, 6):
    _op_padrao = "SE" if _i == 1 else "E"
    if f"sec_regra_{_i}_operador_logico" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_operador_logico"] = _op_padrao

    if f"sec_regra_{_i}_ref_esquerda" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_ref_esquerda"] = "Não usar"

    if f"sec_regra_{_i}_vela_esquerda" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_vela_esquerda"] = "Vela atual"

    if f"sec_regra_{_i}_operador_comp" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_operador_comp"] = "Igual que"

    if f"sec_regra_{_i}_ref_direita" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_ref_direita"] = "Não usar"

    if f"sec_regra_{_i}_vela_direita" not in st.session_state:
        st.session_state[f"sec_regra_{_i}_vela_direita"] = "Vela atual"

if "sinais_entrada_compra_salvo" not in st.session_state:
    st.session_state.sinais_entrada_compra_salvo = False

if "sev_modo_edicao" not in st.session_state:
    st.session_state.sev_modo_edicao = "Avançado"

if "sev_tipo_vela" not in st.session_state:
    st.session_state.sev_tipo_vela = "Completas"

if "sev_estrategia" not in st.session_state:
    st.session_state.sev_estrategia = "Entrada venda (1)"

for _i in range(1, 6):
    _op_padrao = "SE" if _i == 1 else "E"
    if f"sev_regra_{_i}_operador_logico" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_operador_logico"] = _op_padrao

    if f"sev_regra_{_i}_ref_esquerda" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_ref_esquerda"] = "Não usar"

    if f"sev_regra_{_i}_vela_esquerda" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_vela_esquerda"] = "Vela atual"

    if f"sev_regra_{_i}_operador_comp" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_operador_comp"] = "Igual que"

    if f"sev_regra_{_i}_ref_direita" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_ref_direita"] = "Não usar"

    if f"sev_regra_{_i}_vela_direita" not in st.session_state:
        st.session_state[f"sev_regra_{_i}_vela_direita"] = "Vela atual"

if "sinais_entrada_venda_salvo" not in st.session_state:
    st.session_state.sinais_entrada_venda_salvo = False

if "limites_robo_historico" not in st.session_state:
    st.session_state.limites_robo_historico = "Desabilitado"

if "final_limites_robo_historico" not in st.session_state:
    st.session_state.final_limites_robo_historico = "Nao usar"

if "limites_robo_calculo" not in st.session_state:
    st.session_state.limites_robo_calculo = "Financeiro"

if "final_limites_robo_calculo" not in st.session_state:
    st.session_state.final_limites_robo_calculo = "Nao usar"

if "limites_robo_vencedoras" not in st.session_state:
    st.session_state.limites_robo_vencedoras = 0

if "limites_robo_vencedoras_passe" not in st.session_state:
    st.session_state.limites_robo_vencedoras_passe = 0

if "final_limites_robo_vencedoras" not in st.session_state:
    st.session_state.final_limites_robo_vencedoras = 0

if "limites_robo_perdedoras" not in st.session_state:
    st.session_state.limites_robo_perdedoras = 0

if "limites_robo_perdedoras_passe" not in st.session_state:
    st.session_state.limites_robo_perdedoras_passe = 0

if "final_limites_robo_perdedoras" not in st.session_state:
    st.session_state.final_limites_robo_perdedoras = 0

if "limites_robo_limite_total" not in st.session_state:
    st.session_state.limites_robo_limite_total = 0

if "limites_robo_limite_total_passe" not in st.session_state:
    st.session_state.limites_robo_limite_total_passe = 0

if "final_limites_robo_limite_total" not in st.session_state:
    st.session_state.final_limites_robo_limite_total = 0

if "limites_robo_meta_ganho" not in st.session_state:
    st.session_state.limites_robo_meta_ganho = 0

if "limites_robo_meta_ganho_passe" not in st.session_state:
    st.session_state.limites_robo_meta_ganho_passe = 0

if "final_limites_robo_meta_ganho" not in st.session_state:
    st.session_state.final_limites_robo_meta_ganho = 0

if "limites_robo_encerrar_meta_ganho" not in st.session_state:
    st.session_state.limites_robo_encerrar_meta_ganho = "Sim"

if "final_limites_robo_encerrar_meta_ganho" not in st.session_state:
    st.session_state.final_limites_robo_encerrar_meta_ganho = "Nao usar"

if "limites_robo_limite_perda" not in st.session_state:
    st.session_state.limites_robo_limite_perda = 0

if "limites_robo_limite_perda_passe" not in st.session_state:
    st.session_state.limites_robo_limite_perda_passe = 0

if "final_limites_robo_limite_perda" not in st.session_state:
    st.session_state.final_limites_robo_limite_perda = 0

if "limites_robo_encerrar_limite_perda" not in st.session_state:
    st.session_state.limites_robo_encerrar_limite_perda = "Sim"

if "final_limites_robo_encerrar_limite_perda" not in st.session_state:
    st.session_state.final_limites_robo_encerrar_limite_perda = "Nao usar"

if "limites_robo_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_rebaixamento = 0

if "limites_robo_rebaixamento_passe" not in st.session_state:
    st.session_state.limites_robo_rebaixamento_passe = 0

if "final_limites_robo_rebaixamento" not in st.session_state:
    st.session_state.final_limites_robo_rebaixamento = 0

if "limites_robo_encerrar_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_encerrar_rebaixamento = "Não"

if "final_limites_robo_encerrar_rebaixamento" not in st.session_state:
    st.session_state.final_limites_robo_encerrar_rebaixamento = "Nao usar"

if "limites_robo_gatilho_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_gatilho_rebaixamento = 0

if "limites_robo_gatilho_rebaixamento_passe" not in st.session_state:
    st.session_state.limites_robo_gatilho_rebaixamento_passe = 0

if "final_limites_robo_gatilho_rebaixamento" not in st.session_state:
    st.session_state.final_limites_robo_gatilho_rebaixamento = 0

if "limites_robo_recuperacao" not in st.session_state:
    st.session_state.limites_robo_recuperacao = 0

if "limites_robo_recuperacao_passe" not in st.session_state:
    st.session_state.limites_robo_recuperacao_passe = 0

if "final_limites_robo_recuperacao" not in st.session_state:
    st.session_state.final_limites_robo_recuperacao = 0

if "limites_robo_encerrar_recuperacao" not in st.session_state:
    st.session_state.limites_robo_encerrar_recuperacao = "Não"

if "final_limites_robo_encerrar_recuperacao" not in st.session_state:
    st.session_state.final_limites_robo_encerrar_recuperacao = "Nao usar"

if "limites_robo_gatilho_recuperacao" not in st.session_state:
    st.session_state.limites_robo_gatilho_recuperacao = 0

if "limites_robo_gatilho_recuperacao_passe" not in st.session_state:
    st.session_state.limites_robo_gatilho_recuperacao_passe = 0

if "final_limites_robo_gatilho_recuperacao" not in st.session_state:
    st.session_state.final_limites_robo_gatilho_recuperacao = 0

if "limites_robo_salvo" not in st.session_state:
    st.session_state.limites_robo_salvo = False

if "conta_historico" not in st.session_state:
    st.session_state.conta_historico = "Desabilitado"

if "final_conta_historico" not in st.session_state:
    st.session_state.final_conta_historico = "Nao usar"

if "conta_calculo" not in st.session_state:
    st.session_state.conta_calculo = "Financeiro"

if "final_conta_calculo" not in st.session_state:
    st.session_state.final_conta_calculo = "Nao usar"

if "conta_filtro_ativo" not in st.session_state:
    st.session_state.conta_filtro_ativo = "Não"

if "final_conta_filtro_ativo" not in st.session_state:
    st.session_state.final_conta_filtro_ativo = "Nao usar"

if "conta_excluir_manuais" not in st.session_state:
    st.session_state.conta_excluir_manuais = "Não"

if "final_conta_excluir_manuais" not in st.session_state:
    st.session_state.final_conta_excluir_manuais = "Nao usar"

if "conta_filtrar_robos" not in st.session_state:
    st.session_state.conta_filtrar_robos = "Não"

if "final_conta_filtrar_robos" not in st.session_state:
    st.session_state.final_conta_filtrar_robos = "Nao usar"

if "conta_id_minimo" not in st.session_state:
    st.session_state.conta_id_minimo = 0

if "conta_id_minimo_passe" not in st.session_state:
    st.session_state.conta_id_minimo_passe = 0

if "final_conta_id_minimo" not in st.session_state:
    st.session_state.final_conta_id_minimo = 0

if "conta_id_maximo" not in st.session_state:
    st.session_state.conta_id_maximo = 0

if "conta_id_maximo_passe" not in st.session_state:
    st.session_state.conta_id_maximo_passe = 0

if "final_conta_id_maximo" not in st.session_state:
    st.session_state.final_conta_id_maximo = 0

if "conta_meta_ganho" not in st.session_state:
    st.session_state.conta_meta_ganho = 0

if "conta_meta_ganho_passe" not in st.session_state:
    st.session_state.conta_meta_ganho_passe = 0

if "final_conta_meta_ganho" not in st.session_state:
    st.session_state.final_conta_meta_ganho = 0

if "conta_encerrar_meta_ganho" not in st.session_state:
    st.session_state.conta_encerrar_meta_ganho = "Sim"

if "final_conta_encerrar_meta_ganho" not in st.session_state:
    st.session_state.final_conta_encerrar_meta_ganho = "Nao usar"

if "conta_limite_perda" not in st.session_state:
    st.session_state.conta_limite_perda = 0

if "conta_limite_perda_passe" not in st.session_state:
    st.session_state.conta_limite_perda_passe = 0

if "final_conta_limite_perda" not in st.session_state:
    st.session_state.final_conta_limite_perda = 0

if "conta_encerrar_limite_perda" not in st.session_state:
    st.session_state.conta_encerrar_limite_perda = "Sim"

if "final_conta_encerrar_limite_perda" not in st.session_state:
    st.session_state.final_conta_encerrar_limite_perda = "Nao usar"

if "conta_rebaixamento" not in st.session_state:
    st.session_state.conta_rebaixamento = 0

if "conta_rebaixamento_passe" not in st.session_state:
    st.session_state.conta_rebaixamento_passe = 0

if "final_conta_rebaixamento" not in st.session_state:
    st.session_state.final_conta_rebaixamento = 0

if "conta_encerrar_rebaixamento" not in st.session_state:
    st.session_state.conta_encerrar_rebaixamento = "Não"

if "final_conta_encerrar_rebaixamento" not in st.session_state:
    st.session_state.final_conta_encerrar_rebaixamento = "Nao usar"

if "conta_gatilho_rebaixamento" not in st.session_state:
    st.session_state.conta_gatilho_rebaixamento = 0

if "conta_gatilho_rebaixamento_passe" not in st.session_state:
    st.session_state.conta_gatilho_rebaixamento_passe = 0

if "final_conta_gatilho_rebaixamento" not in st.session_state:
    st.session_state.final_conta_gatilho_rebaixamento = 0

if "conta_recuperacao" not in st.session_state:
    st.session_state.conta_recuperacao = 0

if "conta_recuperacao_passe" not in st.session_state:
    st.session_state.conta_recuperacao_passe = 0

if "final_conta_recuperacao" not in st.session_state:
    st.session_state.final_conta_recuperacao = 0

if "conta_encerrar_recuperacao" not in st.session_state:
    st.session_state.conta_encerrar_recuperacao = "Não"

if "final_conta_encerrar_recuperacao" not in st.session_state:
    st.session_state.final_conta_encerrar_recuperacao = "Nao usar"

if "conta_gatilho_recuperacao" not in st.session_state:
    st.session_state.conta_gatilho_recuperacao = 0

if "conta_gatilho_recuperacao_passe" not in st.session_state:
    st.session_state.conta_gatilho_recuperacao_passe = 0

if "final_conta_gatilho_recuperacao" not in st.session_state:
    st.session_state.final_conta_gatilho_recuperacao = 0

if "permissoes_gestao_conta_salvo" not in st.session_state:
    st.session_state.permissoes_gestao_conta_salvo = False

if "ajuste_cancelar_pendente_entrada_sinal_oposto" not in st.session_state:
    st.session_state.ajuste_cancelar_pendente_entrada_sinal_oposto = "Não"

if "final_ajuste_cancelar_pendente_entrada_sinal_oposto" not in st.session_state:
    st.session_state.final_ajuste_cancelar_pendente_entrada_sinal_oposto = "Nao usar"

if "ajuste_reposicionar_stoploss_aumento_favor" not in st.session_state:
    st.session_state.ajuste_reposicionar_stoploss_aumento_favor = "Não"

if "final_ajuste_reposicionar_stoploss_aumento_favor" not in st.session_state:
    st.session_state.final_ajuste_reposicionar_stoploss_aumento_favor = "Nao usar"

if "ajuste_reposicionar_takeprofit_aumento_contra" not in st.session_state:
    st.session_state.ajuste_reposicionar_takeprofit_aumento_contra = "Não"

if "final_ajuste_reposicionar_takeprofit_aumento_contra" not in st.session_state:
    st.session_state.final_ajuste_reposicionar_takeprofit_aumento_contra = "Nao usar"

if "ajuste_movimentar_stoploss_preco_medio" not in st.session_state:
    st.session_state.ajuste_movimentar_stoploss_preco_medio = "Não"

if "final_ajuste_movimentar_stoploss_preco_medio" not in st.session_state:
    st.session_state.final_ajuste_movimentar_stoploss_preco_medio = "Nao usar"

if "ajuste_movimentar_takeprofit_preco_medio" not in st.session_state:
    st.session_state.ajuste_movimentar_takeprofit_preco_medio = "Não"

if "final_ajuste_movimentar_takeprofit_preco_medio" not in st.session_state:
    st.session_state.final_ajuste_movimentar_takeprofit_preco_medio = "Nao usar"

if "ajuste_usar_preco_medio_parciais" not in st.session_state:
    st.session_state.ajuste_usar_preco_medio_parciais = "Não"

if "final_ajuste_usar_preco_medio_parciais" not in st.session_state:
    st.session_state.final_ajuste_usar_preco_medio_parciais = "Nao usar"

if "ajuste_impedir_saida_vela_entrada" not in st.session_state:
    st.session_state.ajuste_impedir_saida_vela_entrada = "Não"

if "final_ajuste_impedir_saida_vela_entrada" not in st.session_state:
    st.session_state.final_ajuste_impedir_saida_vela_entrada = "Nao usar"

if "ajuste_impedir_entrada_vela_saida" not in st.session_state:
    st.session_state.ajuste_impedir_entrada_vela_saida = "Não"

if "final_ajuste_impedir_entrada_vela_saida" not in st.session_state:
    st.session_state.final_ajuste_impedir_entrada_vela_saida = "Nao usar"

if "ajuste_recalcular_preco_medio_saidas_parciais" not in st.session_state:
    st.session_state.ajuste_recalcular_preco_medio_saidas_parciais = "Não"

if "final_ajuste_recalcular_preco_medio_saidas_parciais" not in st.session_state:
    st.session_state.final_ajuste_recalcular_preco_medio_saidas_parciais = "Nao usar"

if "ajustes_finais_salvo" not in st.session_state:
    st.session_state.ajustes_finais_salvo = False

if "comp_enviar_ordem_outro_ativo" not in st.session_state:
    st.session_state.comp_enviar_ordem_outro_ativo = "Não"

if "final_comp_enviar_ordem_outro_ativo" not in st.session_state:
    st.session_state.final_comp_enviar_ordem_outro_ativo = "Nao usar"

if "comp_procurar_entrada_vela_seguinte_saida" not in st.session_state:
    st.session_state.comp_procurar_entrada_vela_seguinte_saida = "Não"

if "final_comp_procurar_entrada_vela_seguinte_saida" not in st.session_state:
    st.session_state.final_comp_procurar_entrada_vela_seguinte_saida = "Nao usar"

if "comp_procurar_saida_vela_seguinte_entrada" not in st.session_state:
    st.session_state.comp_procurar_saida_vela_seguinte_entrada = "Não"

if "final_comp_procurar_saida_vela_seguinte_entrada" not in st.session_state:
    st.session_state.final_comp_procurar_saida_vela_seguinte_entrada = "Nao usar"

if "comp_saldo_ajuste" not in st.session_state:
    st.session_state.comp_saldo_ajuste = 0

if "comp_saldo_ajuste_passe" not in st.session_state:
    st.session_state.comp_saldo_ajuste_passe = 0

if "final_comp_saldo_ajuste" not in st.session_state:
    st.session_state.final_comp_saldo_ajuste = 0

if "complementos_salvo" not in st.session_state:
    st.session_state.complementos_salvo = False

if "final_exibir_indicadores" not in st.session_state:
    st.session_state.final_exibir_indicadores = False

if "final_criar_painel_boleta" not in st.session_state:
    st.session_state.final_criar_painel_boleta = False

if "final_criar_log_expert" not in st.session_state:
    st.session_state.final_criar_log_expert = False

if "final_criar_etiquetas_personalizadas" not in st.session_state:
    st.session_state.final_criar_etiquetas_personalizadas = False

if "final_alterar_layout_grafico" not in st.session_state:
    st.session_state.final_alterar_layout_grafico = False

if "finalizacao_salvo" not in st.session_state:
    st.session_state.finalizacao_salvo = False

if "referencia_tempo_filtro" not in st.session_state:
    st.session_state.referencia_tempo_filtro = "Segundos"

if "final_referencia_tempo_filtro" not in st.session_state:
    st.session_state.final_referencia_tempo_filtro = "Nao usar"

if "tempo_para_nova_entrada" not in st.session_state:
    st.session_state.tempo_para_nova_entrada = 0

if "tempo_para_nova_entrada_passe" not in st.session_state:
    st.session_state.tempo_para_nova_entrada_passe = 0

if "final_tempo_para_nova_entrada" not in st.session_state:
    st.session_state.final_tempo_para_nova_entrada = 0

if "tempo_minimo_posicao" not in st.session_state:
    st.session_state.tempo_minimo_posicao = 0

if "tempo_minimo_posicao_passe" not in st.session_state:
    st.session_state.tempo_minimo_posicao_passe = 0

if "final_tempo_minimo_posicao" not in st.session_state:
    st.session_state.final_tempo_minimo_posicao = 0

if "filtro_tempo_salvo" not in st.session_state:
    st.session_state.filtro_tempo_salvo = False

if "zerar_por_horario" not in st.session_state:
    st.session_state.zerar_por_horario = "Nao"

if "final_zerar_por_horario" not in st.session_state:
    st.session_state.final_zerar_por_horario = "Nao usar"

if "hora_inicial_operacoes" not in st.session_state:
    st.session_state.hora_inicial_operacoes = 0

if "hora_inicial_operacoes_passe" not in st.session_state:
    st.session_state.hora_inicial_operacoes_passe = 0

if "final_hora_inicial_operacoes" not in st.session_state:
    st.session_state.final_hora_inicial_operacoes = 0

if "minuto_inicial_operacoes" not in st.session_state:
    st.session_state.minuto_inicial_operacoes = 0

if "minuto_inicial_operacoes_passe" not in st.session_state:
    st.session_state.minuto_inicial_operacoes_passe = 0

if "final_minuto_inicial_operacoes" not in st.session_state:
    st.session_state.final_minuto_inicial_operacoes = 0

if "hora_final_operacoes" not in st.session_state:
    st.session_state.hora_final_operacoes = 0

if "hora_final_operacoes_passe" not in st.session_state:
    st.session_state.hora_final_operacoes_passe = 0

if "final_hora_final_operacoes" not in st.session_state:
    st.session_state.final_hora_final_operacoes = 0

if "minuto_final_operacoes" not in st.session_state:
    st.session_state.minuto_final_operacoes = 0

if "minuto_final_operacoes_passe" not in st.session_state:
    st.session_state.minuto_final_operacoes_passe = 0

if "final_minuto_final_operacoes" not in st.session_state:
    st.session_state.final_minuto_final_operacoes = 0

if "hora_zerar_operacoes" not in st.session_state:
    st.session_state.hora_zerar_operacoes = 0

if "hora_zerar_operacoes_passe" not in st.session_state:
    st.session_state.hora_zerar_operacoes_passe = 0

if "final_hora_zerar_operacoes" not in st.session_state:
    st.session_state.final_hora_zerar_operacoes = 0

if "minuto_zerar_operacoes" not in st.session_state:
    st.session_state.minuto_zerar_operacoes = 0

if "minuto_zerar_operacoes_passe" not in st.session_state:
    st.session_state.minuto_zerar_operacoes_passe = 0

if "final_minuto_zerar_operacoes" not in st.session_state:
    st.session_state.final_minuto_zerar_operacoes = 0

if "horarios_salvos" not in st.session_state:
    st.session_state.horarios_salvos = False

if "referencia_tempo_pausas" not in st.session_state:
    st.session_state.referencia_tempo_pausas = "Segundos"

if "final_referencia_tempo_pausas" not in st.session_state:
    st.session_state.final_referencia_tempo_pausas = "Nao usar"

if "primeira_pausa_hora" not in st.session_state:
    st.session_state.primeira_pausa_hora = 0

if "primeira_pausa_minuto" not in st.session_state:
    st.session_state.primeira_pausa_minuto = 0

if "primeira_pausa_hora_passe" not in st.session_state:
    st.session_state.primeira_pausa_hora_passe = 0

if "primeira_pausa_minuto_passe" not in st.session_state:
    st.session_state.primeira_pausa_minuto_passe = 0

if "final_primeira_pausa_hora" not in st.session_state:
    st.session_state.final_primeira_pausa_hora = 0

if "final_primeira_pausa_minuto" not in st.session_state:
    st.session_state.final_primeira_pausa_minuto = 0

if "primeira_pausa_periodo" not in st.session_state:
    st.session_state.primeira_pausa_periodo = "Diariamente"

if "final_primeira_pausa_periodo" not in st.session_state:
    st.session_state.final_primeira_pausa_periodo = "Nao usar"

if "primeira_pausa_duracao" not in st.session_state:
    st.session_state.primeira_pausa_duracao = 0

if "primeira_pausa_duracao_passe" not in st.session_state:
    st.session_state.primeira_pausa_duracao_passe = 0

if "final_primeira_pausa_duracao" not in st.session_state:
    st.session_state.final_primeira_pausa_duracao = 0

if "segunda_pausa_hora" not in st.session_state:
    st.session_state.segunda_pausa_hora = 0

if "segunda_pausa_minuto" not in st.session_state:
    st.session_state.segunda_pausa_minuto = 0

if "segunda_pausa_hora_passe" not in st.session_state:
    st.session_state.segunda_pausa_hora_passe = 0

if "segunda_pausa_minuto_passe" not in st.session_state:
    st.session_state.segunda_pausa_minuto_passe = 0

if "final_segunda_pausa_hora" not in st.session_state:
    st.session_state.final_segunda_pausa_hora = 0

if "final_segunda_pausa_minuto" not in st.session_state:
    st.session_state.final_segunda_pausa_minuto = 0

if "segunda_pausa_periodo" not in st.session_state:
    st.session_state.segunda_pausa_periodo = "Diariamente"

if "final_segunda_pausa_periodo" not in st.session_state:
    st.session_state.final_segunda_pausa_periodo = "Nao usar"

if "segunda_pausa_duracao" not in st.session_state:
    st.session_state.segunda_pausa_duracao = 0

if "segunda_pausa_duracao_passe" not in st.session_state:
    st.session_state.segunda_pausa_duracao_passe = 0

if "final_segunda_pausa_duracao" not in st.session_state:
    st.session_state.final_segunda_pausa_duracao = 0

if "pausas_operacionais_salvas" not in st.session_state:
    st.session_state.pausas_operacionais_salvas = False

if "tipo_calculo_aumento_contra" not in st.session_state:
    st.session_state.tipo_calculo_aumento_contra = "Em pontos"

if "final_tipo_calculo_aumento_contra" not in st.session_state:
    st.session_state.final_tipo_calculo_aumento_contra = "Nao usar"

if "distancia_contra_1" not in st.session_state:
    st.session_state.distancia_contra_1 = 0

if "volume_contra_1" not in st.session_state:
    st.session_state.volume_contra_1 = 0

if "distancia_contra_1_passe" not in st.session_state:
    st.session_state.distancia_contra_1_passe = 0

if "volume_contra_1_passe" not in st.session_state:
    st.session_state.volume_contra_1_passe = 0

if "final_distancia_contra_1" not in st.session_state:
    st.session_state.final_distancia_contra_1 = 0

if "final_volume_contra_1" not in st.session_state:
    st.session_state.final_volume_contra_1 = 0

if "distancia_contra_2" not in st.session_state:
    st.session_state.distancia_contra_2 = 0

if "volume_contra_2" not in st.session_state:
    st.session_state.volume_contra_2 = 0

if "distancia_contra_2_passe" not in st.session_state:
    st.session_state.distancia_contra_2_passe = 0

if "volume_contra_2_passe" not in st.session_state:
    st.session_state.volume_contra_2_passe = 0

if "final_distancia_contra_2" not in st.session_state:
    st.session_state.final_distancia_contra_2 = 0

if "final_volume_contra_2" not in st.session_state:
    st.session_state.final_volume_contra_2 = 0

if "distancia_contra_3" not in st.session_state:
    st.session_state.distancia_contra_3 = 0

if "volume_contra_3" not in st.session_state:
    st.session_state.volume_contra_3 = 0

if "distancia_contra_3_passe" not in st.session_state:
    st.session_state.distancia_contra_3_passe = 0

if "volume_contra_3_passe" not in st.session_state:
    st.session_state.volume_contra_3_passe = 0

if "final_distancia_contra_3" not in st.session_state:
    st.session_state.final_distancia_contra_3 = 0

if "final_volume_contra_3" not in st.session_state:
    st.session_state.final_volume_contra_3 = 0

if "distancia_contra_4" not in st.session_state:
    st.session_state.distancia_contra_4 = 0

if "volume_contra_4" not in st.session_state:
    st.session_state.volume_contra_4 = 0

if "distancia_contra_4_passe" not in st.session_state:
    st.session_state.distancia_contra_4_passe = 0

if "volume_contra_4_passe" not in st.session_state:
    st.session_state.volume_contra_4_passe = 0

if "final_distancia_contra_4" not in st.session_state:
    st.session_state.final_distancia_contra_4 = 0

if "final_volume_contra_4" not in st.session_state:
    st.session_state.final_volume_contra_4 = 0

if "distancia_contra_5" not in st.session_state:
    st.session_state.distancia_contra_5 = 0

if "volume_contra_5" not in st.session_state:
    st.session_state.volume_contra_5 = 0

if "distancia_contra_5_passe" not in st.session_state:
    st.session_state.distancia_contra_5_passe = 0

if "volume_contra_5_passe" not in st.session_state:
    st.session_state.volume_contra_5_passe = 0

if "final_distancia_contra_5" not in st.session_state:
    st.session_state.final_distancia_contra_5 = 0

if "final_volume_contra_5" not in st.session_state:
    st.session_state.final_volume_contra_5 = 0

if "aumento_contra_salvo" not in st.session_state:
    st.session_state.aumento_contra_salvo = False

if "tipo_calculo_aumento_favor" not in st.session_state:
    st.session_state.tipo_calculo_aumento_favor = "Em pontos"

if "final_tipo_calculo_aumento_favor" not in st.session_state:
    st.session_state.final_tipo_calculo_aumento_favor = "Nao usar"

if "distancia_favor_1" not in st.session_state:
    st.session_state.distancia_favor_1 = 0

if "volume_favor_1" not in st.session_state:
    st.session_state.volume_favor_1 = 0

if "distancia_favor_1_passe" not in st.session_state:
    st.session_state.distancia_favor_1_passe = 0

if "volume_favor_1_passe" not in st.session_state:
    st.session_state.volume_favor_1_passe = 0

if "final_distancia_favor_1" not in st.session_state:
    st.session_state.final_distancia_favor_1 = 0

if "final_volume_favor_1" not in st.session_state:
    st.session_state.final_volume_favor_1 = 0

if "distancia_favor_2" not in st.session_state:
    st.session_state.distancia_favor_2 = 0

if "volume_favor_2" not in st.session_state:
    st.session_state.volume_favor_2 = 0

if "distancia_favor_2_passe" not in st.session_state:
    st.session_state.distancia_favor_2_passe = 0

if "volume_favor_2_passe" not in st.session_state:
    st.session_state.volume_favor_2_passe = 0

if "final_distancia_favor_2" not in st.session_state:
    st.session_state.final_distancia_favor_2 = 0

if "final_volume_favor_2" not in st.session_state:
    st.session_state.final_volume_favor_2 = 0

if "distancia_favor_3" not in st.session_state:
    st.session_state.distancia_favor_3 = 0

if "volume_favor_3" not in st.session_state:
    st.session_state.volume_favor_3 = 0

if "distancia_favor_3_passe" not in st.session_state:
    st.session_state.distancia_favor_3_passe = 0

if "volume_favor_3_passe" not in st.session_state:
    st.session_state.volume_favor_3_passe = 0

if "final_distancia_favor_3" not in st.session_state:
    st.session_state.final_distancia_favor_3 = 0

if "final_volume_favor_3" not in st.session_state:
    st.session_state.final_volume_favor_3 = 0

if "distancia_favor_4" not in st.session_state:
    st.session_state.distancia_favor_4 = 0

if "volume_favor_4" not in st.session_state:
    st.session_state.volume_favor_4 = 0

if "distancia_favor_4_passe" not in st.session_state:
    st.session_state.distancia_favor_4_passe = 0

if "volume_favor_4_passe" not in st.session_state:
    st.session_state.volume_favor_4_passe = 0

if "final_distancia_favor_4" not in st.session_state:
    st.session_state.final_distancia_favor_4 = 0

if "final_volume_favor_4" not in st.session_state:
    st.session_state.final_volume_favor_4 = 0

if "distancia_favor_5" not in st.session_state:
    st.session_state.distancia_favor_5 = 0

if "volume_favor_5" not in st.session_state:
    st.session_state.volume_favor_5 = 0

if "distancia_favor_5_passe" not in st.session_state:
    st.session_state.distancia_favor_5_passe = 0

if "volume_favor_5_passe" not in st.session_state:
    st.session_state.volume_favor_5_passe = 0

if "final_distancia_favor_5" not in st.session_state:
    st.session_state.final_distancia_favor_5 = 0

if "final_volume_favor_5" not in st.session_state:
    st.session_state.final_volume_favor_5 = 0

if "aumento_favor_salvo" not in st.session_state:
    st.session_state.aumento_favor_salvo = False

if "tipo_calculo_saidas_parciais" not in st.session_state:
    st.session_state.tipo_calculo_saidas_parciais = "Em pontos"

if "final_tipo_calculo_saidas_parciais" not in st.session_state:
    st.session_state.final_tipo_calculo_saidas_parciais = "Nao usar"

if "distancia_parcial_1" not in st.session_state:
    st.session_state.distancia_parcial_1 = 0

if "volume_parcial_1" not in st.session_state:
    st.session_state.volume_parcial_1 = 0

if "distancia_parcial_1_passe" not in st.session_state:
    st.session_state.distancia_parcial_1_passe = 0

if "volume_parcial_1_passe" not in st.session_state:
    st.session_state.volume_parcial_1_passe = 0

if "final_distancia_parcial_1" not in st.session_state:
    st.session_state.final_distancia_parcial_1 = 0

if "final_volume_parcial_1" not in st.session_state:
    st.session_state.final_volume_parcial_1 = 0

if "distancia_parcial_2" not in st.session_state:
    st.session_state.distancia_parcial_2 = 0

if "volume_parcial_2" not in st.session_state:
    st.session_state.volume_parcial_2 = 0

if "distancia_parcial_2_passe" not in st.session_state:
    st.session_state.distancia_parcial_2_passe = 0

if "volume_parcial_2_passe" not in st.session_state:
    st.session_state.volume_parcial_2_passe = 0

if "final_distancia_parcial_2" not in st.session_state:
    st.session_state.final_distancia_parcial_2 = 0

if "final_volume_parcial_2" not in st.session_state:
    st.session_state.final_volume_parcial_2 = 0

if "distancia_parcial_3" not in st.session_state:
    st.session_state.distancia_parcial_3 = 0

if "volume_parcial_3" not in st.session_state:
    st.session_state.volume_parcial_3 = 0

if "distancia_parcial_3_passe" not in st.session_state:
    st.session_state.distancia_parcial_3_passe = 0

if "volume_parcial_3_passe" not in st.session_state:
    st.session_state.volume_parcial_3_passe = 0

if "final_distancia_parcial_3" not in st.session_state:
    st.session_state.final_distancia_parcial_3 = 0

if "final_volume_parcial_3" not in st.session_state:
    st.session_state.final_volume_parcial_3 = 0

if "distancia_parcial_4" not in st.session_state:
    st.session_state.distancia_parcial_4 = 0

if "volume_parcial_4" not in st.session_state:
    st.session_state.volume_parcial_4 = 0

if "distancia_parcial_4_passe" not in st.session_state:
    st.session_state.distancia_parcial_4_passe = 0

if "volume_parcial_4_passe" not in st.session_state:
    st.session_state.volume_parcial_4_passe = 0

if "final_distancia_parcial_4" not in st.session_state:
    st.session_state.final_distancia_parcial_4 = 0

if "final_volume_parcial_4" not in st.session_state:
    st.session_state.final_volume_parcial_4 = 0

if "saidas_parciais_salvas" not in st.session_state:
    st.session_state.saidas_parciais_salvas = False

if st.session_state.etapa == 1:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>1. De um nome para seu robo</h3>", unsafe_allow_html=True)

        input_col, sufixo_col = st.columns([6, 1])
        with input_col:
            st.text_input(
                "De um nome para seu robo",
                key="nome_input",
                label_visibility="collapsed",
            )
        with sufixo_col:
            st.markdown("<div style='padding-top: 0.5rem;'>.mq5</div>", unsafe_allow_html=True)

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            st.button("Voltar", disabled=True, use_container_width=True)
        with nav_dir:
            if st.button("Avancar", use_container_width=True):
                nome = st.session_state.nome_input.strip()
                if nome:
                    st.session_state.nome_robo = nome
                    st.session_state.etapa = 2
                    st.rerun()
                st.warning("Informe um nome para o robo.")

if st.session_state.etapa == 2:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>2. CONFIGURACAO INICIAL</h3>", unsafe_allow_html=True)
        st.markdown(
            "<p class='center-note'>Se desabilitar algum dos lados podera pular as configuracoes de sinais</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_ini, col_fim = st.columns(2, gap="large")

            with col_ini:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🚀 Iniciar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "🛒 Deseja operar na compra",
                    ["Sim", "Nao"],
                    key="operar_compra",
                )
                st.selectbox(
                    "💸 Deseja operar na venda",
                    ["Sim", "Nao"],
                    key="operar_venda",
                )
                st.selectbox(
                    "⚙️ Modo de processamento",
                    ["A cada tick", "A cada segundo"],
                    key="modo_processamento",
                )

            with col_fim:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🏁 Finalizar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "🛒 Deseja operar na compra",
                    ["Nao usar", "Sim", "Nao"],
                    key="final_operar_compra",
                )
                st.selectbox(
                    "💸 Deseja operar na venda",
                    ["Nao usar", "Sim", "Nao"],
                    key="final_operar_venda",
                )
                st.selectbox(
                    "⚙️ Modo de processamento",
                    ["Nao usar", "A cada tick", "A cada segundo"],
                    key="final_modo_processamento",
                )

            st.divider()

            st.selectbox(
                "🌎 Escolha o mercado desejado",
                ["B3", "Forex"],
                key="mercado",
            )

            st.selectbox(
                "📈 Selecione o tipo operacional",
                ["Swing Trade", "Day Trade"],
                key="tipo_operacional",
            )

            st.markdown(
                "<p class='center-note'>Algumas configuracoes de B3 podem nao funcionar no FOREX e vice-versa</p>",
                unsafe_allow_html=True,
            )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 1
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.config_inicial_salva = True
                st.session_state.etapa = 3
                st.rerun()

if st.session_state.etapa == 3:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>3. PARAMETROS DE EXECUCAO</h3>", unsafe_allow_html=True)
        st.markdown(
            "<p class='center-note'>Defina os parametros de execucao do robo</p>",
            unsafe_allow_html=True,
        )

        tempos_grafico = [
            "Corrente",
            "1 Minuto (M1)",
            "2 Minutos (M2)",
            "3 Minutos (M3)",
            "4 Minutos (M4)",
            "5 Minutos (M5)",
            "6 Minutos (M6)",
            "10 Minutos (M10)",
            "30 Minutos (M30)",
            "1 Hora (H1)",
            "2 Horas (H2)",
            "3 Horas (H3)",
            "4 Horas (H4)",
            "6 Horas (H6)",
            "8 Horas (H8)",
            "12 Horas (H12)",
            "1 Dia (D1)",
            "1 Semana (W1)",
            "1 Mes (MN1)",
        ]

        with st.container(border=True):
            st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🕒 Tempo grafico</h4>", unsafe_allow_html=True)
            col_t_ini, col_t_fim = st.columns(2, gap="large")
            with col_t_ini:
                st.selectbox(
                    "🟢 Iniciar",
                    tempos_grafico,
                    key="tempo_grafico_principal",
                )
            with col_t_fim:
                st.selectbox(
                    "🔴 Finalizar",
                    ["Nao usar", *tempos_grafico],
                    key="tempo_grafico_finalizar",
                )

            st.divider()

            st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>📦 Volume e spread</h4>", unsafe_allow_html=True)
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")

            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input(
                    "Volume inicial",
                    min_value=0,
                    step=1,
                    key="volume_inicial",
                )
                st.number_input(
                    "Spread maximo (pontos)",
                    min_value=0,
                    step=1,
                    key="spread_maximo",
                )

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input(
                    "Volume inicial",
                    min_value=0,
                    step=1,
                    key="volume_passe",
                )
                st.number_input(
                    "Spread maximo (pontos)",
                    min_value=0,
                    step=1,
                    key="spread_passe",
                )

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input(
                    "Volume inicial",
                    min_value=0,
                    step=1,
                    key="volume_finalizar",
                )
                st.number_input(
                    "Spread maximo (pontos)",
                    min_value=0,
                    step=1,
                    key="spread_finalizar",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 2
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.parametros_execucao_salvos = True
                st.session_state.etapa = 4
                st.rerun()

if st.session_state.etapa == 4:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>4. TIPO DE ORDENS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>E possivel personalizar a posicao do preco de entrada e saida durante um sinal</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_ini, col_fim = st.columns(2, gap="large")
            with col_ini:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🚀 Iniciar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "📏 Tipo de calculo das distancias",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_distancias",
                )
                st.markdown("<p style='text-align: center; font-weight:700; margin: 0.25rem 0 0.25rem 0;'>Entradas</p>", unsafe_allow_html=True)
                st.selectbox(
                    "🟢 Ordem de entrada",
                    ["A mercado", "Pendente"],
                    key="ordem_entrada",
                )
                st.markdown("<p style='text-align: center; font-weight:700; margin: 0.25rem 0 0.25rem 0;'>Saidas</p>", unsafe_allow_html=True)
                st.selectbox(
                    "🔴 Ordem de saida",
                    ["A mercado", "Pendente"],
                    key="ordem_saida",
                )

            with col_fim:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🏁 Finalizar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "📏 Tipo de calculo das distancias",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_distancias",
                )
                st.markdown("<p style='text-align: center; font-weight:700; margin: 0.25rem 0 0.25rem 0;'>Entradas</p>", unsafe_allow_html=True)
                st.selectbox(
                    "🟢 Ordem de entrada",
                    ["Nao usar", "A mercado", "Pendente"],
                    key="final_ordem_entrada",
                )
                st.markdown("<p style='text-align: center; font-weight:700; margin: 0.25rem 0 0.25rem 0;'>Saidas</p>", unsafe_allow_html=True)
                st.selectbox(
                    "🔴 Ordem de saida",
                    ["Nao usar", "A mercado", "Pendente"],
                    key="final_ordem_saida",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 3
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.tipo_ordens_salvas = True
                st.session_state.etapa = 5
                st.rerun()

if st.session_state.etapa == 5:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>5. ALVOS PERSONALIZADOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>E possivel personalizar uma distancia para o stoploss e/ou takeprofit</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Os alvos personalizados serao comparados com os alvos padroes</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_ini, col_fim = st.columns(2, gap="large")

            with col_ini:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🚀 Iniciar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "📏 Tipo de calculo das distancias",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_alvos",
                )
                st.selectbox(
                    "🛡️ Usar stoploss personalizado",
                    ["Nao", "Sim"],
                    key="usar_stoploss_personalizado",
                )
                st.selectbox(
                    "🎯 Usar takeprofit personalizado",
                    ["Nao", "Sim"],
                    key="usar_takeprofit_personalizado",
                )

            with col_fim:
                st.markdown("<h4 style='text-align: center; margin: 0 0 0.75rem 0;'>🏁 Finalizar</h4>", unsafe_allow_html=True)
                st.selectbox(
                    "📏 Tipo de calculo das distancias",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_alvos",
                )
                st.selectbox(
                    "🛡️ Usar stoploss personalizado",
                    ["Nao usar", "Nao", "Sim"],
                    key="final_usar_stoploss_personalizado",
                )
                st.selectbox(
                    "🎯 Usar takeprofit personalizado",
                    ["Nao usar", "Nao", "Sim"],
                    key="final_usar_takeprofit_personalizado",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 4
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.alvos_personalizados_salvos = True
                st.session_state.etapa = 6
                st.rerun()

if st.session_state.etapa == 6:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>6. STOPLOSS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Defina o limite de perda aceitavel por operacao e o tipo de calculo das distancias</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Unidade: pontos / percentual (dependendo do select)</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>A medida que a operacao anda a favor, o stoploss podera ser reposicionado para acompanhar o preco corrente</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_stoploss",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_stoploss",
                )

            st.divider()

            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input("🛑 Stoploss inicial", min_value=0, step=1, key="stoploss_inicial")
                st.number_input("🟢 Inicio do Break Even SL", min_value=0, step=1, key="inicio_break_even_sl")
                st.number_input("📍 Distancia do Break Even SL", min_value=0, step=1, key="distancia_break_even_sl")
                st.number_input("🟠 Inicio do Trailing Stop", min_value=0, step=1, key="inicio_trailing_stop")
                st.number_input("🔁 Passo do Trailing Stop", min_value=0, step=1, key="passo_trailing_stop")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("🛑 Stoploss inicial", min_value=0, step=1, key="stoploss_passe")
                st.number_input("🟢 Inicio do Break Even SL", min_value=0, step=1, key="inicio_break_even_sl_passe")
                st.number_input("📍 Distancia do Break Even SL", min_value=0, step=1, key="distancia_break_even_sl_passe")
                st.number_input("🟠 Inicio do Trailing Stop", min_value=0, step=1, key="inicio_trailing_stop_passe")
                st.number_input("🔁 Passo do Trailing Stop", min_value=0, step=1, key="passo_trailing_stop_passe")

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input("🛑 Stoploss inicial", min_value=0, step=1, key="final_stoploss_inicial")
                st.number_input("🟢 Inicio do Break Even SL", min_value=0, step=1, key="final_inicio_break_even_sl")
                st.number_input("📍 Distancia do Break Even SL", min_value=0, step=1, key="final_distancia_break_even_sl")
                st.number_input("🟠 Inicio do Trailing Stop", min_value=0, step=1, key="final_inicio_trailing_stop")
                st.number_input("🔁 Passo do Trailing Stop", min_value=0, step=1, key="final_passo_trailing_stop")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 5
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.stoploss_salvo = True
                st.session_state.etapa = 7
                st.rerun()

if st.session_state.etapa == 7:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>7. TAKE PROFIT</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Defina o alvo da operacao e o tipo de calculo da distancia de referencia</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>A medida que a operacao anda contra, o takeprofit podera ser reposicionado para facilitar uma saida</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_takeprofit",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_takeprofit",
                )

            st.divider()

            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input("🎯 TakeProfit inicial", min_value=0, step=1, key="takeprofit_inicial")
                st.number_input("🟢 Inicio do Break Even TP", min_value=0, step=1, key="inicio_break_even_tp")
                st.number_input("📍 Distancia do Break Even TP", min_value=0, step=1, key="distancia_break_even_tp")
                st.number_input("🟠 Inicio do Trailing Profit", min_value=0, step=1, key="inicio_trailing_profit")
                st.number_input("🔁 Passo do Trailing Profit", min_value=0, step=1, key="passo_trailing_profit")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("🎯 TakeProfit inicial", min_value=0, step=1, key="takeprofit_passe")
                st.number_input("🟢 Inicio do Break Even TP", min_value=0, step=1, key="inicio_break_even_tp_passe")
                st.number_input("📍 Distancia do Break Even TP", min_value=0, step=1, key="distancia_break_even_tp_passe")
                st.number_input("🟠 Inicio do Trailing Profit", min_value=0, step=1, key="inicio_trailing_profit_passe")
                st.number_input("🔁 Passo do Trailing Profit", min_value=0, step=1, key="passo_trailing_profit_passe")

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input("🎯 TakeProfit inicial", min_value=0, step=1, key="final_takeprofit_inicial")
                st.number_input("🟢 Inicio do Break Even TP", min_value=0, step=1, key="final_inicio_break_even_tp")
                st.number_input("📍 Distancia do Break Even TP", min_value=0, step=1, key="final_distancia_break_even_tp")
                st.number_input("🟠 Inicio do Trailing Profit", min_value=0, step=1, key="final_inicio_trailing_profit")
                st.number_input("🔁 Passo do Trailing Profit", min_value=0, step=1, key="final_passo_trailing_profit")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 6
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.takeprofit_salvo = True
                st.session_state.etapa = 8
                st.rerun()

if st.session_state.etapa == 8:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>8. SAIDA TEMPORAL</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Saida pelo tempo sem depender do stoploss e/ou takeprofit</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Pode configurar um tempo de saida tanto para operacoes positivas quanto para negativas</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            col_ref_ini, col_ref_fim = st.columns(2, gap="large")
            with col_ref_ini:
                st.selectbox(
                    "⏱️ Referencia de tempo (Iniciar)",
                    ["Segundos", "Minutos", "Horas", "Velas"],
                    key="referencia_tempo_saida",
                )
            with col_ref_fim:
                st.selectbox(
                    "⏱️ Referencia de tempo (Finalizar)",
                    ["Nao usar", "Segundos", "Minutos", "Horas", "Velas"],
                    key="final_referencia_tempo_saida",
                )

            st.divider()

            referencia_tempo = st.session_state.referencia_tempo_saida

            st.markdown("<p style='text-align: center; font-weight: 800; margin: 0 0 0.75rem 0;'>✅ Operacoes positivas</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="tempo_saida_operacoes_positivas")
                st.number_input("Saldo maximo", min_value=0, step=1, key="saldo_maximo_operacoes_positivas")
                st.number_input("Saldo minimo", min_value=0, step=1, key="saldo_minimo_operacoes_positivas")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="tempo_saida_operacoes_positivas_passe")
                st.number_input("Saldo maximo", min_value=0, step=1, key="saldo_maximo_operacoes_positivas_passe")
                st.number_input("Saldo minimo", min_value=0, step=1, key="saldo_minimo_operacoes_positivas_passe")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="final_tempo_saida_operacoes_positivas")
                st.number_input("Saldo maximo", min_value=0, step=1, key="final_saldo_maximo_operacoes_positivas")
                st.number_input("Saldo minimo", min_value=0, step=1, key="final_saldo_minimo_operacoes_positivas")

            st.divider()

            st.markdown("<p style='text-align: center; font-weight: 800; margin: 0 0 0.75rem 0;'>❌ Operacoes negativas</p>", unsafe_allow_html=True)
            c_ini2, c_passe2, c_fim2 = st.columns(3, gap="large")
            with c_ini2:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="tempo_saida_operacoes_negativas")
                st.number_input("Saldo maximo", min_value=0, step=1, key="saldo_maximo_operacoes_negativas")
                st.number_input("Saldo minimo", min_value=0, step=1, key="saldo_minimo_operacoes_negativas")
            with c_passe2:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="tempo_saida_operacoes_negativas_passe")
                st.number_input("Saldo maximo", min_value=0, step=1, key="saldo_maximo_operacoes_negativas_passe")
                st.number_input("Saldo minimo", min_value=0, step=1, key="saldo_minimo_operacoes_negativas_passe")
            with c_fim2:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input(f"Tempo de saida ({referencia_tempo})", min_value=0, step=1, key="final_tempo_saida_operacoes_negativas")
                st.number_input("Saldo maximo", min_value=0, step=1, key="final_saldo_maximo_operacoes_negativas")
                st.number_input("Saldo minimo", min_value=0, step=1, key="final_saldo_minimo_operacoes_negativas")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 7
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.saida_temporal_salva = True
                st.session_state.etapa = 9
                st.rerun()

if st.session_state.etapa == 9:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>9. FILTRO DE TEMPO</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Referencia de tempo para procurar entrada e/ou sinais de saida</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Deixar os valores zerados desabilita o recurso do filtro de temporizacao</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            col_ref_ini, col_ref_fim = st.columns(2, gap="large")
            with col_ref_ini:
                st.selectbox(
                    "⏱️ Referencia de tempo (Iniciar)",
                    ["Segundos", "Minutos", "Horas", "Velas"],
                    key="referencia_tempo_filtro",
                )
            with col_ref_fim:
                st.selectbox(
                    "⏱️ Referencia de tempo (Finalizar)",
                    ["Nao usar", "Segundos", "Minutos", "Horas", "Velas"],
                    key="final_referencia_tempo_filtro",
                )

            st.divider()

            referencia_tempo = st.session_state.referencia_tempo_filtro
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input(
                    f"Tempo para nova entrada ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="tempo_para_nova_entrada",
                )
                st.number_input(
                    f"Tempo minimo de posicao ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="tempo_minimo_posicao",
                )

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input(
                    f"Tempo para nova entrada ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="tempo_para_nova_entrada_passe",
                )
                st.number_input(
                    f"Tempo minimo de posicao ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="tempo_minimo_posicao_passe",
                )

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input(
                    f"Tempo para nova entrada ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="final_tempo_para_nova_entrada",
                )
                st.number_input(
                    f"Tempo minimo de posicao ({referencia_tempo})",
                    min_value=0,
                    step=1,
                    key="final_tempo_minimo_posicao",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 8
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.filtro_tempo_salvo = True
                st.session_state.etapa = 10
                st.rerun()

if st.session_state.etapa == 10:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>10. HORARIOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Gerencie seu horario operacional</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Para operar independente de horario, basta deixar o horario inicial igual ao horario final</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_z_ini, col_z_fim = st.columns(2, gap="large")
            with col_z_ini:
                st.selectbox(
                    "🧹 Deseja zerar por horario (Iniciar)",
                    ["Sim", "Nao"],
                    key="zerar_por_horario",
                )
            with col_z_fim:
                st.selectbox(
                    "🧹 Deseja zerar por horario (Finalizar)",
                    ["Nao usar", "Sim", "Nao"],
                    key="final_zerar_por_horario",
                )

            st.divider()

            horas = list(range(24))
            minutos = list(range(60))

            st.markdown("<p style='text-align: center; font-weight: 800; margin: 0 0 0.75rem 0;'>Horario inicial das operacoes</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_inicial_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_inicial_operacoes", label_visibility="collapsed")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_inicial_operacoes_passe", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_inicial_operacoes_passe", label_visibility="collapsed")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="final_hora_inicial_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="final_minuto_inicial_operacoes", label_visibility="collapsed")

            st.markdown("<p style='text-align: center; font-weight: 800; margin: 0.75rem 0 0.75rem 0;'>Horario final das operacoes</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_final_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_final_operacoes", label_visibility="collapsed")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_final_operacoes_passe", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_final_operacoes_passe", label_visibility="collapsed")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="final_hora_final_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="final_minuto_final_operacoes", label_visibility="collapsed")

            st.markdown("<p style='text-align: center; font-weight: 800; margin: 0.75rem 0 0.75rem 0;'>Horario de zerar as operacoes</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_zerar_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_zerar_operacoes", label_visibility="collapsed")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="hora_zerar_operacoes_passe", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="minuto_zerar_operacoes_passe", label_visibility="collapsed")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="final_hora_zerar_operacoes", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="final_minuto_zerar_operacoes", label_visibility="collapsed")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 9
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.horarios_salvos = True
                st.session_state.etapa = 11
                st.rerun()

if st.session_state.etapa == 11:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>11. PAUSAS OPERACIONAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Selecione os dados para identificacao dos criterios das pausas</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>As pausas sao aplicadas somente na procura de sinal de entrada</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            horas = list(range(24))
            minutos = list(range(60))
            periodos = ["Diariamente", "Segundas", "Tercas", "Quartas", "Quintas", "Sextas", "Sabados"]

            col_ref_ini, col_ref_fim = st.columns(2, gap="large")
            with col_ref_ini:
                st.selectbox(
                    "⏱️ Referencia de tempo (Iniciar)",
                    ["Segundos", "Minutos", "Horas", "Velas"],
                    key="referencia_tempo_pausas",
                )
            with col_ref_fim:
                st.selectbox(
                    "⏱️ Referencia de tempo (Finalizar)",
                    ["Nao usar", "Segundos", "Minutos", "Horas", "Velas"],
                    key="final_referencia_tempo_pausas",
                )

            st.divider()

            referencia_tempo = st.session_state.referencia_tempo_pausas

            st.markdown("<p style='text-align: center; font-weight: 900; margin: 0 0 0.75rem 0;'>Primeira pausa</p>", unsafe_allow_html=True)
            st.markdown("<p class='center-note'>Horario da pausa</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="primeira_pausa_hora", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="primeira_pausa_minuto", label_visibility="collapsed")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="primeira_pausa_hora_passe", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="primeira_pausa_minuto_passe", label_visibility="collapsed")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="final_primeira_pausa_hora", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="final_primeira_pausa_minuto", label_visibility="collapsed")

            st.markdown("<p class='center-note' style='margin-top: 0.75rem;'>Periodo</p>", unsafe_allow_html=True)
            col_p_ini, col_p_fim = st.columns(2, gap="large")
            with col_p_ini:
                st.selectbox("📅 Periodo (Iniciar)", periodos, key="primeira_pausa_periodo")
            with col_p_fim:
                st.selectbox("📅 Periodo (Finalizar)", ["Nao usar", *periodos], key="final_primeira_pausa_periodo")

            st.markdown("<p class='center-note' style='margin-top: 0.75rem;'>Duracao (Unidade: " + str(referencia_tempo) + ")</p>", unsafe_allow_html=True)
            d_ini, d_passe, d_fim = st.columns(3, gap="large")
            with d_ini:
                st.number_input("Duracao", min_value=0, step=1, key="primeira_pausa_duracao")
            with d_passe:
                st.number_input("Duracao", min_value=0, step=1, key="primeira_pausa_duracao_passe")
            with d_fim:
                st.number_input("Duracao", min_value=0, step=1, key="final_primeira_pausa_duracao")

            st.divider()

            st.markdown("<p style='text-align: center; font-weight: 900; margin: 0 0 0.75rem 0;'>Segunda pausa</p>", unsafe_allow_html=True)
            st.markdown("<p class='center-note'>Horario da pausa</p>", unsafe_allow_html=True)
            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="segunda_pausa_hora", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="segunda_pausa_minuto", label_visibility="collapsed")
            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="segunda_pausa_hora_passe", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="segunda_pausa_minuto_passe", label_visibility="collapsed")
            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                h, m = st.columns(2)
                with h:
                    st.caption("Hora")
                    st.selectbox("Hora", horas, key="final_segunda_pausa_hora", label_visibility="collapsed")
                with m:
                    st.caption("Minuto")
                    st.selectbox("Minuto", minutos, key="final_segunda_pausa_minuto", label_visibility="collapsed")

            st.markdown("<p class='center-note' style='margin-top: 0.75rem;'>Periodo</p>", unsafe_allow_html=True)
            col_p_ini, col_p_fim = st.columns(2, gap="large")
            with col_p_ini:
                st.selectbox("📅 Periodo (Iniciar)", periodos, key="segunda_pausa_periodo")
            with col_p_fim:
                st.selectbox("📅 Periodo (Finalizar)", ["Nao usar", *periodos], key="final_segunda_pausa_periodo")

            st.markdown("<p class='center-note' style='margin-top: 0.75rem;'>Duracao (Unidade: " + str(referencia_tempo) + ")</p>", unsafe_allow_html=True)
            d_ini, d_passe, d_fim = st.columns(3, gap="large")
            with d_ini:
                st.number_input("Duracao ", min_value=0, step=1, key="segunda_pausa_duracao")
            with d_passe:
                st.number_input("Duracao ", min_value=0, step=1, key="segunda_pausa_duracao_passe")
            with d_fim:
                st.number_input("Duracao ", min_value=0, step=1, key="final_segunda_pausa_duracao")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 10
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.pausas_operacionais_salvas = True
                st.session_state.etapa = 12
                st.rerun()

if st.session_state.etapa == 12:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>12. AUMENTO CONTRA</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Determine a referencia para aumentos contra</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Ordens tipo limitadas colocadas a partir da entrada para aumento de posicao se a operacao for contra</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_aumento_contra",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_aumento_contra",
                )

            st.divider()
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-weight: 900; margin: 0 0 0.75rem 0;'>Aumentos contra</p>", unsafe_allow_html=True)

            c_ini, c_passe, c_fim = st.columns(3, gap="large")

            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(f"Distancia contra {i}", min_value=0, step=1, key=f"distancia_contra_{i}")
                    with v:
                        st.number_input(f"Volume {i}", min_value=0, step=1, key=f"volume_contra_{i}")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(
                            f"Distancia contra {i}",
                            min_value=0,
                            step=1,
                            key=f"distancia_contra_{i}_passe",
                        )
                    with v:
                        st.number_input(
                            f"Volume {i}",
                            min_value=0,
                            step=1,
                            key=f"volume_contra_{i}_passe",
                        )

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(
                            f"Distancia contra {i}",
                            min_value=0,
                            step=1,
                            key=f"final_distancia_contra_{i}",
                        )
                    with v:
                        st.number_input(
                            f"Volume {i}",
                            min_value=0,
                            step=1,
                            key=f"final_volume_contra_{i}",
                        )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 11
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.aumento_contra_salvo = True
                st.session_state.etapa = 13
                st.rerun()

if st.session_state.etapa == 13:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>13. AUMENTO A FAVOR</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Determine a referencia para aumentos a favor</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Ordens pendentes tipo gatilhos colocadas a partir da entrada para aumento de posicao se a operacao for a favor</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_aumento_favor",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_aumento_favor",
                )

            st.divider()
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-weight: 900; margin: 0 0 0.75rem 0;'>Aumentos a favor</p>", unsafe_allow_html=True)

            c_ini, c_passe, c_fim = st.columns(3, gap="large")

            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(f"Distancia a favor {i}", min_value=0, step=1, key=f"distancia_favor_{i}")
                    with v:
                        st.number_input(f"Volume {i}", min_value=0, step=1, key=f"volume_favor_{i}")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(
                            f"Distancia a favor {i}",
                            min_value=0,
                            step=1,
                            key=f"distancia_favor_{i}_passe",
                        )
                    with v:
                        st.number_input(
                            f"Volume {i}",
                            min_value=0,
                            step=1,
                            key=f"volume_favor_{i}_passe",
                        )

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                for i in range(1, 6):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(
                            f"Distancia a favor {i}",
                            min_value=0,
                            step=1,
                            key=f"final_distancia_favor_{i}",
                        )
                    with v:
                        st.number_input(
                            f"Volume {i}",
                            min_value=0,
                            step=1,
                            key=f"final_volume_favor_{i}",
                        )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 12
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.aumento_favor_salvo = True
                st.session_state.etapa = 14
                st.rerun()

if st.session_state.etapa == 14:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>14. SAIDAS PARCIAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Determine a referencia para a distancia das parciais</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Distancias positivas serao ordens limites no ganho e negativas, ordens gatilhos no loss</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_saidas_parciais",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_saidas_parciais",
                )

            st.divider()
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-weight: 900; margin: 0 0 0.75rem 0;'>Saidas parciais</p>", unsafe_allow_html=True)

            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                for i in range(1, 5):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(f"Distancia parcial {i}", step=1, key=f"distancia_parcial_{i}")
                    with v:
                        st.number_input(f"Volume {i}", min_value=0, step=1, key=f"volume_parcial_{i}")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                for i in range(1, 5):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(f"Distancia parcial {i}", step=1, key=f"distancia_parcial_{i}_passe")
                    with v:
                        st.number_input(f"Volume {i}", min_value=0, step=1, key=f"volume_parcial_{i}_passe")

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                for i in range(1, 5):
                    d, v = st.columns(2)
                    with d:
                        st.number_input(f"Distancia parcial {i}", step=1, key=f"final_distancia_parcial_{i}")
                    with v:
                        st.number_input(f"Volume {i}", min_value=0, step=1, key=f"final_volume_parcial_{i}")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 13
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.saidas_parciais_salvas = True
                st.session_state.etapa = 15
                st.rerun()

if st.session_state.etapa == 15:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>15. GRADIENTE LINEAR</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>Escolha a referencia para distancias dos alvos e ordens do gradiente</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>O gradiente sera recorrente ou limitado a quantidade de ordens definido</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            col_tc_ini, col_tc_fim = st.columns(2, gap="large")
            with col_tc_ini:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Iniciar)",
                    ["Em pontos", "Percentual"],
                    key="tipo_calculo_gradiente_linear",
                )
            with col_tc_fim:
                st.selectbox(
                    "📏 Tipo de calculo da distancia (Finalizar)",
                    ["Nao usar", "Em pontos", "Percentual"],
                    key="final_tipo_calculo_gradiente_linear",
                )

            st.divider()
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            c_ini, c_passe, c_fim = st.columns(3, gap="large")

            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input("Quantidade de niveis", min_value=0, step=1, key="quantidade_niveis_gradiente_linear")
                st.number_input("Distancia dos niveis", min_value=0, step=1, key="distancia_niveis_gradiente_linear")
                st.number_input("Volume das ordens", min_value=0, step=1, key="volume_ordens_gradiente_linear")
                st.number_input("Alvo parcial", min_value=0, step=1, key="alvo_parcial_gradiente_linear")
                st.number_input("Limite de entradas", min_value=0, step=1, key="limite_entradas_gradiente_linear")
                st.number_input("Reposicionar ordem", min_value=0, step=1, key="reposicionar_ordem_gradiente_linear")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("Quantidade de niveis", min_value=0, step=1, key="quantidade_niveis_gradiente_linear_passe")
                st.number_input("Distancia dos niveis", min_value=0, step=1, key="distancia_niveis_gradiente_linear_passe")
                st.number_input("Volume das ordens", min_value=0, step=1, key="volume_ordens_gradiente_linear_passe")
                st.number_input("Alvo parcial", min_value=0, step=1, key="alvo_parcial_gradiente_linear_passe")
                st.number_input("Limite de entradas", min_value=0, step=1, key="limite_entradas_gradiente_linear_passe")
                st.number_input("Reposicionar ordem", min_value=0, step=1, key="reposicionar_ordem_gradiente_linear_passe")

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input("Quantidade de niveis", min_value=0, step=1, key="final_quantidade_niveis_gradiente_linear")
                st.number_input("Distancia dos niveis", min_value=0, step=1, key="final_distancia_niveis_gradiente_linear")
                st.number_input("Volume das ordens", min_value=0, step=1, key="final_volume_ordens_gradiente_linear")
                st.number_input("Alvo parcial", min_value=0, step=1, key="final_alvo_parcial_gradiente_linear")
                st.number_input("Limite de entradas", min_value=0, step=1, key="final_limite_entradas_gradiente_linear")
                st.number_input("Reposicionar ordem", min_value=0, step=1, key="final_reposicionar_ordem_gradiente_linear")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 14
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.gradiente_linear_salvo = True
                st.session_state.etapa = 16
                st.rerun()

if st.session_state.etapa == 16:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>16. FILTRO DE VELA</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p class='center-note'>O tempo grafico da vela filtro nao precisa ser igual ao do grafico corrente</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p class='center-note'>Aplicado sempre antes de iniciar uma nova posicao</p>",
            unsafe_allow_html=True,
        )

        tempos_grafico = [
            "Corrente",
            "1 Minuto (M1)",
            "2 Minutos (M2)",
            "3 Minutos (M3)",
            "4 Minutos (M4)",
            "5 Minutos (M5)",
            "6 Minutos (M6)",
            "10 Minutos (M10)",
            "15 Minutos (M15)",
            "30 Minutos (M30)",
            "1 Hora (H1)",
            "2 Horas (H2)",
            "3 Horas (H3)",
            "4 Horas (H4)",
            "6 Horas (H6)",
            "8 Horas (H8)",
            "12 Horas (H12)",
            "1 Dia (D1)",
            "1 Semana (W1)",
            "1 Mes (MN1)",
        ]

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            col_t_ini, col_t_fim = st.columns(2, gap="large")
            with col_t_ini:
                st.selectbox("🕒 Tempo grafico da vela (Iniciar)", tempos_grafico, key="tempo_grafico_vela_filtro")
            with col_t_fim:
                st.selectbox(
                    "🕒 Tempo grafico da vela (Finalizar)",
                    ["Nao usar", *tempos_grafico],
                    key="final_tempo_grafico_vela_filtro",
                )

            st.divider()

            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>", unsafe_allow_html=True)
                st.number_input("Tamanho minimo da vela", min_value=0, step=1, key="tamanho_minimo_vela_filtro")
                st.number_input("Tamanho maximo da vela", min_value=0, step=1, key="tamanho_maximo_vela_filtro")
                st.number_input("Minimo do corpo da vela", min_value=0, step=1, key="minimo_corpo_vela_filtro")
                st.number_input("Maximo do corpo da vela", min_value=0, step=1, key="maximo_corpo_vela_filtro")

            with c_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("Tamanho minimo da vela", min_value=0, step=1, key="tamanho_minimo_vela_filtro_passe")
                st.number_input("Tamanho maximo da vela", min_value=0, step=1, key="tamanho_maximo_vela_filtro_passe")
                st.number_input("Minimo do corpo da vela", min_value=0, step=1, key="minimo_corpo_vela_filtro_passe")
                st.number_input("Maximo do corpo da vela", min_value=0, step=1, key="maximo_corpo_vela_filtro_passe")

            with c_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>", unsafe_allow_html=True)
                st.number_input("Tamanho minimo da vela", min_value=0, step=1, key="final_tamanho_minimo_vela_filtro")
                st.number_input("Tamanho maximo da vela", min_value=0, step=1, key="final_tamanho_maximo_vela_filtro")
                st.number_input("Minimo do corpo da vela", min_value=0, step=1, key="final_minimo_corpo_vela_filtro")
                st.number_input("Maximo do corpo da vela", min_value=0, step=1, key="final_maximo_corpo_vela_filtro")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 15
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.vela_filtro_salvo = True
                st.session_state.etapa = 17
                st.rerun()

if st.session_state.etapa == 17:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>17. SINAIS PRONTOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Podera selecionar quais estrategias desejar ou combina-las para usar para sinais de entrada e/ou saida</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<h4 style='text-align: center;'>📊 CANAL DE BANDAS</h4>", unsafe_allow_html=True)

            cb_c1, cb_c2 = st.columns(2, gap="large")
            with cb_c1:
                st.selectbox(
                    "📊 Indicador",
                    [
                        "Nao usar",
                        "Bandas de Bollinger",
                        "Envelopes",
                        "Keltner",
                        "Dochian",
                        "Canal ATR",
                    ],
                    key="canal_bandas_indicador",
                )
            with cb_c2:
                st.selectbox(
                    "🟢 Entrada",
                    [
                        "Nao usar",
                        "Fechou fora",
                        "Fechou dentro e saiu",
                        "Fechou dentro e fechou fora",
                        "Fechou fora e voltou",
                        "Fechou fora e fechou dentro",
                        "Estando fora",
                    ],
                    key="canal_bandas_entrada",
                )

            cb_c3, cb_c4 = st.columns(2, gap="large")
            with cb_c3:
                st.selectbox(
                    "🧭 Sentido",
                    ["Tendencia", "Contra Tendencia"],
                    key="canal_bandas_sentido",
                )
            with cb_c4:
                st.selectbox(
                    "🔴 Saida",
                    [
                        "Nao usar",
                        "Cruzar o centro",
                        "Cruzar o centro e fechar",
                        "Cruzar banda oposta",
                        "Cruzar oposta e fechar",
                    ],
                    key="canal_bandas_saida",
                )

            st.divider()
            st.markdown("<h4 style='text-align: center;'>🔀 CRUZAMENTO DE SINAIS</h4>", unsafe_allow_html=True)

            cr_c1, cr_c2 = st.columns(2, gap="large")
            with cr_c1:
                st.selectbox(
                    "⚡ Sinal rapido",
                    [
                        "Nao usar",
                        "Fechamento da vela",
                        "Abertura da vela",
                        "Maxima da vela",
                        "Minima da vela",
                        "Media movel",
                        "Vidya",
                        "Dema",
                        "Tema",
                        "Frama",
                    ],
                    key="cruzamento_sinal_rapido",
                )
            with cr_c2:
                st.selectbox(
                    "🐢 Sinal lento",
                    [
                        "Nao usar",
                        "Fechamento da vela",
                        "Abertura da vela",
                        "Maxima da vela",
                        "Minima da vela",
                        "Media movel",
                        "Vidya",
                        "Dema",
                        "Tema",
                        "Frama",
                    ],
                    key="cruzamento_sinal_lento",
                )

            cr_c3, cr_c4 = st.columns(2, gap="large")
            with cr_c3:
                st.selectbox(
                    "🟢 Entrada",
                    ["Nao usar", "Cruzamento", "Cruzamento e fechando"],
                    key="cruzamento_entrada",
                )
            with cr_c4:
                st.selectbox(
                    "🧭 Sentido",
                    ["Tendencia", "Contra Tendencia"],
                    key="cruzamento_sentido",
                )

            cr_c5, cr_c6 = st.columns(2, gap="large")
            with cr_c5:
                st.selectbox(
                    "🔴 Saida",
                    ["Nao usar", "Cruzamento oposto", "Cruzar oposto e fechar"],
                    key="cruzamento_saida",
                )
            with cr_c6:
                st.empty()

            st.divider()
            st.markdown("<h4 style='text-align: center;'>📈 SOBRE COMPRADO / VENDIDO</h4>", unsafe_allow_html=True)

            sc_c1, sc_c2 = st.columns(2, gap="large")
            with sc_c1:
                st.selectbox(
                    "📊 Indicador",
                    [
                        "Nao usar",
                        "MACD",
                        "Estocastico",
                        "RSI",
                        "Money Flow Index (MFI)",
                        "Bears Power",
                        "Bulls Power",
                        "Chaikin Oscilador",
                        "Accelerator Oscilador",
                        "Awesome Oscilador",
                        "Commodity Channel Index (CCI)",
                        "DeMarker",
                        "Regressao",
                        "Afastamento da media",
                        "Desvio medio",
                    ],
                    key="sobrecompra_venda_indicador",
                )
            with sc_c2:
                st.selectbox(
                    "🟢 Entrada",
                    [
                        "Nao usar",
                        "Fechou fora",
                        "Fechou dentro e saiu",
                        "Fechou dentro e fechou fora",
                        "Fechou fora e voltou",
                        "Fechou fora e fechou dentro",
                        "Estando fora",
                    ],
                    key="sobrecompra_venda_entrada",
                )

            c_ini, c_passe, c_fim = st.columns(3, gap="large")
            with c_ini:
                st.markdown(
                    "<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Inicial</p>",
                    unsafe_allow_html=True,
                )
                st.number_input(
                    "📈 Sobrecompra",
                    min_value=0,
                    step=1,
                    key="sobrecompra_nivel",
                )
                st.number_input(
                    "📉 Sobrevenda",
                    min_value=0,
                    step=1,
                    key="sobrevenda_nivel",
                )

            with c_passe:
                st.markdown(
                    "<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>",
                    unsafe_allow_html=True,
                )
                st.number_input(
                    "📈 Sobrecompra",
                    min_value=0,
                    step=1,
                    key="sobrecompra_nivel_passe",
                )
                st.number_input(
                    "📉 Sobrevenda",
                    min_value=0,
                    step=1,
                    key="sobrevenda_nivel_passe",
                )

            with c_fim:
                st.markdown(
                    "<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Final</p>",
                    unsafe_allow_html=True,
                )
                st.number_input(
                    "📈 Sobrecompra",
                    min_value=0,
                    step=1,
                    key="final_sobrecompra_nivel",
                )
                st.number_input(
                    "📉 Sobrevenda",
                    min_value=0,
                    step=1,
                    key="final_sobrevenda_nivel",
                )

            sc_c3, sc_c4 = st.columns(2, gap="large")
            with sc_c3:
                st.selectbox(
                    "🧭 Sentido",
                    ["Tendencia", "Contra Tendencia"],
                    key="sobrecompra_venda_sentido",
                )
            with sc_c4:
                st.selectbox(
                    "🔴 Saida",
                    [
                        "Nao usar",
                        "Cruzar o centro",
                        "Cruzar o centro e fechar",
                        "Cruzar banda oposta",
                        "Cruzar oposta e fechar",
                    ],
                    key="sobrecompra_venda_saida",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 16
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.sinais_prontos_salvo = True
                st.session_state.etapa = 19
                st.rerun()

if st.session_state.etapa == 19:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>19. ESCOLHER INDICADORES</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Você poderá selecionar até 4 indicadores para utilizar como sinais e/ou filtros de entrada e/ou saída</p>",
            unsafe_allow_html=True,
        )

        opcoes_indicadores = [
            "Não usar",
            "***Externo",
            "**Keltner",
            "**Dochian",
            "**Regressão",
            "**Afastamento da média",
            "**Desvio Médio",
            "**Canal ATR",
            "Média Móvel",
            "Bandas de Bollinger",
            "MACD",
            "Envelopes",
            "Estocástico",
            "Relative Strength Index (RSI)",
            "Desvio Padrão",
            "Volume",
            "Average True Range (ATR)",
            "Parabolic SAR",
            "Fractal",
            "On Balance Volume (OBV)",
            "Acumulação/Distribuição (A/D)",
            "Money Flow Index (MFI)",
            "Vidya",
            "Dema",
            "Tema",
            "Frama",
            "Trix",
            "Bears Power",
            "Bulls Power",
            "Chaikin Oscilador",
            "Accelerator Oscilador",
            "Awesome Oscilador",
            "Commodity Channel Index (CCI)",
            "DeMarker",
            "Alligator",
            "Nuvem de Ichimoku",
            "Average Directional Index (ADX)",
            "ADX Welles Wilder",
            "Gator Oscilador",
            "Williams Percent Range (WPR)",
            "Market Facilitation Index",
            "Momentum",
            "Relative Vigor Index (RVI)",
        ]

        with st.container(border=True):
            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.selectbox("🧩 Indicador [1]", opcoes_indicadores, key="indicador_escolha_1")
            with c2:
                st.selectbox("🧩 Indicador [2]", opcoes_indicadores, key="indicador_escolha_2")

            c3, c4 = st.columns(2, gap="large")
            with c3:
                st.selectbox("🧩 Indicador [3]", opcoes_indicadores, key="indicador_escolha_3")
            with c4:
                st.selectbox("🧩 Indicador [4]", opcoes_indicadores, key="indicador_escolha_4")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 17
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.escolher_indicadores_salvo = True
                st.session_state.etapa = 21
                st.rerun()

        if st.session_state.escolher_indicadores_salvo:
            st.success("Indicadores salvos.")
if st.session_state.etapa == 21:
    st.markdown("<h3 style='text-align: center;'>🟢 21. SINAIS ENTRADA COMPRA</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.75;'>Página 1/1</p>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align: center;'>No modo de edição avançado, poderá multiplicar, dividir, somar ou subtrair os valores de referência</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>⚙️ Configurações gerais</h4>", unsafe_allow_html=True)

        g1, g2, g3 = st.columns(3, gap="large")
        with g1:
            st.selectbox("⚙️ Modo de edição", ["Avançado", "Básico"], key="sec_modo_edicao")
        with g2:
            st.selectbox("🕯️ Tipo de vela", ["Completas", "Simplificadas"], key="sec_tipo_vela")
        with g3:
            st.selectbox(
                "🧩 Estratégia",
                ["Entrada compra (1)", "Entrada compra (2)", "Entrada compra (3)"],
                key="sec_estrategia",
            )

        st.markdown(
            "<p style='text-align: center;'>Com a vela no modo completo, poderá selecionar qualquer vela do histórico</p>",
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown("<h4 style='text-align: center;'>🧠 Regras condicionais</h4>", unsafe_allow_html=True)

        opcoes_operador_logico = ["SE", "E", "OU", "E SE", "OU SE", "E Também", "OU Também"]
        opcoes_referencia = [
            "Não usar",
            "Valor absoluto",
            "Valor em pontos",
            "Preço de entrada",
            "Preço Médio",
            "Preço Atual",
            "Fechamento da vela",
            "Abertura da vela",
            "Máxima da vela",
            "Mínima da vela",
            "Fechamento do dia",
            "Abertura do dia",
            "Máxima do dia",
            "Mínima do dia",
            "Tamanho da vela",
            "Corpo da vela",
            "Empty Value",
        ]
        opcoes_vela = ["Vela atual", "Vela anterior", "Penúltima vela", "Anti Penúltima"]
        opcoes_operador_comp = [
            "Maior que",
            "Menor que",
            "Maior ou igual que",
            "Menor ou igual que",
            "Igual que",
            "Diferente de",
            "Cruzar p/ cima de",
            "Cruzar p/ baixo de",
            "Cruzar & fechar acima de",
            "Cruzar & fechar abaixo de",
        ]

        h1, h2, h3, h4, h5, h6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3], gap="small")
        with h1:
            st.caption("🔗 Lógico")
        with h2:
            st.caption("⬅️ Ref esq.")
        with h3:
            st.caption("🕯️ Vela esq.")
        with h4:
            st.caption("⚖️ Comp.")
        with h5:
            st.caption("➡️ Ref dir.")
        with h6:
            st.caption("🕯️ Vela dir.")

        for i in range(1, 6):
            c1, c2, c3, c4, c5, c6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3], gap="small")
            with c1:
                st.selectbox(
                    f"Operador lógico {i}",
                    opcoes_operador_logico,
                    key=f"sec_regra_{i}_operador_logico",
                    label_visibility="collapsed",
                )
            with c2:
                st.selectbox(
                    f"Referência esquerda {i}",
                    opcoes_referencia,
                    key=f"sec_regra_{i}_ref_esquerda",
                    label_visibility="collapsed",
                )
            with c3:
                st.selectbox(
                    f"Vela esquerda {i}",
                    opcoes_vela,
                    key=f"sec_regra_{i}_vela_esquerda",
                    label_visibility="collapsed",
                )
            with c4:
                st.selectbox(
                    f"Operador de comparação {i}",
                    opcoes_operador_comp,
                    key=f"sec_regra_{i}_operador_comp",
                    label_visibility="collapsed",
                )
            with c5:
                st.selectbox(
                    f"Referência direita {i}",
                    opcoes_referencia,
                    key=f"sec_regra_{i}_ref_direita",
                    label_visibility="collapsed",
                )
            with c6:
                st.selectbox(
                    f"Vela direita {i}",
                    opcoes_vela,
                    key=f"sec_regra_{i}_vela_direita",
                    label_visibility="collapsed",
                )

        st.info(
            "As 5 linhas são cópias exatas da primeira. A lógica é condicional sequencial, usando operadores (SE, E, OU, etc.)."
        )

    nav_esq, nav_dir = st.columns(2)
    with nav_esq:
        if st.button("Voltar", use_container_width=True):
            st.session_state.etapa = 19
            st.rerun()
    with nav_dir:
        if st.button("Salvar", use_container_width=True):
            st.session_state.sinais_entrada_compra_salvo = True
            st.session_state.etapa = 22
            st.rerun()

    if st.session_state.sinais_entrada_compra_salvo:
        st.success("Configurações de sinais de entrada (compra) salvas.")

if st.session_state.etapa == 22:
    st.markdown("<h3 style='text-align: center;'>🔴 22. SINAIS ENTRADA VENDA</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.75;'>Página 1/1</p>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align: center;'>No modo de edição básico, tem 4 opções de velas de referência</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>⚙️ Configurações gerais</h4>", unsafe_allow_html=True)

        g1, g2, g3 = st.columns(3, gap="large")
        with g1:
            st.selectbox("⚙️ Modo de edição", ["Avançado", "Básico"], key="sev_modo_edicao")
        with g2:
            st.selectbox("🕯️ Tipo de vela", ["Completas", "Simplificadas"], key="sev_tipo_vela")
        with g3:
            st.selectbox(
                "🧩 Estratégia",
                ["Entrada venda (1)", "Entrada venda (2)", "Entrada venda (3)"],
                key="sev_estrategia",
            )

        st.markdown(
            "<p style='text-align: center;'>Se deixar \"Não usar\" em uma das duas opções possíveis de cada linha, a linha será desconsiderada dos sinais</p>",
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown("<h4 style='text-align: center;'>🧠 Regras condicionais</h4>", unsafe_allow_html=True)

        opcoes_operador_logico = ["SE", "E", "OU", "E SE", "OU SE", "E Também", "OU Também"]
        opcoes_referencia = [
            "Não usar",
            "Valor absoluto",
            "Valor em pontos",
            "Preço de entrada",
            "Preço Médio",
            "Preço Atual",
            "Fechamento da vela",
            "Abertura da vela",
            "Máxima da vela",
            "Mínima da vela",
            "Fechamento do dia",
            "Abertura do dia",
            "Máxima do dia",
            "Mínima do dia",
            "Tamanho da vela",
            "Corpo da vela",
            "Empty Value",
        ]
        opcoes_vela = ["Vela atual", "Vela anterior", "Penúltima vela", "Anti Penúltima"]
        opcoes_operador_comp = [
            "Maior que",
            "Menor que",
            "Maior ou igual que",
            "Menor ou igual que",
            "Igual que",
            "Diferente de",
            "Cruzar p/ cima de",
            "Cruzar p/ baixo de",
            "Cruzar & fechar acima de",
            "Cruzar & fechar abaixo de",
        ]

        h1, h2, h3, h4, h5, h6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3], gap="small")
        with h1:
            st.caption("🔗 Lógico")
        with h2:
            st.caption("⬅️ Ref esq.")
        with h3:
            st.caption("🕯️ Vela esq.")
        with h4:
            st.caption("⚖️ Comp.")
        with h5:
            st.caption("➡️ Ref dir.")
        with h6:
            st.caption("🕯️ Vela dir.")

        for i in range(1, 6):
            c1, c2, c3, c4, c5, c6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3], gap="small")
            with c1:
                st.selectbox(
                    f"Operador lógico {i}",
                    opcoes_operador_logico,
                    key=f"sev_regra_{i}_operador_logico",
                    label_visibility="collapsed",
                )
            with c2:
                st.selectbox(
                    f"Referência esquerda {i}",
                    opcoes_referencia,
                    key=f"sev_regra_{i}_ref_esquerda",
                    label_visibility="collapsed",
                )
            with c3:
                st.selectbox(
                    f"Vela esquerda {i}",
                    opcoes_vela,
                    key=f"sev_regra_{i}_vela_esquerda",
                    label_visibility="collapsed",
                )
            with c4:
                st.selectbox(
                    f"Operador de comparação {i}",
                    opcoes_operador_comp,
                    key=f"sev_regra_{i}_operador_comp",
                    label_visibility="collapsed",
                )
            with c5:
                st.selectbox(
                    f"Referência direita {i}",
                    opcoes_referencia,
                    key=f"sev_regra_{i}_ref_direita",
                    label_visibility="collapsed",
                )
            with c6:
                st.selectbox(
                    f"Vela direita {i}",
                    opcoes_vela,
                    key=f"sev_regra_{i}_vela_direita",
                    label_visibility="collapsed",
                )

        st.info(
            "As 5 linhas são cópias exatas da primeira. A lógica é condicional sequencial, usando operadores (SE, E, OU, etc.)."
        )

    nav_esq, nav_dir = st.columns(2)
    with nav_esq:
        if st.button("Voltar", use_container_width=True):
            st.session_state.etapa = 21
            st.rerun()
    with nav_dir:
        if st.button("Salvar", use_container_width=True):
            st.session_state.sinais_entrada_venda_salvo = True
            st.session_state.etapa = 23
            st.rerun()

    if st.session_state.sinais_entrada_venda_salvo:
        st.success("Configurações de sinais de entrada (venda) salvas.")

if st.session_state.etapa == 23:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>23. LIMITES DO ROBÔ</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Gerencie limite de ganho e perda para proteger sua conta bem como o cálculo de referência</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            st.markdown("<h4 style='text-align: center;'>Referências das metas</h4>", unsafe_allow_html=True)
            r1, r2 = st.columns(2, gap="large")
            with r1:
                st.selectbox(
                    "📚 Histórico (Iniciar)",
                    ["Desabilitado", "Diário", "Semanal", "Mensal"],
                    key="limites_robo_historico",
                )
            with r2:
                st.selectbox(
                    "📚 Histórico (Finalizar)",
                    ["Nao usar", "Desabilitado", "Diário", "Semanal", "Mensal"],
                    key="final_limites_robo_historico",
                )

            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.selectbox(
                    "📏 Cálculo (Iniciar)",
                    ["Financeiro", "Percentual"],
                    key="limites_robo_calculo",
                )
            with c2:
                st.selectbox(
                    "📏 Cálculo (Finalizar)",
                    ["Nao usar", "Financeiro", "Percentual"],
                    key="final_limites_robo_calculo",
                )

            st.divider()
            st.markdown("<h4 style='text-align: center;'>Limite de operações</h4>", unsafe_allow_html=True)

            l_ini, l_passe, l_fim = st.columns(3, gap="large")
            with l_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input("Vencedoras", min_value=0, step=1, key="limites_robo_vencedoras")
                st.number_input("Perdedoras", min_value=0, step=1, key="limites_robo_perdedoras")
                st.number_input("Limite total", min_value=0, step=1, key="limites_robo_limite_total")
            with l_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("Vencedoras", min_value=0, step=1, key="limites_robo_vencedoras_passe")
                st.number_input("Perdedoras", min_value=0, step=1, key="limites_robo_perdedoras_passe")
                st.number_input("Limite total", min_value=0, step=1, key="limites_robo_limite_total_passe")
            with l_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input("Vencedoras", min_value=0, step=1, key="final_limites_robo_vencedoras")
                st.number_input("Perdedoras", min_value=0, step=1, key="final_limites_robo_perdedoras")
                st.number_input("Limite total", min_value=0, step=1, key="final_limites_robo_limite_total")

            st.divider()
            st.markdown("<h4 style='text-align: center;'>Metas financeiras e controle de encerramento</h4>", unsafe_allow_html=True)
            st.markdown(
                "<p style='text-align: center;'>A referência equivale a moeda base da sua conta na corretora</p>",
                unsafe_allow_html=True,
            )

            m_ini, m_passe, m_fim = st.columns(3, gap="large")
            with m_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="limites_robo_meta_ganho")
                st.number_input("Limite de perda", min_value=0, step=1, key="limites_robo_limite_perda")
                st.number_input("Rebaixamento", min_value=0, step=1, key="limites_robo_rebaixamento")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="limites_robo_gatilho_rebaixamento")
                st.number_input("Recuperação", min_value=0, step=1, key="limites_robo_recuperacao")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="limites_robo_gatilho_recuperacao")
            with m_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="limites_robo_meta_ganho_passe")
                st.number_input("Limite de perda", min_value=0, step=1, key="limites_robo_limite_perda_passe")
                st.number_input("Rebaixamento", min_value=0, step=1, key="limites_robo_rebaixamento_passe")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="limites_robo_gatilho_rebaixamento_passe")
                st.number_input("Recuperação", min_value=0, step=1, key="limites_robo_recuperacao_passe")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="limites_robo_gatilho_recuperacao_passe")
            with m_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="final_limites_robo_meta_ganho")
                st.number_input("Limite de perda", min_value=0, step=1, key="final_limites_robo_limite_perda")
                st.number_input("Rebaixamento", min_value=0, step=1, key="final_limites_robo_rebaixamento")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="final_limites_robo_gatilho_rebaixamento")
                st.number_input("Recuperação", min_value=0, step=1, key="final_limites_robo_recuperacao")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="final_limites_robo_gatilho_recuperacao")

            st.divider()
            e1, e2 = st.columns(2, gap="large")
            with e1:
                st.selectbox(
                    "🧭 Encerrar no trade (Meta de ganho) - Iniciar",
                    ["Sim", "Não"],
                    key="limites_robo_encerrar_meta_ganho",
                )
            with e2:
                st.selectbox(
                    "🧭 Encerrar no trade (Meta de ganho) - Finalizar",
                    ["Nao usar", "Sim", "Não"],
                    key="final_limites_robo_encerrar_meta_ganho",
                )

            e3, e4 = st.columns(2, gap="large")
            with e3:
                st.selectbox(
                    "🧭 Encerrar no trade (Limite de perda) - Iniciar",
                    ["Sim", "Não"],
                    key="limites_robo_encerrar_limite_perda",
                )
            with e4:
                st.selectbox(
                    "🧭 Encerrar no trade (Limite de perda) - Finalizar",
                    ["Nao usar", "Sim", "Não"],
                    key="final_limites_robo_encerrar_limite_perda",
                )

            e5, e6 = st.columns(2, gap="large")
            with e5:
                st.selectbox(
                    "🧭 Encerrar no trade (Rebaixamento) - Iniciar",
                    ["Não", "Sim"],
                    key="limites_robo_encerrar_rebaixamento",
                )
            with e6:
                st.selectbox(
                    "🧭 Encerrar no trade (Rebaixamento) - Finalizar",
                    ["Nao usar", "Não", "Sim"],
                    key="final_limites_robo_encerrar_rebaixamento",
                )

            e7, e8 = st.columns(2, gap="large")
            with e7:
                st.selectbox(
                    "🧭 Encerrar no trade (Recuperação) - Iniciar",
                    ["Não", "Sim"],
                    key="limites_robo_encerrar_recuperacao",
                )
            with e8:
                st.selectbox(
                    "🧭 Encerrar no trade (Recuperação) - Finalizar",
                    ["Nao usar", "Não", "Sim"],
                    key="final_limites_robo_encerrar_recuperacao",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 22
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.limites_robo_salvo = True
                st.session_state.etapa = 24
                st.rerun()

        if st.session_state.limites_robo_salvo:
            st.success("Limites do robô salvos.")

if st.session_state.etapa == 24:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>24. PERMISSÕES / GESTÃO DA CONTA</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Gerencie toda a conta combinando com as permissões do robô</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)

            st.markdown("<h4 style='text-align: center;'>Referências das metas (nível conta)</h4>", unsafe_allow_html=True)

            r1, r2 = st.columns(2, gap="large")
            with r1:
                st.selectbox(
                    "📚 Histórico (Iniciar)",
                    ["Desabilitado", "Diário", "Semanal", "Mensal"],
                    key="conta_historico",
                )
            with r2:
                st.selectbox(
                    "📚 Histórico (Finalizar)",
                    ["Nao usar", "Desabilitado", "Diário", "Semanal", "Mensal"],
                    key="final_conta_historico",
                )

            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.selectbox(
                    "📏 Cálculo (Iniciar)",
                    ["Financeiro", "Percentual"],
                    key="conta_calculo",
                )
            with c2:
                st.selectbox(
                    "📏 Cálculo (Finalizar)",
                    ["Nao usar", "Financeiro", "Percentual"],
                    key="final_conta_calculo",
                )

            st.divider()
            st.markdown("<h4 style='text-align: center;'>Seleção de filtros</h4>", unsafe_allow_html=True)

            f1, f2 = st.columns(2, gap="large")
            with f1:
                st.selectbox("🔎 Filtro de ativo (Iniciar)", ["Não", "Sim"], key="conta_filtro_ativo")
            with f2:
                st.selectbox("🔎 Filtro de ativo (Finalizar)", ["Nao usar", "Não", "Sim"], key="final_conta_filtro_ativo")

            f3, f4 = st.columns(2, gap="large")
            with f3:
                st.selectbox("🧹 Excluir manuais (Iniciar)", ["Não", "Sim"], key="conta_excluir_manuais")
            with f4:
                st.selectbox("🧹 Excluir manuais (Finalizar)", ["Nao usar", "Não", "Sim"], key="final_conta_excluir_manuais")

            f5, f6 = st.columns(2, gap="large")
            with f5:
                st.selectbox("🤖 Filtrar robôs (Iniciar)", ["Não", "Sim"], key="conta_filtrar_robos")
            with f6:
                st.selectbox("🤖 Filtrar robôs (Finalizar)", ["Nao usar", "Não", "Sim"], key="final_conta_filtrar_robos")

            st.divider()
            st.markdown("<h4 style='text-align: center;'>Faixa de IDs</h4>", unsafe_allow_html=True)

            id_ini, id_passe, id_fim = st.columns(3, gap="large")
            with id_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input("ID mínimo", min_value=0, step=1, key="conta_id_minimo")
                st.number_input("ID máximo", min_value=0, step=1, key="conta_id_maximo")
            with id_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("ID mínimo", min_value=0, step=1, key="conta_id_minimo_passe")
                st.number_input("ID máximo", min_value=0, step=1, key="conta_id_maximo_passe")
            with id_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input("ID mínimo", min_value=0, step=1, key="final_conta_id_minimo")
                st.number_input("ID máximo", min_value=0, step=1, key="final_conta_id_maximo")

            st.divider()
            st.markdown("<h4 style='text-align: center;'>Metas financeiras (nível conta)</h4>", unsafe_allow_html=True)

            st.markdown(
                "<p style='text-align: center;'>Os dados valem para toda a conta para execução deste robô</p>",
                unsafe_allow_html=True,
            )

            m_ini, m_passe, m_fim = st.columns(3, gap="large")
            with m_ini:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="conta_meta_ganho")
                st.number_input("Limite de perda", min_value=0, step=1, key="conta_limite_perda")
                st.number_input("Rebaixamento", min_value=0, step=1, key="conta_rebaixamento")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="conta_gatilho_rebaixamento")
                st.number_input("Recuperação", min_value=0, step=1, key="conta_recuperacao")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="conta_gatilho_recuperacao")
            with m_passe:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="conta_meta_ganho_passe")
                st.number_input("Limite de perda", min_value=0, step=1, key="conta_limite_perda_passe")
                st.number_input("Rebaixamento", min_value=0, step=1, key="conta_rebaixamento_passe")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="conta_gatilho_rebaixamento_passe")
                st.number_input("Recuperação", min_value=0, step=1, key="conta_recuperacao_passe")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="conta_gatilho_recuperacao_passe")
            with m_fim:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input("Meta de ganho", min_value=0, step=1, key="final_conta_meta_ganho")
                st.number_input("Limite de perda", min_value=0, step=1, key="final_conta_limite_perda")
                st.number_input("Rebaixamento", min_value=0, step=1, key="final_conta_rebaixamento")
                st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="final_conta_gatilho_rebaixamento")
                st.number_input("Recuperação", min_value=0, step=1, key="final_conta_recuperacao")
                st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="final_conta_gatilho_recuperacao")

            st.divider()
            e1, e2 = st.columns(2, gap="large")
            with e1:
                st.selectbox(
                    "🧭 Encerrar no trade (Meta de ganho) - Iniciar",
                    ["Sim", "Não"],
                    key="conta_encerrar_meta_ganho",
                )
            with e2:
                st.selectbox(
                    "🧭 Encerrar no trade (Meta de ganho) - Finalizar",
                    ["Nao usar", "Sim", "Não"],
                    key="final_conta_encerrar_meta_ganho",
                )

            e3, e4 = st.columns(2, gap="large")
            with e3:
                st.selectbox(
                    "🧭 Encerrar no trade (Limite de perda) - Iniciar",
                    ["Sim", "Não"],
                    key="conta_encerrar_limite_perda",
                )
            with e4:
                st.selectbox(
                    "🧭 Encerrar no trade (Limite de perda) - Finalizar",
                    ["Nao usar", "Sim", "Não"],
                    key="final_conta_encerrar_limite_perda",
                )

            e5, e6 = st.columns(2, gap="large")
            with e5:
                st.selectbox(
                    "🧭 Encerrar no trade (Rebaixamento) - Iniciar",
                    ["Não", "Sim"],
                    key="conta_encerrar_rebaixamento",
                )
            with e6:
                st.selectbox(
                    "🧭 Encerrar no trade (Rebaixamento) - Finalizar",
                    ["Nao usar", "Não", "Sim"],
                    key="final_conta_encerrar_rebaixamento",
                )

            e7, e8 = st.columns(2, gap="large")
            with e7:
                st.selectbox(
                    "🧭 Encerrar no trade (Recuperação) - Iniciar",
                    ["Não", "Sim"],
                    key="conta_encerrar_recuperacao",
                )
            with e8:
                st.selectbox(
                    "🧭 Encerrar no trade (Recuperação) - Finalizar",
                    ["Nao usar", "Não", "Sim"],
                    key="final_conta_encerrar_recuperacao",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 23
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.permissoes_gestao_conta_salvo = True
                st.session_state.etapa = 25
                st.rerun()

        if st.session_state.permissoes_gestao_conta_salvo:
            st.success("Permissões / gestão da conta salvas.")

if st.session_state.etapa == 25:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>25. AJUSTES FINAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Selecione algumas confirmações para os ajustes finais</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            opcoes_sim_nao = ["Sim", "Não"]
            opcoes_nao_sim = ["Não", "Sim"]

            a1, a2 = st.columns(2, gap="large")
            with a1:
                st.selectbox(
                    "🧾 Cancelar pendente de entrada se aparecer sinal oposto (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_cancelar_pendente_entrada_sinal_oposto",
                )
            with a2:
                st.selectbox(
                    "🧾 Cancelar pendente de entrada se aparecer sinal oposto (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_cancelar_pendente_entrada_sinal_oposto",
                )

            b1, b2 = st.columns(2, gap="large")
            with b1:
                st.selectbox(
                    "🎯 Reposicionar stoploss no aumento a favor da operação (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_reposicionar_stoploss_aumento_favor",
                )
            with b2:
                st.selectbox(
                    "🎯 Reposicionar stoploss no aumento a favor da operação (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_reposicionar_stoploss_aumento_favor",
                )

            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.selectbox(
                    "🎯 Reposicionar takeprofit no aumento contra a operação (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_reposicionar_takeprofit_aumento_contra",
                )
            with c2:
                st.selectbox(
                    "🎯 Reposicionar takeprofit no aumento contra a operação (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_reposicionar_takeprofit_aumento_contra",
                )

            d1, d2 = st.columns(2, gap="large")
            with d1:
                st.selectbox(
                    "🧠 Movimentar stoploss com base no preço médio (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_movimentar_stoploss_preco_medio",
                )
            with d2:
                st.selectbox(
                    "🧠 Movimentar stoploss com base no preço médio (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_movimentar_stoploss_preco_medio",
                )

            e1, e2 = st.columns(2, gap="large")
            with e1:
                st.selectbox(
                    "🧠 Movimentar takeprofit com base no preço médio (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_movimentar_takeprofit_preco_medio",
                )
            with e2:
                st.selectbox(
                    "🧠 Movimentar takeprofit com base no preço médio (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_movimentar_takeprofit_preco_medio",
                )

            f1, f2 = st.columns(2, gap="large")
            with f1:
                st.selectbox(
                    "📐 Usar preço médio como referência das parciais (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_usar_preco_medio_parciais",
                )
            with f2:
                st.selectbox(
                    "📐 Usar preço médio como referência das parciais (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_usar_preco_medio_parciais",
                )

            g1, g2 = st.columns(2, gap="large")
            with g1:
                st.selectbox(
                    "🚪 Impedir sinal de saída na vela que gerou entrada (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_impedir_saida_vela_entrada",
                )
            with g2:
                st.selectbox(
                    "🚪 Impedir sinal de saída na vela que gerou entrada (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_impedir_saida_vela_entrada",
                )

            h1, h2 = st.columns(2, gap="large")
            with h1:
                st.selectbox(
                    "🚪 Impedir sinal de entrada na vela que gerou saída (Iniciar)",
                    opcoes_sim_nao,
                    key="ajuste_impedir_entrada_vela_saida",
                )
            with h2:
                st.selectbox(
                    "🚪 Impedir sinal de entrada na vela que gerou saída (Finalizar)",
                    ["Nao usar", *opcoes_sim_nao],
                    key="final_ajuste_impedir_entrada_vela_saida",
                )

            i1, i2 = st.columns(2, gap="large")
            with i1:
                st.selectbox(
                    "🔁 Recalcular o preço médio com base nas saídas parciais (Iniciar)",
                    opcoes_nao_sim,
                    key="ajuste_recalcular_preco_medio_saidas_parciais",
                )
            with i2:
                st.selectbox(
                    "🔁 Recalcular o preço médio com base nas saídas parciais (Finalizar)",
                    ["Nao usar", *opcoes_nao_sim],
                    key="final_ajuste_recalcular_preco_medio_saidas_parciais",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 24
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.ajustes_finais_salvo = True
                st.session_state.etapa = 26
                st.rerun()

        if st.session_state.ajustes_finais_salvo:
            st.success("Ajustes finais salvos.")

if st.session_state.etapa == 26:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>26. COMPLEMENTOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Adicione alguns complementos de ordens e sinais</p>",
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            st.markdown("<p class='center-note'>Legenda: 0 = Nao usar</p>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center;'>Complementos de ordens e sinais</h4>", unsafe_allow_html=True)

            opcoes_nao_sim = ["Não", "Sim"]

            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.selectbox(
                    "📤 Enviar ordem para outro ativo (Cross order) - Iniciar",
                    opcoes_nao_sim,
                    key="comp_enviar_ordem_outro_ativo",
                )
            with c2:
                st.selectbox(
                    "📤 Enviar ordem para outro ativo (Cross order) - Finalizar",
                    ["Nao usar", *opcoes_nao_sim],
                    key="final_comp_enviar_ordem_outro_ativo",
                )

            c3, c4 = st.columns(2, gap="large")
            with c3:
                st.selectbox(
                    "🟢 Procurar entrada na vela seguinte à saída - Iniciar",
                    opcoes_nao_sim,
                    key="comp_procurar_entrada_vela_seguinte_saida",
                )
            with c4:
                st.selectbox(
                    "🟢 Procurar entrada na vela seguinte à saída - Finalizar",
                    ["Nao usar", *opcoes_nao_sim],
                    key="final_comp_procurar_entrada_vela_seguinte_saida",
                )

            c5, c6 = st.columns(2, gap="large")
            with c5:
                st.selectbox(
                    "🔴 Procurar saída na vela seguinte à entrada - Iniciar",
                    opcoes_nao_sim,
                    key="comp_procurar_saida_vela_seguinte_entrada",
                )
            with c6:
                st.selectbox(
                    "🔴 Procurar saída na vela seguinte à entrada - Finalizar",
                    ["Nao usar", *opcoes_nao_sim],
                    key="final_comp_procurar_saida_vela_seguinte_entrada",
                )

            st.divider()
            s1, s2, s3 = st.columns(3, gap="large")
            with s1:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟢 Iniciar</p>", unsafe_allow_html=True)
                st.number_input(
                    "Saldo de ajuste para somar com a conta",
                    min_value=0,
                    step=1,
                    key="comp_saldo_ajuste",
                )
            with s2:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🟡 Passe</p>", unsafe_allow_html=True)
                st.number_input(
                    "Saldo de ajuste para somar com a conta",
                    min_value=0,
                    step=1,
                    key="comp_saldo_ajuste_passe",
                )
            with s3:
                st.markdown("<p style='text-align: center; font-weight: 700; margin: 0 0 0.5rem 0;'>🔴 Finalizar</p>", unsafe_allow_html=True)
                st.number_input(
                    "Saldo de ajuste para somar com a conta",
                    min_value=0,
                    step=1,
                    key="final_comp_saldo_ajuste",
                )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 25
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.complementos_salvo = True
                st.session_state.etapa = 27
                st.rerun()

        if st.session_state.complementos_salvo:
            st.success("Complementos salvos.")

if st.session_state.etapa == 27:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>FINALIZAÇÃO</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Selecione alguns adicionais e finalize o processo de criação do seu robô</p>",
            unsafe_allow_html=True,
        )

        st.checkbox(
            "Exibir indicadores ao carregar o expert advisor em um gráfico",
            key="final_exibir_indicadores",
        )
        st.checkbox("Criar painel e boleta no gráfico", key="final_criar_painel_boleta")
        st.checkbox("Criar log do expert no gráfico", key="final_criar_log_expert")
        st.checkbox(
            "Criar etiquetas personalizadas nas ordens",
            key="final_criar_etiquetas_personalizadas",
        )
        st.checkbox(
            "Alterar layout do gráfico (Cores de fundo e candles)",
            key="final_alterar_layout_grafico",
        )

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 26
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.finalizacao_salvo = True

        if st.session_state.finalizacao_salvo:
            st.success("Finalização salva.")
