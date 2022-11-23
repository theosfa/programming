using System;

namespace FirstProgram {
    class A231 {
        public A231(){}

        public int Solver(int n, int[,] array){
            int answer = 0;

            for(int i = 0; i < n; i ++){
                if (array[i,0] + array[i,1] + array[i,2] >= 2){
                    answer++;
                }
            }

            return answer;
        }
    }
}