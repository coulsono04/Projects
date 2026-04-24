using System;

namespace TrueOrFalse
{
    class Program
    {
        static void Main(string[] args)
        {

            // This project tests skills with handling loops to create a True or False quiz game which is scalable.

            Console.WriteLine("Welcome to 'True or False?'\nPress Enter to begin:");
            string entry = Console.ReadLine();
            Tools.SetUpInputStream(entry);

            string[] questions = { "Is the capital city of England London?", "Is the capital city of France New Mexico?" };
            bool[] answers = { true, false };
            int questionsLength = questions.Length;
            bool[] responses = new bool[questionsLength];
            bool isBool = true;
            if (questions.Length != answers.Length)
            {
                Console.WriteLine("Warning, answers and questions are not the same");
            }
            int askingIndex = 0;
            foreach (string question in questions)
            {
                Console.WriteLine($"{question}, True or False?");
                string input = Console.ReadLine();
                input = input.ToLower();
                if (input == "true" || input == "false")
                {
                    isBool = true;
                }
                else
                {
                    isBool = false;
                }
                while (isBool == false)
                {
                    Console.WriteLine("Please respond with 'true' or 'false'.");
                    input = Console.ReadLine();
                    input = input.ToLower();
                    if (input == "true" || input == "false")
                    {
                        isBool = true;
                    }
                    else
                    {
                        isBool = false;
                    }
                }
                bool inputBool = false;
                if (input == "true")
                {
                    inputBool = true;
                }
                else
                {
                    inputBool = false;
                }
                responses[askingIndex] = inputBool;
                askingIndex++;
            }
            int scoringIndex = 0;
            int score = 0;
            foreach (var num in answers)
            {
                var value = responses[scoringIndex];
                Console.WriteLine($"{scoringIndex}. Input: {value} Answer: {num}");
                if (value == num)
                {
                    score++;
                }
                scoringIndex++;
            }
            Console.WriteLine($"You got {score} out of {questions.Length} correct!");
        }
    }
}
