import streamlit as st
import time
import random

# -----------------------------------------------------------------------------
# 1. Configurações Iniciais da Página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Painel IoT - ESP32",
    page_icon="⚡",
    layout="wide"  # Usa toda a largura da tela
)

# -----------------------------------------------------------------------------
# 2. Título e Explicação
# -----------------------------------------------------------------------------
st.title("⚡ Painel de Controle: Python + ESP32 (Simulação)")
st.markdown("""
Este painel é uma **interface de teste**. Aqui simulamos o que acontecerá
quando você conectar seu ESP32 via MQTT.
""")

st.divider() # Uma linha divisória visual

# -----------------------------------------------------------------------------
# 3. Sidebar (Barra Lateral) - Ótimo para configurações
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("📡 Configuração de Conexão")
    st.info("Simulando conexão MQTT...")
    
    # Um selectbox para simular escolha de servidor
    broker = st.selectbox(
        "Selecione o Broker MQTT",
        ["broker.hivemq.com", "test.mosquitto.org", "Localhost"]
    )
    
    st.success(f"Conectado ao: {broker}")

# -----------------------------------------------------------------------------
# 4. Layout em Colunas (Para organizar a tela)
# -----------------------------------------------------------------------------
col1, col2 = st.columns(2)

# --- COLUNA 1: ATUADORES (Enviar comandos para o ESP32) ---
with col1:
    st.subheader("🎮 Controle (Atuadores)")
    
    st.write("Controle seus dispositivos remotamente:")
    
    # Botão tipo Toggle (Ligar/Desligar)
    # No futuro, isso enviará uma mensagem 'ON' ou 'OFF' via MQTT
    estado_led = st.toggle("Ligar LED da Sala")
    
    if estado_led:
        st.success("Enviando comando: **LED LIGADO** 💡")
        # Aqui entraria o código: client.publish("topico/led", "ON")
    else:
        st.error("Enviando comando: **LED DESLIGADO** ⚫")
        # Aqui entraria o código: client.publish("topico/led", "OFF")

    st.markdown("---") # Separador
    
    # Slider para simular controle de intensidade (PWM) ou Servo Motor
    intensidade = st.slider("Intensidade da Lâmpada (PWM)", 0, 100, 50)
    st.write(f"Valor enviado: **{intensidade}%**")

# --- COLUNA 2: SENSORES (Receber dados do ESP32) ---
with col2:
    st.subheader("🌡️ Monitoramento (Sensores)")
    
    # Botão para atualizar leitura manualmente
    if st.button("Ler Sensor DHT11"):
        # SIMULAÇÃO: Gera um número aleatório entre 20.0 e 35.0
        temperatura_simulada = random.uniform(20.0, 35.0)
        umidade_simulada = random.randint(40, 80)
        
        # Mostrando dados com visual bonito (Métricas)
        kpi1, kpi2 = st.columns(2)
        kpi1.metric(
            label="Temperatura",
            value=f"{temperatura_simulada:.1f} °C",
            delta="1.2 °C" # Mostra uma setinha de variação (simulada)
        )
        kpi2.metric(
            label="Umidade",
            value=f"{umidade_simulada} %",
            delta="-5 %"
        )
        
        st.toast("Dados recebidos com sucesso!", icon="✅")
    else:
        st.info("Clique no botão para ler os sensores.")

# -----------------------------------------------------------------------------
# 5. Gráfico em Tempo Real (Simulado)
# -----------------------------------------------------------------------------
st.divider()
st.subheader("📈 Histórico de Temperatura (Últimas Leituras)")

# Criando dados falsos para o gráfico
dados_grafico = [random.uniform(22, 28) for _ in range(10)]

# Exibindo um gráfico de linha simples
st.line_chart(dados_grafico)

# Rodapé
st.markdown("---")
st.caption("Desenvolvido para aula de IoT - Python e Streamlit")