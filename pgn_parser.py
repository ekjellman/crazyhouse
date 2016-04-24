import sys

filename = sys.argv[1]

game_info = {}
game_count = 0
game_lines = []
crazyhouse_game = False

KNOWN_LABELS = ["Event", "Site", "FICSGamesDBGameNo", "White", "Black",
                "WhiteElo", "BlackElo", "TimeControl", "Date", "Time",
                "WhiteClock", "BlackClock", "PlyCount", "Result",
                "BlackIsComp", "WhiteIsComp", "Variant", "FEN"]

with open(filename, "r") as file_in:
  for line in file_in:
    game_lines.append(line)
    if "crazyhouse" in line.lower():
      crazyhouse_game = True
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
      if crazyhouse_game:
        for line in game_lines:
          print line,
      game_lines = []
      game_info = {}
      game_count += 1
      crazyhouse_game = False
