using System;

namespace Kolokwium{

    class Zadanie1{
        // поля класса
        private int m;
        private int n;

        private int liczb = 0;

        // методы класса
        public Zadanie1(int m, int n){
            this.n = n;
            this.m = m;
            
        }
        public Zadanie1(){}

        public void setN(int n){
            this.n = n;
        }
        public void setM(int n){
            this.n = n;
        }
        public int getLiczb(){
            this.Solver();
            return this.liczb;
        }
        private void Solver(){
            for(int i = m; i <= n; i++){
                if(i % 7 == 0){
                    this.liczb++;
                }
            }
        }

        // public static void Main(String[] args){
        //     Zadanie1 punktA = new Zadanie1(12, 138);
        //     Console.WriteLine("Punkt A:" + punktA.getLiczb());
        //     Zadanie1 punktB = new Zadanie1();
        //     punktB.setM(48);
        //     punktB.setN(215);
        //     Console.WriteLine("Punkt B:" + punktB.getLiczb());
        // }
    }

}