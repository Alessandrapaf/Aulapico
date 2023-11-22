nome="lele"
print(nome)
idade=27
print(idade)
print(nome+" tem "+str(idade)+" anos.")

if idade==27:
    print(nome)
if idade is 27:
    print(nome)
if idade is not 28:
    print(nome)

def printdoguinhos():
    listadoguinhos=["lili","zara","amora","mel"]
    for doguinhos in listadoguinhos:
        print(doguinhos)

printdoguinhos()

def toys():
    listatoys=["cenoura","patinho","porquinho"]
    for toys in listatoys:
        print(toys)

toys()

dicionariolele={"nome": "pico","idade": 33,"profissao": "engenheira"}
print(dicionariolele)
print(dicionariolele.keys())
x = dicionariolele["nome"]
print(x)
y = dicionariolele["profissao"]
print(y)

dicionarioclientes={"cliente1":{"nome": "carmen", "idade": 62}, 
                    "cliente2":{"nome": "alexandre", "idade": 63}}
dadoscliente1 = dicionarioclientes["cliente1"]
print(dadoscliente1)
dadoscliente1["idade"] = 63
print(dadoscliente1)
dicionarioclientes["cliente3"] = {"nome": "mariana", "idade": 33}
print(dicionarioclientes)
dicionarioclientes.pop("cliente2")
print(dicionarioclientes)