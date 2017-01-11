import sys
import os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../schema"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))

from SchemaChecker import *

currentPath = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(currentPath, "key.py")
schemaPath = os.path.join(currentPath, "keyschema.py")

configChecker = SchemaChecker(configPath, schemaPath)
result, config = configChecker.Check()
if not result:
    print "Schema check failed"
    sys.exit(0)
else:
    print "Schema check successful"

def OperateFile(filePath, operator):
    print "Operate on file " + filePath
    originalFile = open(filePath, "r")
    newFile = open(filePath + ".tmp", "w")
    operator(originalFile, newFile)
    originalFile.close()
    newFile.close()
    os.remove(filePath)
    os.rename(filePath + ".tmp", filePath)

def UpdateConst(originalFile, newFile):
    print "Update Const file"
    global config
    keyBuf = ""
    for key in config:
        keyBuf += key["Name"] + " = " + "\"" + key["Name"].lower()  + "\"\n"
    line = originalFile.readline()
    while line:
        temp = line.strip()
        if temp == "### Schema key definition start ###":
            # Define key
            keyBuf = line + keyBuf
            while line:
                if line.strip() == "### Schema key definition end ###":
                    keyBuf += line
                    newFile.write(keyBuf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for type definition"
                sys.exit(0)
        else:
            newFile.write(line)
        line = originalFile.readline()

def UpdateSchema(originalFile, newFile):
    print "Update Schema file"
    global config
    buf = ""
    for key in config:
        uiName = key["Name"]
        rule = ""
        schemaType = "        SchemaType: " + key["SchemaType"]
        if "SchemaRule" in key:
            rule += "        SchemaRule: [\n"
            rule += "            " + key["SchemaRule"] + "\n"
            rule += "        ],\n"
            schemaType += ","
        schemaType += "\n"
        buf += "    AFWConst." + uiName + ": {\n"
        buf += schemaType
        buf += rule
        buf += "    },\n"
    line = originalFile.readline()
    while line:
        if line.strip() == "### Schema key schema start ###":
            # Insert key schema
            buf = line + buf
            while line:
                if line.strip() == "### Schema key schema end ###":
                    buf += line
                    newFile.write(buf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for ui schema"
                sys.exit(0)
        else:
            newFile.write(line)
        line = originalFile.readline()

# AFWConst.py
constPath = os.path.join(currentPath, "../AFWConst.py")
OperateFile(constPath, UpdateConst)

# AFWSchema.py
schemaPath = os.path.join(currentPath, "../AFWSchema.py")
OperateFile(schemaPath, UpdateSchema)
