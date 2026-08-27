# %%
import sys
print(sys.executable)
# %%

import pandas as pd
from time import perf_counter
##data wrangler

# %%
emissoes_gases = pd.read_excel('//home//gggcr//Área de trabalho//Aprendendo PANDAS alura//PANDAS-EMISSAO_GAS_ESTUFA//1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name='GEE Estados')

# %%
emissoes_gases.info()

# %%
emissoes_gases.head()

# %%
##AJUSTANDO A BASE DE DADOS

emissoes_gases['Emissão / Remoção / Bunker'].unique()

# %%
##Coletar os dados de 'Remoção NCI' e 'Remoção'
##analisando os dados de remoção para ver se todos são de retirada de gases estufa
(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') |(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')


# %%
emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]
##retorna todos que estão removendo
# %%
emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]
##vendo se ta realmente removendo ou nao filtrando as colunas dos anos
# %%
emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()
##pra identificar se todos os valores são negativos a gente utiliza o max() pra chegar se tem algum valor maior do que 0.
##como retornou so 0 então todos os valores são negativos, ou seja, todos os dados de remoção são realmente de remoção de gases estufa.

# %%
##identificar se algum valor do tipo bunker corresponde a alguma emissao feita por algum estado

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()


#como retornou nulo então está correto
# %%
## substituir a base de dados para somente os de emissão
#equipe de dados não quer informações de remoção e de bunker
emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']
emissoes_gases 
# %%
##como todos os valores se tornaram só de emissão, podemos remover a coluna de 'Emissão / Remoção / Bunker' da base de dados
emissoes_gases = emissoes_gases.drop(columns='Emissão / Remoção / Bunker')
emissoes_gases
# %%
#ncontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar as atividades econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.

#iltre o DataFrame somente com os dados dos Estados da região Sul do Brasil.

#ltre o DataFrame para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a "Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).

#ncontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.

# %%
emissoes_gases['Nível 1 - Setor'].unique()

# %%
emissoes_gases['Estado'].unique()

# %%
emissoes_gases[emissoes_gases['Estado'].isin(['PR', 'RS', 'SC'])]



# %%
#sltere o dataframe para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a "Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).
emissoes_gasesAM = emissoes_gases[(emissoes_gases['Estado'].isin(['AM'])) & emissoes_gases['Nível 1 - Setor'].isin(['Mudança de Uso da Terra e Floresta'])]
emissoes_gasesAM
# %%
#ncontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.
emissoesagropecuaria = emissoes_gases.loc[(emissoes_gases['Estado'].isin(['PA'])) & (emissoes_gases['Nível 1 - Setor'] == 'Agropecuária'), 2021].max()
emissoesagropecuaria
# %%
emissoes_gases.loc[(emissoes_gases['Nível 1 - Setor'] == 'Agropecuária') & (emissoes_gases['Estado'] == 'PA'), 2021].max()
# %%
######ALTERANDO O FORMATO DO DATAFRAME PARA
# ----- UMA UNICA COLUNA COM AS INFORMAÇÕES DOS ANOS
# ----- UMA UNICA COLUNA COM OS DADOS DE EMISSÃO
# %%
# usa : para pegar todas as linhas 
emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns

# %%
colunas_info = list(emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns
)
colunas_info

# %%
emissoes_gases.loc[:,1970:2021].columns
colunas_emissao = list(emissoes_gases.loc[:,1970:2021]).columns
colunas_emissao
# %%
##metodo MELT , transformar muitas colunas 


# %%



# %%


# %%



# %%



# %%



# %%




# %%




# %%





# %%




# %%





# %%





# %%


