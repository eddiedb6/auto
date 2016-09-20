using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Windows.Automation;
using System.Threading;
using System.Windows;
using MS;

namespace MSTest
{
    class Program
    {
        static void Main(string[] args)
        {
            if (!MSWrapper.StartApp("C:/Windows/System32/calc.exe"))
            {
                System.Console.WriteLine("Failed to start app");
                return;
            }

            Thread.Sleep(3000);
            AutomationElement form = MSWrapper.GetForm("Calculator");
            if (form == null)
            {
                System.Console.WriteLine("Failed to find form");
                return;
            }

            System.Console.WriteLine("Well done!");
        }
    }
}
