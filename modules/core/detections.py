import os
from PyQt5 import QtGui
import cv2
import face_recognition
import numpy as np
from PyQt5.QtCore import QThread


class Detection(QThread):
    def __init__(self):
        super(Detection, self).__init__()

    def unknown_image_encoded(self, img):
        # encode a face given the file name
        face = face_recognition.load_image_file(img)
        encoding = face_recognition.face_encodings(face)[0]
        return encoding

    def exploreFaces(self, faces):
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())
        return faces_encoded, known_face_names


class FaceRecognition(Detection):
    def __init__(self, faces, video_capture, ui):
        super(FaceRecognition, self).__init__()
        self.faces_encoded, self.known_face_names = super().exploreFaces(faces)
        self.video_capture = video_capture
        self.ui = ui

    def classify_video(self):
        ret, img = self.video_capture.read()
        faces_encoded, known_face_names = self.faces_encoded, self.known_face_names
        face_names = []
        if len(faces_encoded) != 0:
            #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            #img = img[:,:,::-1]
            face_locations = face_recognition.face_locations(img)
            unknown_face_encodings = face_recognition.face_encodings(
                img, face_locations)

            for face_encoding in unknown_face_encodings:
                matches = face_recognition.compare_faces(
                    faces_encoded, face_encoding)
                name = "Inconnu"

                face_distances = face_recognition.face_distance(
                    faces_encoded, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = str(known_face_names[best_match_index])[2:]

                face_names.append(name)

                # rectangle et label
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # rectangler le visage
                    cv2.rectangle(img, (left-20, top-20),
                                  (right+20, bottom+20), (255, 0, 0), 2)

                # label avec nom en dessous du visage
                    cv2.rectangle(img, (left-20, bottom - 15),
                                  (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(img, name, (left - 20, bottom + 15),
                                font, 1.0, (255, 255, 255), 2)
            return img

    def classify_img(self, im):
        #faces = get_encoded_faces()
        faces_encoded, known_face_names = self.faces_encoded, self.known_face_names
        img = cv2.imread(im, 1)
        face_names = []
        if len(faces_encoded) != 0:
            #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            #img = img[:,:,::-1]
            face_locations = face_recognition.face_locations(img)
            unknown_face_encodings = face_recognition.face_encodings(
                img, face_locations)

            for face_encoding in unknown_face_encodings:
                matches = face_recognition.compare_faces(
                    faces_encoded, face_encoding)
                name = "iInconnu"

                face_distances = face_recognition.face_distance(
                    faces_encoded, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = str(known_face_names[best_match_index])[1:]

                face_names.append(name)

                # rectangle et label
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # rectangler le visage
                    cv2.rectangle(img, (left-20, top-20),
                                  (right+20, bottom+20), (255, 0, 0), 2)

                # label avec nom en dessous du visage
                    cv2.rectangle(img, (left-20, bottom - 15),
                                  (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(img, name[1:], (left - 20, bottom + 15),
                                font, 1.0, (255, 255, 255), 2)
        # affichage
        return img, face_names

    def run(self):
        while True:
            self.ui.warning_faceDetection_label.setText(
                "Pour arreter , Clickez sur 'ECHAP'")
            imgResult = self.classify_video()
            width = int(
                (imgResult.shape[1] * self.ui.frame_FD.height()) / imgResult.shape[0])
            height = self.ui.frame_FD.height()
            dim = (width, height)
            imgResult = cv2.resize(
                imgResult, dim, interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(imgResult, cv2.COLOR_BGRA2RGB)
            image = QtGui.QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format_RGB888)
            self.ui.detection_faceDetection_label.setPixmap(
                QtGui.QPixmap.fromImage(image))


class ObjectDetection(Detection):
    def __init__(self, cap, ui):
        super(ObjectDetection, self).__init__()
        self.cap = cap
        self.ui = ui
        self.classNames = []
        if 1 == 1:
            self.classNames = {0: 'background',
                               1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
                               5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
                               10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
                               14: 'motorbike', 15: 'person', 16: 'pottedplant',
                               17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}
            self.net = cv2.dnn.readNetFromCaffe(
                'configs/softDetection-caffemodel/MobileNetSSD_deploy.prototxt', 'configs/softDetection-caffemodel/MobileNetSSD_deploy.caffemodel')

        else:
            classesFile = 'configs/mainDetection-yolov3/coco.names'
            with open(classesFile, 'rt') as f:
                self.classNames = f.read().rstrip('\n').split('\n')
            self.modelConfig = 'configs/mainDetection-yolov3/yolov3-tiny.cfg'
            self.modelWeights = 'configs/mainDetection-yolov3/yolov3-tiny.weights'
            self.net = cv2.dnn.readNetFromDarknet(
                self.modelConfig, self.modelWeights)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

    def findObjects(self, outputs, img):
        if 1 == 1:
            detections = outputs
            frame = img
            heightFactor = frame.shape[0]/300.0
            widthFactor = frame.shape[1]/300.0
            frame_resized = cv2.resize(frame, (300, 300))
            cols = frame_resized.shape[1]
            rows = frame_resized.shape[0]
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]  # Confidence of prediction
                if confidence > 0.2:  # Filter prediction
                    class_id = int(detections[0, 0, i, 1])  # Class label
                    hT, wT, cT = frame.shape
                    # Object location
                    xLeftBottom = int(detections[0, 0, i, 3] * cols)
                    yLeftBottom = int(detections[0, 0, i, 4] * rows)
                    xRightTop = int(detections[0, 0, i, 5] * cols)
                    yRightTop = int(detections[0, 0, i, 6] * rows)

                    xLeftBottom_ = int(widthFactor * xLeftBottom)
                    yLeftBottom_ = int(heightFactor * yLeftBottom)
                    xRightTop_ = int(widthFactor * xRightTop)
                    yRightTop_ = int(heightFactor * yRightTop)
                    w, h = int(xLeftBottom*wT), int(yLeftBottom*hT)
                    x, y = int(xRightTop*wT - w / 2), int(yRightTop*hT - h/2)

                    cv2.rectangle(frame, (xLeftBottom_, yLeftBottom_), (xRightTop_, yRightTop_),
                                  (255, 0, 0), 2)
                    # Draw label and confidence of prediction in frame resized
                    if class_id in self.classNames:
                        label = f'{self.classNames[class_id].upper()} {int(confidence*100)}%'
                        # label = classNames[class_id] + ": " + str(confidence)
                        labelSize, baseLine = cv2.getTextSize(
                            label, cv2.FONT_HERSHEY_TRIPLEX, 0.8, 1)

                        yLeftBottom_ = max(yLeftBottom_, labelSize[1])
                        cv2.rectangle(frame, (xLeftBottom_, yLeftBottom_),
                                      (xRightTop_, yLeftBottom_+20),
                                      (255, 0, 0), cv2.FILLED)
                        cv2.putText(frame, label, (xLeftBottom_, yLeftBottom_+labelSize[1]),
                                    cv2.FONT_HERSHEY_DUPLEX, .8, (255, 255, 255), 2)
        else:
            confThreshold = 0.3
            nmsThreshold = 0.1
            hT, wT, cT = img.shape
            bbox = []
            classIds = []
            confs = []
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    if confidence > confThreshold:
                        w, h = int(detection[2]*wT), int(detection[3]*hT)
                        x, y = int(detection[0]*wT - w /
                                   2), int(detection[1]*hT - h/2)
                        bbox.append([x, y, w, h])
                        classIds.append(classID)
                        confs.append(float(confidence))
            indices = cv2.dnn.NMSBoxes(
                bbox, confs, confThreshold, nmsThreshold)
            for i in indices:
                i = i[0]
                box = bbox[i]
                x, y, w, h = box[0], box[1], box[2], box[3]
                cv2.rectangle(img, (x, y), (x+w, y*h), (255, 0, 0), 2)
                cv2.putText(img, f'{self.classNames[classIds[i]].upper()}{int(confs[i]*100)}%',
                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    def detect_object(self, cap):
        if 1 == 1:
            success, frame = cap.read()
            # resize frame for prediction
            frame_resized = cv2.resize(frame, (300, 300))
            heightFactor = frame.shape[0]/300.0
            widthFactor = frame.shape[1]/300.0
            # MobileNet requires fixed dimensions for input image(s)
            # so we have to ensure that it is resized to 300x300 pixels.
            # set a scale factor to image because network the objects has differents size.
            # We perform a mean subtraction (127.5, 127.5, 127.5) to normalize the input;
            # after executing this command our "blob" now has the shape:
            # (1, 3, 300, 300)
            blob = cv2.dnn.blobFromImage(
                frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
            # Set to network the input blob
            self.net.setInput(blob)
            # Prediction of network
            detections = self.net.forward()
            self.findObjects(detections, frame)
            return frame
        else:
            whT = 320
            success, img = cap.read()
            blob = cv2.dnn.blobFromImage(
                img, 1/255, (whT, whT), [0, 0, 0], 1, crop=False)
            self.net.setInput(blob)
            layerNames = self.net.getLayerNames()
            self.net.getUnconnectedOutLayers()
            outputNames = [layerNames[i[0]-1]
                           for i in self.net.getUnconnectedOutLayers()]
            outputs = self.net.forward(outputNames)
            self.findObjects(outputs, img)
            return img

    def run(self):
        while True:
            imgResult = self.detect_object(self.cap)
            width = int(
                (imgResult.shape[1] * self.ui.frame_OD.height()) / imgResult.shape[0])
            height = self.ui.frame_OD.height()
            dim = (width, height)
            imgResult = cv2.resize(
                imgResult, dim, interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(imgResult, cv2.COLOR_BGRA2RGB)
            image = QtGui.QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format_RGB888)
            self.ui.detection_Object_label.setPixmap(
                QtGui.QPixmap.fromImage(image))
