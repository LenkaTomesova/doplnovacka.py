"""
doplnovacka.py 
Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň (jedná se o právní předpisy). Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo, později každé 4. slovo atd., až se text naučí zpaměti. Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zaměnit.

Rozbor 
1 načíst soubor
2 splitnout slova podle mezery do seznamu
3 procházet jednotlivá slova seznamu
  když se jedná o 5-té (10., 15...) slovo:
  procházet písmenka a vytvořit novou proměnnou slovoUpraveno=len(slovo):
  písmenko nahradit pomlčkou
  vynechat interpunkci
  upravené slovo přidat do seznamu
jinak:
cyklus prochází znaky slova, slovoUpraveno += "-"
vysledek.append(slovoUpr.)

else: vysledek.append(prvekseznamu)

původní slovo přidat do seznamu
4 seznam spojit pomocí mezery do řetězce, řetězec uložit do nového souboru

Ukol:
Proveďte optimalizaci kódu programu "doplnovacka.py" tak,
abys problém řešila s využitím vlastní funkce (vstupními parametry bude vložený text
či název souboru, který se má načíst, a celé číslo představující, kolikáté slovo textu
se má zaměnit za hvězdičky). Tuto optimalizovanou verzi nahraj do existujícího projektu
na GitHubu. 
"""
import os.path

vstup = input("Vložte text nebo název souboru, ve kterém chcete vynechat slova: ")
vynechaneSlovo = int(input("Zadejte, kolikáté slovo chcete vynechat: "))
#with open("lorem.txt") as f:
#	text = f.read()
#f.closed

#print(text)
def uprava Textu(text):
	text = text.replace("\n", "# ")
	seznam = []
	seznam = text.split(" ")
	vysledek = []
	interpunkce = ".,?!-;\""
# print(seznam)
	for i in range(0, len(seznam)):
		slovo = seznam[i]
		slovoUpraveno = ""
		if((i + 1) % vynechaneSlovo == 0):
		for pismeno in slovo:
			if pismeno not in interpunkce:
				slovoUpraveno += "*"
			else:
				slovoUpraveno += pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s=" ".join(vysledek)
s=s.replace("#", "\n")
print(s)

jesoubor = os.path.isfile(vstup)
if jeSoubor:
	with open(vstup) as f:
		vstup = f.read()
		upravaTextu(vstup)
else:
	upravaTextu(vstup)