#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>


int* parsing_args(char* str){	 
	if(str == NULL){
  		printf("String is empty\n");
  		exit(0);
	}
	int idx = 0;
	int* array = malloc(3 * sizeof(int));
	int temp = 0;
	int place_number = 1;

	for(int i = strlen(str); i >= 0; i++){
  		if(str[i] == '.'){
			array[idx] = temp;
			idx++;
			temp = 0;
			place_number = 1;
  		} else {
			temp += str[i] * place_number;
			place_number *= 10;
  		}
	}

	return array;
}

int main(){

    char* str = "255.0.0";
    int* arr = parsing_args(str);

    for(int i = 0; i < 3; i++){
        printf("%d\n", arr[i]);
    }



    return 0;
}
