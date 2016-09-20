// UIFunc.h

#ifndef __UIFUNC_H__
#define __UIFUNC_H__

#ifdef UIFUNC_EXPORTS
#define DLL_EXPORTS __declspec(dllexport)
#else
#define DLL_EXPORTS
#endif // UIFUNC_EXPORTS

class DLL_EXPORTS UIFunc
{
public:
    static void mouse_event(unsigned int dwFlags, unsigned int dx, unsigned int dy, unsigned int cButtons, unsigned int dwExtraInfo);
    static void keybd_event(unsigned char bVk, unsigned char bScan, unsigned long dwFlags, unsigned long dwExtraInfo);
    static bool SetCursorPos(int X, int Y);
};

#endif // __UIFUNC_H__