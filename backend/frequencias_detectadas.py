# frequencias_detectadas.py

# Lista global para armazenar frequências detectadas
frequencias_detectadas = []

def adicionar_frequencia(frequencia):
    """
    Adiciona uma frequência à lista global.
    """
    global frequencias_detectadas
    frequencias_detectadas.append(frequencia)

def obter_frequencias():
    """
    Retorna a lista de frequências detectadas.
    """
    global frequencias_detectadas
    return frequencias_detectadas
