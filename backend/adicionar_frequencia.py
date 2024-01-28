# adicionar_frequencia.py

from frequencias_detectadas import adicionar_frequencia

def adicionar_frequencia_nova(frequencia):
    """
    Adiciona uma nova frequência à lista global de frequências detectadas.
    """
    adicionar_frequencia(frequencia)
    print(f"Frequência adicionada: {frequencia} MHz")

if __name__ == "__main__":
    # Exemplo de uso
    nova_frequencia = 2450  # Substitua isso pela frequência que deseja adicionar
    adicionar_frequencia_nova(nova_frequencia)
