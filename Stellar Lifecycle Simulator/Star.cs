using System;

namespace StarLifecycleSimulator
{
    class Star
    {
        public string name;
        public string type;
        public int age;
        public double brightness;

        public Star(string name, string type)
        {
            this.name = name;
            this.type = type;
            brightness = 1.0;
        }
        public Star(string name) : this(name, "Unknown")
        {
            Console.WriteLine("Star type set to default: Unknown.");
        }
        public void Shine()
        {
            Console.WriteLine($"Star {this.name} is shining with brightness {brightness}.");
        }
        public void GrowOlder()
        {
            this.age++;
            brightness *= 0.9;
        }
        public void Supernova()
        {
            brightness = 0;
            Console.WriteLine($"Star {name} has exploded in a supernova.");
        }
    }
}