import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import xlsxwriter

arquivo_excel = xlsxwriter.Workbook('Senadores.xlsx')
aba = arquivo_excel.add_worksheet()

aba.write(0, 0, "Senador")
aba.write(0, 1, "Partido")
aba.write(0, 2, "UF")
aba.write(0, 3, "Mandato")
aba.write(0, 4, "Telefone")
aba.write(0, 5, "E-Mail")

r = requests.get("http://www25.senado.leg.br/web/senadores/em-exercicio/-/e/por-nome")
soup = bs(r.content,"html.parser")

tabela_senadores = soup.find_all("tr")[1:]

row = 1
col = 0
for linha in tabela_senadores:
    aba.write(row, col,     linha.contents[1].text)
    aba.write(row, col + 1, linha.contents[3].text)
    aba.write(row, col + 2, linha.contents[5].text)
    aba.write(row, col + 3, linha.contents[7].text)
    aba.write(row, col + 4, linha.contents[9].text)
    aba.write(row, col + 5, linha.contents[11].text)
    row += 1

arquivo_excel.close()
