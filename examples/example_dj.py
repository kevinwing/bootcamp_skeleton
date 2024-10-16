# main.py in the src/ directory
import sys
import os
import pos_list
import time

# Add the path to the fanuc_ethernet_ip_drivers/src/ directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib/fanuc_ethernet_ip_drivers/src')))

from robot_controller import robot

ROBOT_IP = '129.101.98.215' # DJ

def main():
    robot_obj = robot(ROBOT_IP)
    robot_obj.set_speed(300)
    robot_obj.conveyor('stop')
    handle_pick_and_place(robot_obj, 'open')
    
    # move robot to dj_pos1 - start
    robot_obj.write_cartesian_position(pos_list.dj_pos1)
    
    # move to dj_pos2 - pick
    robot_obj.write_cartesian_position(pos_list.dj_pos2)

    # close gripper to grab die
    handle_pick_and_place(robot_obj, 'close')
    
    # move to dj_pos1 - position safety
    robot_obj.write_cartesian_position(pos_list.dj_pos1)
    
    # move to dj_pos3
    robot_obj.write_cartesian_position(pos_list.dj_pos3) # over belt
    
    # move to dj_pos4 - place
    robot_obj.write_cartesian_position(pos_list.dj_pos4) # place position
    
    # open gripper to release die
    handle_pick_and_place(robot_obj, 'open') # release block
    
    # move to dj_pos3 - position safety
    robot_obj.write_cartesian_position(pos_list.dj_pos3) # return to above belt
    
    # turn belt on going forward
    robot_obj.conveyor('forward')

    # while sensor is false, run belt
    while robot_obj.conveyor_proximity_sensor('right') == 0:
        pass
    robot_obj.conveyor('stop')

    # wait some time
    time.sleep(5)
    
    # turn on belt, in reverse
    robot_obj.conveyor('reverse')

    # while sensor is false, run belt
    while robot_obj.conveyor_proximity_sensor('left') == 0:
        pass
    robot_obj.conveyor('stop') # stop belt
    
    # move to dj_pos5
    robot_obj.write_cartesian_position(pos_list.dj_pos5)

    # move to dj_pos6 - pick
    robot_obj.write_cartesian_position(pos_list.dj_pos6)

    # close gripper to grab die
    handle_pick_and_place(robot_obj, 'close')
    
    # move to dj_pos7
    robot_obj.write_cartesian_position(pos_list.dj_pos7)
    
    # move to dj_pos1
    robot_obj.write_cartesian_position(pos_list.dj_pos1)
    
    # move to dj_pos8 - place
    robot_obj.write_cartesian_position(pos_list.dj_pos8)
    
    # open gripper to release die
    handle_pick_and_place(robot_obj, 'open')
    
    # move to dj_pos9 - end
    robot_obj.write_cartesian_position(pos_list.dj_pos9)


def handle_pick_and_place(rb: robot, action: str):
    if action == 'open':
        rb.schunk_gripper('open')
    else:
        rb.schunk_gripper('close')
    time.sleep(.5)
    

if __name__ == "__main__":
    main()

