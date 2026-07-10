
class Joint:
    def __init__(self, name, point, axis, limits):
        self.name = name
        self.point = point
        self.axis = axis
        self.limits = limits

        # will be filled later
        self.twist = None
        
class RobotModel():
    def __init__(self,name,joints,M,frame):
        self.name = name
        self.joints = joints
        self.M = M
        self.frame = frame