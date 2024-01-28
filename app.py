from scapy.all import sniff, RadioTap, Dot11
from flask import Flask, jsonify, render_template
import threading
import can  # Importa o módulo para interagir com o barramento CAN

app = Flask(__name__, template_folder='backend/templates')

@app.route('/')
def index():
    return render_template('index.html')

frequencias_detectadas = []
stop_rastreamento = threading.Event()
lock = threading.Lock()

def rastrear_frequencias():
    global frequencias_detectadas
    global stop_rastreamento

    # Adicione a configuração do barramento CAN para 3G e 4G
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    while not stop_rastreamento.is_set():
        message = bus.recv(timeout=1.0)

        with lock:
            if message is not None:
                frequencia = message.arbitration_id
                if frequencia not in frequencias_detectadas:
                    frequencias_detectadas.append(frequencia)
                    print(f"Frequência detectada: {frequencia} MHz")

def callback(pkt):
    global frequencias_detectadas

    with lock:
        if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):
            frequencia = pkt[RadioTap].ChannelFrequency
            if frequencia not in frequencias_detectadas:
                frequencias_detectadas.append(frequencia)
                print(f"Frequência detectada: {frequencia} MHz")

@app.route('/escanear', methods=['GET'])
def escanear_frequencias():
    global stop_rastreamento
    stop_rastreamento.clear()

    t = threading.Thread(target=rastrear_frequencias)
    t.start()

    return jsonify({"status": "Rastreamento iniciado"})

@app.route('/parar', methods=['GET'])
def parar_rastreamento():
    global stop_rastreamento
    stop_rastreamento.set()

    return jsonify({"status": "Rastreamento interrompido"})

@app.route('/frequencias', methods=['GET'])
def obter_frequencias():
    with lock:
        return jsonify({"frequencias": frequencias_detectadas})

if __name__ == '__main__':
    app.run(debug=True)
