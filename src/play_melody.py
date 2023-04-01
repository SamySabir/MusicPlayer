import musicalbeeps
from melody import Melody

if __name__ == "__main__":
    player = musicalbeeps.Player()
    melody = Melody("lmao.txt")
    melody.change_tempo(1)
    melody.play(player)