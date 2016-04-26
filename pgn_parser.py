import sys
import collections

KNOWN_LABELS = ["Event", "Site", "FICSGamesDBGameNo", "White", "Black",
                "WhiteElo", "BlackElo", "TimeControl", "Date", "Time",
                "WhiteClock", "BlackClock", "PlyCount", "Result",
                "BlackIsComp", "WhiteIsComp", "Variant", "FEN", "SetUp",
                "WhiteRD", "BlackRD"]

# START HERE: Take all the crazyhouse .pgn files, and make a "top-rated" set
#             of games where both players are 2200(?) and above.
#             Then, start using this to make an opening book, maybe.
#             Also, modify this to be importable into our main program.

def read_pgn(filename):
  game_infos = []
  game_info = {}
  game_count = 0
  with open(filename, "r") as file_in:
    for line in file_in:
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
        game_infos.append(game_info)
        game_info = {}
        game_count += 1
  return game_infos

if __name__ == "__main__":
  filename = sys.argv[1]
  print read_pgn(filename)

