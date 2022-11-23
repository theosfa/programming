using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static ProjectLogin.Database;

namespace ProjectLogin{
    class Run{
        static void Main(string[] args)
        {   
            SQLiteConnection sqlite_conn;
            sqlite_conn = Database.CreateConnection();
            // string ans = "";
            // int lang = 0;

            // while (ans != "0") {
            //     if (lang == 0) {
            //         System.Console.WriteLine("1. Change lang");
            //         System.Console.WriteLine("2. Sign in");
            //         System.Console.WriteLine("3. Sign up");
            //         System.Console.WriteLine("4. Exit");
            //     } else if (lang == 1){
            //         System.Console.WriteLine();
            //     } else {

            //     }
                
            // }
            // CreateTable(sqlite_conn, "LoginBase");
            // InsertData(sqlite_conn, "LoginBase", "theos", "12345678", "theos.fa@gmail.com", "Fedor", "16");
            System.Console.WriteLine(GetPassword(sqlite_conn, "LoginBase", "theos"));
        }
    }
}