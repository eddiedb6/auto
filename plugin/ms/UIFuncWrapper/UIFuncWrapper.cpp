// This is the main DLL file.

#include "stdafx.h"

#include "UIFuncWrapper.h"
#include "UIFunc.h"

namespace UIFuncWrapper 
{
    void Wrapper::mouse_event(unsigned int dwFlags, unsigned int dx, unsigned int dy, unsigned int cButtons, unsigned int dwExtraInfo)
    {
        UIFunc::mouse_event(dwFlags, dx, dy, cButtons, dwExtraInfo);
    }

    void Wrapper::keybd_event(unsigned char bVk, unsigned char bScan, unsigned long dwFlags, unsigned long dwExtraInfo)
    {
        UIFunc::keybd_event(bVk, bScan, dwFlags, dwExtraInfo);
    }

    bool Wrapper::SetCursorPos(int X, int Y)
    {
        return UIFunc::SetCursorPos(X, Y);
    }
}