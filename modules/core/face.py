class Face:
    def __init__(self, personId, faceImage, faceEncode):
        self.personId = personId
        self.faceImage = faceImage
        self.faceEncode = faceEncode

    def FaceId(self):
        return self.faceId

    def PersonId(self):
        return self.personId

    def FaceImage(self):
        return self.faceImage

    def FaceEncode(self):
        return self.faceEncode

    def setFaceId(self, faceId):
        self.faceId = faceId
