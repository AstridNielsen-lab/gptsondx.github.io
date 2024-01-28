from flask import Flask, render_template, jsonify
from flask import Blueprint
import threading
import can
from scapy.all import sniff, RadioTap, Dot11
import curses

# Crie o Blueprint 'tecnologia_bp'
tecnologia_bp = Blueprint('tecnologia_bp', __name__, template_folder='templates', static_folder='static')

app = Flask(__name__, template_folder='backend/templates')
app.register_blueprint(tecnologia_bp, url_prefix='/tecnologia')  # Adicione um prefixo à URL do Blueprint

frequencias_detectadas = []
informacoes_escaneadas = []  # Adicione esta lista para armazenar informações

stop_rastreamento = threading.Event()
lock = threading.Lock()

def rastrear_frequencias(stdscr):
    global frequencias_detectadas, informacoes_escaneadas
    curses.curs_set(0)
    stdscr.clear()

    # Adicione a configuração do barramento CAN para 3G, 4G e 5G
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    try:
        while not stop_rastreamento.is_set():
            message = bus.recv(timeout=1.0)

            with lock:
                if message is not None:
                    frequencia = message.arbitration_id
                    frequencias_detectadas.append(frequencia)
                    # Processar informações conforme necessário
                    informacao = f"Nova informação: {frequencia}"
                    informacoes_escaneadas.append(informacao)
    except KeyboardInterrupt:
        pass

def callback(pkt):
    global frequencias_detectadas

    with lock:
        if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):
            frequencia = pkt[RadioTap].ChannelFrequency
            frequencias_detectadas.append(frequencia)

# Atualize a rota para a página inicial
@app.route('/')
def home():
    with lock:
        return render_template('index.html')

# Atualize a rota para exibir as informações escaneadas
@app.route('/informacoes', methods=['GET'])
def obter_informacoes():
    with lock:
        return jsonify({"informacoes": informacoes_escaneadas})

# Adicione a rota para escanear
@app.route('/escanear', methods=['GET'])
def escanear_frequencias():
    global stop_rastreamento
    stop_rastreamento.clear()

    # Inicia a captura de pacotes Wi-Fi
    sniff(prn=callback, store=0)

    return jsonify({"status": "Rastreamento iniciado"})

# Adicione a rota para parar o rastreamento
@app.route('/parar', methods=['GET'])
def parar_rastreamento():
    global stop_rastreamento
    stop_rastreamento.set()

    return jsonify({"status": "Rastreamento interrompido"})

if __name__ == '__main__':
    app.run(debug=True)
