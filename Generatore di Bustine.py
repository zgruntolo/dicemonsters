import random

def creazione_bustina(soglie, carte):
    rarita_scelta = random.choices(list(carte.keys()), weights=soglie)[0]
    carta_scelta = random.choice(carte[rarita_scelta])
    return carta_scelta

def aprire_bustina():
    carte = {
        "comune": ['Melm Caramel', 'Melm Magimel', 'Melm Shieldmel', 'Pirocinghiale', 'Grenado', 'Insetto Fuliggine', 'Explocactus', 'Cacknight', 'Cacbard', 'Cacpriest' ,'Belladonna Timida', 'Glicine Labirinto (Viticcio Violento)', 'Glicine Labirinto (Viticcio Spinoso)', 'Glicine Labirinto (Viticcio Radice)', 'Glicine Labirinto (Viticcio Protettivo)', 'Glicine Labirinto (Viticcio Magico)', 'Servobot Ripristinatore', 'Servobot Manipolatore', 'Servobot Assistente', 'Golem da Combattimento', 'Pescespina (pesce)', 'Pinnaculeo (pesce)', 'Pinnaiuto (pesce)', 'Pinnascudo (pesce)', 'King Crab (Chela di Protezione)', 'King Crab (Chela di Attacco)', 'King Crab (Chela Magica)', 'Spargitore Micoide', 'Micoide', 'Micoidemante (Micoide)', 'Servobot Caricatore R', 'Servobot Caricatore B', 'Servobot Caricatore V', 'King Melm (mano del comando)', 'King Melm (mano della spada)', 'King Melm (mano dello scudo)', 'Bambola da c. (Arto canalizzatore)', 'Bambola da c. (Arto protettivo)', 'Bambola da c. (Arto multiplo)', 'Bambola da c. (Arto estrapolante)', 'Bambola da c. (testa sacrificale)', 'Bambola da c. (testa subacquea)', 'Bambola da c. (testa batteria)', 'Bambola da c. (magicannone)', 'Bambola da c. (magimortaio)', 'Demidrago (Testa di Fuoco)', 'Demidrago (Testa di Fulmine)', 'Demidrago (Testa di Terra)', 'Demidrago (Testa di Aria)', 'Idrozoa', 'Terrordottero', 'Draco Rosso', 'Draco Verde', 'Draco Blu'],
        "non_comune": ['Melm Knightmel', 'Pirocinghiale Capobranco', 'Rovo Senziente', 'Megaservobot Ripristinatore', 'Micoide Alfa', 'Micoidemante Alfa (Micoide)', 'Melm Acemel', 'King Melm', 'Agnello Vegetale', 'Megaservobot Manipolatore', 'Servobot Sabotatore', 'Golem Amplificatore', 'Medusa', 'King Crab', 'Pescebanco (pesce)', 'Bambola da combattimento', 'Aviano delle Bambole', 'Bambola cingolata', 'Bambola da c. (magilaser)', 'Demidrago', 'Terrordottero Parassita', 'Malocchio rosso', 'Malocchio azzurro', 'Malocchio verde', 'Coccatrice', 'Malocchio vitreo', 'Terrordottero cacciacarcasse', 'Demone delle Maree', 'Demone Spinato'],
        "rara": ['Pirocinghiale Mistico', 'Dinocorno (Unicorno)', 'Fogliacorno (Unicorno)', 'Glicine Labirinto', 'Robocorno (Unicorno)', 'Narvacorno (Unicorno)', 'Spinalodonte (pesce)', 'Pegacorno (Unicorno)', 'Spargitore Micoide Supremo', 'Acchiappadraghi', 'Golem Fortezza', 'Tigre Bianca', 'Demidrago Meccanico', 'Arcanum del Cancello', 'Arcanum del Cielo', 'Arcanum del Forgia', 'Arcanum del Gelo', 'Demone del Baratto', 'Demone del Sacrificio', 'Demone delle Ombre']
    }

    soglie = [(3, 2, 1), (3, 2, 1), (2, 3, 1), (1, 3, 2)]

    bustina = [creazione_bustina(soglie, carte) for soglie in soglie]

    for carta in bustina:
        print(f"{carta}")

if __name__ == "__main__":
    aprire_bustina()