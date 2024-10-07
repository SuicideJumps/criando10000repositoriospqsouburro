#  # 2️⃣ Calculadora de partidas Rankeadas
# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

# ## Objetivo:

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

# Se vitórias for menor do que 10 = Ferro
# Se vitórias for entre 11 e 20 = Bronze
# Se vitórias for entre 21 e 50 = Prata
# Se vitórias for entre 51 e 80 = Ouro
# Se vitórias for entre 81 e 90 = Diamante
# Se vitórias for entre 91 e 100= Lendário
# Se vitórias for maior ou igual a 101 = Imortal

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
 

  
class Partidas:
     
     def __init__(self, vitoria, derrota):
          self.vit = vitoria
          self.derr = derrota
   
     def vitoria(self):
          return self.vit
     def derrota(self):
          return self.derr 
     def resultado(self):
          return self.vit - self.derr
          
vit = int(input('Voce tem qts vitórias? '))  
derr = int(input('Voce tem qts derrotas? '))
partida = Partidas(vit,derr)

print(f'São {partida.vitoria()} vitórias')
print(f'São {partida.derrota()} derrotas')


if partida.resultado() < 1:
     print(f'Voce é tão horroroso que esta com saldo de vitória negativo "{partida.resultado()}", voce está no rank ESTRUME.')
elif 0 >= partida.resultado() >= 10 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank FERRO.')
elif 11>= partida.resultado() >= 20 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank CRONZA.')
elif 21 >= partida.resultado() >= 50 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank PRATA.')
elif 51 >= partida.resultado() >= 80 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank OURO.')
elif 81 >= partida.resultado() >= 90 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank DIAMANTE.')          
elif 91 >= partida.resultado() >= 100 :
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank LENDARIO.')
else:
     print(f'Voce possui o saldo positivo de "{partida.resultado()}" vitórias, voce está no rank IMORTAL.')
     
