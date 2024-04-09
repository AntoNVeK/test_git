all: exe lib

exe: solution.c
	gcc solution.c -fPIC -ldl -o solution -Wl,-rpath=.

lib: func.c
	gcc -shared func.c -fPIC -o libmain.so

clean:
	-rm solution libmain.so
