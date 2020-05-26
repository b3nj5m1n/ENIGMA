# Makefile for enigma simulator

# So we don't have to use hard tabs for indent
.RECIPEPREFIX +=

# Compiler and flags for compiler
CC = gcc
CFLAGS = -c

# Input and output dirs
ODIR = obj
SDIR = src

# Output binary
OUT = bin/enigma

all: $(OUT)

$(OUT): steckbrett.o
    $(CC) $(ODIR)/steckbrett.o -o $(OUT)

steckbrett.o: src/steckbrett.c
    $(CC) $(CFLAGS) $(SDIR)/steckbrett.c -o $(ODIR)/steckbrett.o

clean:
    rm -rf $(ODIR)/*.o
