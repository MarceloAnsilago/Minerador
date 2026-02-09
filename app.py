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
                st.success("Configuracao de aumento a favor salva.")
