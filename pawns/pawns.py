class Pawns:
  def __init__(self):
    self.column_sets = self.create_column_sets()
    self.column_set_ids = self.create_column_set_ids(self.column_sets)
    self.tabletop_set_ids = self.create_tabletop_set_ids()

  def print_column_set(self, b, p):
    for i in range(5):
      if p == i:
        print("P", end="")
      elif b == i:
        print("B", end="")
      else:
        print(".", end="")

  def print_column_sets(self):
    id = 0
    for b in range(5):
      for p in range(5):
        if b != p:
          self.print_column_set(b, p)
          print(":", id)
          id += 1

  def create_column_sets(self):
    column_sets = [list(range(20)), list(range(20))]
    id = 0
    for b in range(5):
      for p in range(5):
        if b != p:
          column_sets[0][id] = b
          column_sets[1][id] = p
          id += 1
    return column_sets

  def create_column_set_ids(self, column_sets):
    column_set_ids = [[-1 for i in range(5)] for j in range(5)]
    for id in range(20):
      column_set_ids[column_sets[0][id]][column_sets[1][id]] = id
    return column_set_ids

  def column_id(self, tabletop_id, column):
    while column > 0:
      tabletop_id = tabletop_id // 20
      column = column - 1
    return tabletop_id % 20

  def create_tabletop_set_ids(self):
    return [[self.column_id(tabletop_id, column) for column in range(3)] for tabletop_id in range(8000)]

  def tabletop_set_id_from_columns_ids(self, id0, id1, id2):
    return 400 * id2 + 20 * id1 + id0

  def tabletop_set_status(self, tabletop_id):
    win0 = 0
    win1 = 0
    tabletop_columns_set = [self.tabletop_set_ids[tabletop_id][i] for i in range(3)]
    # jogador 0 já ganhou
    if self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[0]] and \
      self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[1]] and \
      self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[2]]:
      win0 = 1
    # jogador 1 já ganhou
    if self.column_sets[1][tabletop_columns_set[0]] == self.column_sets[0][3] and \
      self.column_sets[1][tabletop_columns_set[1]] == self.column_sets[0][3] and \
      self.column_sets[1][tabletop_columns_set[2]] == self.column_sets[0][3]:
      win1 = 1
    return win0 + 2 * win1

  def print_column_set_by_id(self, id):
    self.print_column_set(self.column_sets[0][id],self.column_sets[1][id])

  def print_tabletop_set(self, tabletop_id):
    for i in range(3):
      column_id = self.tabletop_set_ids[tabletop_id][i]
      self.print_column_set_by_id(column_id)
      print()
    print()
