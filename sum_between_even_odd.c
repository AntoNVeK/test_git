#include <stdio.h>
#include <stdlib.h>
#include "sum_between_even_odd.h"
#include "index_first_even.h"
#include "index_last_odd.h"


int sum_between_even_odd(int array[],int size){
    int summa = 0;
    for(int i =  index_first_even(array, size); i < index_last_odd(array,size); ++i){
        summa += abs(array[i]);
    }
    return summa;
}