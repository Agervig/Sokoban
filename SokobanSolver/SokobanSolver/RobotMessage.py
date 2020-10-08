class RobotMessage:
    def __init__(self, p):
        self.path = self.convertPath(p)
        self.message = self.createMessage(self.path)

    def convertPath(self, p):
        return 0

    def createMessage(self, path):
        return 0

    def sendMessage():
        return 0
