using System;

namespace StarLifecycleSimulator
{
    class Program
    {
        static void Main(string[] args)
        {
            // This project assess skills usings classes/Abstraction, and works alongside the other file "Stars" which holds the class. This file runs the main program

            /* Star Simulations */

            Star sun = new Star("Sun", "G-Type");
            sun.Shine();
            sun.GrowOlder();
            sun.Shine();
            sun.Supernova();

            Star unknownStar = new Star("Mystery Star");
            unknownStar.Shine();
            unknownStar.GrowOlder();
        }
    }
}