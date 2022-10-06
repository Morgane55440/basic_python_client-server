cdef extern from "mathfun.h":  
    unsigned long long fibo(unsigned long index)

def fibo_c(index : int) -> int:  
   return fibo(index)