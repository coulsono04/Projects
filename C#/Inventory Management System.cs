using System;
using System.Collections.Generic;


public class InventoryManagement
{
    public static void Main(string[] args)
    {
        // This program assesses creating and managing lists, through an inventory management system.

        List<string> inventoryList = new List<string>();
        inventoryList.AddRange(new string[] { "Printer", "Laptop", "Desk Chair", "Monitor", "Keyboard" });
        Console.WriteLine(inventoryList.Count);

        bool hasDeskChair = inventoryList.Contains("Desk Chair");
        Console.WriteLine(hasDeskChair);
        bool removed = inventoryList.Remove("Printer");
        // Print each element of updated inventory list
        foreach (string element in inventoryList)
        {
            Console.WriteLine(element);
        }
        // Create new list of new items
        List<string> newItems = new List<string> { "Mouse", "Desk Lamp" };
        inventoryList.AddRange(new string[] { newItems[0], newItems[1] });
        Console.WriteLine("------");
        // Checks the list to see what needs to be removed
        foreach (string element in inventoryList)
        {
            Console.WriteLine(element);
        }
        inventoryList.RemoveRange(4, 2);
        // Add top 3 items to new list
        List<string> topInventory = new List<string> { inventoryList[0], inventoryList[1], inventoryList[2] };
        // Search through list
        Console.WriteLine("---TopInventory List---");
        foreach (string element in topInventory)
        {
            Console.WriteLine(element);
        }
    }
}