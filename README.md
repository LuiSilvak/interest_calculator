# Calculadora de Juros Compostos em Python

Esta calculadora simples permite calcular o valor futuro de um investimento ou empréstimo utilizando a fórmula de juros compostos.


## Funcionalidades

- Calcula o valor futuro de um investimento baseado em:
  - Capital inicial.
  - Taxa de juros (%).
  - Número de períodos.
- Exibe o resultado formatado em reais com duas casas decimais.
- Trata entradas inválidas.


## Requisitos

- Python 3.x


## Como Usar

1. Clone o repositório:
   
```bash
git clone https://github.com/LuiSilvak/interest_calculator.git 
cd interest_calculator
```


2. Execute o programa:

```bash
python interest_calculator.py
```

3. Siga as instruções no terminal para:

- Inserir o capital inicial, taxa de juros e número de períodos.
- Visualizar o valor futuro.


## Exemplo de Execução

```bash
=== Calculadora de Juros Compostos ===
Digite o capital inicial (em R$): 5000
Digite a taxa de juros (em % ao período): 2
Digite o número de períodos: 24

Valor Futuro: R$8191.94
```

## Melhorias Futuras

- Adicionar suporte para calcular o montante acumulado em intervalos personalizados.
- Criar uma interface gráfica utilizando Tkinter ou PyQt.
- Exportar os cálculos para um arquivo CSV.


## Licença

Este projeto está licenciado sob a MIT License.