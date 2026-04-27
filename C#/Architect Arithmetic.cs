using System;

namespace ArchitectArithmetic
{
    class Program
    {
        public static void Main(string[] args)
        {
            // This project assesses skills with methods to assess a floors total area with shape functions and calculate the cost of materials.

            CalculateTotalCost();
        }
        static double Rectangle(double length, double width)
        {
            return length * width;
        }
        static double Circle(double radius)
        {
            return Math.PI * Math.Pow(radius, 2);
        }
        static double Triangle(double bottom, double height)
        {
            return 0.5 * bottom * height;
        }
        static void CalculateTotalCost()
        {
            // Tests methods are working properly
            double testRect1 = Rectangle(4, 5);
            double testCircle1 = Circle(4);
            double testTriangle1 = Triangle(10, 9);
            Console.WriteLine(testRect1);
            Console.WriteLine(testCircle1);
            Console.WriteLine(testTriangle1);

            // Main Calculation of the floor plan
            double triangle1 = Triangle(750, 500);
            double rectangle1 = Rectangle(2500, 1500);
            double circle1 = Circle(375);
            // Divided by 2 as its a semi circle
            circle1 /= 2;
            // Testing values
            Console.WriteLine(rectangle1);
            Console.WriteLine(circle1);
            Console.WriteLine(triangle1);
            // Adding them together
            double floorPlan = triangle1 + rectangle1 + circle1;
            // Working out cost in Mexican Pesos
            double floorPlanCost = floorPlan * 180;
            // Value before rounding
            Console.WriteLine($"The value before rounding is {floorPlanCost}.");
            floorPlanCost = Math.Round(floorPlanCost, 2);
            Console.WriteLine($"The value after rounding is {floorPlanCost}.");
            // Final write up line
            Console.WriteLine($"The total cost of the floorplan, which space is {floorPlan} is {floorPlanCost} Mexican Pesos.");
        }
    }
}
