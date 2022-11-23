using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectLogin
{
    class Database{
        public static SQLiteConnection CreateConnection()
      {

        SQLiteConnection sqlite_conn;
        // Create a new database connection:
        sqlite_conn = new SQLiteConnection("Data Source=database.db;Version=3;New=True;Compress=True;");
        // Open the connection:
        try{
            sqlite_conn.Open();
        } catch (Exception ex){

        }
        return sqlite_conn;
      }

      public static void CreateTable(SQLiteConnection conn, string tableName)
      {
         SQLiteCommand sqlite_cmd;
         string Createsql = "CREATE TABLE " + tableName + "(Login VARCHAR(20),Password VARCHAR(20),Email VARCHAR(20),Name VARCHAR(20),Age VARCHAR(20))";
         sqlite_cmd = conn.CreateCommand();
         sqlite_cmd.CommandText = Createsql;
         sqlite_cmd.ExecuteNonQuery();
      }

      public static void InsertData(SQLiteConnection conn, string tableName, string login, string password, string email, string name, string age)
      {
         SQLiteCommand sqlite_cmd;
         sqlite_cmd = conn.CreateCommand();
         sqlite_cmd.CommandText = "INSERT INTO " + tableName + "(Login, Password, Email, Name, Age) VALUES ('" + login + "','" + password + "','" + email + "','" + name + "','" + age + "');";
         sqlite_cmd.ExecuteNonQuery();

      }

      public static bool CheckIfExist(SQLiteConnection conn, string tableName, string login){
        SQLiteCommand sqlite_cmd = conn.CreateCommand();
        bool answer;
        sqlite_cmd.CommandText = "SELECT count(*) FROM " + tableName + " WHERE Login='" + login + "'";
        int count = Convert.ToInt32(sqlite_cmd.ExecuteScalar());
        if(count == 1){
            answer = true;
        } else {
            answer = false;
        }
            return answer;
      }

      public static string GetPassword(SQLiteConnection conn, string tableName, string login){
        SQLiteCommand sqlite_cmd = conn.CreateCommand();
        sqlite_cmd.CommandText = "SELECT Password FROM " + tableName + " WHERE Login='" + login + "'"; 
        return sqlite_cmd.ExecuteScalar().ToString();
      }

      public static void CloseDataBase(SQLiteConnection conn){
        conn.Close();
      }

      public static void UserData(SQLiteConnection conn, string tableName, Language lang, string login)
      {
        SQLiteDataReader sqlite_datareader;
        SQLiteCommand sqlite_cmd;
        string answer = "";
        sqlite_cmd = conn.CreateCommand();
        sqlite_cmd.CommandText = "SELECT Password FROM " + tableName + " WHERE EXISTS Login = '" + login + "'";
        
        answer += lang.UserName() +  sqlite_cmd.ExecuteScalar().ToString();
        Console.WriteLine(answer);
        }
      

      public static void AllUsersData(SQLiteConnection conn, string tableName, string login)
      {
        SQLiteDataReader sqlite_datareader;
        SQLiteCommand sqlite_cmd;
        sqlite_cmd = conn.CreateCommand();
        sqlite_cmd.CommandText = "SELECT * FROM " + tableName;

        sqlite_datareader = sqlite_cmd.ExecuteReader();
        while (sqlite_datareader.Read())
        {
          string myreader = sqlite_datareader.GetString(0);
          Console.WriteLine(myreader);
        }
      }
    }
}

