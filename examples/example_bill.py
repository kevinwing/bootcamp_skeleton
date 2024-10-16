# main.py in the src/ directory
import sys
import os
import pos_list
import time

# Add the path to the fanuc_ethernet_ip_drivers/src/ directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib/fanuc_ethernet_ip_drivers/src')))

from robot_controller import robot

ROBOT_IP = '129.101.98.214' # BILL

GRIPPER_DELAY = 3


def main():
    robot_obj = robot(ROBOT_IP)
    robot_obj.set_speed(200)
    robot_obj.conveyor('stop')
   
    # ensure gripper is open
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)
    
    # move robot to pos1
    robot_obj.write_cartesian_position(pos_list.bill_pos1)
    
    # move to bill_pos2 - pick
    robot_obj.write_cartesian_position(pos_list.bill_pos2)

    # close gripper to grab die
    robot_obj.onRobot_gripper_close(75, 40)
    time.sleep(GRIPPER_DELAY)
    
    # move back to bill_pos1 for safety
    robot_obj.write_cartesian_position(pos_list.bill_pos1)
    
    # move to bill_pos3
    robot_obj.write_cartesian_position(pos_list.bill_pos3)
    
    # move to bill_pos4 - place
    robot_obj.write_cartesian_position(pos_list.bill_pos4)
    
    # open gripper to release die
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)

    # move back to bill_pos3 for safety
    robot_obj.write_cartesian_position(pos_list.bill_pos3)

    # move to bill_pos5
    robot_obj.write_cartesian_position(pos_list.bill_pos5)

    # move to bill_pos6 - pick
    robot_obj.write_cartesian_position(pos_list.bill_pos6)

    # close gripper on die
    robot_obj.onRobot_gripper_close(75, 40)
    time.sleep(GRIPPER_DELAY)
    
    # move back to bill_pos5 for safety
    robot_obj.write_cartesian_position(pos_list.bill_pos5)

    # move to bill_pos1
    robot_obj.write_cartesian_position(pos_list.bill_pos1)

    # move to bill_pos2 - place
    robot_obj.write_cartesian_position(pos_list.bill_pos2)

    # open gripper to release die
    robot_obj.onRobot_gripper_close(135, 40)
    time.sleep(GRIPPER_DELAY)

    # move back to bill_pos1 - end
    robot_obj.write_cartesian_position(pos_list.bill_pos1)


def handle_pick_and_place(rb: robot, action: str):
    if action == 'open':
        rb.schunk_gripper('open')
    else:
        rb.schunk_gripper('close')
    # rb.start_robot()
    time.sleep(.5)
    

if __name__ == "__main__":
    main()

