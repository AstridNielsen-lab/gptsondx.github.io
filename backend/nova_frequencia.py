# nova_frequencia.py

from frequencias_detectadas import adicionar_frequencia

def callback(pkt):
    """
    Callback para processar pacotes e adicionar novas frequências à lista global.
    """
    if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11):
        frequencia = pkt[RadioTap].ChannelFrequency
        adicionar_frequencia(frequencia)
        print(f"Frequência detectada: {frequencia} MHz")

def escanear_nova_frequencia():
    """
    Inicia o escaneamento para detectar novas frequências.
    """
    sniff(iface="wlan0", prn=callback, store=0)

if __name__ == "__main__":
    # Exemplo de uso
    escanear_nova_frequencia()
