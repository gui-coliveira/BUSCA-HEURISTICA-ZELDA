def converte_terreno(terreno, converte_variavel):
    terreno_convertido= []
    for linha in terreno:
        linha_convertida = []
        for item in linha:
            linha_convertida.append(converte_variavel[item])
        terreno_convertido.append(linha_convertida)
    return terreno_convertido