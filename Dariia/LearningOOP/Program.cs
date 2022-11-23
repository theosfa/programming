using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;

namespace Kolokwium
{
    class Program
    {
        public static int AgeComparer(Animals left,Animals right)
        {
            if (left.age > right.age) return 1;
            else if (left.age == right.age) return 0;
            return -1;
        }
        // static void Main(string[] args)
        // {
        //     // Declare a list of type int.

        //     var repo = new MyRepo<Animals>();
        //     var animal1 = new Animals(5) { Title = "Cat" };
        //     repo.Add(animal1);
        //     var animal2 = new Animals(7) { Title = "Dog" };
        //     repo.Add(animal2);
        //     var animal3 = new Animals(1) { Title = "deer" };
        //     repo.Add(animal3);
        //     var animal4 = new Animals(3) { Title = "fox" };
        //     repo.Add(animal4);

        //     repo.Sort(AgeComparer).Show();

        //     repo.Filter((x) => x.age > 4).Show();
        //     Console.ReadLine();
        // }

    }
    public class Animals : ICloneable
    {
        
        public int age {get; set;}

        public Animals(int age){
            this.age = age;
        }
        public object Clone()
        {
            return (object)new Animals(age);
        }
    }

    public class MyRepo<T> where T : class, ICloneable
    {
        private List<T> elements;
        public int Size { get { return elements.Count; } }
        public MyRepo()
        {
            elements = new List<T>();
        }

        public void Add(T obj)
        {
            elements.Add((T)obj.Clone());
        }

        public MyRepo<T> Filter(Predicate<T> predicate)
        {
            MyRepo<T> result = new MyRepo<T>();

            foreach (var item in elements)
            {
                if(predicate(item)) result.Add(item);
            }

            return result;

        }

        public MyRepo<T> Sort(Comparison<T> comparer)
        {
            List<T> sorted = Filter((x) => true).elements;
            sorted.Sort(comparer);

            MyRepo<T> result = new MyRepo<T>();
            result.elements = sorted;

            return result;
        }
        public void Show()
        {
            Console.WriteLine(this.ToString());
        }

        public override string ToString()
        {
            if (elements.Count > 0)
            {
                string result = $"{elements.Count} : ";

                foreach (T item in elements)
                {
                    result += $"{item.ToString()}, ";
                }

                return result.Substring(0, result.Length - 2) + ";";
            }

            return "Empty";

        }



    }

}