# Management Interface for Smart Homes
WIP
## TO DO
- [ ] **Platform**
    - [x] Initial "server" structure
    - [x] Server abstraction from devices
    - [x] Individual lamps gets/sets
    - [ ] Auto Generate DEVICE_ID
    - [ ] Django Implementation
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

- [ ] **Misc**
    - [ ] Report


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


        
