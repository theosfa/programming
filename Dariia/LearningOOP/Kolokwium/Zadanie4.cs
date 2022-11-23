using System;

namespace Kolokwium{

    interface DoubleInt{
        bool Check();
    }
    interface MersaneInt{
        bool Check();
    }
    class Zadanie41 : DoubleInt{
        // поля класса
        private int num;

        // методы класса
        public Zadanie41(int num){
            this.num = num;
            
        }
        public bool Check(){
            int n = Solver();
            bool check = false;
            if (n == 2){
                check = true;
            }
            return check;
        }
        public int getNum(){
            return this.num;
        }
        private int Solver(){
            int a = this.num;
            int n = 0;
            while (a > 0)
            {
                n++;
                a = a /10 ;
            }
            return n;
        }
    }

    class Zadanie42 : MersaneInt{
        // поля класса
        private int num;

        // методы класса
        public Zadanie42(int num){
            this.num = num;
            
        }
        public bool Check(){
            bool check = false;
            if ((this.num + 1) % 2 == 0){
                check = true;
            }
            return check;
        }
        public int getNum(){
            return this.num;
        }
    }

    // class Program
    // {
    //     public static bool Action(DoubleInt doubleInt)
    //     {
    //         return doubleInt.Check();
    //     }
    //     public static bool Action(MersaneInt mersaneInt)
    //     {
    //         return mersaneInt.Check();
    //     }
    //     public static void Main(string[] args)
    //     {
    //         int n = 15;
    //         Zadanie41 first = new Zadanie41(n);
    //         Zadanie42 second = new Zadanie42(n);
    //         bool f = Action(first);
    //         bool s = Action(second);
    //         Console.WriteLine("First : " + f);
    //         Console.WriteLine("Second : " + s);
    //     }
    // }

}