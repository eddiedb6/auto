// UIFunc.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"

// This is the main DLL file.

#include "stdafx.h"

#include "UIFunc.h"

#include <Windows.h>
#include <string>

void UIFunc::mouse_event(unsigned int dwFlags, unsigned int dx, unsigned int dy, unsigned int cButtons, unsigned int dwExtraInfo)
{
    ::mouse_event(dwFlags, dx, dy, cButtons, dwExtraInfo);
}

void UIFunc::keybd_event(unsigned char bVk, unsigned char bScan, unsigned long dwFlags, unsigned long dwExtraInfo)
{
    ::keybd_event(bVk, bScan, dwFlags, dwExtraInfo);
}

bool UIFunc::SetCursorPos(int X, int Y)
{
    return ::SetCursorPos(X, Y) ? true : false;
}





