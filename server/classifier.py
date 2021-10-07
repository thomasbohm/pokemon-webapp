import torch
from torchvision import models, transforms
from PIL import Image

class Classifier:
    def __init__(self):
        self.model = models.mobilenet_v3_large(pretrained=False, progress=False)
        self.model.load_state_dict(torch.load('./best.pt', map_location=torch.device('cpu')))
        self.model.eval()

        self.transform = transforms.Compose([transforms.Resize((256, 256)), 
                                             transforms.ToTensor(),
                                             transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                  std=[0.229, 0.224, 0.225])])
    
    def classify(self, img_path):
        img = Image.open(img_path)
        with torch.no_grad():
            img = self.transform(img).unsqueeze(0)
            pred = self.model(img)

            pokemon_id = int(pred.argmax() +1)

        return pokemon_id, *POKEMON_NAMES[pokemon_id]

POKEMON_NAMES = {
    1: ('Bulbasaur', 'Bisasam'),
    2: ('Ivysaur', 'Bisaknosp'),
    3: ('Venusaur', 'Bisaflor'),
    4: ('Charmander', 'Glumanda'),
    5: ('Charmeleon', 'Glutexo'),
    6: ('Charizard', 'Glurak'),
    7: ('Squirtle', 'Schiggy'),
    8: ('Wartortle', 'Schillok'),
    9: ('Blastoise', 'Turtok'),
    10: ('Caterpie', 'Raupy'),
    11: ('Metapod', 'Safcon'),
    12: ('Butterfree', 'Smettbo'),
    13: ('Weedle', 'Hornliu'),
    14: ('Kakuna', 'Kokuna'),
    15: ('Beedrill', 'Bibor'),
    16: ('Pidgey', 'Taubsi'),
    17: ('Pidgeotto', 'Tauboga'),
    18: ('Pidgeot', 'Tauboss'),
    19: ('Rattata', 'Rattfratz'),
    20: ('Raticate', 'Rattikarl'),
    21: ('Spearow', 'Habitak'),
    22: ('Fearow', 'Ibitak'),
    23: ('Ekans', 'Rettan'),
    24: ('Arbok', 'Arbok'),
    25: ('Pikachu', 'Pikachu'),
    26: ('Raichu', 'Raichu'),
    27: ('Sandshrew', 'Sandan'),
    28: ('Sandslash', 'Sandamer'),
    29: ('Nidoran♀', 'Nidoran♀'),
    30: ('Nidorina', 'Nidorina'),
    31: ('Nidoqueen', 'Nidoqueen'),
    32: ('Nidoran♂', 'Nidoran♂'),
    33: ('Nidorino', 'Nidorino'),
    34: ('Nidoking', 'Nidoking'),
    35: ('Clefairy', 'Piepi'),
    36: ('Clefable', 'Pixi'),
    37: ('Vulpix', 'Vulpix'),
    38: ('Ninetales', 'Vulnona'),
    39: ('Jigglypuff', 'Pummeluff'),
    40: ('Wigglytuff', 'Knuddeluff'),
    41: ('Zubat', 'Zubat'),
    42: ('Golbat', 'Golbat'),
    43: ('Oddish', 'Myrapla'),
    44: ('Gloom', 'Duflor'),
    45: ('Vileplume', 'Giflor'),
    46: ('Paras', 'Paras'),
    47: ('Parasect', 'Parasek'),
    48: ('Venonat', 'Bluzuk'),
    49: ('Venomoth', 'Omot'),
    50: ('Diglett', 'Digda'),
    51: ('Dugtrio', 'Digdri'),
    52: ('Meowth', 'Mauzi'),
    53: ('Persian', 'Snobilikat'),
    54: ('Psyduck', 'Enton'),
    55: ('Golduck', 'Entoron'),
    56: ('Mankey', 'Menki'),
    57: ('Primeape', 'Rasaff'),
    58: ('Growlithe', 'Fukano'),
    59: ('Arcanine', 'Arkani'),
    60: ('Poliwag', 'Quapsel'),
    61: ('Poliwhirl', 'Quaputzi'),
    62: ('Poliwrath', 'Quappo'),
    63: ('Abra', 'Abra'),
    64: ('Kadabra', 'Kadabra'),
    65: ('Alakazam', 'Simsala'),
    66: ('Machop', 'Machollo'),
    67: ('Machoke', 'Maschock'),
    68: ('Machamp', 'Machomei'),
    69: ('Bellsprout', 'Knofensa'),
    70: ('Weepinbell', 'Ultrigaria'),
    71: ('Victreebel', 'Sarzenia'),
    72: ('Tentacool', 'Tentacha'),
    73: ('Tentacruel', 'Tentoxa'),
    74: ('Geodude', 'Kleinstein'),
    75: ('Graveler', 'Georok'),
    76: ('Golem', 'Geowaz'),
    77: ('Ponyta', 'Ponita'),
    78: ('Rapidash', 'Gallopa'),
    79: ('Slowpoke', 'Flegmon'),
    80: ('Slowbro', 'Lahmus'),
    81: ('Magnemite', 'Magnetilo'),
    82: ('Magneton', 'Magneton'),
    83: ("Farfetch'd", 'Porenta'),
    84: ('Doduo', 'Dodu'),
    85: ('Dodrio', 'Dodri'),
    86: ('Seel', 'Jurob'),
    87: ('Dewgong', 'Jugong'),
    88: ('Grimer', 'Sleima'),
    89: ('Muk', 'Sleimok'),
    90: ('Shellder', 'Muschas'),
    91: ('Cloyster', 'Austos'),
    92: ('Gastly', 'Nebulak'),
    93: ('Haunter', 'Alpollo'),
    94: ('Gengar', 'Gengar'),
    95: ('Onix', 'Onix'),
    96: ('Drowzee', 'Traumato'),
    97: ('Hypno', 'Hypno'),
    98: ('Krabby', 'Krabby'),
    99: ('Kingler', 'Kingler'),
    100: ('Voltorb', 'Voltobal'),
    101: ('Electrode', 'Lektrobal'),
    102: ('Exeggcute', 'Owei'),
    103: ('Exeggutor', 'Kokowei'),
    104: ('Cubone', 'Tragosso'),
    105: ('Marowak', 'Knogga'),
    106: ('Hitmonlee', 'Kicklee'),
    107: ('Hitmonchan', 'Nockchan'),
    108: ('Lickitung', 'Schlurp'),
    109: ('Koffing', 'Smogon'),
    110: ('Weezing', 'Smogmog'),
    111: ('Rhyhorn', 'Rihorn'),
    112: ('Rhydon', 'Rizeros'),
    113: ('Chansey', 'Chaneira'),
    114: ('Tangela', 'Tangela'),
    115: ('Kangaskhan', 'Kangama'),
    116: ('Horsea', 'Seeper'),
    117: ('Seadra', 'Seemon'),
    118: ('Goldeen', 'Goldini'),
    119: ('Seaking', 'Golking'),
    120: ('Staryu', 'Sterndu'),
    121: ('Starmie', 'Starmie'),
    122: ('Mr. Mime', 'Pantimos'),
    123: ('Scyther', 'Sichlor'),
    124: ('Jynx', 'Rossana'),
    125: ('Electabuzz', 'Elektek'),
    126: ('Magmar', 'Magmar'),
    127: ('Pinsir', 'Pinsir'),
    128: ('Tauros', 'Tauros'),
    129: ('Magikarp', 'Karpador'),
    130: ('Gyarados', 'Garados'),
    131: ('Lapras', 'Lapras'),
    132: ('Ditto', 'Ditto'),
    133: ('Eevee', 'Evoli'),
    134: ('Vaporeon', 'Aquana'),
    135: ('Jolteon', 'Blitza'),
    136: ('Flareon', 'Flamara'),
    137: ('Porygon', 'Porygon'),
    138: ('Omanyte', 'Amonitas'),
    139: ('Omastar', 'Amoroso'),
    140: ('Kabuto', 'Kabuto'),
    141: ('Kabutops', 'Kabutops'),
    142: ('Aerodactyl', 'Aerodactyl'),
    143: ('Snorlax', 'Relaxo'),
    144: ('Articuno', 'Arktos'),
    145: ('Zapdos', 'Zapdos'),
    146: ('Moltres', 'Lavados'),
    147: ('Dratini', 'Dratini'),
    148: ('Dragonair', 'Dragonir'),
    149: ('Dragonite', 'Dragoran'),
    150: ('Mewtwo', 'Mewtu'),
    151: ('Mew', 'Mew')
}