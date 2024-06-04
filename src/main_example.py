# main.py in the src/ directory
import sys
import os

# Add the path to the fanuc_ethernet_ip_drivers/src/ directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib/fanuc_ethernet_ip_drivers/src')))

from robot_controller import robot

ROBOT_IP = '129.101.98.215' # DJ
# ROBOT_IP = '129.101.98.214' # BILL

pos1 = [623.989258, 8.540856, 200.0, 179.9, 0.0, -60.0] # start position
pos2 = [623.989258, 8.540856, 57.229496, 179.9, 0.0, -60.0] # pick position 1
pos3 = [623.989258, 8.540856, 400.0, 179.9, 0.0, -60.0]
pos4 = [745.704712, 632.666138, 400.0, 179.9, 0.0, -60.0]
pos5 = [745.704712, 632.666138, 255.171265, 179.9, 0.0, -60.0] # pick position 2
pos6 = [82.742859, 632.666138, 400.0, 179.9, 0.0, -60.0]
pos7 = [82.742859, 632.666138, 255.171265, 179.9, 0.0, -60.0]
pos8 = [620.989258, 5.540856, 200.0, 179.9, 0.0, 30.0] # start position rotated 90 degrees
pos9 = [620.989258, 5.540856, 57.229496, 179.9, 0.0, 30.0] # end position rotated 90 degrees
pos10 = [620.989258, 5.540856, 200.0, 179.9, 0.0, -60.0] # end position

def main():
    robot_obj = robot(ROBOT_IP)
    robot_obj.set_speed(100)
    
    # move robot to pos1
    robot_obj.write_cartesian_position(pos1)
    
    # move to pos2 - pick position 1
    robot_obj.write_cartesian_position(pos2)

    handle_pick_and_place(robot_obj, 'close')
    
    robot_obj.write_cartesian_position(pos3) # safe position
    
    robot_obj.write_cartesian_position(pos4) # over belt
    
    robot_obj.write_cartesian_position(pos5) # place position
    
    handle_pick_and_place(robot_obj, 'open') # release block
    
    robot_obj.write_cartesian_position(pos4) # return to above belt
    
    # reverse, forward, stop
    robot_obj.conveyor('forward')
    
    robot_obj.write_cartesian_position(pos6, False)
    
    while robot_obj.conveyor_proximity_sensor('left') == 0:
        pass
    robot_obj.conveyor('stop')
    
    robot_obj.write_cartesian_position(pos7)
    
    handle_pick_and_place(robot_obj, 'close')
    
    robot_obj.write_cartesian_position(pos6)
    
    robot_obj.write_cartesian_position(pos8)
    
    robot_obj.write_cartesian_position(pos9)
    
    handle_pick_and_place(robot_obj, 'open')
    
    robot_obj.write_cartesian_position(pos10)


def handle_pick_and_place(rb: robot, action: str):
    if action == 'open':
        rb.schunk_gripper('open')
    else:
        rb.schunk_gripper('close')
    # rb.start_robot()
    time.sleep(.5)
    

if __name__ == "__main__":
    main()

