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
        sys.tracebacklimit = 0
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


# if(str(sys.argv[1]) == "-get"):
#     for val in mods:
#         module = __import__(val)
#         if hasattr(module,"lampget"):
#             if(len(sys.argv)>2):
#                 if(str(sys.argv[2]) == str(module.DEVICE_ID)):
#                     print(module.lampget())
#                     break
#             else:
#                 print(module.lampget())

# if(str(sys.argv[1]) == "-set"):
#     for val in mods:
#         module = __import__(val)
#         if hasattr(module,"lampset"):
#             if(len(sys.argv)>2):
#                 if(str(sys.argv[2]) == str(module.DEVICE_ID)):
#                     print(module.lampset())
#                     break
#             else:
#                 print(module.lampset())



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


