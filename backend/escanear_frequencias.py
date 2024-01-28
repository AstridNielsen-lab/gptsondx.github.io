import can
import time

frequencias_detectadas = []

def callback(pkt):
    global frequencias_detectadas

    if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):
        frequencia = pkt[RadioTap].ChannelFrequency
        if frequencia not in frequencias_detectadas:
            frequencias_detectadas.append(frequencia)
            print(f"Frequência detectada: {frequencia} MHz")

def escanear_frequencias():
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    try:
        while True:
            message = bus.recv(timeout=1.0)
            
            if message is not None:
                frequencia = message.arbitration_id
                print(f"Frequência detectada: {frequencia} MHz")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    escanear_frequencias()
