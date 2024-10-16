import sys
import os

# Add the path to the fanuc_ethernet_ip_drivers/src/ directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib/fanuc_ethernet_ip_drivers/src')))

from robot_controller import robot

# ROBOT_IP = '129.101.98.215' # DJ
ROBOT_IP = '129.101.98.214' # BILL


robot_obj = robot(ROBOT_IP)

print(robot_obj.read_current_cartesian_pose())
# dj.schunk_gripper('open')
