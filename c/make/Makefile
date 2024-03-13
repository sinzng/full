OBJF = test1.o test2.o test3.o
test : $(OBJF) 
	gcc -o $@ $^
test1 : test1.c a.h
	gcc -c $<
test2 : test2.c a.h b.h
	gcc -c $*.c
test3 : test3.c b.h c.h
	gcc -c $<
clean :
	rm -rf $^
