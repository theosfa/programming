using System;

namespace ProjectLogin{
    class User{
        string Login{get;}
        string Email{get;}
        string Password;
        string NameSurname{get;}
        int age{get;}

        public User(string Login, string Email, string Password, string NameSurname, int age){
            this.Login = Login;
            this.Email = Email;
            this.Password = Password;
            this.NameSurname = NameSurname;
            this.age = age;
            Console.WriteLine("User created");
        }
    }
}