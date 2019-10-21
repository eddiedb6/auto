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
        public static Process StartApp(String path)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Start process: {0}", path);
            }

            Process app = Process.Start(path);
            return app;
        }

        public static AutomationElement GetDesktop()
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Get desktop");
            }

            return AutomationElement.RootElement;
        }

        public static AutomationElement GetForm(String caption)
        {
            // If use descendant scope, it could find the form. 
            // But following element finding in the form will be failed.
            AutomationElement form = GetElementByTextInChildrenScope(caption, GetDesktop());
            if (form != null)
            {
                return form;
            }

            return TryGetElementByText(caption, GetDesktop());
        }

        public static AutomationElement TryGetElementByText(String text, AutomationElement parent)
        {
            AutomationElement element = GetElementByTextInDescendantScope(text, parent);
            if (element != null)
            {
                return element;
            }

            element = GetElementByTextInChildrenScope(text, parent);
            if (element != null)
            {
                return element;
            }

            element = GetElementByTextInSubtreeScope(text, parent);
            if (element != null)
            {
                return element;
            }

            return element;
        }

        public static AutomationElement TryGetElementByType(String typeText, AutomationElement parent)
        {
            AutomationElement element = GetElementByTypeInDescendantScope(typeText, parent);
            if (element != null)
            {
                return element;
            }

            element = GetElementByTypeInChildrenScope(typeText, parent);
            if (element != null)
            {
                return element;
            }

            element = GetElementByTypeInSubtreeScope(typeText, parent);
            if (element != null)
            {
                return element;
            }

            return element;
        }

        public static AutomationElement GetElementByTextInChildrenScope(String text, AutomationElement parent)
        {
            return GetElementByText(text, parent, TreeScope.Children);
        }

        public static AutomationElement GetElementByTextInDescendantScope(String text, AutomationElement parent)
        {
            return GetElementByText(text, parent, TreeScope.Descendants);
        }

        public static AutomationElement GetElementByTextInSubtreeScope(String text, AutomationElement parent)
        {
            return GetElementByText(text, parent, TreeScope.Subtree);
        }
        
        public static AutomationElement GetElementByText(String text, AutomationElement parent, TreeScope scop)
        {
            text = ConvertUFT8String(text);

            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Find by text: {0}, {1}, {2}", text, parent, scop);
            }

            return parent.FindFirst(scop, new PropertyCondition(AutomationElement.NameProperty, text));
        }

        public static AutomationElement GetElementByTypeInDescendantScope(String typeText, AutomationElement parent)
        {
            return GetElementByType(typeText, parent, TreeScope.Descendants);
        }

        public static AutomationElement GetElementByTypeInChildrenScope(String typeText, AutomationElement parent)
        {
            return GetElementByType(typeText, parent, TreeScope.Children);
        }

        public static AutomationElement GetElementByTypeInSubtreeScope(String typeText, AutomationElement parent)
        {
            return GetElementByType(typeText, parent, TreeScope.Subtree);
        }
        
        public static AutomationElement GetElementByType(String typeText, AutomationElement parent, TreeScope scop)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Find by type: {0}, {1}, {2}", GetControlTypeFromText(typeText), parent, scop);
            }

            return parent.FindFirst(TreeScope.Children, new PropertyCondition(AutomationElement.ControlTypeProperty, GetControlTypeFromText(typeText)));
        }

        public static void SendMouseEvent(uint dwFlags, uint dx, uint dy, uint cButtons, uint dwExtraInfo)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Mouse event: {0}, {1}, {2}, {3}, {4}", dwFlags, dx, dy, cButtons, dwExtraInfo);
            }

            Wrapper.mouse_event(dwFlags, dx, dy, cButtons, dwExtraInfo);
        }

        public static void SendKeyEvent(byte bVk, byte bScan, uint dwFlags, uint dwExtraInfo)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Key event: {0}, {1}, {2}, {3}", bVk, bScan, dwFlags, dwExtraInfo);
            }

            Wrapper.keybd_event(bVk, bScan, dwFlags, dwExtraInfo);
        }

        static ControlType GetControlTypeFromText(String typeText)
        {
            if (!controlTypeMap.ContainsKey(typeText))
            {
                throw new System.Exception("[MS Plugin] Control type is not defined");
            }

            return controlTypeMap[typeText];
        }

        public static bool SetFocus(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Set focus: {0}", element);
            }

            if (element == null)
            {
                return false;
            }

            element.SetFocus();
            return true;
        }

        public static bool SetCursorPos(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Set cursor pos: {0}", element);
            }

            if (element == null)
            {
                return false;
            }

            Point p = element.GetClickablePoint();
            return Wrapper.SetCursorPos((int)p.X, (int)p.Y);
        }

        public static bool Click(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Click: {0}", element);
            }

            if (element == null)
            {
                return false;
            }

            Point p = element.GetClickablePoint();
            Wrapper.SetCursorPos((int)p.X, (int)p.Y);
            Wrapper.mouse_event(MOUSEEVENT_LEFTDOWN | MOUSEEVENT_LEFTUP, (uint)(p.X), (uint)(p.Y), 0, 0);

            return true;
        }

        public static bool IsCheckboxChecked(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Is checkbox checked: {0}", element);
            }

            if (element == null)
            {
                return false;
            }

            object objPattern;
            if (element.TryGetCurrentPattern(TogglePattern.Pattern, out objPattern))
            {
                TogglePattern togPattern = objPattern as TogglePattern;
                if (togPattern.Current.ToggleState == ToggleState.On)
                {
                    return true;
                }
            }

            return false;
        }   

        public static bool IsEnabled(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Is enabled: {0}", element);
            }

            if (element == null)
            {
                return false;
            }

            bool isEnabled = (bool)(element.GetCurrentPropertyValue(AutomationElement.IsEnabledProperty));
            return isEnabled;
        }

        public static string GetText(AutomationElement element)
        {
            if (debug)
            {
                System.Console.WriteLine("[MS Plugin] Get text: {0}", element);
            }

            if (element == null)
            {
                return null;
            }

            ControlType controlType = element.GetCurrentPropertyValue(AutomationElement.ControlTypeProperty) as ControlType;

            if (controlType == ControlType.Edit)
            {
                return element.GetCurrentPropertyValue(ValuePattern.ValueProperty) as string;
            }
            else if (controlType == ControlType.Document)
            {
                TextPattern text = (TextPattern)(element.GetCurrentPattern(TextPattern.Pattern));
                if (text != null)
                {
                    System.Windows.Automation.Text.TextPatternRange[] textRange;
                    textRange = text.GetSelection();
                    return textRange[0].GetText(-1);
                }
            }
            else
            {
                string text = element.GetCurrentPropertyValue(ValuePattern.ValueProperty) as string;
                if (text == null)
                {
                    return element.GetCurrentPropertyValue(AutomationElement.NameProperty) as string;
                }
            }
            
            return null;
        }

        static String ConvertUFT8String(String utf8String)
        {
            if (utf8String.Length <= 0)
            {
                return "";
            }

            char[] utf8Chars = utf8String.ToCharArray();
            int len = utf8Chars.GetLength(0);
            byte[] utf8Bytes = new byte[len];
            for (int i = 0; i < len; ++i)
            {
                utf8Bytes[i] = (byte)utf8Chars[i];
            }
            
            return Encoding.UTF8.GetString(utf8Bytes);
        }

        static bool debug = false;
        static Dictionary<String, ControlType> controlTypeMap = new Dictionary<string, ControlType>()
        {
            {"uiapptab", ControlType.Tab},
            {"uieditbox", ControlType.Edit}
        };

        const int MOUSEEVENT_LEFTDOWN = 0x02;
        const int MOUSEEVENT_LEFTUP = 0x04;
    }
}
