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

if "config_inicial_salva" not in st.session_state:
    st.session_state.config_inicial_salva = False

if "tempo_grafico_principal" not in st.session_state:
    st.session_state.tempo_grafico_principal = "Corrente"

if "volume_inicial" not in st.session_state:
    st.session_state.volume_inicial = 1

if "spread_maximo" not in st.session_state:
    st.session_state.spread_maximo = 0

if "parametros_execucao_salvos" not in st.session_state:
    st.session_state.parametros_execucao_salvos = False

if "tipo_calculo_distancias" not in st.session_state:
    st.session_state.tipo_calculo_distancias = "Em pontos"

if "ordem_entrada" not in st.session_state:
    st.session_state.ordem_entrada = "A mercado"

if "ordem_saida" not in st.session_state:
    st.session_state.ordem_saida = "A mercado"

if "tipo_ordens_salvas" not in st.session_state:
    st.session_state.tipo_ordens_salvas = False

if "tipo_calculo_alvos" not in st.session_state:
    st.session_state.tipo_calculo_alvos = "Em pontos"

if "usar_stoploss_personalizado" not in st.session_state:
    st.session_state.usar_stoploss_personalizado = "Nao"

if "usar_takeprofit_personalizado" not in st.session_state:
    st.session_state.usar_takeprofit_personalizado = "Nao"

if "alvos_personalizados_salvos" not in st.session_state:
    st.session_state.alvos_personalizados_salvos = False

if "tipo_calculo_stoploss" not in st.session_state:
    st.session_state.tipo_calculo_stoploss = "Em pontos"

if "stoploss_inicial" not in st.session_state:
    st.session_state.stoploss_inicial = 0

if "inicio_break_even_sl" not in st.session_state:
    st.session_state.inicio_break_even_sl = 0

if "distancia_break_even_sl" not in st.session_state:
    st.session_state.distancia_break_even_sl = 0

if "inicio_trailing_stop" not in st.session_state:
    st.session_state.inicio_trailing_stop = 0

if "passo_trailing_stop" not in st.session_state:
    st.session_state.passo_trailing_stop = 0

if "stoploss_salvo" not in st.session_state:
    st.session_state.stoploss_salvo = False

if "tipo_calculo_takeprofit" not in st.session_state:
    st.session_state.tipo_calculo_takeprofit = "Em pontos"

if "takeprofit_inicial" not in st.session_state:
    st.session_state.takeprofit_inicial = 0

if "inicio_break_even_tp" not in st.session_state:
    st.session_state.inicio_break_even_tp = 0

if "distancia_break_even_tp" not in st.session_state:
    st.session_state.distancia_break_even_tp = 0

if "inicio_trailing_profit" not in st.session_state:
    st.session_state.inicio_trailing_profit = 0

if "passo_trailing_profit" not in st.session_state:
    st.session_state.passo_trailing_profit = 0

if "takeprofit_salvo" not in st.session_state:
    st.session_state.takeprofit_salvo = False

if "referencia_tempo_saida" not in st.session_state:
    st.session_state.referencia_tempo_saida = "Segundos"

if "tempo_saida_operacoes_positivas" not in st.session_state:
    st.session_state.tempo_saida_operacoes_positivas = 0

if "saldo_maximo_operacoes_positivas" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_positivas = 0

if "saldo_minimo_operacoes_positivas" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_positivas = 0

if "tempo_saida_operacoes_negativas" not in st.session_state:
    st.session_state.tempo_saida_operacoes_negativas = 0

if "saldo_maximo_operacoes_negativas" not in st.session_state:
    st.session_state.saldo_maximo_operacoes_negativas = 0

if "saldo_minimo_operacoes_negativas" not in st.session_state:
    st.session_state.saldo_minimo_operacoes_negativas = 0

if "saida_temporal_salva" not in st.session_state:
    st.session_state.saida_temporal_salva = False

if "tipo_calculo_gradiente_linear" not in st.session_state:
    st.session_state.tipo_calculo_gradiente_linear = "Em pontos"

if "quantidade_niveis_gradiente_linear" not in st.session_state:
    st.session_state.quantidade_niveis_gradiente_linear = 0

if "distancia_niveis_gradiente_linear" not in st.session_state:
    st.session_state.distancia_niveis_gradiente_linear = 0

if "volume_ordens_gradiente_linear" not in st.session_state:
    st.session_state.volume_ordens_gradiente_linear = 0

if "alvo_parcial_gradiente_linear" not in st.session_state:
    st.session_state.alvo_parcial_gradiente_linear = 0

if "limite_entradas_gradiente_linear" not in st.session_state:
    st.session_state.limite_entradas_gradiente_linear = 0

if "reposicionar_ordem_gradiente_linear" not in st.session_state:
    st.session_state.reposicionar_ordem_gradiente_linear = 0

if "gradiente_linear_salvo" not in st.session_state:
    st.session_state.gradiente_linear_salvo = False

if "tempo_grafico_vela_filtro" not in st.session_state:
    st.session_state.tempo_grafico_vela_filtro = "Corrente"

if "tamanho_minimo_vela_filtro" not in st.session_state:
    st.session_state.tamanho_minimo_vela_filtro = 0

if "tamanho_maximo_vela_filtro" not in st.session_state:
    st.session_state.tamanho_maximo_vela_filtro = 0

if "minimo_corpo_vela_filtro" not in st.session_state:
    st.session_state.minimo_corpo_vela_filtro = 0

if "maximo_corpo_vela_filtro" not in st.session_state:
    st.session_state.maximo_corpo_vela_filtro = 0

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

if "sobrevenda_nivel" not in st.session_state:
    st.session_state.sobrevenda_nivel = 2

if "sobrecompra_venda_sentido" not in st.session_state:
    st.session_state.sobrecompra_venda_sentido = "Tendencia"

if "sobrecompra_venda_saida" not in st.session_state:
    st.session_state.sobrecompra_venda_saida = "Nao usar"

if "sinais_prontos_salvo" not in st.session_state:
    st.session_state.sinais_prontos_salvo = False

if "resumo_validacao_final_salvo" not in st.session_state:
    st.session_state.resumo_validacao_final_salvo = False

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

if "configurar_indicadores_salvo" not in st.session_state:
    st.session_state.configurar_indicadores_salvo = False

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

if "limites_robo_calculo" not in st.session_state:
    st.session_state.limites_robo_calculo = "Financeiro"

if "limites_robo_vencedoras" not in st.session_state:
    st.session_state.limites_robo_vencedoras = 0

if "limites_robo_perdedoras" not in st.session_state:
    st.session_state.limites_robo_perdedoras = 0

if "limites_robo_limite_total" not in st.session_state:
    st.session_state.limites_robo_limite_total = 0

if "limites_robo_meta_ganho" not in st.session_state:
    st.session_state.limites_robo_meta_ganho = 0

if "limites_robo_encerrar_meta_ganho" not in st.session_state:
    st.session_state.limites_robo_encerrar_meta_ganho = "Sim"

if "limites_robo_limite_perda" not in st.session_state:
    st.session_state.limites_robo_limite_perda = 0

if "limites_robo_encerrar_limite_perda" not in st.session_state:
    st.session_state.limites_robo_encerrar_limite_perda = "Sim"

if "limites_robo_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_rebaixamento = 0

if "limites_robo_encerrar_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_encerrar_rebaixamento = "Não"

if "limites_robo_gatilho_rebaixamento" not in st.session_state:
    st.session_state.limites_robo_gatilho_rebaixamento = 0

if "limites_robo_recuperacao" not in st.session_state:
    st.session_state.limites_robo_recuperacao = 0

if "limites_robo_encerrar_recuperacao" not in st.session_state:
    st.session_state.limites_robo_encerrar_recuperacao = "Não"

if "limites_robo_gatilho_recuperacao" not in st.session_state:
    st.session_state.limites_robo_gatilho_recuperacao = 0

if "limites_robo_salvo" not in st.session_state:
    st.session_state.limites_robo_salvo = False

if "conta_historico" not in st.session_state:
    st.session_state.conta_historico = "Desabilitado"

if "conta_calculo" not in st.session_state:
    st.session_state.conta_calculo = "Financeiro"

if "conta_filtro_ativo" not in st.session_state:
    st.session_state.conta_filtro_ativo = "Não"

if "conta_excluir_manuais" not in st.session_state:
    st.session_state.conta_excluir_manuais = "Não"

if "conta_filtrar_robos" not in st.session_state:
    st.session_state.conta_filtrar_robos = "Não"

if "conta_id_minimo" not in st.session_state:
    st.session_state.conta_id_minimo = 0

if "conta_id_maximo" not in st.session_state:
    st.session_state.conta_id_maximo = 0

if "conta_meta_ganho" not in st.session_state:
    st.session_state.conta_meta_ganho = 0

if "conta_encerrar_meta_ganho" not in st.session_state:
    st.session_state.conta_encerrar_meta_ganho = "Sim"

if "conta_limite_perda" not in st.session_state:
    st.session_state.conta_limite_perda = 0

if "conta_encerrar_limite_perda" not in st.session_state:
    st.session_state.conta_encerrar_limite_perda = "Sim"

if "conta_rebaixamento" not in st.session_state:
    st.session_state.conta_rebaixamento = 0

if "conta_encerrar_rebaixamento" not in st.session_state:
    st.session_state.conta_encerrar_rebaixamento = "Não"

if "conta_gatilho_rebaixamento" not in st.session_state:
    st.session_state.conta_gatilho_rebaixamento = 0

if "conta_recuperacao" not in st.session_state:
    st.session_state.conta_recuperacao = 0

if "conta_encerrar_recuperacao" not in st.session_state:
    st.session_state.conta_encerrar_recuperacao = "Não"

if "conta_gatilho_recuperacao" not in st.session_state:
    st.session_state.conta_gatilho_recuperacao = 0

if "permissoes_gestao_conta_salvo" not in st.session_state:
    st.session_state.permissoes_gestao_conta_salvo = False

if "ajuste_cancelar_pendente_entrada_sinal_oposto" not in st.session_state:
    st.session_state.ajuste_cancelar_pendente_entrada_sinal_oposto = "Não"

if "ajuste_reposicionar_stoploss_aumento_favor" not in st.session_state:
    st.session_state.ajuste_reposicionar_stoploss_aumento_favor = "Não"

if "ajuste_reposicionar_takeprofit_aumento_contra" not in st.session_state:
    st.session_state.ajuste_reposicionar_takeprofit_aumento_contra = "Não"

if "ajuste_movimentar_stoploss_preco_medio" not in st.session_state:
    st.session_state.ajuste_movimentar_stoploss_preco_medio = "Não"

if "ajuste_movimentar_takeprofit_preco_medio" not in st.session_state:
    st.session_state.ajuste_movimentar_takeprofit_preco_medio = "Não"

if "ajuste_usar_preco_medio_parciais" not in st.session_state:
    st.session_state.ajuste_usar_preco_medio_parciais = "Não"

if "ajuste_impedir_saida_vela_entrada" not in st.session_state:
    st.session_state.ajuste_impedir_saida_vela_entrada = "Não"

if "ajuste_impedir_entrada_vela_saida" not in st.session_state:
    st.session_state.ajuste_impedir_entrada_vela_saida = "Não"

if "ajuste_recalcular_preco_medio_saidas_parciais" not in st.session_state:
    st.session_state.ajuste_recalcular_preco_medio_saidas_parciais = "Não"

if "ajustes_finais_salvo" not in st.session_state:
    st.session_state.ajustes_finais_salvo = False

if "comp_enviar_ordem_outro_ativo" not in st.session_state:
    st.session_state.comp_enviar_ordem_outro_ativo = "Não"

if "comp_procurar_entrada_vela_seguinte_saida" not in st.session_state:
    st.session_state.comp_procurar_entrada_vela_seguinte_saida = "Não"

if "comp_procurar_saida_vela_seguinte_entrada" not in st.session_state:
    st.session_state.comp_procurar_saida_vela_seguinte_entrada = "Não"

if "comp_saldo_ajuste" not in st.session_state:
    st.session_state.comp_saldo_ajuste = 0

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

if "tempo_para_nova_entrada" not in st.session_state:
    st.session_state.tempo_para_nova_entrada = 0

if "tempo_minimo_posicao" not in st.session_state:
    st.session_state.tempo_minimo_posicao = 0

if "filtro_tempo_salvo" not in st.session_state:
    st.session_state.filtro_tempo_salvo = False

if "zerar_por_horario" not in st.session_state:
    st.session_state.zerar_por_horario = "Nao"

if "hora_inicial_operacoes" not in st.session_state:
    st.session_state.hora_inicial_operacoes = 0

if "minuto_inicial_operacoes" not in st.session_state:
    st.session_state.minuto_inicial_operacoes = 0

if "hora_final_operacoes" not in st.session_state:
    st.session_state.hora_final_operacoes = 0

if "minuto_final_operacoes" not in st.session_state:
    st.session_state.minuto_final_operacoes = 0

if "hora_zerar_operacoes" not in st.session_state:
    st.session_state.hora_zerar_operacoes = 0

if "minuto_zerar_operacoes" not in st.session_state:
    st.session_state.minuto_zerar_operacoes = 0

if "horarios_salvos" not in st.session_state:
    st.session_state.horarios_salvos = False

if "referencia_tempo_pausas" not in st.session_state:
    st.session_state.referencia_tempo_pausas = "Segundos"

if "primeira_pausa_hora" not in st.session_state:
    st.session_state.primeira_pausa_hora = 0

if "primeira_pausa_minuto" not in st.session_state:
    st.session_state.primeira_pausa_minuto = 0

if "primeira_pausa_periodo" not in st.session_state:
    st.session_state.primeira_pausa_periodo = "Diariamente"

if "primeira_pausa_duracao" not in st.session_state:
    st.session_state.primeira_pausa_duracao = 0

if "segunda_pausa_hora" not in st.session_state:
    st.session_state.segunda_pausa_hora = 0

if "segunda_pausa_minuto" not in st.session_state:
    st.session_state.segunda_pausa_minuto = 0

if "segunda_pausa_periodo" not in st.session_state:
    st.session_state.segunda_pausa_periodo = "Diariamente"

if "segunda_pausa_duracao" not in st.session_state:
    st.session_state.segunda_pausa_duracao = 0

if "pausas_operacionais_salvas" not in st.session_state:
    st.session_state.pausas_operacionais_salvas = False

if "tipo_calculo_aumento_contra" not in st.session_state:
    st.session_state.tipo_calculo_aumento_contra = "Em pontos"

if "distancia_contra_1" not in st.session_state:
    st.session_state.distancia_contra_1 = 0

if "volume_contra_1" not in st.session_state:
    st.session_state.volume_contra_1 = 0

if "distancia_contra_2" not in st.session_state:
    st.session_state.distancia_contra_2 = 0

if "volume_contra_2" not in st.session_state:
    st.session_state.volume_contra_2 = 0

if "distancia_contra_3" not in st.session_state:
    st.session_state.distancia_contra_3 = 0

if "volume_contra_3" not in st.session_state:
    st.session_state.volume_contra_3 = 0

if "distancia_contra_4" not in st.session_state:
    st.session_state.distancia_contra_4 = 0

if "volume_contra_4" not in st.session_state:
    st.session_state.volume_contra_4 = 0

if "distancia_contra_5" not in st.session_state:
    st.session_state.distancia_contra_5 = 0

if "volume_contra_5" not in st.session_state:
    st.session_state.volume_contra_5 = 0

if "aumento_contra_salvo" not in st.session_state:
    st.session_state.aumento_contra_salvo = False

if "tipo_calculo_aumento_favor" not in st.session_state:
    st.session_state.tipo_calculo_aumento_favor = "Em pontos"

if "distancia_favor_1" not in st.session_state:
    st.session_state.distancia_favor_1 = 0

if "volume_favor_1" not in st.session_state:
    st.session_state.volume_favor_1 = 0

if "distancia_favor_2" not in st.session_state:
    st.session_state.distancia_favor_2 = 0

if "volume_favor_2" not in st.session_state:
    st.session_state.volume_favor_2 = 0

if "distancia_favor_3" not in st.session_state:
    st.session_state.distancia_favor_3 = 0

if "volume_favor_3" not in st.session_state:
    st.session_state.volume_favor_3 = 0

if "distancia_favor_4" not in st.session_state:
    st.session_state.distancia_favor_4 = 0

if "volume_favor_4" not in st.session_state:
    st.session_state.volume_favor_4 = 0

if "distancia_favor_5" not in st.session_state:
    st.session_state.distancia_favor_5 = 0

if "volume_favor_5" not in st.session_state:
    st.session_state.volume_favor_5 = 0

if "aumento_favor_salvo" not in st.session_state:
    st.session_state.aumento_favor_salvo = False

if "tipo_calculo_saidas_parciais" not in st.session_state:
    st.session_state.tipo_calculo_saidas_parciais = "Em pontos"

if "distancia_parcial_1" not in st.session_state:
    st.session_state.distancia_parcial_1 = 0

if "volume_parcial_1" not in st.session_state:
    st.session_state.volume_parcial_1 = 0

if "distancia_parcial_2" not in st.session_state:
    st.session_state.distancia_parcial_2 = 0

if "volume_parcial_2" not in st.session_state:
    st.session_state.volume_parcial_2 = 0

if "distancia_parcial_3" not in st.session_state:
    st.session_state.distancia_parcial_3 = 0

if "volume_parcial_3" not in st.session_state:
    st.session_state.volume_parcial_3 = 0

if "distancia_parcial_4" not in st.session_state:
    st.session_state.distancia_parcial_4 = 0

if "volume_parcial_4" not in st.session_state:
    st.session_state.volume_parcial_4 = 0

if "saidas_parciais_salvas" not in st.session_state:
    st.session_state.saidas_parciais_salvas = False

if st.session_state.etapa == 1:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>De um nome para seu robo</h3>", unsafe_allow_html=True)

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
        st.markdown("<h3 style='text-align: center;'>CONFIGURACAO INICIAL</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Se desabilitar algum dos lados podera pular as configuracoes de sinais</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Deseja operar na compra",
            ["Sim", "Nao"],
            key="operar_compra",
        )

        st.selectbox(
            "Deseja operar na venda",
            ["Sim", "Nao"],
            key="operar_venda",
        )

        st.markdown(
            "<p style='text-align: center;'>Algumas configuracoes de B3 podem nao funcionar no FOREX e vice-versa</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Escolha o mercado desejado",
            ["B3", "Forex"],
            key="mercado",
        )

        st.selectbox(
            "Selecione o tipo operacional",
            ["Swing Trade", "Day Trade"],
            key="tipo_operacional",
        )

        st.selectbox(
            "Modo de processamento",
            ["A cada tick", "A cada segundo"],
            key="modo_processamento",
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
        st.markdown(
            "<p style='text-align: center;'>Defina o tempo grafico que forcara abertura na janela correta</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tempo grafico principal",
            [
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
            ],
            key="tempo_grafico_principal",
        )

        st.markdown(
            "<p style='text-align: center;'>Esses parametros podem ser alterados futuramente quando o robo estiver finalizado</p>",
            unsafe_allow_html=True,
        )

        st.number_input(
            "Volume inicial",
            min_value=0,
            step=1,
            key="volume_inicial",
        )

        st.number_input(
            "Spread maximo",
            min_value=0,
            step=1,
            key="spread_maximo",
        )

        st.markdown("<p style='text-align: center;'>(Em pontos)</p>", unsafe_allow_html=True)

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
        st.markdown("<h3 style='text-align: center;'>TIPO DE ORDENS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>E possivel personalizar a posicao do preco de entrada e saida durante um sinal</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo das distancias",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_distancias",
        )

        st.markdown("<p style='text-align: center;'><strong>Ordens de entradas</strong></p>", unsafe_allow_html=True)
        st.selectbox(
            "Ordem de entrada",
            ["A mercado", "Pendente"],
            key="ordem_entrada",
        )

        st.markdown("<p style='text-align: center;'><strong>Ordens de saidas</strong></p>", unsafe_allow_html=True)
        st.selectbox(
            "Ordem de saida",
            ["A mercado", "Pendente"],
            key="ordem_saida",
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
        st.markdown("<h3 style='text-align: center;'>ALVOS PERSONALIZADOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>E possivel personalizar uma distancia para o stoploss e/ou takeprofit</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo das distancias",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_alvos",
        )

        st.markdown(
            "<p style='text-align: center;'>Os alvos personalizados serao comparados com os alvos padroes</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Usar stoploss personalizado",
            ["Nao", "Sim"],
            key="usar_stoploss_personalizado",
        )

        st.selectbox(
            "Usar takeprofit personalizado",
            ["Nao", "Sim"],
            key="usar_takeprofit_personalizado",
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
        st.markdown("<h3 style='text-align: center;'>STOPLOSS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Defina o limite de perda aceitavel por operacao e o tipo de calculo das distancias</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_stoploss",
        )

        st.number_input(
            "Stoploss inicial",
            min_value=0,
            step=1,
            key="stoploss_inicial",
        )

        st.markdown(
            "<p style='text-align: center;'>Unidade: pontos / percentual (dependendo do select)</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align: center;'>A medida que a operacao anda a favor, o stoploss podera ser reposicionado para acompanhar o preco corrente</p>",
            unsafe_allow_html=True,
        )

        st.number_input(
            "Inicio do Break Even SL",
            min_value=0,
            step=1,
            key="inicio_break_even_sl",
        )

        st.number_input(
            "Distancia do Break Even SL",
            min_value=0,
            step=1,
            key="distancia_break_even_sl",
        )

        st.number_input(
            "Inicio do Trailing Stop",
            min_value=0,
            step=1,
            key="inicio_trailing_stop",
        )

        st.number_input(
            "Passo do Trailing Stop",
            min_value=0,
            step=1,
            key="passo_trailing_stop",
        )

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
        st.markdown("<h3 style='text-align: center;'>TAKE PROFIT</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Defina o alvo da operacao e o tipo de calculo da distancia de referencia</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_takeprofit",
        )

        st.number_input(
            "TakeProfit inicial",
            min_value=0,
            step=1,
            key="takeprofit_inicial",
        )

        st.markdown(
            "<p style='text-align: center;'>A medida que a operacao anda contra, o takeprofit podera ser reposicionado para facilitar uma saida</p>",
            unsafe_allow_html=True,
        )

        st.number_input(
            "Inicio do Break Even TP",
            min_value=0,
            step=1,
            key="inicio_break_even_tp",
        )

        st.number_input(
            "Distancia do Break Even TP",
            min_value=0,
            step=1,
            key="distancia_break_even_tp",
        )

        st.number_input(
            "Inicio do Trailing Profit",
            min_value=0,
            step=1,
            key="inicio_trailing_profit",
        )

        st.number_input(
            "Passo do Trailing Profit",
            min_value=0,
            step=1,
            key="passo_trailing_profit",
        )

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
        st.markdown("<h3 style='text-align: center;'>SAIDA TEMPORAL</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Saida pelo tempo sem depender do stoploss e/ou takeprofit</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Referencia de tempo",
            ["Segundos", "Minutos", "Horas", "Velas"],
            key="referencia_tempo_saida",
        )

        st.markdown(
            "<p style='text-align: center;'>Pode configurar um tempo de saida tanto para operacoes positivas quanto para negativas</p>",
            unsafe_allow_html=True,
        )

        referencia_tempo = st.session_state.referencia_tempo_saida

        st.markdown("<p style='text-align: center;'><strong>Operacoes positivas</strong></p>", unsafe_allow_html=True)
        st.number_input(
            f"Tempo de saida ({referencia_tempo})",
            min_value=0,
            step=1,
            key="tempo_saida_operacoes_positivas",
        )
        st.number_input(
            "Saldo maximo",
            min_value=0,
            step=1,
            key="saldo_maximo_operacoes_positivas",
        )
        st.number_input(
            "Saldo minimo",
            min_value=0,
            step=1,
            key="saldo_minimo_operacoes_positivas",
        )

        st.markdown("<p style='text-align: center;'><strong>Operacoes negativas</strong></p>", unsafe_allow_html=True)
        st.number_input(
            f"Tempo de saida ({referencia_tempo})",
            min_value=0,
            step=1,
            key="tempo_saida_operacoes_negativas",
        )
        st.number_input(
            "Saldo maximo",
            min_value=0,
            step=1,
            key="saldo_maximo_operacoes_negativas",
        )
        st.number_input(
            "Saldo minimo",
            min_value=0,
            step=1,
            key="saldo_minimo_operacoes_negativas",
        )

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
        st.markdown("<h3 style='text-align: center;'>FILTRO DE TEMPO</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Referencia de tempo para procurar entrada e/ou sinais de saida</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Referencia de tempo",
            ["Segundos", "Minutos", "Horas", "Velas"],
            key="referencia_tempo_filtro",
        )

        st.markdown(
            "<p style='text-align: center;'>Deixar os valores zerados desabilita o recurso do filtro de temporizacao</p>",
            unsafe_allow_html=True,
        )

        st.number_input(
            "Tempo para nova entrada",
            min_value=0,
            step=1,
            key="tempo_para_nova_entrada",
        )

        st.number_input(
            "Tempo minimo de posicao",
            min_value=0,
            step=1,
            key="tempo_minimo_posicao",
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
        st.markdown("<h3 style='text-align: center;'>HORARIOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Gerencie seu horario operacional</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Deseja zerar por horario",
            ["Sim", "Nao"],
            key="zerar_por_horario",
        )

        st.markdown(
            "<p style='text-align: center;'>Para operar independente de horario, basta deixar o horario inicial igual ao horario final</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Horario inicial das operacoes</strong></p>", unsafe_allow_html=True)
        h_ini_col, m_ini_col = st.columns(2)
        with h_ini_col:
            st.selectbox("Hora", list(range(24)), key="hora_inicial_operacoes")
        with m_ini_col:
            st.selectbox("Minuto", list(range(60)), key="minuto_inicial_operacoes")

        st.markdown("<p style='text-align: center;'><strong>Horario final das operacoes</strong></p>", unsafe_allow_html=True)
        h_fim_col, m_fim_col = st.columns(2)
        with h_fim_col:
            st.selectbox("Hora ", list(range(24)), key="hora_final_operacoes")
        with m_fim_col:
            st.selectbox("Minuto ", list(range(60)), key="minuto_final_operacoes")

        st.markdown("<p style='text-align: center;'><strong>Horario de zerar as operacoes</strong></p>", unsafe_allow_html=True)
        h_zero_col, m_zero_col = st.columns(2)
        with h_zero_col:
            st.selectbox("Hora  ", list(range(24)), key="hora_zerar_operacoes")
        with m_zero_col:
            st.selectbox("Minuto  ", list(range(60)), key="minuto_zerar_operacoes")

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
        st.markdown("<h3 style='text-align: center;'>PAUSAS OPERACIONAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Selecione os dados para identificacao dos criterios das pausas</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Referencia de tempo",
            ["Segundos", "Minutos", "Horas", "Velas"],
            key="referencia_tempo_pausas",
        )

        st.markdown(
            "<p style='text-align: center;'>As pausas sao aplicadas somente na procura de sinal de entrada</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Primeira pausa</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Horario da pausa</p>", unsafe_allow_html=True)
        p1_hora_col, p1_min_col = st.columns(2)
        with p1_hora_col:
            st.selectbox("Hora", list(range(24)), key="primeira_pausa_hora")
        with p1_min_col:
            st.selectbox("Minuto", list(range(60)), key="primeira_pausa_minuto")

        st.selectbox(
            "Periodo",
            ["Diariamente", "Segundas", "Tercas", "Quartas", "Quintas", "Sextas", "Sabados"],
            key="primeira_pausa_periodo",
        )

        st.number_input(
            "Duracao",
            min_value=0,
            step=1,
            key="primeira_pausa_duracao",
        )
        st.markdown(
            f"<p style='text-align: center;'>Unidade: {st.session_state.referencia_tempo_pausas}</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Segunda pausa</strong></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Horario da pausa</p>", unsafe_allow_html=True)
        p2_hora_col, p2_min_col = st.columns(2)
        with p2_hora_col:
            st.selectbox("Hora ", list(range(24)), key="segunda_pausa_hora")
        with p2_min_col:
            st.selectbox("Minuto ", list(range(60)), key="segunda_pausa_minuto")

        st.selectbox(
            "Periodo ",
            ["Diariamente", "Segundas", "Tercas", "Quartas", "Quintas", "Sextas", "Sabados"],
            key="segunda_pausa_periodo",
        )

        st.number_input(
            "Duracao ",
            min_value=0,
            step=1,
            key="segunda_pausa_duracao",
        )
        st.markdown(
            f"<p style='text-align: center;'>Unidade: {st.session_state.referencia_tempo_pausas}</p>",
            unsafe_allow_html=True,
        )

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
        st.markdown("<h3 style='text-align: center;'>AUMENTO CONTRA</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Determine a referencia para aumentos contra</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo da distancia",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_aumento_contra",
        )

        st.markdown(
            "<p style='text-align: center;'>Ordens tipo limitadas colocadas a partir da entrada para aumento de posicao se a operacao for contra</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Aumentos contra</strong></p>", unsafe_allow_html=True)

        c1_col1, c1_col2 = st.columns(2)
        with c1_col1:
            st.number_input("Distancia contra 1", min_value=0, step=1, key="distancia_contra_1")
        with c1_col2:
            st.number_input("Volume 1", min_value=0, step=1, key="volume_contra_1")

        c2_col1, c2_col2 = st.columns(2)
        with c2_col1:
            st.number_input("Distancia contra 2", min_value=0, step=1, key="distancia_contra_2")
        with c2_col2:
            st.number_input("Volume 2", min_value=0, step=1, key="volume_contra_2")

        c3_col1, c3_col2 = st.columns(2)
        with c3_col1:
            st.number_input("Distancia contra 3", min_value=0, step=1, key="distancia_contra_3")
        with c3_col2:
            st.number_input("Volume 3", min_value=0, step=1, key="volume_contra_3")

        c4_col1, c4_col2 = st.columns(2)
        with c4_col1:
            st.number_input("Distancia contra 4", min_value=0, step=1, key="distancia_contra_4")
        with c4_col2:
            st.number_input("Volume 4", min_value=0, step=1, key="volume_contra_4")

        c5_col1, c5_col2 = st.columns(2)
        with c5_col1:
            st.number_input("Distancia contra 5", min_value=0, step=1, key="distancia_contra_5")
        with c5_col2:
            st.number_input("Volume 5", min_value=0, step=1, key="volume_contra_5")

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
        st.markdown("<h3 style='text-align: center;'>AUMENTO A FAVOR</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Determine a referencia para aumentos a favor</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo da distancia",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_aumento_favor",
        )

        st.markdown(
            "<p style='text-align: center;'>Ordens pendentes tipo gatilhos colocadas a partir da entrada para aumento de posicao se a operacao for a favor</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Aumentos a favor</strong></p>", unsafe_allow_html=True)

        f1_col1, f1_col2 = st.columns(2)
        with f1_col1:
            st.number_input("Distancia a favor 1", min_value=0, step=1, key="distancia_favor_1")
        with f1_col2:
            st.number_input("Volume 1", min_value=0, step=1, key="volume_favor_1")

        f2_col1, f2_col2 = st.columns(2)
        with f2_col1:
            st.number_input("Distancia a favor 2", min_value=0, step=1, key="distancia_favor_2")
        with f2_col2:
            st.number_input("Volume 2", min_value=0, step=1, key="volume_favor_2")

        f3_col1, f3_col2 = st.columns(2)
        with f3_col1:
            st.number_input("Distancia a favor 3", min_value=0, step=1, key="distancia_favor_3")
        with f3_col2:
            st.number_input("Volume 3", min_value=0, step=1, key="volume_favor_3")

        f4_col1, f4_col2 = st.columns(2)
        with f4_col1:
            st.number_input("Distancia a favor 4", min_value=0, step=1, key="distancia_favor_4")
        with f4_col2:
            st.number_input("Volume 4", min_value=0, step=1, key="volume_favor_4")

        f5_col1, f5_col2 = st.columns(2)
        with f5_col1:
            st.number_input("Distancia a favor 5", min_value=0, step=1, key="distancia_favor_5")
        with f5_col2:
            st.number_input("Volume 5", min_value=0, step=1, key="volume_favor_5")

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
        st.markdown("<h3 style='text-align: center;'>SAIDAS PARCIAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Determine a referencia para a distancia das parciais</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo da distancia",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_saidas_parciais",
        )

        st.markdown(
            "<p style='text-align: center;'>Distancias positivas serao ordens limites no ganho e negativas, ordens gatilhos no loss</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<p style='text-align: center;'><strong>Saidas parciais</strong></p>", unsafe_allow_html=True)

        p1_col1, p1_col2 = st.columns(2)
        with p1_col1:
            st.number_input("Distancia parcial 1", step=1, key="distancia_parcial_1")
        with p1_col2:
            st.number_input("Volume 1", min_value=0, step=1, key="volume_parcial_1")

        p2_col1, p2_col2 = st.columns(2)
        with p2_col1:
            st.number_input("Distancia parcial 2", step=1, key="distancia_parcial_2")
        with p2_col2:
            st.number_input("Volume 2", min_value=0, step=1, key="volume_parcial_2")

        p3_col1, p3_col2 = st.columns(2)
        with p3_col1:
            st.number_input("Distancia parcial 3", step=1, key="distancia_parcial_3")
        with p3_col2:
            st.number_input("Volume 3", min_value=0, step=1, key="volume_parcial_3")

        p4_col1, p4_col2 = st.columns(2)
        with p4_col1:
            st.number_input("Distancia parcial 4", step=1, key="distancia_parcial_4")
        with p4_col2:
            st.number_input("Volume 4", min_value=0, step=1, key="volume_parcial_4")

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
        st.markdown("<h3 style='text-align: center;'>GRADIENTE LINEAR</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Escolha a referencia para distancias dos alvos e ordens do gradiente</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tipo de calculo da distancia",
            ["Em pontos", "Percentual"],
            key="tipo_calculo_gradiente_linear",
        )

        st.markdown(
            "<p style='text-align: center;'>O gradiente sera recorrente ou limitado a quantidade de ordens definido</p>",
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)
        with c1:
            st.number_input(
                "Quantidade de niveis",
                min_value=0,
                step=1,
                key="quantidade_niveis_gradiente_linear",
            )
        with c2:
            st.number_input(
                "Distancia dos niveis",
                min_value=0,
                step=1,
                key="distancia_niveis_gradiente_linear",
            )

        c3, c4 = st.columns(2)
        with c3:
            st.number_input(
                "Volume das ordens",
                min_value=0,
                step=1,
                key="volume_ordens_gradiente_linear",
            )
        with c4:
            st.number_input(
                "Alvo parcial",
                min_value=0,
                step=1,
                key="alvo_parcial_gradiente_linear",
            )

        c5, c6 = st.columns(2)
        with c5:
            st.number_input(
                "Limite de entradas",
                min_value=0,
                step=1,
                key="limite_entradas_gradiente_linear",
            )
        with c6:
            st.number_input(
                "Reposicionar ordem",
                min_value=0,
                step=1,
                key="reposicionar_ordem_gradiente_linear",
            )

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
        st.markdown("<h3 style='text-align: center;'>FILTRO DE VELA</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>O tempo grafico da vela filtro nao precisa ser igual ao do grafico corrente</p>",
            unsafe_allow_html=True,
        )

        st.selectbox(
            "Tempo grafico da vela",
            [
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
            ],
            key="tempo_grafico_vela_filtro",
        )

        st.markdown(
            "<p style='text-align: center;'>Aplicado sempre antes de iniciar uma nova posicao</p>",
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)
        with c1:
            st.number_input(
                "Tamanho minimo da vela",
                min_value=0,
                step=1,
                key="tamanho_minimo_vela_filtro",
            )
        with c2:
            st.number_input(
                "Tamanho maximo da vela",
                min_value=0,
                step=1,
                key="tamanho_maximo_vela_filtro",
            )

        c3, c4 = st.columns(2)
        with c3:
            st.number_input(
                "Minimo do corpo da vela",
                min_value=0,
                step=1,
                key="minimo_corpo_vela_filtro",
            )
        with c4:
            st.number_input(
                "Maximo do corpo da vela",
                min_value=0,
                step=1,
                key="maximo_corpo_vela_filtro",
            )

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
        st.markdown("<h3 style='text-align: center;'>SINAIS PRONTOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Podera selecionar quais estrategias desejar ou combina-las para usar para sinais de entrada e/ou saida</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>CANAL DE BANDAS</h4>", unsafe_allow_html=True)

        st.selectbox(
            "Indicador",
            ["Nao usar", "Bandas de Bollinger", "Envelopes", "Keltner", "Dochian", "Canal ATR"],
            key="canal_bandas_indicador",
        )

        st.selectbox(
            "Entrada",
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

        st.selectbox(
            "Sentido",
            ["Tendencia", "Contra Tendencia"],
            key="canal_bandas_sentido",
        )

        st.selectbox(
            "Saida",
            [
                "Nao usar",
                "Cruzar o centro",
                "Cruzar o centro e fechar",
                "Cruzar banda oposta",
                "Cruzar oposta e fechar",
            ],
            key="canal_bandas_saida",
        )

        st.markdown("<hr />", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>CRUZAMENTO DE SINAIS</h4>", unsafe_allow_html=True)

        st.selectbox(
            "Sinal rapido",
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

        st.selectbox(
            "Sinal lento",
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

        st.selectbox(
            "Entrada",
            ["Nao usar", "Cruzamento", "Cruzamento e fechando"],
            key="cruzamento_entrada",
        )

        st.selectbox(
            "Sentido",
            ["Tendencia", "Contra Tendencia"],
            key="cruzamento_sentido",
        )

        st.selectbox(
            "Saida",
            ["Nao usar", "Cruzamento oposto", "Cruzar oposto e fechar"],
            key="cruzamento_saida",
        )

        st.markdown("<hr />", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>SOBRE COMPRADO / VENDIDO</h4>", unsafe_allow_html=True)

        st.selectbox(
            "Indicador",
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

        st.selectbox(
            "Entrada",
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

        n1, n2 = st.columns(2)
        with n1:
            st.number_input("Sobrecompra", step=1, key="sobrecompra_nivel")
        with n2:
            st.number_input("Sobrevenda", step=1, key="sobrevenda_nivel")

        st.selectbox(
            "Sentido",
            ["Tendencia", "Contra Tendencia"],
            key="sobrecompra_venda_sentido",
        )

        st.selectbox(
            "Saida",
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
                st.session_state.etapa = 18
                st.rerun()

if st.session_state.etapa == 18:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown(
            "<p style='text-align: center;'>Voce ainda podera alterar todos os parametros diretamente em seu robo quando estiver pronto</p>",
            unsafe_allow_html=True,
        )

        def bloco_info(texto_principal: str, texto_auxiliar: str) -> None:
            st.markdown(
                f"""
                <div style="border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 10px; padding: 14px;">
                    <div style="font-size: 18px; font-weight: 600;">{texto_principal}</div>
                    <div style="font-size: 12px; opacity: 0.75; margin-top: 4px;">{texto_auxiliar}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        r1_c1, r1_c2 = st.columns(2)
        with r1_c1:
            bloco_info("Nao selecionado", "Dados nao requeridos")
        with r1_c2:
            bloco_info("Nao selecionado/Nao selecionado", "Dados nao requeridos")

        r2_c1, r2_c2 = st.columns(2)
        with r2_c1:
            bloco_info("Nao selecionado", "Dados nao requeridos")
        with r2_c2:
            bloco_info("Nao selecionado", "Dados nao requeridos")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 17
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.resumo_validacao_final_salvo = True
                st.session_state.etapa = 19
                st.rerun()

if st.session_state.etapa == 19:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>ESCOLHER INDICADORES</h3>", unsafe_allow_html=True)

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

        st.selectbox("Escolha o indicador [1]", opcoes_indicadores, key="indicador_escolha_1")
        st.selectbox("Escolha o indicador [2]", opcoes_indicadores, key="indicador_escolha_2")
        st.selectbox("Escolha o indicador [3]", opcoes_indicadores, key="indicador_escolha_3")
        st.selectbox("Escolha o indicador [4]", opcoes_indicadores, key="indicador_escolha_4")

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 18
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.escolher_indicadores_salvo = True
                st.session_state.etapa = 20
                st.rerun()

        if st.session_state.escolher_indicadores_salvo:
            st.success("Indicadores salvos.")

if st.session_state.etapa == 20:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>CONFIGURAR INDICADORES</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Você ainda poderá alterar todos os parâmetros diretamente em seu robô quando estiver pronto</p>",
            unsafe_allow_html=True,
        )

        def bloco_status_indicador(numero: int, valor: str) -> None:
            texto = f"[{numero}] Não selecionado" if valor == "Não usar" else f"[{numero}] {valor}"
            st.markdown(
                f"""
                <div style="border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 10px; padding: 14px;">
                    <div style="font-size: 18px; font-weight: 600;">{texto}</div>
                    <div style="font-size: 12px; opacity: 0.75; margin-top: 4px;">Dados não requeridos</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        r1_c1, r1_c2 = st.columns(2)
        with r1_c1:
            bloco_status_indicador(1, st.session_state.indicador_escolha_1)
        with r1_c2:
            bloco_status_indicador(2, st.session_state.indicador_escolha_2)

        r2_c1, r2_c2 = st.columns(2)
        with r2_c1:
            bloco_status_indicador(3, st.session_state.indicador_escolha_3)
        with r2_c2:
            bloco_status_indicador(4, st.session_state.indicador_escolha_4)

        nav_esq, nav_dir = st.columns(2)
        with nav_esq:
            if st.button("Voltar", use_container_width=True):
                st.session_state.etapa = 19
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.configurar_indicadores_salvo = True
                st.session_state.etapa = 21
                st.rerun()

        if st.session_state.configurar_indicadores_salvo:
            st.success("Configuração de indicadores salva.")

if st.session_state.etapa == 21:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>SINAIS ENTRADA COMPRA</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.75;'>Página 1/1</p>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>No modo de edição avançado, poderá multiplicar, dividir, somar ou subtrair os valores de referência</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Configurações gerais</h4>", unsafe_allow_html=True)

        g1, g2, g3 = st.columns(3)
        with g1:
            st.selectbox("Modo de edição", ["Avançado", "Básico"], key="sec_modo_edicao")
        with g2:
            st.selectbox("Tipo de vela", ["Completas", "Simplificadas"], key="sec_tipo_vela")
        with g3:
            st.selectbox(
                "Estratégia",
                ["Entrada compra (1)", "Entrada compra (2)", "Entrada compra (3)"],
                key="sec_estrategia",
            )

        st.markdown(
            "<p style='text-align: center;'>Com a vela no modo completo, poderá selecionar qualquer vela do histórico</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Regras condicionais</h4>", unsafe_allow_html=True)

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

        h1, h2, h3, h4, h5, h6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3])
        with h1:
            st.caption("Operador lógico")
        with h2:
            st.caption("Referência esquerda")
        with h3:
            st.caption("Vela (esq.)")
        with h4:
            st.caption("Operador")
        with h5:
            st.caption("Referência direita")
        with h6:
            st.caption("Vela (dir.)")

        for i in range(1, 6):
            c1, c2, c3, c4, c5, c6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3])
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
                st.session_state.etapa = 20
                st.rerun()
        with nav_dir:
            if st.button("Salvar", use_container_width=True):
                st.session_state.sinais_entrada_compra_salvo = True
                st.session_state.etapa = 22
                st.rerun()

        if st.session_state.sinais_entrada_compra_salvo:
            st.success("Configurações de sinais de entrada (compra) salvas.")

if st.session_state.etapa == 22:
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.markdown("<h3 style='text-align: center;'>SINAIS ENTRADA VENDA</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.75;'>Página 1/1</p>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>No modo de edição básico, tem 4 opções de velas de referência</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Configurações gerais</h4>", unsafe_allow_html=True)

        g1, g2, g3 = st.columns(3)
        with g1:
            st.selectbox("Modo de edição", ["Avançado", "Básico"], key="sev_modo_edicao")
        with g2:
            st.selectbox("Tipo de vela", ["Completas", "Simplificadas"], key="sev_tipo_vela")
        with g3:
            st.selectbox(
                "Estratégia",
                ["Entrada venda (1)", "Entrada venda (2)", "Entrada venda (3)"],
                key="sev_estrategia",
            )

        st.markdown(
            "<p style='text-align: center;'>Se deixar \"Não usar\" em uma das duas opções possíveis de cada linha, a linha será desconsiderada dos sinais</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Regras condicionais</h4>", unsafe_allow_html=True)

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

        h1, h2, h3, h4, h5, h6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3])
        with h1:
            st.caption("Operador lógico")
        with h2:
            st.caption("Referência esquerda")
        with h3:
            st.caption("Vela (esq.)")
        with h4:
            st.caption("Operador")
        with h5:
            st.caption("Referência direita")
        with h6:
            st.caption("Vela (dir.)")

        for i in range(1, 6):
            c1, c2, c3, c4, c5, c6 = st.columns([1.2, 2.2, 1.3, 2.2, 2.2, 1.3])
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

        st.info("As 5 linhas são cópias exatas da primeira. A lógica é condicional sequencial, usando operadores (SE, E, OU, etc.).")

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
        st.markdown("<h3 style='text-align: center;'>LIMITES DO ROBÔ</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Gerencie limite de ganho e perda para proteger sua conta bem como o cálculo de referência</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Referências das metas</h4>", unsafe_allow_html=True)

        r1, r2 = st.columns(2)
        with r1:
            st.selectbox(
                "Histórico",
                ["Desabilitado", "Diário", "Semanal", "Mensal"],
                key="limites_robo_historico",
            )
        with r2:
            st.selectbox(
                "Cálculo",
                ["Financeiro", "Percentual"],
                key="limites_robo_calculo",
            )

        st.markdown("<h4 style='text-align: center;'>Limite de operações</h4>", unsafe_allow_html=True)

        l1, l2, l3 = st.columns(3)
        with l1:
            st.number_input("Vencedoras", min_value=0, step=1, key="limites_robo_vencedoras")
        with l2:
            st.number_input("Perdedoras", min_value=0, step=1, key="limites_robo_perdedoras")
        with l3:
            st.number_input("Limite total", min_value=0, step=1, key="limites_robo_limite_total")

        st.markdown("<h4 style='text-align: center;'>Metas financeiras e controle de encerramento</h4>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>A referência equivale a moeda base da sua conta na corretora</p>",
            unsafe_allow_html=True,
        )

        m1, m2 = st.columns(2)
        with m1:
            st.number_input("Meta de ganho", min_value=0, step=1, key="limites_robo_meta_ganho")
        with m2:
            st.selectbox(
                "Encerrar no trade (Meta de ganho)",
                ["Sim", "Não"],
                key="limites_robo_encerrar_meta_ganho",
            )

        p1, p2 = st.columns(2)
        with p1:
            st.number_input("Limite de perda", min_value=0, step=1, key="limites_robo_limite_perda")
        with p2:
            st.selectbox(
                "Encerrar no trade (Limite de perda)",
                ["Sim", "Não"],
                key="limites_robo_encerrar_limite_perda",
            )

        rb1, rb2 = st.columns(2)
        with rb1:
            st.number_input("Rebaixamento", min_value=0, step=1, key="limites_robo_rebaixamento")
        with rb2:
            st.selectbox(
                "Encerrar no trade (Rebaixamento)",
                ["Não", "Sim"],
                key="limites_robo_encerrar_rebaixamento",
            )

        rb3, rb4 = st.columns(2)
        with rb3:
            st.number_input(
                "Gatilho (Rebaixamento)",
                min_value=0,
                step=1,
                key="limites_robo_gatilho_rebaixamento",
            )
        with rb4:
            st.number_input("Recuperação", min_value=0, step=1, key="limites_robo_recuperacao")

        rc1, rc2 = st.columns(2)
        with rc1:
            st.selectbox(
                "Encerrar no trade (Recuperação)",
                ["Não", "Sim"],
                key="limites_robo_encerrar_recuperacao",
            )
        with rc2:
            st.number_input(
                "Gatilho (Recuperação)",
                min_value=0,
                step=1,
                key="limites_robo_gatilho_recuperacao",
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
        st.markdown(
            "<p style='text-align: center;'>Gerencie toda a conta combinando com as permissões do robô</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Referências das metas (nível conta)</h4>", unsafe_allow_html=True)

        r1, r2 = st.columns(2)
        with r1:
            st.selectbox(
                "Histórico",
                ["Desabilitado", "Diário", "Semanal", "Mensal"],
                key="conta_historico",
            )
        with r2:
            st.selectbox(
                "Cálculo",
                ["Financeiro", "Percentual"],
                key="conta_calculo",
            )

        st.markdown("<h4 style='text-align: center;'>Seleção de filtros</h4>", unsafe_allow_html=True)

        f1, f2, f3 = st.columns(3)
        with f1:
            st.selectbox("Filtro de ativo", ["Não", "Sim"], key="conta_filtro_ativo")
        with f2:
            st.selectbox("Excluir manuais", ["Não", "Sim"], key="conta_excluir_manuais")
        with f3:
            st.selectbox("Filtrar robôs", ["Não", "Sim"], key="conta_filtrar_robos")

        id1, id2 = st.columns(2)
        with id1:
            st.number_input("ID mínimo", min_value=0, step=1, key="conta_id_minimo")
        with id2:
            st.number_input("ID máximo", min_value=0, step=1, key="conta_id_maximo")

        st.markdown("<h4 style='text-align: center;'>Metas financeiras (nível conta)</h4>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Os dados valem para toda a conta para execução deste robô</p>",
            unsafe_allow_html=True,
        )

        m1, m2 = st.columns(2)
        with m1:
            st.number_input("Meta de ganho", min_value=0, step=1, key="conta_meta_ganho")
        with m2:
            st.selectbox(
                "Encerrar no trade (Meta de ganho)",
                ["Sim", "Não"],
                key="conta_encerrar_meta_ganho",
            )

        p1, p2 = st.columns(2)
        with p1:
            st.number_input("Limite de perda", min_value=0, step=1, key="conta_limite_perda")
        with p2:
            st.selectbox(
                "Encerrar no trade (Limite de perda)",
                ["Sim", "Não"],
                key="conta_encerrar_limite_perda",
            )

        rb1, rb2 = st.columns(2)
        with rb1:
            st.number_input("Rebaixamento", min_value=0, step=1, key="conta_rebaixamento")
        with rb2:
            st.selectbox(
                "Encerrar no trade (Rebaixamento)",
                ["Não", "Sim"],
                key="conta_encerrar_rebaixamento",
            )

        rb3, rb4 = st.columns(2)
        with rb3:
            st.number_input("Gatilho (Rebaixamento)", min_value=0, step=1, key="conta_gatilho_rebaixamento")
        with rb4:
            st.number_input("Recuperação", min_value=0, step=1, key="conta_recuperacao")

        rc1, rc2 = st.columns(2)
        with rc1:
            st.selectbox(
                "Encerrar no trade (Recuperação)",
                ["Não", "Sim"],
                key="conta_encerrar_recuperacao",
            )
        with rc2:
            st.number_input("Gatilho (Recuperação)", min_value=0, step=1, key="conta_gatilho_recuperacao")

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
        st.markdown("<h3 style='text-align: center;'>AJUSTES FINAIS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Selecione algumas confirmações para os ajustes finais</p>",
            unsafe_allow_html=True,
        )

        opcoes_sim_nao = ["Sim", "Não"]

        st.selectbox(
            "Cancelar pendente de entrada se aparecer sinal oposto",
            opcoes_sim_nao,
            key="ajuste_cancelar_pendente_entrada_sinal_oposto",
        )
        st.selectbox(
            "Reposicionar stoploss no aumento a favor da operação",
            opcoes_sim_nao,
            key="ajuste_reposicionar_stoploss_aumento_favor",
        )
        st.selectbox(
            "Reposicionar takeprofit no aumento contra a operação",
            opcoes_sim_nao,
            key="ajuste_reposicionar_takeprofit_aumento_contra",
        )
        st.selectbox(
            "Movimentar stoploss com base no preço médio",
            opcoes_sim_nao,
            key="ajuste_movimentar_stoploss_preco_medio",
        )
        st.selectbox(
            "Movimentar takeprofit com base no preço médio",
            opcoes_sim_nao,
            key="ajuste_movimentar_takeprofit_preco_medio",
        )
        st.selectbox(
            "Usar preço médio como referência das parciais",
            opcoes_sim_nao,
            key="ajuste_usar_preco_medio_parciais",
        )
        st.selectbox(
            "Impedir sinal de saída na vela que gerou entrada",
            opcoes_sim_nao,
            key="ajuste_impedir_saida_vela_entrada",
        )
        st.selectbox(
            "Impedir sinal de entrada na vela que gerou saída",
            opcoes_sim_nao,
            key="ajuste_impedir_entrada_vela_saida",
        )
        st.selectbox(
            "Recalcular o preço médio com base nas saídas parciais",
            ["Não", "Sim"],
            key="ajuste_recalcular_preco_medio_saidas_parciais",
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
        st.markdown("<h3 style='text-align: center;'>COMPLEMENTOS</h3>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align: center;'>Adicione alguns complementos de ordens e sinais</p>",
            unsafe_allow_html=True,
        )

        st.markdown("<h4 style='text-align: center;'>Complementos de ordens e sinais</h4>", unsafe_allow_html=True)

        opcoes_nao_sim = ["Não", "Sim"]

        st.selectbox(
            "Enviar ordem para outro ativo (Cross order)",
            opcoes_nao_sim,
            key="comp_enviar_ordem_outro_ativo",
        )
        st.selectbox(
            "Procurar entrada na vela seguinte à saída",
            opcoes_nao_sim,
            key="comp_procurar_entrada_vela_seguinte_saida",
        )
        st.selectbox(
            "Procurar saída na vela seguinte à entrada",
            opcoes_nao_sim,
            key="comp_procurar_saida_vela_seguinte_entrada",
        )

        st.number_input(
            "Saldo de ajuste para somar com a conta",
            min_value=0,
            step=1,
            key="comp_saldo_ajuste",
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
