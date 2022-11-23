using System;

namespace ProjectLogin{
    class Language{
        int lang{get; set;}

        Language(){
            lang = 0;
        }

        public string UserName(){
            switch (lang){
                case 0:
                return "User name";
                break;
                case 1:
                return "Nazwa użytkownika";
                break;
            }
            return "Ім'я користувача";
        } 
        public string Password(){
            switch (lang){
                case 0:
                return "Password";
                break;
                case 1:
                return "Hasło";
                break;
            }
            return "Пароль";
        }

        public string Email(){
            return "Email";
        }

        public string Name(){
            switch (lang){
                case 0:
                return "Name";
                break;
                case 1:
                return "Imę";
                break;
            }
            return "Ім'я";
        }

        public string Age(){
            switch (lang){
                case 0:
                return "Age";
                break;
                case 1:
                return "Wiek";
                break;
            }
            return "Вік";
        }

        public void MainPage(){
            switch (lang){
                case 0:
                System.Console.WriteLine("1. Change lang");
                System.Console.WriteLine("2. Sign in");
                System.Console.WriteLine("3. Sign up");
                System.Console.WriteLine("4. List of users");
                System.Console.WriteLine("0. Exit");
                break;
                case 1:
                System.Console.WriteLine("1. Zmień język");
                System.Console.WriteLine("2. Zalogować się");
                System.Console.WriteLine("3. Podpisywać się");
                System.Console.WriteLine("4. Lista użytkowników");
                System.Console.WriteLine("0. Wyjście");
                break;
                case 2:
                System.Console.WriteLine("1. Змініти мову");
                System.Console.WriteLine("2. Увійти");
                System.Console.WriteLine("3. Зареєструватись");
                System.Console.WriteLine("4. Список користувачів");
                System.Console.WriteLine("0. Вихід");
                break;
            }
            
            
        }

        

        public void ChangingLanguagePage(){
            switch (lang){
                case 0:
                System.Console.WriteLine(LanguageIs());
                System.Console.WriteLine("Select lang :");
                System.Console.WriteLine("1. Polish");
                System.Console.WriteLine("2. Ukranian");
                System.Console.WriteLine("0. Cancel changes");
                break;
                case 1:
                System.Console.WriteLine(LanguageIs());
                System.Console.WriteLine("Wybierz język");
                System.Console.WriteLine("1. Angelski");
                System.Console.WriteLine("2. Ukraiński");
                System.Console.WriteLine("0. Anuluj zmiany");
                break;
                case 2:
                System.Console.WriteLine(LanguageIs());
                System.Console.WriteLine("Виберіть мову :");
                System.Console.WriteLine("1. Англійска");
                System.Console.WriteLine("2. Польска");
                System.Console.WriteLine("0. Скасувати зміни");
                break;
            }
        }

        public void SignInPage(){
            switch (lang){
                case 0:
                System.Console.WriteLine("Sign in");
                System.Console.WriteLine("2. Sign in");
                System.Console.WriteLine("3. Sign up");
                System.Console.WriteLine("4. List of users");
                System.Console.WriteLine("0. Exit");
                break;
                case 1:
                System.Console.WriteLine("1. Zmień język");
                System.Console.WriteLine("2. Zalogować się");
                System.Console.WriteLine("3. Podpisywać się");
                System.Console.WriteLine("4. Lista użytkowników");
                System.Console.WriteLine("0. Wyjście");
                break;
                case 2:
                System.Console.WriteLine("1. Змініти мову");
                System.Console.WriteLine("2. Увійти");
                System.Console.WriteLine("3. Зареєструватись");
                System.Console.WriteLine("4. Список користувачів");
                System.Console.WriteLine("0. Вихід");
                break;
            }
        }

        public string LanguageIs(){
            if (lang == 0) {
                    return "Current language is : English";
                } else if (lang == 1){
                    return "Obecny język jest : Polska";
                }
                return "Текущою мовою є : Українська";
        }

    }
}