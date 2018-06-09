using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 20;
            /*conditions such as i % 2 == 0 are useless here because  if a number can be divided by 4, it can
            be divided by 2. Same for, 2 3 4 5 6 7 8 9. So we can begin on 11 */
            while ( i % 11 != 0 || i % 12 != 0 || i % 13 != 0 ||
                     i % 14 != 0 || i % 15 != 0 || i % 16 != 0 || i % 17 != 0 ||
                     i % 18 != 0 || i % 19 != 0 || i % 20 != 0)
            {
                i += 20;
            }
            Console.WriteLine(i);
            Console.ReadLine();
        }
    }
}
