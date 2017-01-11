import sys
import os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../schema"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))

from SchemaChecker import *

currentPath = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(currentPath, "ui.py")
schemaPath = os.path.join(currentPath, "uischema.py")

configChecker = SchemaChecker(configPath, schemaPath)
result, config = configChecker.Check()
if not result:
    print "Schema check failed"
    sys.exit(0)
else:
    print "Schema check successful"

def GenerateUIClassFile(element):
    print "Generate class file " + element["Class"] + ".py"
    className = element["Class"]
    parentName = element["Parent"]
    parents = [parentName]
    if "Abilities" in element:
        for ability in element["Abilities"]:
            parents.append(ability)
    buf = "import AFWConst\n"
    inherites = ", ".join(parents)
    for parent in parents:
        buf += "from " + parent + " import " + parent + "\n"
    buf += "\nclass " + className + "(" + inherites + "):\n"
    buf += "    def __init__(self, manager, config, parentConfig):\n"
    buf += "        " + parentName + ".__init__(self, manager, config, parentConfig)\n"
    if "Abilities" in element:
        for ability in element["Abilities"]:
            buf += "        " + ability + ".__init__(self, self._plugin)\n"
    return buf

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
    typeBuf = ""
    collectionBuf = ""
    for element in config:
        typeBuf += element["Name"] + " = " + "\"" + element["Name"].lower()  + "\"\n"
        collectionBuf += "    " + element["Name"] + ",\n"
    line = originalFile.readline()
    while line:
        temp = line.strip()
        if temp == "### UI types definition start ###":
            # Define UI types
            typeBuf = line + typeBuf
            while line:
                if line.strip() == "### UI types definition end ###":
                    typeBuf += line
                    newFile.write(typeBuf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for type definition"
                sys.exit(0)
        elif temp == "### UI types collection start ###":
            # Add types in collection
            collectionBuf = line + collectionBuf
            while line:
                if line.strip() == "### UI types collection end ###":
                    collectionBuf += line
                    newFile.write(collectionBuf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for type collection"
                sys.exit(0)
        else:
            newFile.write(line)
        line = originalFile.readline()

def UpdateUIManager(originalFile, newFile):
    print "Update UI Manager file"
    global config
    factoryBuf = ""
    importBuf = ""
    for element in config:
        uiName = element["Name"]
        className = element["Class"]
        factoryBuf += "        AFWConst." + uiName + ": lambda manager, config, parentConfig: " + className + "(manager, config, parentConfig),\n"
        importBuf += "from " + className + " import " + className + "\n"
    line = originalFile.readline()
    while line:
        temp = line.strip()
        if temp == "### UI type factory initialize start ###":
            # Insert UI type in UI factory
            factoryBuf = line + factoryBuf
            while line:
                if line.strip() == "### UI type factory initialize end ###":
                    factoryBuf += line
                    newFile.write(factoryBuf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for ui factory"
                sys.exit(0)
        elif temp == "### UI type import start ###":
            # Import UI type in UI factory
            importBuf = line + importBuf
            while line:
                if line.strip() == "### UI type import end ###":
                    importBuf += line
                    newFile.write(importBuf)
                    break
                line = originalFile.readline()
            if not line:
                print "Could not fine end for ui import in factory"
                sys.exit(0)
        else:
            newFile.write(line)
        line = originalFile.readline()

def UpdateSchema(originalFile, newFile):
    print "Update Schema file"
    global config
    buf = ""
    for element in config:
        uiName = element["Name"]
        rule = ""
        if "SchemaRule" in element:
            rule += "        SchemaRule: [\n"
            rule += "            " + element["SchemaRule"] + "\n"
            rule += "        ],\n"
        buf += "    AFWConst." + uiName + ": {\n"
        buf += rule
        buf += "        SchemaType: SchemaTypeDict\n"
        buf += "    },\n"
    line = originalFile.readline()
    while line:
        if line.strip() == "### App types schema start ###":
            # Insert UI schema
            buf = line + buf
            while line:
                if line.strip() == "### App types schema end ###":
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

# Generate UI class files
for element in config:
    classFilePath = os.path.join(currentPath, "../ui/" + element["Class"] + ".py")
    if os.path.exists(classFilePath):
        continue
    classFile = open(classFilePath, "w")
    classFile.write(GenerateUIClassFile(element))
    classFile.close()        
        
# AFWConst.py
constPath = os.path.join(currentPath, "../AFWConst.py")
OperateFile(constPath, UpdateConst)

# AFWUIManager.py
uiManagerPath = os.path.join(currentPath, "../ui/AFWUIManager.py")
OperateFile(uiManagerPath, UpdateUIManager)

# AFWSchema.py
schemaPath = os.path.join(currentPath, "../AFWSchema.py")
OperateFile(schemaPath, UpdateSchema)
