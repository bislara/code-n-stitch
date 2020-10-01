# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captureIT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# importing the required packages
from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 10.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

class Ui_RecordIt(object):
    def setupUi(self, RecordIt):
        self.state = "stop"
        RecordIt.setObjectName("RecordIt")
        RecordIt.resize(192, 62)
        self.record = QtWidgets.QLabel(RecordIt)
        self.record.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.record.setText("")
        self.record.setPixmap(QtGui.QPixmap("record.png"))
        self.record.setScaledContents(True)
        self.record.setObjectName("record")
        self.record.mousePressEvent = self.clickRecord
        self.pause = QtWidgets.QLabel(RecordIt)
        self.pause.setGeometry(QtCore.QRect(60, 20, 51, 21))
        self.pause.setText("")
        self.pause.setPixmap(QtGui.QPixmap("pause.svg"))
        self.pause.setScaledContents(True)
        self.pause.setObjectName("pause")
        self.pause.mousePressEvent = self.clickPause
        self.capture = QtWidgets.QLabel(RecordIt)
        self.capture.setGeometry(QtCore.QRect(120, 20, 47, 21))
        self.capture.setText("")
        self.capture.setPixmap(QtGui.QPixmap("capture.svg"))
        self.capture.setScaledContents(True)
        self.capture.setObjectName("capture")
        self.capture.mousePressEvent = self.clickCapture

        self.retranslateUi(RecordIt)
        QtCore.QMetaObject.connectSlotsByName(RecordIt)

    def retranslateUi(self, RecordIt):
        _translate = QtCore.QCoreApplication.translate
        RecordIt.setWindowTitle(_translate("RecordIt", "CaptureIT"))

    def recordScreen(self):

        while True:
            if self.state != "pause":
                # Take screenshot using PyAutoGUI
                img = pyautogui.screenshot()

                # Convert the screenshot to a numpy array
                frame = np.array(img)

                # Convert it from BGR(Blue, Green, Red) to
                # RGB(Red, Green, Blue)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Write it to the output file
                out.write(frame)

            # Stop recording when we press 'q'
            if cv2.waitKey(1) == ord('q') or self.state == "stop":
                break

        # Release the Video writer
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()

    def clickRecord(self, event):
        if self.state == "stop" or self.state == "pause":
            self.state = "start"
            self.record.setPixmap(QtGui.QPixmap("stop.svg"))
            self.recordScreen()
        else:
            self.state = "stop"
            self.record.setPixmap(QtGui.QPixmap("record.png"))

    def clickPause(self, event):
        if self.state == "start":
            self.state = "pause"
            self.record.setPixmap(QtGui.QPixmap("record.png"))
        else:
            self.state = "start"
            self.record.setPixmap(QtGui.QPixmap("stop.svg"))

    def clickCapture(self, event):
        img = pyautogui.screenshot("captureIT_img.jpg")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecordIt = QtWidgets.QWidget()
    ui = Ui_RecordIt()
    ui.setupUi(RecordIt)
    RecordIt.show()
    sys.exit(app.exec_())

