# 🚀 Análise de Desempenho de API

Este projeto é uma aplicação web interativa desenvolvida com **Streamlit** para analisar matematicamente o comportamento do tempo médio de resposta de uma API, conforme a quantidade de requisições por segundo aumenta e se aproxima de sua capacidade crítica.

## 📌 Funcionalidades

- **Análise de Limites (Cálculo):** Utiliza a biblioteca `SymPy` para calcular o limite do tempo de resposta pela esquerda e pela direita quando a API atinge sua capacidade máxima.
- **Simulação de Cargas:** Calcula o tempo exato de resposta (em milissegundos) para diferentes volumes de requisições.
- **Visualização Gráfica:** Gera um gráfico interativo utilizando `Matplotlib` e `NumPy` para ilustrar o crescimento assintótico do tempo de resposta.

## 🧮 O Modelo Matemático

O sistema modela o tempo médio de resposta $T(x)$ em milissegundos em função da quantidade de requisições por segundo $x$, dado pela função:

$$T(x) = \frac{1000}{50 - x}$$

- **x:** Quantidade de requisições por segundo (req/s).
- **T(x):** Tempo médio de resposta da API (ms).
- **Capacidade crítica:** 50 req/s (ponto onde ocorre a assíntota vertical).

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)**
- **[Streamlit](https://streamlit.io/)**: Para a criação da interface web.
- **[SymPy](https://www.sympy.org/)**: Para o cálculo simbólico dos limites.
- **[NumPy](https://numpy.org/)**: Para a geração dos pontos de dados do gráfico.
- **[Matplotlib](https://matplotlib.org/)**: Para a renderização do gráfico de desempenho.

## ⚙️ Como executar o projeto na sua máquina

Siga os passos abaixo para rodar o projeto localmente.

### 1. Pré-requisitos
Certifique-se de ter o **Python** instalado na sua máquina.

### 2. Clone ou baixe o projeto
Se você baixou os arquivos, abra o terminal e navegue até a pasta do projeto:
```bash
cd caminho/para/a/pasta/do/projeto
