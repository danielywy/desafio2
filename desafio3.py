import statistics
import time

produtos = {
    "Produto1": 10, "Produto2": 15, "Produto3": 20, "Produto4": 15, "Produto5": 25,
    "Produto6": 30, "Produto7": 35, "Produto8": 40, "Produto9": 20, "Produto10": 15,
    "Produto11": 45, "Produto12": 30, "Produto13": 25, "Produto14": 20, "Produto15": 15,
    "Produto16": 50, "Produto17": 40, "Produto18": 35, "Produto19": 30, "Produto20": 25,
    "Produto21": 10, "Produto22": 15, "Produto23": 20, "Produto24": 25, "Produto25": 30,
    "Produto26": 35, "Produto27": 40, "Produto28": 45, "Produto29": 50, "Produto30": 55
}

valores = []
for valor in produtos.values():
    valores.append(valor)

print("Valores:", valores)

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    return statistics.multimode(lista)  

def calcular_variancia(lista):
    return statistics.variance(lista)

def calcular_desvio_padrao(lista):
    return statistics.stdev(lista)

def calcular_amplitude(lista):
    return max(lista) - min(lista)

print("\n   Estatísticas     ")
time.sleep(0.5)
print("Média:", calcular_media(valores))
time.sleep(0.5)
print("Mediana:", calcular_mediana(valores))
time.sleep(0.5)
print("Moda:", calcular_moda(valores))
time.sleep(0.5)
print("Variância:", calcular_variancia(valores))
time.sleep(0.5)
print("Desvio padrão:", calcular_desvio_padrao(valores))
time.sleep(0.5)
print("Amplitude:", calcular_amplitude(valores))
time.sleep(2)


print("\n   Perguntas   ")
time.sleep(0.5)
print("1. Diferença entre média e mediana:")
time.sleep(0.5)
print("- Média é a soma de todos os valores dividida pela quantidade total.")
time.sleep(0.5)
print("- Mediana é o valor central da lista ordenada. Menos sensível a valores extremos.")
time.sleep(0.5)
print("\n2. Por que a moda é importante?")
time.sleep(0.5)
print("- Indica o valor mais frequente, útil para identificar padrões comuns.")
time.sleep(0.5)
print("\n3. Significado da variância:")
time.sleep(0.5)
print("- Mede a dispersão dos dados em relação à média. Quanto maior, mais espalhados.")
time.sleep(0.5)
print("\n4. Relação entre desvio padrão e variância:")
time.sleep(0.5)
print("- Desvio padrão é a raiz quadrada da variância. Ambos medem a dispersão dos dados.")
