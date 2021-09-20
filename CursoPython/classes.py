class MetaClasse(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Pessoa':
            return type.__new__(mcs, name, bases, namespace)
        # detecta se o metodo existe
        if 'pagar' not in namespace:
            print(f'Metodo "pagar" nao encontrado em {name}')
        # impede que o método seja sobrescrito
        if 'falar' in namespace:
            del namespace['falar']

        return type.__new__(mcs, name, bases, namespace)


class Pessoa(metaclass=MetaClasse):
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer(self,alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} começou a comer {alimento}')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        else:
            print(f'{self.nome} parou de comer')
            self.comendo = False
    def falar(self,assunto):
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        else:
            print(f'{self.nome} é {type(self)} e começou a falar sobre {assunto}')
            self.falando = True
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        else:
            print(f'{self.nome} parou de falar')
            self.falando = False
    def pessoa_paga(self):
        self.pagar()

class Cliente(Pessoa):
    def __init__(self,nome,idade,comendo=False,falando=False,comprando=False):
        super().__init__(nome ,idade,comendo=False,falando=False)
        self.comprando = comprando
    def comprar(self, item):
        if self.comprando:
            print(f'{self.nome} já está comprando')
            return
        print(f'{self.nome} começou a comprar {item}')
        self.comprando = True
    def parar_comprar(self):
        if not self.comprando:
            print(f'{self.nome} não está comprando')
            return
        print(f'{self.nome} parou de comprar')
        self.comprando = False
    def pagar(self):
        print('Pagou')


class Aluno(Pessoa):
    def __init__(self,nome,idade,comendo=False,falando=False,estudando=False):
        super().__init__(nome ,idade,comendo=False,falando=False)
        self.estudando = estudando

    def estudar(self,materia):
        if self.estudando:
            print(f'{self.nome} já está estudando')
            return
        print(f'{self.nome} começou a estudar {materia}')
        self.estudando = True

    def falar(self,nada):
        print('Hello moto')
