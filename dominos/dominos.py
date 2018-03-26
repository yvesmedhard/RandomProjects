class DominosGame:
  N = None
  K = None
  available_parts = None

  def __init__(self):
    self.start_game()

  def start_game(self):
    self.setup()
    print(self.N)
    print(self.K)
    for domino in self.available_parts:
      print(domino.normal, domino.invertido, domino.simetrico)

  def setup(self):
    print("Digite n e k: ")
    entrada = input().split(" ")
    self.N = int(entrada[0])
    self.K = int(entrada[0])
    print("Digite as peças por linha: ")
    parts = []
    for i in range(self.N):
      entrada
      parts.append(Domino(*))

    self.available_parts = parts

class Domino:
  extremidade1 = None
  extremidade2 = None
  def __init__(self, extremidade1, extremidade2):
    self.extremidade1 = extremidade1
    self.extremidade2 = extremidade2

  def normal(self):
    return [self.extremidade1, self.extremidade2]

  def invertido(self):
    return [self.extremidade2, self.extremidade1]

  def simetrico(self):
    return self.extremidade1 == self.extremidade2


DominosGame()