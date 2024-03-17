import tkinter.filedialog
import csv
import json
import xml.etree.ElementTree as ET

# Die beiden hier geforderten Dateien fanden sich für das Ergebnis 2021
# auf der Webseite der Bundeswahlleiterin unter:
# > Bundestagswahl 2021 > Ergebnisse > Open Data
#
# Die Parteienliste fand sich unter:
# Bereitgestellte Daten > Beschreibende Daten > btw21_parteien.csv
# <https://bundeswahlleiterin.de/dam/jcr/9c660d9e-ef9f-4ec4-8f06-da1d031a2057/btw21_parteien.csv>
parties_csv = tkinter.filedialog.askopenfilename(title="btwNN_parteien.csv", filetypes=[("btwNN_parteien.csv", "*.csv")])
if parties_csv == '':
    exit(0)
# Die Ergebnisse fanden sich unter:
# Ergebnisdateien > Verzeichnis "date" > XML-Dateien > sitze_VV.xml
# https://www.bundeswahlleiterin.de/bundestagswahlen/2021/ergebnisse/opendata/btw21/20210926_hauptwahl/daten/sitze_05.xml
seats_xml = tkinter.filedialog.askopenfilename(title="sitze_x.xml", filetypes=[("sitze_NN.xml", "*.xml")])
if seats_xml == '':
    exit(0)

with open(parties_csv, newline="", encoding = "utf-8-sig") as f:
    reader = csv.DictReader(filter(lambda row: row[0]!='#', f), delimiter=";")
    parties = list(filter(lambda x: x['Gruppenart_XML'] != 'EINZELBEWERBER', reader))

parties_dict = dict(map(lambda x: (x['Gruppenschluessel'], x['Gruppenname_kurz']), parties))

results_dict = {}

tree = ET.parse(seats_xml)
bund = tree.find("Gebiet[@Gebietsart='BUND']")
for sitze in bund.iterfind("SitzeGruppe"):
    gruppe = parties_dict[sitze.attrib['Gruppe']]
    count = sitze.attrib['Gesamt']
    print(f'"{gruppe}": {count},')
