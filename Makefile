CC=gcc

all: exe

exe: cw2.c
	$(CC) cw2.c -o cw -lm
