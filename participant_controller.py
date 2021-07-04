from controller import Robot

# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    print("Hello World from Python!")
