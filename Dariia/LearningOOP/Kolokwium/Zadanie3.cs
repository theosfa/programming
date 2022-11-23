using System;

namespace Kolokwium{

    class Zadanie3{
        // поля класса
        private int num;
        private int sum;

        // методы класса
        public Zadanie3(int num){
            this.num = num;
            this.sum = 0;
            
        }
        public int getNum(){
            return this.num;
        }
        public int getSum(){
            this.Solver();
            return this.sum;
        }
        private void Solver(){
            int a = this.num;
            while (a > 0)
            {
                this.sum += a % 10;
                a = a /10 ;
            }
        }
    }

    class Zadanie31{
        private int m;
        private int n;
        private int[] sums;

        public Zadanie31(int m, int n){
            this.n = n;
            this.m = m;
            this.sums = new int[this.n-this.m+1];
        }

        public int[] getSums(){
            this.Solver();
            return this.sums;
        }
        public void Solver(){
            int j = 0;
            for(int i = m; i <= n; i++){
                Zadanie3 buff = new Zadanie3(i);
                this.sums[j] = buff.getSum();
                j++;
            }
        }
        // public static void Main(String[] args){
        //     Zadanie3 first = new Zadanie3(257);
        //     Console.WriteLine("First sum:" + first.getSum());
        //     int m = Convert.ToInt32(Console.ReadLine());
        //     int n = Convert.ToInt32(Console.ReadLine());
        //     Zadanie31 second = new Zadanie31(m, n);
        //     int[] sums = second.getSums();
        //     for(int i = 0; i < sums.Length; i++){
        //         Console.WriteLine("Second sums[" + i + "]:" + second.getSums()[i]);
        //     }
        // }
    }

}