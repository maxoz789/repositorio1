meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso",
             "CREEPY": "aterrador siniestro",
             "XD": "UNA EXPRECION RISA",
            "LOL": "Una respuesta común a algo gracioso",}
           
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict [word])
else:
    print("no se encontro la palabra :c")
