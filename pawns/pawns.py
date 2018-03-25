class Pawns:
  winner = {}
  def __init__(self):
    self.column_sets = self.create_column_sets()
    self.col_ids = self.create_col_ids()
    self.column_set_ids = self.create_column_set_ids(self.column_sets)
    self.tabletop_set_ids = self.create_tabletop_set_ids()
    self.column_graph = self.create_players_column_graphs()
    self.tabletop_graph = self.create_tabletop_graph()
    self.states_graph = self.create_states_graph()
    self.cache_winner_list()

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
          print(":", id,"[", b, "]", "[", p, "]")
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

  def create_col_ids(self):
    col_id = [[-1 for col in range(3)] for ID in range(8000)]
    for i in range(20):
      for j in range(20):
        for k in range(20):
          tabletop_id = 400 * k + 20 * j + i
          col_id[tabletop_id][0] = i
          col_id[tabletop_id][1] = j
          col_id[tabletop_id][2] = k
    return col_id

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
    # player 0 já ganhou
    if self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[0]] and \
      self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[1]] and \
      self.column_sets[1][3] == self.column_sets[0][tabletop_columns_set[2]]:
      win0 = 1
    # player 1 já ganhou
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

  def column_valid_moves(self, id):
    b = self.column_sets[0][id]
    p = self.column_sets[1][id]
    if b == 4:
        # o branco já chegou no final
        return []
    if b == 3 and p == 4:
        # aqui o branco está na penúltima casa, mas
        # não pode se mover porque o preto está na última casa
        return []
    if p == b + 1:
        # o branco só pode "pular" o preto e parar
        # na casa imediatamente após o preto
        return [self.column_set_ids[b + 2][p]]

    # Se nenhuma das condições anteriores foi satisfeita, então o peão
    # branco pode se mover para qualquer casa entre ele até peão preto ou
    # até o fim da linha no caso dele já ter ultrapassado o peão preto.
    valid_moves = []
    limit = 5 if p < b else p

    for i in range(b + 1, limit):
        valid_moves.append(self.column_set_ids[i][p])
    return valid_moves

  def reverse(self, id):
    b = self.column_sets[0][id]
    p = self.column_sets[1][id]
    return self.column_set_ids[4 - p][4 - b]

  def create_players_column_graphs(self):
    player_1_graph = [self.column_valid_moves(id) for id in range(20)]
    player_2_graph = [[self.reverse(j) for j in player_1_graph[self.reverse(id)]] for id in range(20)]
    return [player_1_graph, player_2_graph]


  def tabletop_valid_moves(self, tabletop_id, player):
    if self.tabletop_set_status(tabletop_id):
      return []
    cached_column_ids = self.col_ids[tabletop_id]
    result = []
    for i in range(3):
      cached_column_ids_copy = cached_column_ids.copy()
      for id in self.column_graph[player][cached_column_ids[i]]:
        cached_column_ids_copy[i] = id
        id_tabletop = self.tabletop_set_id_from_columns_ids(*cached_column_ids_copy)
        result.append(id_tabletop)
    # Se não há jogadas válidas então "passar a vez" é válida!
    if len(result) == 0:
      result.append(tabletop_id)
    return result

  def create_tabletop_graph(self):
    tabletop_graph = [[], []]
    for player in range(2):
      tabletop_graph[player] = [self.tabletop_valid_moves(tabletop_id, player) for tabletop_id in range(8000)]
    return tabletop_graph

  def create_states_graph(self):
    states_graph = {}
    for player in range(2):
      for tabletop_id in range(8000):
        states_graph[(player, tabletop_id)] = []
        for y in self.tabletop_graph[player][tabletop_id]:
            states_graph[(player, tabletop_id)].append((1 - player, y))
    return states_graph

  def wins(self, player, state):
    # (i, x) not in vencedor.keys() means it was not visited
    # vencedor[(i, x)] = 1          means it is being visited
    # vencedor[(i, x)] = 2          means it has no winning strategy
    # vencedor[(i, x)] = 3          means it has a winning strategy

    # mark as visited:
    self.winner[(player, state)] = 1
    # no terminal node has a winning strategy:
    if self.tabletop_set_status(state):
      self.winner[(player, state)] = 2
      return
    for p, s in self.states_graph[(player, state)]:
      # Se você implementou o grafo reduzido descrito na seção anterior,
      # então use phi(y) no lugar de y até o final desta função.
      if not (p, s) in self.winner.keys(): self.wins(p, s)
      if self.winner[(p, s)] == 2:
        self.winner[(player, state)] = 3
    if self.winner[(player, state)] == 1:
      self.winner[(player, state)] = 2

  def cache_winner_list(self):
    for player in range(2):
      for tabletop_id in range(8000):
        if not (player, tabletop_id) in self.winner.keys():
          self.wins(player, tabletop_id)

  def player_have_winner_strategy(self, player, tabltop_id):
    return self.winner[(player, tabltop_id)] == 3

  def rival_has_winner_strategy(self, player, state):
    valid_moves = self.tabletop_graph[player][state]
    rival_winning_strategy = []
    for move in valid_moves:
      if self.winner[(1 - player , move)] == 3:
        rival_winning_strategy.append(move)
    return len(rival_winning_strategy) > 0

  def possible_moves(self, player, id):
    valid_moves = []
    if isinstance(id, list):
      valid_moves = self.tabletop_graph[player][self.tabletop_set_id_from_columns_ids(*id)]
    else:
      valid_moves = self.tabletop_graph[player][id]
    return valid_moves

  def print_possible_moves(self, player, id):
    valid_moves = []
    if isinstance(id, list):
      valid_moves = self.tabletop_graph[player][self.tabletop_set_id_from_columns_ids(*id)]
    else:
      valid_moves = self.tabletop_graph[player][id]
    for move in valid_moves:
      self.print_tabletop_set(move)

  def best_strategy(self, player, state):
    if self.player_have_winner_strategy(player, state):
      pm = self.possible_moves(player, state)
      rival_winning_strategies = []
      for m in pm:
        if self.rival_has_winner_strategy(1 - player, m):
          rival_winning_strategies.append(m)
      good_moves = list(set(pm) - set(rival_winning_strategies))
      return good_moves
    else:
      return[]

class PawnsGame:
  def __init__(self):
    self.pawns = Pawns()
    self.game_over = False
    self.game_state = self.pawns.tabletop_set_id_from_columns_ids(3,3,3)
    self.player = None
    self.player_turn = None
    self.start_game()

  def start_game(self):
    self.set_placement()
    self.game_loop()

  def set_placement(self):
    print("comece")
    placement = input()
    if placement == "primeiro":
      self.player = 0
      self.player_turn = True
    elif placement == "segundo":
      self.player = 1
      self.player_turn = False

  def game_loop(self):
    self.pawns.print_tabletop_set(self.game_state)
    while self.game_over != True:
      if self.player_turn:
        # move = self.best_move(player, state)
        # self.set_game_state(move)
        # self.player_turn = False
        # self.write_to_output(self.get_move_output(move))

        move = self.read_input_move(self.player, input())
        self.set_game_state(move)
        self.player_turn = False
      else:
        move = self.read_input_move(1 - self.player, input())
        self.set_game_state(move)
        self.player_turn = True

      self.game_over = self.pawns.tabletop_set_status(self.game_state) > 0
      self.pawns.print_tabletop_set(self.game_state)

  def set_game_state(self, move):
    self.game_state = move

  def read_input_move(self, player, input):
    input = input.split(" ")
    column = int(input[0]) - 1
    pawn_placement = int(input[1])
    new_column_id = self.create_column_id(player, self.game_state, column, pawn_placement)
    final_columns = [None] * 3
    for i in range(3):
      if i == column:
        final_columns[i] = new_column_id
      else:
        final_columns[i] = self.pawns.column_id(self.game_state, i)
    return self.pawns.tabletop_set_id_from_columns_ids(*final_columns)

  def create_column_id(self, player, game_state, column, pawn_moves):
    current_column_id = self.pawns.col_ids[game_state][column]
    pawns_placement_0 = self.pawns.column_sets[0][current_column_id]
    pawns_placement_1 = self.pawns.column_sets[1][current_column_id]

    if player:
      return self.pawns.column_set_ids[pawns_placement_0][pawns_placement_1 - pawn_moves]
    else:
      return self.pawns.column_set_ids[pawns_placement_0 + pawn_moves][pawns_placement_1]




# id = p.tabletop_set_id_from_columns_ids(3,3,3)
# print(p.player_have_winner_strategy(0, id))
# print(p.rival_has_winner_strategy(0,id))
# p.print_possible_moves(0, id)
# print("Best Strategies")
# for strategy in  p.best_strategy(0, id):
#   p.print_possible_moves(0, strategy)