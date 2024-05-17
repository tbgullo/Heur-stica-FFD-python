import math

class pattern:
    def __init__(self, id, cost, type, fill, lengh, freq):
        self.id = id
        self.cost = cost
        self.type = type
        self.fill = fill
        self.lengh = lengh
        self.freq = freq

class pattern_k:
    def __init__(self, id, cost, typeS ,typeK, fill, lengh, freq):
        self.id = id
        self.cost = cost
        self.typeS = typeS
        self.typeK = typeK
        self.fill = fill
        self.lengh = lengh
        self.freq = freq

def FFD_js(l,m, L):

    item_sorted = sorted(l, key=lambda x : -x)     #Ordena o tamanho dos itens em decrescente
    padroes = []
    id_aux = 0

    for object in L: 

        for i in range(m):
            Perda = []
            linha = [0.0] * m

            valor_aux = object / item_sorted[i]
            valor = math.floor(valor_aux)
            valor = (valor * 10) / 10
            linha[l.index(item_sorted[i])] = valor

            object_tam = object - valor * item_sorted[i]
            object_aux = object_tam

            for j in range(i+1, m):

                object_tam = object_aux

                valor_aux = object_tam / item_sorted[j]
                valor = math.floor(valor_aux)
                valor = (valor * 10) / 10
                

                object_tam = object_tam - valor * item_sorted[j]


                if valor != 0 or object_tam>=0 :
                    linha[l.index(item_sorted[j])] = valor
                    object_aux = object_tam

                else:
                    break

            new_pattern = pattern(id= id_aux, cost= object_aux, type=L.index(object) + 1, fill=linha, lengh=object, freq= 0)
            padroes.append(new_pattern)
            id_aux += 1

    padroes = [padroes for padroes in padroes if padroes.cost >= 0]
    return padroes  

def FFD_jsk(l, L, R, S):

    item_sorted = sorted(l, key=lambda x : -x)     #Ordena o tamanho dos itens em decrescente
    padroes = []
    id_aux = 0

    for object in range (S-1): 

        for retalhos in range (1,R):

            for i in range(m):

                Perda = []
                linha = [0.0] * m

                valor_aux = (L[object] - L[retalhos]) / item_sorted[i]
                valor = math.floor(valor_aux)
                valor = (valor * 10) / 10
                linha[l.index(item_sorted[i])] = valor

                object_tam = (L[object] - L[retalhos]) - valor * item_sorted[i]
                object_aux = object_tam
        
                
                for j in range(i+1, m):
                    
                    object_tam = object_aux

                    valor_aux = object_tam / item_sorted[j]
                    valor = math.floor(valor_aux)
                    valor = (valor * 10) / 10
                    

                    object_tam = object_tam - valor * item_sorted[j]

                    if valor != 0 or object_tam >=0 :
                        linha[l.index(item_sorted[j])] = valor
                        object_aux = object_tam

                    else:
                        break   
                    
                new_pattern = pattern_k(id= id_aux, cost= object_aux, typeK= retalhos , typeS = object + 1, fill=linha, lengh=L[retalhos], freq= 0)
                padroes.append(new_pattern)
                id_aux += 1
                
    padroes = [padroes for padroes in padroes if padroes.cost >= 0]
    return padroes  

# Dados do problema
    
S = 2       #objetos +1         #Objetos
R = 4       #retalhos +1        #Retalhos
L = [1000,     400, 500,600]        #Comprimento obj/retalho
e = [100000,  3,3,3]            #Estoque
U = 12

m = 15                         #Itens


l= [395, 220, 184, 326, 313, 173, 275, 320, 159, 200, 339, 212, 304, 218, 244]
d= [10, 15, 37, 40, 41, 21, 33, 49, 30, 11, 41, 40, 24, 20, 41]

#FFD_js(l, m ,L)
FFD_jsk(l, L, R, S)