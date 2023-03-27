tipo_terreno = {
    "g":"GRAMA",
    "a":"AREIA",
    "f":"FLORESTA",
    "m":"MONTANHA",
    "w":"AGUA"
}

terreno =[]

with open("/home/driven/Documentos/Uesb/IA/BUSCA-HEURISTICA-ZELDA/ambiente/terreno.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp=[]
        for caracter in linha:
            if caracter != '\n':
                temp.append(tipo_terreno[caracter])
        terreno.append(temp)

def retorna_terreno():
    return terreno