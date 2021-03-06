from math import *

class Node(object):

	def __init__(self, estado="aberto", pai=None, custo=0, tamanho=1, lin=0, col=0):
		self.pai = pai
		self.custo = custo
		self.tamanho = tamanho
		self.col = col
		self.lin = lin
		self.estado = estado

	def __str__(self):
		return "[ linha: %d coluna: %d custo: %f tamanho: %f]" %(self.lin, self.col, self.custo, self.tamanho)

	def __repr__(self):
		return "[ linha: %d coluna: %d custo: %f tamanho: %f]" %(self.lin, self.col, self.custo, self.tamanho)

	def __eq__(self, node):
		if node == None:
			return False
		if self.col == node.col and self.lin == node.lin:
			return True
		return False
		




def pegaFilhos(node, map):
	filhos = []
	lin = node.lin
	col = node.col
	lin1 = node.lin + 1
	linm1 = node.lin - 1
	col1 = node.col + 1
	colm1 = node.col - 1

	diag = sqrt(2)

	if lin1<len(map) and map[lin1][col] == 0: #baixo
		#print("1")
		filhos.append(Node(lin=lin1, col=col, pai=node))

	if lin1<len(map) and colm1>=0 and map[lin1][colm1] == 0: #esquerda-baixo
		#print("2")
		filhos.append(Node(lin=lin1, col=colm1, pai=node, tamanho=diag))

	if colm1>=0 and map[lin][colm1] == 0: #esquerda
		#print("3")
		filhos.append(Node(lin=lin,col=colm1, pai=node))

	if linm1>=0 and colm1>=0 and map[linm1][colm1] == 0: #esquerda-cima
		#print("4")
		filhos.append(Node(lin=linm1, col=colm1, pai=node, tamanho=diag))

	if linm1 >=0 and map[linm1][col]==0: #cima
		#print("5")
		filhos.append(Node(lin=linm1, col=col, pai=node))

	if linm1 >= 0 and col1<len(map[0]) and map[linm1][col1]==0: #direita-cima
		#print("6")
		filhos.append(Node(lin=linm1, col=col1, pai=node, tamanho=diag))

	if (col1<len(map[0])) and (map[lin][col1]==0): #direita
		#print("7")
		filhos.append(Node(lin=lin, col=col1, pai=node))

	if lin1<len(map) and col1<len(map[0]) and map[lin1][col1]==0:#direita-baixo
		#print("8")
		filhos.append(Node(lin=lin1, col=col1, pai=node, tamanho=diag))

	return filhos


def imprimeCaminho(node):
	while node != None:
		print(node)
		node = node.pai

def imprimeCaminhoBonito(node, mapa, obj):

	for i in range(len(mapa)):
		for j in range(len(mapa[i])):
			if mapa[i][j] == 0:
				mapa[i][j] = " "
			else:
				mapa[i][j] = "#"

	mapa[obj.lin][obj.col] = 'G'


	i = 0
	while node != None:
		mapa[node.lin][node.col] = '1'
		node = node.pai
		i += 1


	for linha in mapa:
		print(linha)

	print("PASSOS: "+str(i))


def hLR(node, objetivo): #heuristica euclidiana
	deltax = abs(objetivo.col - node.col)
	deltay = abs(objetivo.lin - node.lin)
	h2 = deltax**2 + deltay**2
	return sqrt(h2)

def hMan(node, objetivo): #heuristica de Manhattan
	deltax = abs(objetivo.col - node.col)
	deltay = abs(objetivo.lin - node.lin)
	return deltay+deltax

def binarySearch(alist, item_custo):

    first = 0
    last = len(alist)-1
    found = False
    midpoint = 0


    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint].custo == item_custo:
        	found = True
        else:
            if item_custo < alist[midpoint].custo:
                last = midpoint-1
            else:
                first = midpoint+1

    return midpoint

def insere(lista, item):
	if len(lista) == 1:

		if lista[0].custo<item.custo:
			lista.append(item)
		else:
			lista.insert(0,item)

		return lista

	i = binarySearch(lista, item.custo)

	
	if (len(lista)-1)>i:
		if item.custo>lista[i].custo:
			i+=1
	else:
		lista.append(item)
		return lista

	lista.insert(i, item)
	return lista
