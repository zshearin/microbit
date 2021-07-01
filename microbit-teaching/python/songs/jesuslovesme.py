
from microbit import *
import music

#This is jesuslovesme song
jesus = ["G4:4", "E","E","D", "E", "G", "G4:8", "A4:4", "A", "C5:4", "A4:4", "A", "G", "G4:8", "G4:4","E","E", "D", "E", "G", "G4:8", "A4:4", "A", "G", "C", "E", "D", "C4:8", "G", "E4:4", "G", "A", "C5:12", "G4:8", "E4:4", "C", "E", "D4:12", "G4:8", "E4:4", "G", "A", "C5:8", "A4:4", "G", "C", "E", "D", "C4:16" ]
while True:
	music.play(jesus)
	sleep(1000)

