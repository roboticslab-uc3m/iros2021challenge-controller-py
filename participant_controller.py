from controller import Robot

# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Initialize devices
motor_left = robot.getDevice('wheel_left_joint')
motor_right = robot.getDevice('wheel_right_joint')
gps = robot.getDevice('gps')

motor_left.setVelocity(0.0)
motor_right.setVelocity(0.0)

motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

gps.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    print("Hello World from Python!", gps.getValues())
    motor_left.setVelocity(5.0)
    motor_right.setVelocity(5.0)
