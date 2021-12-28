# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from ctypes import *
import binascii

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# global so 
# ///////////////////////////////////////////////////////////////
crypt_library = cdll.LoadLibrary("../../build/libcryptolab.so")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "加密系统"
        description = "一个加解密综合服务菜单式展示界面,包括多种加密算法以及协议."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_fangshe.clicked.connect(self.buttonClick)
        widgets.btn_liu.clicked.connect(self.buttonClick)
        widgets.btn_liu_2.clicked.connect(self.buttonClick)
        widgets.btn_duichen.clicked.connect(self.buttonClick)
        widgets.btn_feiduichen.clicked.connect(self.buttonClick)
        widgets.btn_DH.clicked.connect(self.buttonClick)
        widgets.btn_SSL.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME  自定义qss主题
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes/py_dracula_dark.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_fangshe":
            widgets.stackedWidget.setCurrentWidget(widgets.fang_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_liu":
            widgets.stackedWidget.setCurrentWidget(widgets.liu_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_liu_2":
            widgets.stackedWidget.setCurrentWidget(widgets.liu_2_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_duichen":
            widgets.stackedWidget.setCurrentWidget(widgets.duichen_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_feiduichen":
            widgets.stackedWidget.setCurrentWidget(widgets.feiduichen_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "btn_DH":
            widgets.stackedWidget.setCurrentWidget(widgets.DH_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_SSL":
            widgets.stackedWidget.setCurrentWidget(widgets.SSL_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            AppFunctions.test(self,widgets)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # Affine加密
    def Affine_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        miwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        key1 = int(widgets.lineEdit_5.text())
        key2 = int(widgets.lineEdit_6.text())
        crypt_library.Affine_encrypt.argtypes=[c_int , c_int , c_char_p , c_char_p]
        crypt_library.Affine_encrypt(key1, key2, mingwen , miwen)
        widgets.plainTextEdit_14.setPlainText(bytes.decode(miwen))

    
    # Affine解密
    def Affine_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        key1 = int(widgets.lineEdit_5.text())
        key2 = int(widgets.lineEdit_6.text())
        crypt_library.Affine_decrypt.argtypes=[c_int , c_int , c_char_p , c_char_p]
        crypt_library.Affine_decrypt(key1, key2, miwen , mingwen)        
        widgets.plainTextEdit_14.setPlainText(bytes.decode(mingwen))

    # RC4 加密
    def RC4_encrypt(self):
        key = str.encode(widgets.plainTextEdit_18.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_12.toPlainText())
        s_box = create_string_buffer(256)
        s = cast(s_box,c_char_p)
        crypt_library.RC4_set_key.argtypes=[c_char_p,c_char_p]
        crypt_library.RC4_set_key(s,key)
        crypt_library.RC4_enc_dec.argtypes=[c_char_p,c_char_p]
        crypt_library.RC4_enc_dec.restype=c_char_p
        miwen = crypt_library.RC4_enc_dec(s,mingwen)
        widgets.plainTextEdit_11.setPlainText(miwen.hex())

    def RC4_decrypt(self):
        key = str.encode(widgets.plainTextEdit_18.toPlainText())
        miwen = str.encode(widgets.plainTextEdit_12.toPlainText())
        s_box = create_string_buffer(256)
        s = cast(s_box,c_char_p)
        crypt_library.RC4_set_key.argtypes=[c_char_p,c_char_p]
        crypt_library.RC4_set_key(s,key)
        crypt_library.RC4_enc_dec.argtypes=[c_char_p,c_char_p]
        crypt_library.RC4_enc_dec.restype=c_char_p
        mingwen = crypt_library.RC4_enc_dec(s,binascii.unhexlify(miwen))
        widgets.plainTextEdit_11.setPlainText(bytes.decode(mingwen))
    
    # LSFR加密
    def LSFR_encrypt(self):
        key = str.encode(widgets.plainTextEdit_23.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_22.toPlainText())
        c_box = create_string_buffer(4)
        c = cast(c_box,c_char_p)
        crypt_library.LFSR_set_key.argtypes=[c_char_p,c_char_p]
        crypt_library.LFSR_set_key(c,key)
        crypt_library.LFSR_enc_dec.argtypes=[c_char_p,c_char_p]
        crypt_library.LFSR_enc_dec.restype=c_char_p
        miwen = crypt_library.LFSR_enc_dec(c,mingwen)
        widgets.plainTextEdit_21.setPlainText(miwen.hex())

    def LSFR_decrypt(self):
        key = str.encode(widgets.plainTextEdit_23.toPlainText())
        miwen = str.encode(widgets.plainTextEdit_22.toPlainText())
        c_box = create_string_buffer(4)
        c = cast(c_box,c_char_p)
        crypt_library.LFSR_set_key.argtypes=[c_char_p,c_char_p]
        crypt_library.LFSR_set_key(c,key)
        crypt_library.LFSR_enc_dec.argtypes=[c_char_p,c_char_p]
        crypt_library.LFSR_enc_dec.restype=c_char_p
        mingwen = crypt_library.LFSR_enc_dec(c,binascii.unhexlify(miwen))
        widgets.plainTextEdit_21.setPlainText(bytes.decode(mingwen))

    # DES加密函数
    def DES_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_4.toPlainText())
        key = str.encode(widgets.lineEdit_2.text())
        crypt_library.DES_generateKeys.argtypes=[c_char_p]
        crypt_library.DES_generateKeys(key)
        crypt_library.DES_encrypt.argtypes= [c_char_p]
        crypt_library.DES_encrypt.restype= c_char_p
        miwen =crypt_library.DES_encrypt(mingwen)
        widgets.plainTextEdit_3.setPlainText(bytes.decode(miwen))
    
    # DES解密函数
    def DES_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_4.toPlainText())
        key = str.encode(widgets.lineEdit_2.text())
        crypt_library.DES_generateKeys.argtypes=[c_char_p]
        crypt_library.DES_generateKeys(key)
        crypt_library.DES_decrypt.argtypes= [c_char_p]
        crypt_library.DES_decrypt.restype= c_char_p
        mingwen =crypt_library.DES_decrypt(miwen)

        try:
            plain = bytes.decode(mingwen)
        except UnicodeDecodeError:
            plain = "Key Error"
        widgets.plainTextEdit_3.setPlainText(plain)
    
    # RSA
    def RSA_gen_key(self):
        e = c_int() #(widgets.plainTextEdit_25.toPlainText())
        n = c_int() #(widgets.plainTextEdit_24.toPlainText())
        d = c_int() #(widgets.plainTextEdit_26.toPlainText())
        crypt_library.RSA_gen_key.argtypes=(POINTER(c_int), POINTER(c_int), POINTER(c_int))
        crypt_library.RSA_gen_key(pointer(e),pointer(d),pointer(n))
        widgets.plainTextEdit_25.setPlainText(str(e.value))
        widgets.plainTextEdit_24.setPlainText(str(n.value))
        widgets.plainTextEdit_26.setPlainText(str(d.value))
        widgets.plainTextEdit_27.setPlainText(str(n.value))
    
    def RSA_pubkey_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        e = int(widgets.plainTextEdit_25.toPlainText())
        n = int(widgets.plainTextEdit_24.toPlainText())
        crypt_library.RSA_pubkey_encrypt.argtypes=(c_char_p,c_int,c_int)
        crypt_library.RSA_pubkey_encrypt.restype=c_char_p
        miwen = crypt_library.RSA_pubkey_encrypt(mingwen,e,n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(miwen))

    def RSA_pubkey_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        e = int(widgets.plainTextEdit_25.toPlainText())
        n = int(widgets.plainTextEdit_24.toPlainText())
        crypt_library.RSA_pubkey_decrypt.argtypes=(c_char_p,c_int,c_int)
        crypt_library.RSA_pubkey_decrypt.restype=c_char_p
        mingwen = crypt_library.RSA_pubkey_decrypt(miwen,e,n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(mingwen))

    def RSA_privkey_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        d = int(widgets.plainTextEdit_26.toPlainText())
        n = int(widgets.plainTextEdit_27.toPlainText())
        crypt_library.RSA_privkey_encrypt.argtypes=(c_char_p,c_int,c_int)
        crypt_library.RSA_privkey_encrypt.restype=c_char_p
        miwen = crypt_library.RSA_privkey_encrypt(mingwen,d,n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(miwen))

    def RSA_privkey_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        d = int(widgets.plainTextEdit_26.toPlainText())
        n = int(widgets.plainTextEdit_27.toPlainText())
        crypt_library.RSA_privkey_decrypt.argtypes=(c_char_p,c_int,c_int)
        crypt_library.RSA_privkey_decrypt.restype=c_char_p
        mingwen = crypt_library.RSA_privkey_decrypt(miwen,d,n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(mingwen))

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
