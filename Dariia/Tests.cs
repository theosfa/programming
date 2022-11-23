using System;

namespace DariaLearningProgramming
{
    class Tests
    {
        public static void Test_A4()
        {
            A4 test1 = new A4();
            int count = 0;
            for (int i = 0; i <= 100; i++)
            {
                if (test1.Solver(i) == "Yes!" && i > 3 && i % 2 == 0)
                {
                    count += 1;
                }
                if (test1.Solver(i) == "No!" && (i < 3 || i % 2 != 0))
                {
                    count += 1;
                }
            }
            if (count == 101)
            {
                Console.WriteLine("All tests passed");
            }
            else
            {
                Console.WriteLine("All tests not passed");
            }

        }

        public static void Test_A71()
        {
            
            int count = 0;


            int n = 4;
            String[] s1 = new String[n];
            A71 test1 = new A71(s1);
            s1[0] = "word";
            s1[1] = "localization";
            s1[2] = "Interpersperation";
            s1[3] = "a";
            String[] s1_solved = test1.Solver(n);
            s1[0] = "word";
            s1[1] = "l10n";
            s1[2] = "I15n";
            s1[3] = "a";
            int count_s1 = 0;
            for (int i = 0; i < n; i++)
            {
                if(s1[i].Equals(s1_solved[i]))
                {
                    count_s1++;
                }
            }
            if(count_s1 == 4)
            {
                count++;
            }


            String[] s2 = new String[n];
            A71 test2 = new A71(s2);
            s2[0] = "word";
            s2[1] = "localizatiohafern";
            s2[2] = "Interperspe71524ration";
            s2[3] = "a";
            String[] s2_solved = test1.Solver(n);
            s2[0] = "word";
            s2[1] = "l15n";
            s2[2] = "I20n";
            s2[3] = "a";
            int count_s2 = 0;
            for (int i = 0; i < n; i++)
            {
                if (s2[i].Equals(s2_solved[i]))
                {
                    count_s2++;
                }
            }
            if (count_s2 == 4)
            {
                count++;
            }

            if (count == 2)
            {
                Console.WriteLine("All tests passed");
            }
            else
            {
                Console.WriteLine("All tests not passed");
            }

        }
    }
}