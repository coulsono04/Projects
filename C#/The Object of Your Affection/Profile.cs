using System;

namespace DatingProfile
{
    class Profile
    {
        // This is where the class for the dating app project is created, with a focus on improving skills with encapsulation.

        private string name;
        private int age;
        private string city;
        private string country;
        private string pronouns;
        private string[] hobbies;

        public Profile(string name, int age, string city, string country, string[] hobbies, string pronouns = "they/them")
        {
            this.name = name;
            this.age = age;
            this.city = city;
            this.country = country;
            this.pronouns = pronouns;
            this.hobbies = hobbies ?? new string[0];
        }

        public string ViewProfile()
        {
            string mainString = this.name + ", " + this.age + ", " + this.city + ", " + this.country + ", " + this.pronouns + ", hobbies: ";
            string result = string.Join(", ", this.hobbies);
            return mainString + result;

        }

        public void SetHobbies(string[] hobbies)
        {
            this.hobbies = hobbies;
        }

    }
}
