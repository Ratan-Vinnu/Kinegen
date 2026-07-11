import json
from model import Joint, RobotModel
from valid import validate_robot
from poe import compute_twist

def load_robot_json(filepath):

    with open(filepath, "r") as file:
        data = json.load(file)  

    joints = []

    for j in data["joints"]:

        joint = Joint(
            j["name"],
            j["point"],
            j["axis"],
            j["limits"]
        )

        joint.twist = compute_twist(joint.axis, joint.point)

        joints.append(joint)

    robot = RobotModel(
        data["name"],
        joints,
        data["M"],
        data["frame"]
    )

    validate_robot(robot)

    return robot

if __name__ == "__main__":
    robot = load_robot_json("MR_LP_6R_Robot_Arm.json")


robot = load_robot_json("MR_LP_6R_Robot_Arm.json")