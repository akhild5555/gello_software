import rtde_control
import rtde_receive
import rtde_io
import time

ROBOT_HOST = '192.168.1.121'

rtde_c = None
rtde_r = None

try:
    rtde_c = rtde_control.RTDEControlInterface(ROBOT_HOST)
    rtde_r = rtde_receive.RTDEReceiveInterface(ROBOT_HOST)
    rtde_io_obj = rtde_io.RTDEIOInterface(ROBOT_HOST)

    if not rtde_c.isConnected():
        exit()
    if not rtde_r.isConnected():
        exit()

    rtde_io_obj.setStandardDigitalOut(7, True)
    time.sleep(0.5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if rtde_c:
        rtde_c.disconnect()
    if rtde_r:
        rtde_r.disconnect()