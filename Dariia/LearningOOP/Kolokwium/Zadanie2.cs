using System;

namespace Kolokwium{

    class Zadanie2{
        // поля класса
        private int a;
        private int b;
        private int c;

        private double pole = 0.0;

        // методы класса
        public Zadanie2(int a, int b, int c){
            this.a = a;
            this.b = b;
            this.c = c;
            
        }
        public int getA(){
            return this.a;
        }
        public int getB(){
            return this.b;
        }
        public int getC(){
            return this.c;
        }
        public double getPole(){
            this.Solver();
            return this.pole;
        }
        private void Solver(){
            double p = (this.a + this.b + this.c)/2;
            double s = p*(p - this.a)*(p - this.b)*(p - this.c);
            if (s > 0){
                this.pole = Math.Sqrt(s);
            }
        }
    }
    class Triangle : Zadanie2 {
        public Triangle(int a, int b, int c)
        : base(a, b, c){

        }

        public bool Rownoboczny(){
            bool rownoboczny = false;
            if (getA() == getB() || getA() == getC() || getB() == getC()){
                rownoboczny = true;
            }
            return rownoboczny;
        }
        // public static void Main(String[] args){
        //     Triangle triangle = new Triangle(3, 4, 4);
        //     bool rownoboczny = false;
        //     if(triangle.getPole() != 0){
        //         rownoboczny = triangle.Rownoboczny();
        //         Console.WriteLine("Pole:" + triangle.getPole());
        //         Console.WriteLine("Rownoboczny:" + rownoboczny);
        //     }else{
        //         Console.WriteLine("No such triangle");
        //     }
        // }
    }

}