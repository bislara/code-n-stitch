from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtGui
import re, smtplib, ssl
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
try:
    from PySide2 import QtWinExtras
except ImportError:
    pass


files = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        MainWindow.setFixedSize(1301, 855)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titleFrame = QFrame(self.centralwidget)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(10, 9, 1281, 61))
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(573, 10, 141, 41))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.loginGroupBox = QGroupBox(self.centralwidget)
        self.loginGroupBox.setObjectName(u"loginGroupBox")
        self.loginGroupBox.setGeometry(QRect(10, 80, 1281, 211))
        self.mailserverLineEdit = QLineEdit(self.loginGroupBox)
        self.mailserverLineEdit.setObjectName(u"mailserverLineEdit")
        self.mailserverLineEdit.setGeometry(QRect(230, 20, 361, 41))
        self.mailserverLineEdit.setAlignment(Qt.AlignCenter)
        self.mailserverLabel = QLabel(self.loginGroupBox)
        self.mailserverLabel.setObjectName(u"mailserverLabel")
        self.mailserverLabel.setGeometry(QRect(40, 20, 171, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.mailserverLabel.setFont(font1)
        self.serverportLineEdit = QLineEdit(self.loginGroupBox)
        self.serverportLineEdit.setObjectName(u"serverportLineEdit")
        self.serverportLineEdit.setGeometry(QRect(880, 20, 71, 41))
        self.serverportLineEdit.setAlignment(Qt.AlignCenter)
        self.serverportIntValidator = QIntValidator()
        self.serverportIntValidator.setRange(0, 65535)
        self.serverportLineEdit.setValidator(self.serverportIntValidator)
        self.serverportLabel = QLabel(self.loginGroupBox)
        self.serverportLabel.setObjectName(u"serverportLabel")
        self.serverportLabel.setGeometry(QRect(690, 20, 181, 41))
        self.serverportLabel.setFont(font1)
        self.usernameLineEdit = QLineEdit(self.loginGroupBox)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(230, 80, 361, 41))
        self.usernameLineEdit.setAlignment(Qt.AlignCenter)
        self.usernameLabel = QLabel(self.loginGroupBox)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(40, 80, 171, 41))
        self.usernameLabel.setFont(font1)
        self.passwordLabel = QLabel(self.loginGroupBox)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(690, 80, 171, 41))
        self.passwordLabel.setFont(font1)
        self.passwordLineEdit = QLineEdit(self.loginGroupBox)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(880, 80, 361, 41))
        self.passwordLineEdit.setAlignment(Qt.AlignCenter)
        self.starttlsRadioButton = QRadioButton(self.loginGroupBox)
        self.starttlsRadioButton.setObjectName(u"starttlsRadioButton")
        self.starttlsRadioButton.setGeometry(QRect(980, 30, 141, 20))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.starttlsRadioButton.setFont(font2)
        self.usesslRadioButton = QRadioButton(self.loginGroupBox)
        self.usesslRadioButton.setObjectName(u"usesslRadioButton")
        self.usesslRadioButton.setGeometry(QRect(1130, 30, 111, 20))
        self.usesslRadioButton.setFont(font2)
        self.loginPushButton = QPushButton(self.loginGroupBox)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setGeometry(QRect(520, 150, 241, 51))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.loginPushButton.setFont(font3)
        self.messageGroupBox = QGroupBox(self.centralwidget)
        self.messageGroupBox.setObjectName(u"messageGroupBox")
        self.messageGroupBox.setGeometry(QRect(9, 299, 1281, 521))
        self.fromLabel = QLabel(self.messageGroupBox)
        self.fromLabel.setObjectName(u"fromLabel")
        self.fromLabel.setGeometry(QRect(40, 30, 71, 41))
        self.fromLabel.setFont(font1)
        self.fromLineEdit = QLineEdit(self.messageGroupBox)
        self.fromLineEdit.setObjectName(u"fromLineEdit")
        self.fromLineEdit.setGeometry(QRect(160, 30, 421, 41))
        self.fromLineEdit.setAlignment(Qt.AlignCenter)
        self.toLabel = QLabel(self.messageGroupBox)
        self.toLabel.setObjectName(u"toLabel")
        self.toLabel.setGeometry(QRect(690, 30, 71, 41))
        self.toLabel.setFont(font1)
        self.subjectLineEdit = QLineEdit(self.messageGroupBox)
        self.subjectLineEdit.setObjectName(u"subjectLineEdit")
        self.subjectLineEdit.setGeometry(QRect(160, 90, 1081, 41))
        self.subjectLineEdit.setAlignment(Qt.AlignCenter)
        self.subjectLabel = QLabel(self.messageGroupBox)
        self.subjectLabel.setObjectName(u"subjectLabel")
        self.subjectLabel.setGeometry(QRect(40, 90, 101, 41))
        self.subjectLabel.setFont(font1)
        self.toLineEdit = QLineEdit(self.messageGroupBox)
        self.toLineEdit.setObjectName(u"toLineEdit")
        self.toLineEdit.setGeometry(QRect(810, 30, 431, 41))
        self.toLineEdit.setAlignment(Qt.AlignCenter)
        self.messagePlainTextEdit = QPlainTextEdit(self.messageGroupBox)
        self.messagePlainTextEdit.setObjectName(u"messagePlainTextEdit")
        self.messagePlainTextEdit.setGeometry(QRect(40, 190, 761, 321))
        self.messageLabel = QLabel(self.messageGroupBox)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setGeometry(QRect(40, 150, 121, 41))
        self.messageLabel.setFont(font1)
        self.attachmentsLabel = QLabel(self.messageGroupBox)
        self.attachmentsLabel.setObjectName(u"attachmentsLabel")
        self.attachmentsLabel.setGeometry(QRect(820, 230, 171, 41))
        self.attachmentsLabel.setFont(font1)
        self.attachmentsPushButton = QPushButton(self.messageGroupBox)
        self.attachmentsPushButton.setObjectName(u"attachmentsPushButton")
        self.attachmentsPushButton.setGeometry(QRect(1010, 220, 231, 61))
        self.attachmentsPushButton.setFont(font3)
        self.sendmailPushButton = QPushButton(self.messageGroupBox)
        self.sendmailPushButton.setObjectName(u"sendmailPushButton")
        self.sendmailPushButton.setGeometry(QRect(820, 360, 421, 61))
        self.sendmailPushButton.setFont(font3)
        self.quitPushButton = QPushButton(self.messageGroupBox)
        self.quitPushButton.setObjectName(u"quitPushButton")
        self.quitPushButton.setGeometry(QRect(820, 450, 421, 61))
        self.quitPushButton.setFont(font3)
        self.attachmentsLineEdit = QLineEdit(self.messageGroupBox)
        self.attachmentsLineEdit.setObjectName(u"attachmentsLineEdit")
        self.attachmentsLineEdit.setEnabled(True)
        self.attachmentsLineEdit.setGeometry(QRect(820, 290, 421, 41))
        self.attachmentsLineEdit.setAlignment(Qt.AlignCenter)
        self.attachmentsLineEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyMailer", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"PyMailer", None))
        self.loginGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.mailserverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"smtp.gmail.com", None))
        self.mailserverLabel.setText(QCoreApplication.translate("MainWindow", u"MAIL SERVER", None))
        self.serverportLineEdit.setText("")
        self.serverportLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"587", None))
        self.serverportLabel.setText(QCoreApplication.translate("MainWindow", u"SERVER PORT", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yourusername@gmail.com", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yourpassword", None))
        self.starttlsRadioButton.setText(QCoreApplication.translate("MainWindow", u"STARTTLS", None))
        self.usesslRadioButton.setText(QCoreApplication.translate("MainWindow", u"USE SSL", None))
        self.loginPushButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.messageGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.fromLabel.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.fromLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yourusername@gmail.com", None))
        self.toLabel.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.subjectLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your subject here", None))
        self.subjectLabel.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.toLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter email addresses separated by space", None))
        self.messagePlainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your message here", None))
        self.messageLabel.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.attachmentsLabel.setText(QCoreApplication.translate("MainWindow", u"Attachments:", None))
        self.attachmentsPushButton.setText(QCoreApplication.translate("MainWindow", u"Select File(s)", None))
        self.sendmailPushButton.setText(QCoreApplication.translate("MainWindow", u"Send Mail", None))
        self.quitPushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.attachmentsLineEdit.setText("")
        self.attachmentsLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))

        # Disabling Everything Below The LOGIN
        self.messageGroupBox.setEnabled(False)

        # Connecting Buttons To Handlers
        self.quitPushButton.clicked.connect(self.quitApplication)
        self.loginPushButton.clicked.connect(self.loginToSMTPServer)
        self.attachmentsPushButton.clicked.connect(self.selectAttachments)
        self.sendmailPushButton.clicked.connect(self.sendMail)

    
    # Button Handlers
    def quitApplication(self):
        try:
            server.quit()
        finally:
            app.quit()


    def loginToSMTPServer(self):
        self.loginPushButton.setEnabled(False)
        mailServer = self.mailserverLineEdit.text() if bool(re.search(r"^\w+\.\w+\.[a-zA-z]{1,3}$", self.mailserverLineEdit.text())) else None
        serverPort = int(self.serverportLineEdit.text())
        username = self.usernameLineEdit.text() if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", self.usernameLineEdit.text())) else None
        password = self.passwordLineEdit.text()
        startTls = self.starttlsRadioButton.isChecked()
        useSsl = self.usesslRadioButton.isChecked()
        
        if not mailServer or not username:
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Invalid Credentials")
            self.msgBox.setIcon(QMessageBox.Critical)
            self.msgBox.setText("Please ensure proper credentials are given, make sure to check if the mail server and username and correct.")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
            self.loginPushButton.setEnabled(True)
            return

        loggedIn = False
        error = None
        context = ssl.create_default_context()
        global server

        if startTls:
            try:
                server = smtplib.SMTP(mailServer, serverPort)
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(username, password)
                loggedIn = True
            except Exception as e:
                error = str(e)
        elif useSsl:
            try:
                server = smtplib.SMTP_SSL(mailServer, serverPort, context=context)
                server.login(username, password)
                loggedIn = True
            except Exception as e:
                error = str(e)
        else:
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Select Connection Type")
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Please select connection type, 'STARTTLS' or 'USESSL', to ensure the security of the connection.")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
            self.loginPushButton.setEnabled(True)
            return


        if not loggedIn:
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Login Failed")
            self.msgBox.setIcon(QMessageBox.Critical)
            self.msgBox.setText("Unable to login to the server, please check if all the connection credentials are correct. If you are using gmail as smtp server, make sure to enable less secure apps, or use app passwords (recommended) or unlock display captcha and retry.")
            self.msgBox.setInformativeText("Click 'Show Details' to check the error log.")
            self.msgBox.setDetailedText(error)
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
        else:
            self.loginGroupBox.setEnabled(False)
            self.messageGroupBox.setEnabled(True)
            self.fromLineEdit.setText(username)
            self.fromLineEdit.setReadOnly(True)
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Login Successful")
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Server login successful, you may now proceed to write your email and send it.")
            self.msgBox.setInformativeText("Please make sure to click on 'Quit' to close the SMTP connection and close the application properly.")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()

        self.loginPushButton.setEnabled(True)
        

    def selectAttachments(self):
        self.attachmentsFileDialog = QFileDialog(self.centralwidget)
        f = self.attachmentsFileDialog.getOpenFileNames(self.centralwidget, "Select Files", "")
        global files
        files = None if not f else [Path(file) for file in f[0]]
        txt = ""
        if files:
            for file in files:
                txt += f"{file.name}, "
            txt = txt[0:-2]
        else:
            txt = "None"
        self.attachmentsLineEdit.setText(txt)
        self.attachmentsLineEdit.setReadOnly(True)


    def sendMail(self):
        fromEmail = self.fromLineEdit.text().strip()
        to = self.toLineEdit.text().strip().split(" ")
        subject = self.subjectLineEdit.text().strip()
        message = self.messagePlainTextEdit.toPlainText().strip()
        global files
        attachments = files

        self.sendMailThread = SendMailThread(fromEmail, to, subject, message, attachments)
        self.messageGroupBox.setEnabled(False)
        self.sendMailThread.start()
        self.sendMailThread.finished.connect(self.postMailStuff)
    

    def postMailStuff(self):
        self.messageGroupBox.setEnabled(True)
        if mailSendError:
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Mail Error")
            self.msgBox.setIcon(QMessageBox.Critical)
            self.msgBox.setText("An error occured while trying to send the email. Please try again.")
            self.msgBox.setInformativeText("Click 'Show Details' to check the error log.")
            self.msgBox.setDetailedText(mailSendError)
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
        else:
            self.msgBox = QtWidgets.QMessageBox(self.centralwidget)
            self.msgBox.setWindowTitle("Mail Sent Successful")
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Your mail has been sent successfully. You can send another mail if you want to.")
            self.msgBox.setInformativeText("Please make sure to click on 'Quit' to close the SMTP connection and close the application properly.")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
        
        self.toLineEdit.clear()
        self.subjectLineEdit.clear()
        self.messagePlainTextEdit.clear()
        global files
        files = None
        self.attachmentsLineEdit.setText("None")


class SendMailThread(QThread):
    def __init__(self, fromEmail, to, subject, message, attachments):
        super(SendMailThread, self).__init__()
        self.fromEmail = fromEmail
        self.to = to
        self.subject = subject
        self.message = message
        self.attachments = attachments

    def run(self):
        msg = MIMEMultipart()
        # FIXME: msg['From'] is actually name of the sender.
        msg['From'] = self.fromEmail
        msg['To'] = COMMASPACE.join(self.to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        if self.attachments:
            for path in self.attachments:
                part = MIMEBase('application', "octet-stream")
                with open(path, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                'attachment; filename={}'.format(Path(path).name)
                                )
                msg.attach(part)

        global mailSendError
        mailSendError = None
        try:
            server.sendmail(self.fromEmail, self.to, msg.as_string())
        except Exception as e:
            mailSendError = str(e)



if __name__ == "__main__":
    import sys

    QtWinExtras.QtWin.setCurrentProcessExplicitAppUserModelID("rudranshjoshi.python.pymailer")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
