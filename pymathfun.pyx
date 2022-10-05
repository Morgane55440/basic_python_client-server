cdef extern from "mathfun.h":  
    int fibo(int index)

def fibo_c(index : int) -> int:  
   return fibo(index)