import sys
import collections

filename = sys.argv[1]

game_info = {}
game_count = 0
game_lines = []

KNOWN_LABELS = ["Event", "Site", "FICSGamesDBGameNo", "White", "Black",
                "WhiteElo", "BlackElo", "TimeControl", "Date", "Time",
                "WhiteClock", "BlackClock", "PlyCount", "Result",
                "BlackIsComp", "WhiteIsComp", "Variant", "FEN", "SetUp",
                "WhiteRD", "BlackRD"]

elo_ratings = collections.defaultdict(int)

# START HERE: Take all the crazyhouse .pgn files, and make a "top-rated" set
#             of games where both players are 2200(?) and above.
#             Then, start using this to make an opening book, maybe.
#             Also, modify this to be importable into our main program.

def handle_game():
  black_elo = int(game_info["BlackElo"])
  white_elo = int(game_info["WhiteElo"])
  black_elo /= 100
  white_elo /= 100
  elo_ratings[black_elo] += 1
  elo_ratings[white_elo] += 1

with open(filename, "r") as file_in:
  for line in file_in:
    game_lines.append(line)
    if line[0] == "[":
      # -3 because of the assert below
      label, info = line[1:-3].split(" ", 1)
      info = info.strip("\"")
      assert line[-3:] == "]\r\n"
      assert label not in game_info
      if label in KNOWN_LABELS:
        game_info[label] = info
      else:
        raise ValueError("Unknown label: {}".format(label))
    if line[0] == "1":
      assert "Moves" not in game_info
      game_info["Moves"] = line
    if line == "\r\n":
      continue
    if line == "\n":
      handle_game()
      game_lines = []
      game_info = {}
      game_count += 1

print elo_ratings
