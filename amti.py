numeroPedido = 0
filaClientesNormal = []
filaClienteIdoso = []
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
        filaClienteIdoso.append(Cliente(name=name, idade=idade,
                                 npedido=npedido.get("npedido", None)))

def posicaoCliente():
    name = input("Informe um nome para a pesquisa: ")
    for cliente in filaClienteIdoso:
        if name == cliente.name:
            print("Posição do cliente na fila preferencial é: " + (filaClienteIdoso.index+1))
            return
    for cliente in filaClientesNormal:
        if name == cliente.name: 
            print("Posição do cliente na fila preferencial é: " + (filaClientesNormal.index+1))
            return
    print("Não exite cliente com o nome informado.")
    return

def escolherItem():
    itens =[]
    while True:
        item = Item()
        item.desc = input("Informe o item: ")
        item.valor = input("Informe o valordo item: ")
        item.tempo = input("Informe o tempo item: ")
        opcao = input("Mais Itens? (sim ou nao)")  
        if(opcao == "nao"):
            break
    itens.append(item)
    pedido = Pedido(numeroPedido, itens, item.valor, item.tempo)
    filaPedidos.append(pedido)
    return

def fazendoPedido():
    global numeroPedido
    numeroPedido = numeroPedido +1 
    if len(filaClienteIdoso) > 0:
        escolherItem()
        filaClienteIdoso[0].numeroPedido = numeroPedido
        filaEspera.append(filaClienteIdoso[0])
        filaClienteIdoso.pop(0)
        return

    if len(filaClientesNormal) > 0:
        escolherItem()
        filaClientesNormal[0].numeroPedido = numeroPedido
        filaEspera.append(filaClientesNormal[0])
        filaClientesNormal.pop(0)
        return

    print("Nenhum cliente cadastrado ainda.")

inserirCliente(name="teste", idade=10)
inserirCliente(name="testeIdoso", idade=70)
