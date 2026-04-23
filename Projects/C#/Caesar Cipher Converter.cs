using System;

namespace CaesarCipher
{
    class Program
    {
        static void Main(string[] args)
        {

            // This project assesses loops and creates a text-to-Caesar-Cipher converter.

            char[] alphabet = new char[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
            Console.WriteLine("Secret Message>>");
            string message = Console.ReadLine();
            char[] secretMessage = message.ToCharArray();
            char[] encryptedMessage = new char[secretMessage.Length];

            for (int i = 0; i < secretMessage.Length; i++)
            {
                char letter = secretMessage[i];
                int alphabetPosition = Array.IndexOf(alphabet, letter);
                int newAlphabetPosition = (alphabetPosition + 3) % 26;

                char letterEncoded = alphabet[newAlphabetPosition];
                encryptedMessage[i] = letterEncoded;
            }
            string finalArray = String.Join("", encryptedMessage);
            Console.WriteLine($"Your encoded message is: {finalArray}");
        }
    }
}