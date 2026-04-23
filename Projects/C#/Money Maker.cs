using System;

namespace MoneyMaker
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            // This project finds how many coins of varying values make up a certain amount of money, to test numbers and operators skills.

            Console.WriteLine("Welcome to Money Maker!");
            Console.WriteLine("what is the amount you'd like to convert?");
            string totalAsString = Console.ReadLine();
            double totalAsDouble = Convert.ToDouble(totalAsString);
            Console.WriteLine($"{totalAsDouble} is equal to...");

            int goldCoin = 10;
            int silverCoin = 5;
            double goldCoins = Math.Floor(totalAsDouble / goldCoin);
            double remainder = goldCoins % goldCoin;
            double silverCoins = Math.Floor(remainder / silverCoin);
            remainder = remainder % silverCoin;

            Console.WriteLine(goldCoins);
            Console.WriteLine(silverCoins);
            Console.WriteLine(remainder);
        }
    }
}
