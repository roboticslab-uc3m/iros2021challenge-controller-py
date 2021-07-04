from controller import Robot

# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Initialize devices
motor_left = robot.getDevice('wheel_left_joint')
motor_right = robot.getDevice('wheel_right_joint')

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    print("Hello World from Python!")
