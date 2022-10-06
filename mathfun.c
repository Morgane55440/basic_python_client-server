unsigned long long fibo(unsigned long index){
    unsigned long cur = 0;
    unsigned long next = 1;
    for (unsigned long i = 0; i < index; i++){
        unsigned long temp = cur;
        cur = next;
        next += temp;
    }
    return cur;
}