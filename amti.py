class Cliente:
    def __init__(self, *args, **kwarg):
        self.name = kwarg.get("name", "")
        self.idade = kwarg.get("idade", 0)
        self.numeroPedido = kwarg.get("pedido", 0)

class Pedido:
    def __init__(self, *args, **kwarg):
        self.numero = kwarg.get("numero", 0)
        self.item = kwarg.get("item", {} )
        self.valorTotal = kwarg.get("valorTotal", 0)
        self.tempoPreparo = kwarg.get("tempoPreparo", 0)

filaClientesNormal = []
filaClienteIdoso = []
filaPedidos =[]
filaEspera = []
numeroPedido = 0

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

def pedido():
   
    if len(filaClienteIdoso) > 0:
              
        
        numeroPedido = numeroPedido + 1
        filaClienteIdoso[0].numeroPedido = numeroPedido
        filaEspera.append(filaClienteIdoso[0])
        filaClienteIdoso.pop(0)
        return
        
    if len(filaClientesNormal) > 0:
        numeroPedido = numeroPedido + 1
        filaClientesNormal[0].numeroPedido = numeroPedido
        filaEspera.append(filaClientesNormal[0])
        filaClientesNormal.pop(0)
        return
 
    print("Nenhum cliente cadastrado ainda.")


inserirCliente(name="teste", idade=10)
inserirCliente(name="testeIdoso", idade=70)

for cliente in filaClienteIdoso:
    print(cliente.name)

for cliente in filaClientesNormal:
    print(cliente.name)