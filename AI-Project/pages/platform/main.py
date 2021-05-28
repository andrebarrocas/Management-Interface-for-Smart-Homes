from .importdir import *
import sys
import inspect
import traceback

# if(len(sys.argv) <= 1):
#     print("Provide -get or -set arg")
#     sys.exit()

# if "-debug" in sys.argv:
#     sys.tracebacklimit = 1000
# else:
#     

PLUGINS = "./devices/"
LOADED = []
mods = []

def start():   
    try:
        #sys.tracebacklimit = 0
        do(PLUGINS, globals())
        global mods
        mods = get_module_names_in_dir(PLUGINS)
        loadDevices()
    except:
        print("Error loading some devices")
        print("If needed, use -debug to print full trace")
   

def loadDevices():
    #reload()
    error = []
    global LOADED
    LOADED = []
    for val in mods:
        try:    
            module = getattr(sys.modules[__name__], val)
            if hasattr(module,"lampget"):
                print(module.lampget())
                LOADED.append(module.lampget())
        except:
            error.append(val)
            pass
    #Later on: Add a popup on error
    print("Error loading the following module:",error)

def loadStatus():
    #reload()
    devices = []
    for val in mods:
        try:    
            module = getattr(sys.modules[__name__], val)
            if hasattr(module,"lampget"):
                print(module.lampget())
                devices.append(module.lampget())
        except:
            pass
    #Later on: Add a popup on error
    return devices


def setSpecificDevice(id):
    #reload()
    for val in mods:  
        module = getattr(sys.modules[__name__], val)
        if hasattr(module,"lampset"):
            if(str(id) == str(module.DEVICE_ID)):
                print(module.lampset())

def getSpecificDevice(id):
    #reload()
    for val in mods:  
        module = getattr(sys.modules[__name__], val)
        if hasattr(module,"lampset"):
            if(str(id) == str(module.DEVICE_ID)):
                print(module.lampget())

def getDevices():
    return LOADED

def setDevices(id):
    #reload()
    for val in mods:  
        module = getattr(sys.modules[__name__], val)
        if hasattr(module,"lampset"):
            print(module.lampset())

def turnAllOff():
    for val in mods:
        try:
            module = getattr(sys.modules[__name__], val)
            if hasattr(module,"lampset"):
                if(module.lampget()['state'] == "on"):
                    print(module.lampset())
        except:
            pass

def turnAllOn():
    for val in mods:
        try:    
            module = getattr(sys.modules[__name__], val)
            if hasattr(module,"lampset"):
                if(module.lampget()['state'] == "off"):
                    print(module.lampset())
        except:
            pass






