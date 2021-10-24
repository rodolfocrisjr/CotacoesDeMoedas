from selenium import webdriver

# Passo 1: Pesquisar a cotação do Dólar
navegador = webdriver.Chrome("chromedriver.exe")
navegador.get("https://dolarhoje.com/")
valor_dolar = navegador.find_element_by_xpath('//*[@id="nacional"]').get_attribute("value")
valor_dolar = valor_dolar.replace(",",".")
print(f'A cotação atual do Dólar é: R$ {valor_dolar}')

# Passo 2: Pesquisar a cotação do Euro
navegador.get("https://dolarhoje.com/euro-hoje/")
valor_euro = navegador.find_element_by_xpath('//*[@id="nacional"]').get_attribute("value")
valor_euro = valor_euro.replace(",",".")
print(f'A cotação atual do Euro é: R$ {valor_euro}')

# Passo 3: Pesquisar a cotação do Ouro
navegador.get("https://dolarhoje.com/ouro-hoje/")
valor_ouro = navegador.find_element_by_xpath('//*[@id="nacional"]').get_attribute("value")
valor_ouro = valor_ouro.replace(",",".")
print(f'A cotação atual do Ouro é: R$ {valor_ouro}')