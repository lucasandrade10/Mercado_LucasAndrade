from produto import produto

class estoque:
    def __init__(self):
        self.lista = []
        self.total = 0.0

    def cadastro(self,nome,preco, tipo, quantidade):
        if len(self.lista) == 0:
            prod = produto(nome, preco, tipo, quantidade)
            self.lista.append(prod)
            print '%d %s(s) cadastrado(s) com suceeso \n' % (prod.getQuantia(), prod.getNome())
        else:
            existente = False
            for i in range(len(self.lista)):
                if self.lista[i].getNome() == nome:
                    print '%s ja cadastrado no sistema \n'%nome
                    existente = True
                    break
            if existente == False:
                prod = produto(nome, preco, tipo, quantidade)
                self.lista.append(prod)
                print '%d %s(s) cadastrado(s) com sucesso \n' % (prod.getQuantia(), prod.getNome())

    def vender(self,produto_ven):
        total = 0
        existente = False
        teste = False
        for i in range(len(self.lista)):
            if self.lista[i].getNome() == produto_ven:
                print '==> %s (%s). R$%.2f' % (self.lista[i].getNome(), self.lista[i].getTipo(), self.lista[i].getPreco())
                quant = int(raw_input("Digite a quantidade que deseja vender: "))
                estoque = self.lista[i].getQuantia()
                teste = False
                if quant < 0:
                    print 'valor invalido \n'
                    teste = True
                    continue
                elif estoque < quant:
                    print 'Nao e possivel vender pois nao ha %s suficiente \n' % produto_ven
                else:
                    estoque -= quant
                    self.lista[i].setQuantia(estoque)
                    total = quant * self.lista[i].getPreco()
                    print '==> total arrecadado: R$ %.2f \n' % total
                existente = True
                break
        if existente == False and teste == False:
            print produto_ven + ' nao cadastrado(a) no sistema.'
        return total

    def imprimir(self,total):
        for i in range(len(self.lista)):
            print '%d) %s (%s) R$ %2.f' % (
            (i + 1), self.lista[i].getNome(), self.lista[i].getTipo(), self.lista[i].getPreco())
            print '   Restante: %d \n' % self.lista[i].getQuantia()
        print 'Total arrecadado em vendas: R$ %.2f\n' % (total)
