# ---------------------------------------------------------------------------- #
#                                 app functions                                #
# ---------------------------------------------------------------------------- #
from .core import *
from main import *
import re
import cv2


def isValidNumber(num) -> bool:
    try:
        tmp = int(num)
        if (len(num) == 10):
            return True
        return False
    except:
        return False


def isValidEmail(email) -> bool:
    if re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
        return True
    return False


class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 2px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    def AddformValidate(self):
        if len(self.ui.add_firstname.text()) < 3:
            return False, "please entre a valide firstname."
        if len(self.ui.add_lastname.text()) < 3:
            return False, "please entre a valide lastname."
        if isValidEmail(self.ui.add_email.text()) == False:
            return False, "please entre a valide email adress."
        if isValidNumber(self.ui.add_phone.text()) == False:
            return False, "plase entre a valide phone number."
        if len(self.ui.add_adress.toPlainText()) < 20:
            return False, "adress is too short or invalide, please try again."
        return True, "please wait..."

    def browseImage(self) -> str:
        filename = QFileDialog.getOpenFileName(
            self, 'Open File', 'c\\', 'Image files(*.jpg *.png)')
        imagePath = filename[0]
        return imagePath

    def ImageLabel(self, image) -> QLabel:
        imgLabel = QtWidgets.QLabel(None)
        imgLabel.setText("")
        imgLabel.setStyleSheet("border-radius:20px;")
        imgLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image)
        imgLabel.setPixmap(pixmap)
        return imgLabel

    def count_cameras(self):
        max_tested = 20
        for i in range(max_tested):
            temp_camera = cv2.VideoCapture(i)
            if temp_camera.isOpened():
                temp_camera.release()
                continue
            return i

    def NewPerson(self, person) -> bool:
        try:
            Database().addPerson(person)
            return True
        except:
            return False

    def getData(self):
        try:
            persons = Database().getPerson()
            for person in persons:
                pass
            return True, persons
        except:
            return False, []

    def CheckUnicity(self, person):
        return Database().isUnique(person)
