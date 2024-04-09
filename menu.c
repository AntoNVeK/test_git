all: exe

exe: solution.c
	gcc solution.c -fPIC -ldl -o solution


clean:
	-rm solution





#include <stdio.h>
#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if(argc < 4) {
        printf("Usage: %s <library> <function> <argument>\n", argv[0]);
        return 1;
    }

    const char *libname = strcat("./", argv[1]);
    const char *funcname = argv[2];
    int arg = atoi(argv[3]);

    void *lib = dlopen(libname, RTLD_LAZY);
    if(lib == NULL) {
        fprintf(stderr, "Error loading library: %s\n", dlerror());
        return 1;
    }

    int (*func)(int) = dlsym(lib, funcname);
    if(func == NULL) {
        fprintf(stderr, "Error finding function: %s\n", dlerror());
        dlclose(lib);
        return 1;
    }

    int result = func(arg);
    printf("%d\n", result);

    dlclose(lib);
    return 0;
}




