# importando libs
from selenium.webdriver.common.by import By
from selenium import webdriver

# definindo navegador e url
driver = webdriver.Edge()
driver.get('https://www.ssp.sp.gov.br/transparenciassp/consulta.aspx')

# clicando no botao de furto
driver.find_element(By.ID, 'cphBody_btnFurtoVeiculo').click()

id_anos = ["cphBody_lkAno20", "cphBody_lkAno21", "cphBody_lkAno22"]

# iterando sobre os anos
for i in range(len(id_anos)):
    driver.find_element(By.ID, f'{id_anos[i]}').click()

    # iterando sobre os meses - percorrendo 1 a 12 nos ids
    for i in range(12):
        driver.find_element(By.ID, f'cphBody_listMes{i+1}').click()
        driver.find_element(By.ID, 'cphBody_ExportarBOLink').click()