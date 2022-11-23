using System;

namespace FirstProgram {
    class A158 {
        public A158(){}

        public int Solver(int n, int k, int[] array){
            int answer = 0;

            for(int i = 0; i < n; i++){
                if(array[i] >= array[k-1] && array[i] > 0){
                    answer++;
                }
            }
            return answer;
        }
    }
}