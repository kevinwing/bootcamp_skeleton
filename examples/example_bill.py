# main.py in the src/ directory
import sys
import os
import pos_list
import time

# Add the path to the fanuc_ethernet_ip_drivers/src/ directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib/fanuc_ethernet_ip_drivers/src')))

from robot_controller import robot

# ROBOT_IP = '129.101.98.215' # DJ
ROBOT_IP = '129.101.98.214' # BILL

GRIPPER_DELAY = 3

pos1 = [628.0, 52.0, 150.0, 30.0, 90.0, -60.0]
pos2 = [628.0, 52.0, 90.0, 30.0, 90.0, -60.0]
# pos2 = [623.989258, 8.540856, 57.229496, 179.9, 0.0, -60.0] # pick position 1
# pos3 = [623.989258, 8.540856, 400.0, 179.9, 0.0, -60.0]
pos3 = [510.22430419921875, -374.48681640625, 246.85316467285156, -8.164989471435547, 89.82064819335938, -98.10063171386719]
# pos4 = [745.704712, 632.666138, 400.0, 179.9, 0.0, -60.0]
pos4 = [510.22430419921875, -374.48681640625, 146.85316467285156, -8.164989471435547, 89.82064819335938, -98.10063171386719]

# pos3 = [510.22430419921875, -374.48681640625, 246.85316467285156, -8.164989471435547, 89.82064819335938, -98.10063171386719]
pos_safe = [510.22430419921875, -324.48681640625, 246.85316467285156, -178.40240478515625, -1.1804476976394653, -91.60868072509766]
pos5 = [510.22430419921875, -374.48681640625, 246.85316467285156, -178.40240478515625, -1.1804476976394653, -91.60868072509766]

pos6 = [530.3931884765625, -150.28045654296875, -100.18257904052734, -178.40240478515625, -1.1804476976394653, -91.60868072509766]
# pos5 = [745.704712, 632.666138, 255.171265, 179.9, 0.0, -60.0] # pick position 2
# pos6 = [82.742859, 632.666138, 400.0, 179.9, 0.0, -60.0]
# pos7 = [82.742859, 632.666138, 255.171265, 179.9, 0.0, -60.0]
# pos8 = [620.989258, 5.540856, 200.0, 179.9, 0.0, 30.0] # start position rotated 90 degrees
# pos9 = [620.989258, 5.540856, 57.229496, 179.9, 0.0, 30.0] # end position rotated 90 degrees
# pos10 = [620.989258, 5.540856, 200.0, 179.9, 0.0, -60.0] # end position

def main():
    robot_obj = robot(ROBOT_IP)
    robot_obj.set_speed(200)
    robot_obj.conveyor('stop')
   
    # ensure gripper is open
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)
    
    # move robot to pos1
    robot_obj.write_cartesian_position(pos1)
    
    # move to pos2 - pick position 1
    robot_obj.write_cartesian_position(pos2)

    robot_obj.onRobot_gripper_close(75, 40)
    time.sleep(GRIPPER_DELAY)
    
    robot_obj.write_cartesian_position(pos1) # safe position
    
    robot_obj.write_cartesian_position(pos3) # over belt
    
    robot_obj.write_cartesian_position(pos4) # place position
    
    # handle_pick_and_place(robot_obj, 'open') # release block
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)

    robot_obj.write_cartesian_position(pos3) # over belt

    robot_obj.write_cartesian_position(pos5)

    robot_obj.write_cartesian_position(pos6)

    robot_obj.onRobot_gripper_close(75, 40)
    time.sleep(GRIPPER_DELAY)
    
    robot_obj.write_cartesian_position(pos5)

    robot_obj.write_cartesian_position(pos1)

    robot_obj.write_cartesian_position(pos2)

    # handle_pick_and_place(robot_obj, 'open') # release block
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)

    robot_obj.write_cartesian_position(pos1)
    
    # while robot_obj.conveyor_proximity_sensor('right') == 0:
        # pass
    # robot_obj.conveyor('stop')

    # time.sleep(5)
    
    # robot_obj.conveyor('reverse')

    # while robot_obj.conveyor_proximity_sensor('left') == 0:
        # pass

    # robot_obj.conveyor('stop')
    
    # robot_obj.write_cartesian_position(pos_list.pos5)

    # robot_obj.write_cartesian_position(pos_list.pos6)
    #
    # handle_pick_and_place(robot_obj, 'close')
    
    # robot_obj.write_cartesian_position(pos_list.pos7)
    
    # robot_obj.write_cartesian_position(pos_list.pos1)
    
    # robot_obj.write_cartesian_position(pos_list.pos8)
    
    # handle_pick_and_place(robot_obj, 'open')
    
    # robot_obj.write_cartesian_position(pos_list.pos9)


def handle_pick_and_place(rb: robot, action: str):
    if action == 'open':
        rb.schunk_gripper('open')
    else:
        rb.schunk_gripper('close')
    # rb.start_robot()
    time.sleep(.5)
    

if __name__ == "__main__":
    main()

