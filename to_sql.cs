
using System;
using System.Collections;
using System.Data;
using System.Data.SqlClient;
using System.Data.SqlTypes;
using System.IO;
using System.Linq;
using Microsoft.SqlServer.Server;
using Microsoft.VisualBasic;
using System.Threading;
using System.Collections.Generic;

namespace To_SQL
{

    //public partial class UserDefinedFunctions
    public static class MAIN

    {
        private static void Main(string [] args)
        {
            string header = GetCsvHeader("C:/Data/test.txt");
            string data = GetCsvBody("C:/Data/test.txt");
            //string test = CreateSQL(header);
            System.Console.WriteLine(CreateSQL(header));
            System.Console.WriteLine(insertsql(test)) ;
        }


        public static string CreateSQL(string csv) {
            var data = csv.Split(';');
            var table_name = "table";
            var sql = "CREATE TABLE " + table_name + " (";
            foreach (var item in data){
                sql = sql + "[" + item + "]" + " VARCHAR(MAX),";
            }
            return sql.TrimEnd(',') + ")"; 
        }

        public static string insertsql(string csv)
        { 
        var data = csv.Split(';');
        var table_name = "table";
        var sql = "INSERT INTO " + table_name + " VALUES (";
            foreach (var item in data){
                sql = sql + "(" + item + "]" + " VARCHAR(MAX),";
            }
            return sql.TrimEnd(',') + ")"; 
        }


        public static string 
            GetCsvHeader(string  filename)
        {
            var lines = File.ReadAllLines(filename);//.Select(a => a.Split(';'));
            var csv = from line in lines
                      let data = line.Split(';')
                      select  data[0] + ";" + data[1] + ";" + data[2]
                      ;

            foreach (var i in csv)
            {
                return i;
            }
            return "No File";

        }

        public static string GetCsvBody(string filename)
        {
            var lines = File.ReadAllLines(filename);//.Select(a => a.Split(';'));
            var csv = from line in lines
                      let data = line.Split(';')
                      select data[0] + ";" + data[1] + ";" + data[2]
                      ;

            foreach (var i in csv)
            {
                return i;
            }
            return "No File";

        }
    }
}


