# Management Interface for Smart Homes
WIP
## TO DO
- [ ] **Platform**
    - [x] Initial "server" structure
    - [x] Server abstraction from devices
    - [x] Individual lamps gets/sets
    - [x] Django Implementation
    - [ ] Auto Generate DEVICE_ID
    - [ ] Add more device types
    - [ ] Group devices and create automations
    - [ ] Automatic platform refresh (get timers)
    - [ ] Security concerns (including input sanitization)
    - [ ] (Optional) Code refractoring 
    

- [ ] **UI**
    - [x] Initial UI
    - [ ] Device Groups
    - [ ] Turn all on/off
    - [ ] Add new device using .py upload form
    - [ ] Present an error (banner/notification style) if any module fails to load

- [ ] **Misc**
    - [ ] Report

- [ ] **Questions**
    - [ ] A command to turn all lights on/off should broadcast all lights with on/off command or should we see which lamps are "on/off" and send the commands to those specific lights? Benchmark timing in both solutions maybe?


## Platform basic commands
 - **Get all devices state/info:** 
    -  python main.py -get
 - **Set all devices state:** 
     - python main.py -set
 - **Get specific device state/info**
     - python main.py -get DEVICE_ID
 - **Set specific device state**
     - python main.py -set DEVICE_ID
 - **Print full trace - debug purposes**
     - python main.py [-set,-get] -debug


        
