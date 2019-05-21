
from microbit import *
import music

#This is the jeopardy theme song
jeopardy = ["C5:4", "F", "C", "F4:4", "C5:4", "F", "C5:8", "C5:4", "F", "C", "F", "A5:6", "G5:2","F5:2","E5:2", "D5:2", "Db5:2", "C5:4", "F", "C", "F4:4","C5:4", "F", "C5:8", "F5:6","D5:2", "C5:4", "Bb4:4", "A", "G", "F"]
while True:
	music.play(jeopardy)
	sleep(1000)

