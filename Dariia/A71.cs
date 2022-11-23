using System;
using System.Collections.Generic;
using System.Text;

namespace DariaLearningProgramming
{
    class A71
    {
        String[] s;
        public A71(String[] a)
        {
            s = a;
        }

        public String[] Solver(int n)
        {
            String[] d = new String[n];
            for (int i = 0; i < n; i++)
            {
                if (s[i].Length > 10)
                {
                    d[i] = s[i].Substring(0, 1) + (s[i].Length - 2).ToString() + s[i].Substring(s[i].Length - 1);
                }
                else
                {
                    d[i] = s[i];
                }

            }


            return d;
        }


    }
}