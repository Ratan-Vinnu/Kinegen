from kinegen.fk import forward_kinematics, check_se3, get_joint_positions
from kinegen.parser import robot
import numpy as np
import matplotlib.pyplot as plt

thetas = []
for i in robot.joints:
    thetas.append(0)
thetas = [0,np.pi/2,0,0,np.pi/2,0]

T = forward_kinematics(robot, thetas)
print(T)