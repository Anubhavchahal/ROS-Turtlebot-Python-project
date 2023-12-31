from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(360)

while a > 1:
      rc.move_straight()
      a = rc.get_laser(360)
      print("Current distance to wall: %f" % a)

print("Wall is at %f meters! Stop the robot!" %a)
rc.turn("counter-clockwise", 0.3, 5.5)
a = rc.get_laser(360)
while a > 1:
      rc.move_straight()
      a = rc.get_laser(360)
      print("Current distance to wall: %f" % a)
rc.stop_robot()
print("Wall is at %f meters! Stop the robot!" %a)
rc.turn("counter-clockwise", 0.3, 5.5)
a = rc.get_laser(360)
while a > 1:
      rc.move_straight()
      a = rc.get_laser(360)
      print("Current distance to wall: %f" % a)
rc.stop_robot()
print("Wall is at %f meters! Stop the robot!" %a)
rc.turn("clockwise", 0.3, 6.5)
a = rc.get_laser(360)
while a > 1:
      rc.move_straight()
      a = rc.get_laser(360)
      print("Current distance to wall: %f" % a)
rc.stop_robot()
print("Wall is at %f meters! Stop the robot!" %a)