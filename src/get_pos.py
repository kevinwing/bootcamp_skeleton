import sys
sys.path.append('/home/krw/ros2/fanuc-ethernet_ip_drivers/src/')
from robot_controller import robot

robot_ip = '129.101.98.215'

dj = robot(robot_ip)

print(dj.read_current_cartesian_pose())
# dj.schunk_gripper('open')