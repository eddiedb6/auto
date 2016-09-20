import clr
import time

clr.AddReferenceToFile("MS.dll")
import MS

if not MS.MSWrapper.StartApp("C:/Windows/System32/calc.exe"):
    print("Failed to start app")
    exit

time.sleep(3)
form = MS.MSWrapper.GetForm("Calculator")
if form is None:
    print("Failed to find form")
    exit

print("Well done!")