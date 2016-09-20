// UIFuncWrapper.h

#pragma once

using namespace System;

namespace UIFuncWrapper {
    public ref class Wrapper
    {
    public:
        static void mouse_event(unsigned int dwFlags, unsigned int dx, unsigned int dy, unsigned int cButtons, unsigned int dwExtraInfo);
        static void keybd_event(unsigned char bVk, unsigned char bScan, unsigned long dwFlags, unsigned long dwExtraInfo);
        static bool SetCursorPos(int X, int Y);
    };
}
