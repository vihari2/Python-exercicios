#exercicio faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#pelo pygame - mixer

from pygame import mixer
mixer.init()
mixer.music.load('music01.mp3')
mixer.music.play()

#para repetir a musica em loop: mixer.music.play(-1)

#pelo playsound 

import playsound
playsound.playsound('music01.mp3')