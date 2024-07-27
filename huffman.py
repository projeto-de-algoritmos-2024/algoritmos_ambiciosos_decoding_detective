from heapq import heapify, heappush, heappop
from collections import Counter

class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.left = None
        self.right = None
    
    def __lt__(self, no):
        return self.frequencia < no.frequencia

def arvore_huffman(word):
    frequencia_caracteres = Counter(word)

    heap = [No(caractere, frequencia) for caractere, frequencia in frequencia_caracteres.items()]
    heapify(heap)

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merge = No(None, left.frequencia + right.frequencia)
        merge.left = left
        merge.right = right
        heappush(heap, merge)
    
    return heappop(heap)

def geracao_codigo(raiz):
    codigo = {}

    def code(no_atual : No, no : No):
        if no_atual is not None:
            if no_atual.caractere is not None:
                codigo[no_atual.caractere] = no
            code(no_atual.left, no + "0")
            code(no_atual.right, no + "1")
    
    code(raiz, "")
    
    return codigo

def compressao(word):
    raiz = arvore_huffman(word)
    code = geracao_codigo(raiz)

    word_codificada = ''.join(code[caractere] for caractere in word)

    return word_codificada, code

def descompressao(word_codificada, code : Counter):
    codigo_reverso = {c: k for k, c in code.items()}
    
    codigo = ""
    word = ""

    for bit in word_codificada:
        codigo += bit
        if codigo in codigo_reverso:
            word += codigo_reverso[codigo]
            codigo = ""
    
    return word