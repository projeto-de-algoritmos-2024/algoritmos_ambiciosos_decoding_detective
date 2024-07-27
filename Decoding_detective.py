import random as rd
from huffman import compressao, descompressao

WORDS = ["decoding", "detective", "huffman"]
# WORD_SELECTED = rd.choice(WORDS)
WORD_SELECTED = "decoding"

word_codificada, codigos = compressao(WORD_SELECTED)
word_descodificada = descompressao(word_codificada, codigos)

print(f"A palavra é {WORD_SELECTED}")
print(f"Texto Codificado: {word_codificada}")
print(f"Códigos: {codigos}")
print(f"Texto descodificado: {word_descodificada}")