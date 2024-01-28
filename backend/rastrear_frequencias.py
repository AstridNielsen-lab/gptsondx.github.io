from scapy.all import *

frequencias_detectadas = []

def callback(pkt):
    global frequencias_detectadas

    if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):
        frequencia = pkt[RadioTap].ChannelFrequency
        if frequencia not in frequencias_detectadas:
            frequencias_detectadas.append(frequencia)
            print(f"Frequência detectada: {frequencia} MHz")

def escanear_frequencias():
    sniff(iface="wlan0", prn=callback, store=0)

if __name__ == "__main__":
    escanear_frequencias()
