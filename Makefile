COMP=-c -std=c99


all: menu.o index_first_even.o index_last_odd.o sum_before_even_and_after_odd.o sum_between_even_odd.o
		gcc menu.o index_first_even.o index_last_odd.o sum_before_even_and_after_odd.o sum_between_even_odd.o

menu.o: menu.c index_first_even.h index_last_odd.h sum_between_even_odd.h sum_before_even_and_after_odd.h
		gcc $(COMP) menu.c


index_first_even.o: index_first_even.c index_first_even.h
		gcc $(COMP) index_first_even.c


index_last_odd.o: index_last_odd.c index_last_odd.h
		gcc $(COMP) index_last_odd.c

sum_before_even_and_after_odd.o: sum_before_even_and_after_odd.c sum_between_even_odd.h index_first_even.h index_last_odd.h
		gcc $(COMP) sum_before_even_and_after_odd.c

sum_between_even_odd.o: sum_between_even_odd.c sum_before_even_and_after_odd.h sum_between_even_odd.h index_first_even.h index_last_odd.h
		gcc $(COMP) sum_between_even_odd.c