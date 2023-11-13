# Importando libs
import pandas as pd

anos = [2020,2021]
meses = [1,2,3,4,5,6,8,9,10,11,12]

dados_combinados = pd.DataFrame()

for ano in anos:
    x = open("Arquivos_unidos.csv","a")
    for mes in meses:    
        arquivosUnidos = open(f'planilhas/DadosBO_{ano}_{mes}(FURTO DE VEÍCULOS).xls')
        dados_combinados = arquivosUnidos.read()
        #print(dados_combinados)    
        x.write(dados_combinados)