
class RoboMRSA():

    def __init__(self, possicao_x=0, possicao_y=0, orientacao='N'):
        self.possicao_x = possicao_x
        self.possicao_y = possicao_y
        self.orientacao = orientacao
    # Metodo que recebe um srt 'M' para andar uma posição,
    # 'R' rotacionar para direita e 'L' para esquerda
    # retornado a posição final da cordena X, Y ,
    def movimento(self, mov):
        for a in list(mov):
            x = a.upper()
            if self.orientacao == 'N':
                if x == "R":
                    if self.orientacao == 'N':
                        self.orientacao = 'E'
                elif x == "L":
                    if self.orientacao == 'N':
                        self.orientacao = 'W'
                elif x == "M":
                    if self.possicao_y < 4:
                        self.possicao_y += 1
                    else:
                        self.possicao_y

            elif self.orientacao == 'E':
                if x == "R":
                    if self.orientacao == 'E':
                        self.orientacao = 'S'
                elif x == "L":
                    if self.orientacao == 'E':
                        self.orientacao = 'N'
                elif x == 'M':
                    if self.possicao_x < 4:
                        self.possicao_x += 1
                    else:
                        self.possicao_x

            elif self.orientacao == 'S':
                if x == "R":
                    if self.orientacao == 'S':
                        self.orientacao = 'W'
                elif x == "L":
                    if self.orientacao == 'S':
                        self.orientacao = 'E'
                elif x == 'M':
                    if self.possicao_y > 0:
                        self.possicao_y -= 1
                    else:
                        self.possicao_y

            elif self.orientacao == 'W':
                if x == "R":
                    if self.orientacao == 'W':
                        self.orientacao = 'N'
                elif x == "L":
                    if self.orientacao == 'W':
                        self.orientacao = 'S'
                elif x == 'M':
                    if self.possicao_x > 0:
                        self.possicao_x -= 1
                    else:
                        self.possicao_x

        return f'({self.possicao_x}, {self.possicao_y}, {self.orientacao})'


'''if __name__ == '__main__':
    bob = RoboMRSA()
    print(bob.movimento('MML'))'''

print('Olá! Meu nome é Radarzinho.')
name = input('Qual o seu nome? ')
print(f'Muito prazer {name}!')
instrucao = "Vamos as intruções:"
instrucao += " 'M' para avançar uma posição, "
instrucao += "'R' rotacionar 90º a direita "
instrucao += " e 'L' rotacionar 90º a esquerda. "
instrucao += "Será retornado a posição final nas cordenada"
instrucao += " (x, y, direção), "
instrucao += " direção=[N:Norte, S:Sul, E:Leste, W:Oeste]."
instrucao += "Exemplo: 'MML' vai avançar 2 posições e "
instrucao += "L vai rotacionar 90º para esquerda, retornando"
instrucao += "(0, 2, W). Caso queira sair digite 's'."
print(instrucao)
cordenadas = input("Pode digitar as cordenadas: ")
radarzinho = RoboMRSA()
print(radarzinho.movimento(cordenadas))
while cordenadas != 's':
    cordenadas = input("Digite novamente, ou 'sair' para finalizar: ")
    if cordenadas == 's':
        print('Fim das operações!')
    else:
        print(radarzinho.movimento(cordenadas))
