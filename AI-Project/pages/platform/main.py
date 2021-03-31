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
#     sys.tracebacklimit = 0

PLUGINS = "./devices/"

def reload():   
    try:
        do(PLUGINS, globals())
    except:
        print("Error loading some devices")
        print("If needed, use -debug to print full trace")

mods = get_module_names_in_dir(PLUGINS)


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
    reload()
    for val in mods:  
        module = __import__(val)
        if hasattr(module,"lampset"):
            if(str(id) == str(module.DEVICE_ID)):
                print(module.lampset())

def getSpecificDevice(id):
    reload()
    for val in mods:  
        module = __import__(val)
        if hasattr(module,"lampset"):
            if(str(id) == str(module.DEVICE_ID)):
                print(module.lampget())

def getDevices():
    reload()
    devices = []
    error = []
    for val in mods:
        try:  
            module = __import__(val)
            if hasattr(module,"lampget"):
                print(module.lampget())
                devices.append(module.lampget())
        except:
            traceback.print_exc()
            error.append(val)
            pass
    #Later on: Add a popup on error
    print("Error loading the following module:",error)
    return devices

def setDevices(id):
    reload()
    for val in mods:  
        module = __import__(val)
        if hasattr(module,"lampset"):
            print(module.lampset())


