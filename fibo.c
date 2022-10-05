int fibo(int index){
    int cur = 0;
    int next = 1;
    for (int i = 0; i < index; i++){
        int temp = cur;
        cur = next;
        next += temp;
    }
    return cur;
}