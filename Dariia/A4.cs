using System;

namespace DariaLearningProgramming
{
    class A4
    {
        public A4() { }

        public String Solver(int mass)
        {
            if (mass > 3 && mass % 2 == 0)
            {
                return "Yes!";
            }
            else
            {
                return "No!";
            }
        }
    }
}