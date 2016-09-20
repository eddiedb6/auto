using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.IO;
using System.Diagnostics;
using System.Windows.Automation;
using System.Windows;
using UIFuncWrapper;

namespace MS
{
    public class MSWrapper
    {
        public static bool StartApp(String path)
        {
            Process app = Process.Start(path);
            return app != null;
        }

        public static bool SetCursorPos(AutomationElement element)
        {
            Point p = element.GetClickablePoint();
            return Wrapper.SetCursorPos((int)p.X, (int)p.Y);
        }

        public static void SendMouseEvent(uint dwFlags, uint dx, uint dy, uint cButtons, uint dwExtraInfo)
        {
            Wrapper.mouse_event(dwFlags, dx, dy, cButtons, dwExtraInfo);
        }

        public static void SendKeyEvent(byte bVk, byte bScan, uint dwFlags, uint dwExtraInfo)
        {
            Wrapper.keybd_event(bVk, bScan, dwFlags, dwExtraInfo);
        }

        public static AutomationElement GetDesktop()
        {
            return AutomationElement.RootElement;
        }

        public static AutomationElement GetForm(String caption)
        {
            return GetElementByTextDescendant(caption, AutomationElement.RootElement);
        }

        public static AutomationElement GetElementByTextDescendant(String text, AutomationElement parent)
        {
            return GetElementByText(text, parent, TreeScope.Descendants);
        }
        
        public static AutomationElement GetElementByText(String text, AutomationElement parent, TreeScope scop)
        {
            return parent.FindFirst(scop, new PropertyCondition(AutomationElement.NameProperty, text));
        }
    }
}
