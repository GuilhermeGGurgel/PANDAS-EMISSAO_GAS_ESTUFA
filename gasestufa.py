import pandas as pd
from time import perf_counter


print("Iniciando a leitura...")
inicio = perf_counter()

emissoes_gases = pd.read_excel('C:\\Users\\guilh\\Documents\\GitHub\\PANDAS-EMISSAO_GAS_ESTUFA\\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name='GEE Estados')

print(f"Arquivo carregado em {perf_counter() - inicio:.1f} segundos")
print("Dimensões:", emissoes_gases.shape)
print(emissoes_gases.head())


