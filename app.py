import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def tempo_resposta(x):
    return 1000 / (50 - x)


# ==========================================
# 1. CABEÇALHO E DESCRIÇÃO DA INTERFACE
# ==========================================
st.title("Análise de Desempenho de API")

st.write(
    """
    Esta aplicação permite analisar o comportamento do tempo médio
    de resposta de uma API conforme aumenta a quantidade de
    requisições por segundo.
    """
)

st.markdown("""
### Variáveis do modelo

- **x:** quantidade de requisições por segundo (req/s)
- **T(x):** tempo médio de resposta da API (ms)
- **Capacidade crítica:** 50 req/s
""")

st.divider()


# ==========================================
# 2. DEFINIÇÃO DE FUNÇÕES E LÓGICA (SYMPY)
# ==========================================

carga = st.slider(
    "Quantidade de requisições por segundo",
    min_value=1.0,
    max_value=49.9,
    value=30.0,
    step=0.1
)

tempo = tempo_resposta(carga)

st.metric(
    "Tempo médio de resposta previsto",
    f"{tempo:.2f} ms"
)

# Lógica de alerta com base na carga
if carga >= 45:
    st.warning(
        "Atenção: a carga está na região crítica do modelo."
    )
else:
    st.success(
        "A carga está abaixo da região crítica."
    )

# Lógica de alerta com base no SLA
sla = 200

if tempo <= sla:
    st.success(
        f"O tempo previsto está dentro do SLA de {sla} ms."
    )
else:
    st.error(
        f"O tempo previsto ultrapassa o SLA de {sla} ms."
    )

# ==========================================
# 3. SEÇÃO INFORMATIVA: ANÁLISE DE LIMITES E SIMULAÇÃO DE CARGAS 
# =========================================
x = sp.symbols('x')
T = 1000 / (50 - x)

limite_esquerda = sp.limit(T, x, 50, dir='-')
limite_direita = sp.limit(T, x, 50, dir='+')

st.subheader("Simulação de Limites")
st.write(f"**Limite à esquerda** de T(x) quando x se aproxima de 50: `{limite_esquerda}`")
st.write(f"**Limite à direita** de T(x) quando x se aproxima de 50: `{limite_direita}`")

st.subheader("Simulação de Cargas")
cargas = [10, 20, 30, 40, 45, 48, 49, 49.5, 49.9]

for carga in cargas:
    tempo = tempo_resposta(carga)
    st.text(f"{carga} req/s -> {tempo:.2f} ms")


# ==========================================
# 4. EXIBIÇÃO GRÁFICA DOS RESULTADOS MATEMÁTICOS
# =========================================

st.subheader("Representação Gráfica")

x_valores = np.linspace(0, 49.9, 500)
y_valores = tempo_resposta(x_valores)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    x_valores,
    y_valores,
    label="T(x) = 1000 / (50 - x)"
)

ax.axvspan(
    45,
    50,
    alpha=0.2,
    label="Região crítica"
)

ax.axvline(
    50,
    linestyle="--",
    label="Assíntota x = 50"
)

ax.scatter(
    carga,
    tempo,
    s=80,
    label=f"Carga selecionada: {carga:.1f} req/s"
)

ax.set_xlabel("Requisições por segundo")
ax.set_ylabel("Tempo médio de resposta (ms)")
ax.set_title("Comportamento do tempo de resposta da API")
ax.legend()
ax.grid(True)

st.pyplot(fig)