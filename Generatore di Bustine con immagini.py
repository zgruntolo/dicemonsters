import random
from PIL import Image

class Carta:
    def __init__(self, nome, immagine):
        self.nome = nome
        self.immagine = immagine

def crea_lista(lista_nomi):
    vecchia_lista = lista_nomi
    nuova_lista = []
    for nome_carta in vecchia_lista:
        nome_immagine = nome_carta.replace(" ", "_").lower() + ".png"
        nuova_carta = Carta(nome_carta, nome_immagine)
        nuova_lista.append(nuova_carta)
    return nuova_lista

def aprire_bustina(soglia_comune, soglia_non_comune):
    probabilità = random.randint(1, 6)

    if probabilità <= soglia_comune:
        carta = random.choice(comuni)
    elif soglia_comune < probabilità <= soglia_non_comune:
        carta = random.choice(non_comuni)
    else:
        carta = random.choice(rare)

    immagine = Image.open(carta.immagine)
    immagine.show()
    return carta

if __name__ == "__main__":

	comuni = ['Melm Caramel', 'Melm Magimel', 'Melm Shieldmel', 'Pirocinghiale', 'Grenado', 'Insetto Fuliggine', 'Explocactus', 'Cacknight', 'Cacbard', 'Cacpriest' ,'Belladonna Timida', 'Glicine Labirinto (Viticcio Violento)', 'Glicine Labirinto (Viticcio Spinoso)', 'Glicine Labirinto (Viticcio Radice)', 'Glicine Labirinto (Viticcio Protettivo)', 'Glicine Labirinto (Viticcio Magico)', 'Servobot Ripristinatore', 'Servobot Manipolatore', 'Servobot Assistente', 'Golem da Combattimento', 'Pescespina (pesce)', 'Pinnaculeo (pesce)', 'Pinnaiuto (pesce)', 'Pinnascudo (pesce)', 'King Crab (Chela di Protezione)', 'King Crab (Chela di Attacco)', 'King Crab (Chela Magica)', 'Spargitore Micoide', 'Micoide', 'Micoidemante (Micoide)', 'Servobot Caricatore R', 'Servobot Caricatore B', 'Servobot Caricatore V', 'King Melm (mano del comando)', 'King Melm (mano della spada)', 'King Melm (mano dello scudo)', 'Bambola da c. (Arto canalizzatore)', 'Bambola da c. (Arto protettivo)', 'Bambola da c. (Arto multiplo)', 'Bambola da c. (Arto estrapolante)', 'Bambola da c. (testa sacrificale)', 'Bambola da c. (testa subacquea)', 'Bambola da c. (testa batteria)', 'Bambola da c. (magicannone)', 'Bambola da c. (magimortaio)', 'Demidrago (Testa di Fuoco)', 'Demidrago (Testa di Fulmine)', 'Demidrago (Testa di Terra)', 'Demidrago (Testa di Aria)', 'Idrozoa', 'Terrordottero', 'Draco Rosso', 'Draco Verde', 'Draco Blu']
	non_comuni = ['Melm Knightmel', 'Pirocinghiale Capobranco', 'Rovo Senziente', 'Megaservobot Ripristinatore', 'Micoide Alfa', 'Micoidemante Alfa (Micoide)', 'Melm Acemel', 'King Melm', 'Agnello Vegetale', 'Megaservobot Manipolatore', 'Servobot Sabotatore', 'Golem Amplificatore', 'Medusa', 'King Crab', 'Pescebanco (pesce)', 'Bambola da combattimento', 'Aviano delle Bambole', 'Bambola cingolata', 'Bambola da c. (magilaser)', 'Demidrago', 'Terrordottero Parassita', 'Malocchio rosso', 'Malocchio azzurro', 'Malocchio verde', 'Coccatrice', 'Malocchio vitreo', 'Terrordottero cacciacarcasse', 'Demone delle Maree', 'Demone Spinato']
	rare = ['Pirocinghiale Mistico', 'Dinocorno (Unicorno)', 'Fogliacorno (Unicorno)', 'Glicine Labirinto', 'Robocorno (Unicorno)', 'Narvacorno (Unicorno)', 'Spinalodonte (pesce)', 'Pegacorno (Unicorno)', 'Spargitore Micoide Supremo', 'Acchiappadraghi', 'Golem Fortezza', 'Tigre Bianca', 'Demidrago Meccanico', 'Arcanum del Cancello', 'Arcanum del Cielo', 'Arcanum del Forgia', 'Arcanum del Gelo', 'Demone del Baratto', 'Demone del Sacrificio', 'Demone delle Ombre']

	comuni = crea_lista(comuni)
	non_comuni = crea_lista(non_comuni)
	rare = crea_lista(rare)

	bustina = []

	bustina.append(aprire_bustina(3, 5))
	bustina.append(aprire_bustina(3, 5))
	bustina.append(aprire_bustina(2, 5))
	bustina.append(aprire_bustina(2, 4))

	for carta in bustina:
    		print(carta.nome, sep = "\n")