using System;

namespace DatingProfile
{
    class Program
    {
        static void Main(string[] args)
        {
            // This project practices skills using encapsulation by creating a dating profile service. This cs file handles creating the individuals profile object.

            string[] hobs = { "listening to audiobooks and podcasts", "playing rec sports like bowling and kickball", "writing a speculative fiction novel", "reading advice columns" };
            Profile sam = new Profile("Sam Drakkila", 30, "New York", "USA", hobs, "he/him");
            Console.WriteLine(sam.ViewProfile());

        }
    }
}
