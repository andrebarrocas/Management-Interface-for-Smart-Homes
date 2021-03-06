import importdir
import sys
import inspect

if(len(sys.argv) <= 1):
    print("Provide -get or -set arg")
    sys.exit()

if "-debug" in sys.argv:
    sys.tracebacklimit = 1000
else:
    sys.tracebacklimit = 0

PLUGINS = "devices/"

try:
    importdir.do(PLUGINS, globals())
except:
    print("Error loading some devices")
    print("If needed, use -debug to print full trace")

mods = importdir.__get_module_names_in_dir("devices/")

if(str(sys.argv[1]) == "-get"):
    for val in mods:
        module = __import__(val)
        if hasattr(module,"lampget"):
            if(len(sys.argv)>2):
                if(str(sys.argv[2]) == str(module.DEVICE_ID)):
                    print(module.lampget())
                    break
            else:
                print(module.lampget())

if(str(sys.argv[1]) == "-set"):
    for val in mods:
        module = __import__(val)
        if hasattr(module,"lampset"):
            if(len(sys.argv)>2):
                if(str(sys.argv[2]) == str(module.DEVICE_ID)):
                    print(module.lampset())
                    break
            else:
                print(module.lampset())