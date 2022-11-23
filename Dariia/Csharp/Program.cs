using System;

namespace Csharp {
    
    class Program {
        public static void reverse(string text,int n = 0){
            if(n < text.Length)
            {
                Console.Write(text[text.Length-(n+1)]);
                reverse(text, n + 1);
            }
        }

        public static int find(int n,int m)
        {
            int rand = new Random().Next(n,m);
            int steps = 0;

            Console.WriteLine(rand);

            while(true)
            {
                int middle = (n + m) / 2;
                steps++;

                if ((n + m) / 2 > rand)
                {
                    m = middle;
                }
                else if ((n + m) / 2 < rand)
                {
                    n = middle;
                }
                else break;
            }

            return steps;
        }
        static void Main(string[] args) {
            Deck deck = new Deck();
            int steps = find(100, 200);
            reverse("Hello!");
        }
    }
}
        