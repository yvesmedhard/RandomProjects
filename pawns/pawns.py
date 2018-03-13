class Pawns:
    def __init__():
        self.posicloes_coluna = gerar_vetores_posicao_coluna()
        self.config_id = preenche_config_id(gerar_vetores_posicao_coluna())

    def imprime_coluna(b, p):
      for i in range(5):
        if p == i:
          print("P", end="")
        elif b == i:
          print("B", end="")
        else:
          print(".", end="")      
              
    def enumera_configs_coluna():
      id = 0
      for b in range(5):
        for p in range(5):
          if b != p:
            imprime_coluna(b, p)
            print(":", id)
            id += 1                  

    def gerar_vetores_posicao_coluna():
      posicoes_coluna = [list(range(20)), list(range(20))]
      id = 0
      for b in range(5):
        for p in range(5):
          if b != p:
            posicoes_coluna[0][id] = b
            posicoes_coluna[1][id] = p
            id += 1
      return posicoes_coluna


    def preenche_config_id(self):
      config_id = [[-1 for i in range(5)] for j in range(5)]
      for id in range(20):
        config_id[self.posicoes_coluna[0][id]][self.posicoes_coluna[1][id]] = id
      return config_id

    def get_id(id0, id1, id2):
      return 400 * id2 + 20 * id1 + id0

    def get_col_id(ID, col):
      while col > 0:
        ID = ID // 20
        col = col - 1
      return ID % 20

    def col_id():
      return [[get_col_id(ID, col) for col in range(3)] for ID in range(8000)]

    def terminal(self, ID):
      ganhou0 = 0
      ganhou1 = 0
      v = [col_id()[ID][i] for i in range(3)]
      # jogador 0 já ganhou
      if self.posicoes_coluna[1][3] == self.posicoes_coluna[0][v[0]] and \
        self.posicoes_coluna[1][3] == self.posicoes_coluna[0][v[1]] and \
        self.posicoes_coluna[1][3] == self.posicoes_coluna[0][v[2]]:
        ganhou0 = 1
      # jogador 1 já ganhou
      if self.posicoes_coluna[1][v[0]] == self.posicoes_coluna[0][3] and \
        self.posicoes_coluna[1][v[1]] == self.posicoes_coluna[0][3] and \
        self.posicoes_coluna[1][v[2]] == self.posicoes_coluna[0][3]:
        ganhou1 = 1
      return ganhou0 + 2 * ganhou1

    def imprime_config_coluna(self, id): 
      imprime_coluna(self.posicoes_coluna[0][id],self.posicoes_coluna[1][id])

    def imprime_config(ID):
      for i in range(3):
        id = col_id[ID][i]
        imprime_config_coluna(id)
        print()
      print()
Pawns().terminal(3)
