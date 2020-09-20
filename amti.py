numeroPedido = 0
filaClientesNormal = []
filaClientesIdoso = []
filaPedidos =[]
filaEspera = []

class Cliente:
    def __init__(self, *args, **kwarg):
        self.name = kwarg.get("name", "")
        self.idade = kwarg.get("idade", 0)
        self.numeroPedido = kwarg.get("pedido", 0)

class Pedido:
    def __init__(self, *args, **kwarg):
        self.numero = kwarg.get("numero", 0)
        self.item = kwarg.get("item", [] )
        self.valorTotal = kwarg.get("valorTotal", 0)
        self.tempoPreparo = kwarg.get("tempoPreparo", 0)

class Item:
     def __init__(self, *args, **kwarg):
        self.desc = kwarg.get("desc", "" )
        self.valor = kwarg.get("valor", 0)
        self.tempo = kwarg.get("tempo", 0)

def inserirCliente(name, idade, **npedido):
    if idade <= 65:
        filaClientesNormal.append(Cliente(name=name, idade=idade,
                                   npedido=npedido.get("npedido", None)))
    else:
        filaClientesIdoso.append(Cliente(name=name, idade=idade,
                                 npedido=npedido.get("npedido", None)))

def posicaoCliente():
    name = input("Informe um nome para a pesquisa: ")
    posicaoI = 0
    posicaoN = 0
    for cliente in filaClientesIdoso:
        posicaoI = posicaoI +1
        if name == cliente.name:
            print("Posição do cliente na fila preferencial é: " + str(posicaoI))
            return
    for cliente in filaClientesNormal:
        posicaoN = posicaoN +1
        if name == cliente.name:
            print("Posição do cliente na fila normal é: " + str(posicaoN))
            return
    print("Não exite cliente com o nome informado.")
    return

def escolherItem():
    global numeroPedido
    itens =[]
    while True:
        item = Item()
        item.desc = input("Informe o item: ")
        item.valor = float(input("Informe o valor do item: "))
        item.tempo = int(input("Informe o tempo item: "))
        itens.append(item)
        opcao = input("Mais Itens? (sim ou nao)")  
        if(opcao == "nao"):
            break
    valorTotal = 0
    tempoTotal = 0
    for iten in itens:
        tempoTotal = tempoTotal + iten.tempo
        valorTotal = valorTotal + iten.valor
    pedido = Pedido(numero = numeroPedido, item = itens, valorTotal = valorTotal, tempoPreparo = tempoTotal)
    filaPedidos.append(pedido)
    return


def fazendoPedido():
    global numeroPedido
    numeroPedido = numeroPedido +1 
    if len(filaClientesIdoso) > 0:
        print("CLIENTE SENDO ATENDIDO: " + filaClientesIdoso[0].name)        
        filaClientesIdoso[0].numeroPedido = numeroPedido
        escolherItem()
        filaEspera.append(filaClientesIdoso[0])
        filaClientesIdoso.pop(0)
        return

    if len(filaClientesNormal) > 0:
        print("CLIENTE SENDO ATENDIDO: " + filaClientesNormal[0].name)
        escolherItem()
        filaClientesNormal[0].numeroPedido = numeroPedido
        filaEspera.append(filaClientesNormal[0])
        filaClientesNormal.pop(0)
        return

    print("Nenhum cliente cadastrado ainda.")

def chamarPedido():
    callItem = int(input("Informe o numero do pedido que esta pronto: "))
    for pedido in filaEspera:
        if (callItem == pedido.numeroPedido):
            filaEspera.pop()
    for pedido in filaPedidos:
        if (callItem == pedido.numero):
            filaPedidos.pop()
     
print("######################  INICIO  ###################################")
print("ADICIONANDO CLIENTES")
inserirCliente(name="Teste", idade=49)
inserirCliente(name="Teste2", idade=18)
inserirCliente(name="Teste3", idade=68)
print("DONE!!!")
print("----------------------")
print("LISTA NORMAL:")
for cliente in filaClientesNormal:
    print("     " + cliente.name)
print("----------------------")
print("LISTA IDOSO:")
for cliente in filaClientesIdoso:
    print("     " + cliente.name)
print("----------------------")
print("LISTA ESPERA:")
for pedido in filaEspera:
    print("     " + pedido)
print("----------------------")
print("LISTA PEDIDOS:")
for pedidos in filaPedidos:
    print("     " + pedidos)
print("#########################################################")
print("PROCURANDO CLIENTE NAS LISTAS")
#posicaoCliente()
#posicaoCliente()
#posicaoCliente()
print("#########################################################")
print("FAZENDO PEDIDO")
fazendoPedido()
fazendoPedido()
print("#########################################################")
print("LISTA NORMAL:")
for cliente in filaClientesNormal:
    print("     " + cliente.name)
print("----------------------")
print("LISTA IDOSO:")
for cliente in filaClientesIdoso:
    print("     " + cliente.name)
print("----------------------")
print("LISTA ESPERA:")
for espera in filaEspera:
    print("    Nome: " + espera.name + " - Numero Pedido: " + str(espera.numeroPedido))
print("----------------------")
print("LISTA PEDIDOS:")
for pedidos in filaPedidos:
    print("   -Numero Pedido: " + str(pedidos.numero) + "\n   -Iten(s):") 
    for item in pedidos.item:
        print("      *" + item.desc)
    print( "   -Valor(R$): " + str(pedidos.valorTotal) + "\n   -Tempo: " + str(pedidos.tempoPreparo) + " min(s).")
print("#########################################################")
print("CHAMANDO PEDIDO PEDIDO")
chamarPedido()
print("#########################################################")
print("LISTA NORMAL:")
for cliente in filaClientesNormal:
    print("     " + cliente.name)
print("----------------------")
print("LISTA IDOSO:")
for cliente in filaClientesIdoso:
    print("     " + cliente.name)
print("----------------------")
print("LISTA ESPERA:")
for espera in filaEspera:
    print("    Nome: " + espera.name + " - Numero Pedido: " + str(espera.numeroPedido))
print("----------------------")
print("LISTA PEDIDOS:")
for pedidos in filaPedidos:
    print("   -Numero Pedido: " + str(pedidos.numero) + "\n   -Iten(s):") 
    for item in pedidos.item:
        print("      *" + item.desc)
    print( "   -Valor(R$): " + str(pedidos.valorTotal) + "\n   -Tempo: " + str(pedidos.tempoPreparo) + " min(s).")
print("#########################################################")