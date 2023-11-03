# Importando libs
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import os
import time

# Definindo navegador e url
edge = webdriver.Edge()
edge.get('https://www.ssp.sp.gov.br/transparenciassp/consulta.aspx')

# Clica no botão de furto
edge.find_element(By.ID, 'cphBody_btnFurtoVeiculo').click()

id_anos = ["cphBody_lkAno20", "cphBody_lkAno21", "cphBody_lkAno22"]

# Diretório de download
diretorio_download = r"C:\Users\Leticia\Downloads"

# Cria um DataFrame vazio para armazenar os dados combinados
dados_combinados = pd.DataFrame()

# Itera sobre os anos
for i in range(len(id_anos)):
    # Espera até que o elemento do ano fique visível
    WebDriverWait(edge, 120).until(EC.visibility_of_element_located((By.ID, f'{id_anos[i]}')))
    
    # Cria uma instância de ActionChains para lidar com ações de mouse
    actions = ActionChains(edge)
    
    # Encontra o elemento do ano
    element_ano = edge.find_element(By.ID, f'{id_anos[i]}')
    
    # Move o mouse para o elemento do ano
    actions.move_to_element(element_ano).perform()
    
    # Clica no elemento do ano
    element_ano.click()

    # Itera sobre os meses
    for j in range(12):
        # Espera até que o elemento de bloqueio desapareça
        WebDriverWait(edge, 600).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "blockUI blockOverlay"))
        )
        # Aguarda alguns segundos antes de clicar no mês
        time.sleep(10)  # 10 segundos

        edge.find_element(By.ID, f'cphBody_listMes{j+1}').click()
        edge.find_element(By.ID, 'cphBody_ExportarBOLink').click()

        # Aguarda o download do arquivo e lista os arquivos no diretório de download
        arquivos = os.listdir(diretorio_download)

        # Itera sobre os arquivos no diretório
        for arquivo in arquivos:
            if arquivo.endswith(".xlsx"):  # Verifica se é um arquivo Excel
                caminho_do_arquivo = os.path.join(diretorio_download, arquivo)
                df = pd.read_excel(caminho_do_arquivo)
                dados_combinados = dados_combinados.append(df, ignore_index=True)

# Salva o DataFrame combinado em um arquivo Excel
dados_combinados.to_excel('arquivo_combinado.xlsx', index=False)

# Fecha o navegador
edge.quit()