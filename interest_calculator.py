# Calculadora de Juros Compostos

def calcular_juros_compostos(capital, taxa, periodos):
    return capital * (1 + taxa / 100) ** periodos

def calculadora_juros_compostos():
    print("=== Calculadora de Juros Compostos ===")
    try:
        capital = float(input("Digite o capital inicial (em R$): "))
        taxa = float(input("Digite a taxa de juros (em % ao período): "))
        periodos = int(input("Digite o número de períodos: "))

        valor_futuro = calcular_juros_compostos(capital, taxa, periodos)
        print(f"\nValor Futuro: R${valor_futuro:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


if __name__ == "__main__":
    calculadora_juros_compostos()