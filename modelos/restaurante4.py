# 1 tornando o projeto aderente ao padrão de mercado

#import da classe Avaliacao
from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._avaliacao=[]
        self._ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
   
    @classmethod
    def listar_restarantes(cls):
        print(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'.ljust(15)} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alterar_estado(self):
        self._ativo=not self._ativo

# criando um método para receber as avaliações

    def receber_avaliacao(self,cliente,nota):
        avaliacao=Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
   
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas,1)
        return media



