using System;

namespace PasswordChecker
{
    class Program
    {
        public static void Main(string[] args)
        {

            // This project tests skills with conditional statements such as if stataments to assess how good and secure a user-input password is.

            int minLength = 8;
            string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string lowercase = "abcdefghijklmnopqrstuvwxyz";
            string digits = "0123456789";
            string specialChars = "!£$%^&*()-_=+~#";

            Console.WriteLine("Enter a password");
            string password = Console.ReadLine();
            int len = password.Length;

            int score = 0;
            if (len >= minLength)
            {
                score++;
                Console.WriteLine(score);
            }
            if (Tools.Contains(password, uppercase))
            {
                score++;
                Console.WriteLine(score);
            }
            if (Tools.Contains(password, lowercase))
            {
                score++;
                Console.WriteLine(score);
            }
            if (Tools.Contains(password, digits))
            {
                score++;
                Console.WriteLine(score);
            }
            if (Tools.Contains(password, specialChars))
            {
                score++;
                Console.WriteLine(score);
            }
            switch (score)
            {
                case >= 4:
                    Console.WriteLine("Extremely strong");
                    break;
                case 3:
                    Console.WriteLine("Strong");
                    break;
                case 2:
                    Console.WriteLine("Medium");
                    break;
                case 1:
                    Console.WriteLine("Weak");
                    break;
                default:
                    Console.WriteLine("The Password does not meet the standards");
                    break;
            }


        }
    }
}
