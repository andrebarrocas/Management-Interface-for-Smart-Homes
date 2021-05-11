# import sys
# import asyncio
# import pyatv

# NAME = "Apple TV"
# DEVICE_TYPE = "APPLE_TV"
# DEVICE_ID = "8978"

# async def lampgetstatus(loop):
#     atvs = await pyatv.scan(loop, timeout=2)
#     atv = await pyatv.connect(atvs[0], loop)
#     pwr = atv.power
#     state = str(pwr.power_state).split('.')[1]
#     data = {
#         "id": DEVICE_ID,
#         "name": NAME,
#         "state": state
#     }
#     return data

# def lampget():
#     loop = asyncio.new_event_loop()
#     try:
#         asyncio.set_event_loop(loop)
#         return loop.run_until_complete(lampgetstatus(loop))
#     finally:
#         try:
#             _cancel_all_tasks(loop)
#             loop.run_until_complete(loop.shutdown_asyncgens())
#         except:
#             pass

# async def lampsetstatus(loop):
#     atvs = await pyatv.scan(loop, timeout=2)
#     atv = await pyatv.connect(atvs[0], loop)
#     pwr = atv.power
#     state = str(pwr.power_state).split('.')[1]
#     print(state)
#     if state == "On":
#         await pwr.turn_off()
#     else: 
#         await pwr.turn_on()

#     return "Ok"

# def lampset():
#     loop = asyncio.new_event_loop()
#     try:
#         asyncio.set_event_loop(loop)
#         return loop.run_until_complete(lampsetstatus(loop))
#     finally:
#         try:
#             _cancel_all_tasks(loop)
#             loop.run_until_complete(loop.shutdown_asyncgens())
#         except:
#             pass



    