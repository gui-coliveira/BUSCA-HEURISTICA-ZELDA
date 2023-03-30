tipo_terreno = {
    "g": "GRAMA",
    "a": "AREIA",
    "f": "FLORESTA",
    "m": "MONTANHA",
    "w": "AGUA"
}

terreno = []
dungeon1 = []
dungeon2 = []
dungeon3 = []

with open("./ambiente/terreno.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caracter in linha:
            if caracter != '\n':
                temp.append(tipo_terreno[caracter])
        terreno.append(temp)

with open("./ambiente/dungeon1.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caracter in linha:
            if caracter != '\n':
                temp.append(tipo_terreno[caracter])
        dungeon1.append(temp)

with open("./ambiente/dungeon2.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caracter in linha:
            if caracter != '\n':
                temp.append(tipo_terreno[caracter])
        dungeon2.append(temp)

with open("./ambiente/dungeon3.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caracter in linha:
            if caracter != '\n':
                temp.append(tipo_terreno[caracter])
        dungeon3.append(temp)

def retorna_terreno():
    return terreno

def retorna_dungeon1():
    return dungeon1

def retorna_dungeon2():
    return dungeon2

def retorna_dungeon3():
    return dungeon3