import pandas as pd

df_principal = pd.read_excel("/content/Aula 01_Imersão Python - Tabela de ações pura.xlsx", sheet_name="Principal")
df_total_acoes = pd.read_excel("/content/Aula 01_Imersão Python - Tabela de ações pura.xlsx", sheet_name="Total_de_acoes")
df_tb_chatgpt = pd.read_excel("/content/Aula 01_Imersão Python - Tabela de ações pura.xlsx", sheet_name="ChatGPT")

print("DataFrame Principal:")
print(df_principal)

print("DataFrame Total de Ações:")
print(df_total_acoes)

print("DataFrame ChatGPT:")
print(df_tb_chatgpt)
