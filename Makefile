default: pylib

pylib: libmathfun.so
	rm pymathfun.c && python3 setup.py build_ext --inplace

libmathfun.so: mathfun.c
	gcc -Wall -shared -o libmathfun.so -fPIC mathfun.c


clean:
	rm  *.so
