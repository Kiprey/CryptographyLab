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
import socket
import threading

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# global so
# ///////////////////////////////////////////////////////////////
crypt_library = cdll.LoadLibrary("../../build/libcryptolab.so")
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recv_thread = None
thread_exit_flag = False
DH_class = None

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

        # APP NAMEf
        # ///////////////////////////////////////////////////////////////
        title = "加密系统"
        description = "一个加解密综合服务菜单式展示界面,包括多种加密算法以及协议."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

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
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

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
            widgets.stackedWidget.setCurrentWidget(
                widgets.fang_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_liu":
            widgets.stackedWidget.setCurrentWidget(
                widgets.liu_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_liu_2":
            widgets.stackedWidget.setCurrentWidget(
                widgets.liu_2_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_duichen":
            widgets.stackedWidget.setCurrentWidget(
                widgets.duichen_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_feiduichen":
            widgets.stackedWidget.setCurrentWidget(
                widgets.feiduichen_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_DH":
            widgets.stackedWidget.setCurrentWidget(widgets.DH_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_SSL":
            widgets.stackedWidget.setCurrentWidget(
                widgets.SSL_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_save":
            AppFunctions.test(self.ui)

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
        crypt_library.Affine_encrypt.argtypes = [
            c_int, c_int, c_char_p, c_char_p]
        crypt_library.Affine_encrypt(key1, key2, mingwen, miwen)
        widgets.plainTextEdit_14.setPlainText(bytes.decode(miwen))

    # Affine解密

    def Affine_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_15.toPlainText())
        key1 = int(widgets.lineEdit_5.text())
        key2 = int(widgets.lineEdit_6.text())
        crypt_library.Affine_decrypt.argtypes = [
            c_int, c_int, c_char_p, c_char_p]
        crypt_library.Affine_decrypt(key1, key2, miwen, mingwen)
        widgets.plainTextEdit_14.setPlainText(bytes.decode(mingwen))

    # RC4 加密
    def RC4_encrypt(self):
        key = str.encode(widgets.plainTextEdit_18.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_12.toPlainText())
        s_box = create_string_buffer(256)
        s = cast(s_box, c_char_p)
        crypt_library.RC4_set_key.argtypes = [c_char_p, c_char_p]
        crypt_library.RC4_set_key(s, key)
        crypt_library.RC4_enc_dec.argtypes = [c_char_p, c_char_p]
        crypt_library.RC4_enc_dec.restype = c_char_p
        miwen = crypt_library.RC4_enc_dec(s, mingwen)
        widgets.plainTextEdit_11.setPlainText(miwen.hex())

    def RC4_decrypt(self):
        key = str.encode(widgets.plainTextEdit_18.toPlainText())
        miwen = str.encode(widgets.plainTextEdit_12.toPlainText())
        s_box = create_string_buffer(256)
        s = cast(s_box, c_char_p)
        crypt_library.RC4_set_key.argtypes = [c_char_p, c_char_p]
        crypt_library.RC4_set_key(s, key)
        crypt_library.RC4_enc_dec.argtypes = [c_char_p, c_char_p]
        crypt_library.RC4_enc_dec.restype = c_char_p
        mingwen = crypt_library.RC4_enc_dec(s, binascii.unhexlify(miwen))
        widgets.plainTextEdit_11.setPlainText(bytes.decode(mingwen))

    # LSFR加密
    def LSFR_encrypt(self):
        key = str.encode(widgets.plainTextEdit_23.toPlainText())
        mingwen = str.encode(widgets.plainTextEdit_22.toPlainText())
        c_box = create_string_buffer(4)
        c = cast(c_box, c_char_p)
        crypt_library.LFSR_set_key.argtypes = [c_char_p, c_char_p]
        crypt_library.LFSR_set_key(c, key)
        crypt_library.LFSR_enc_dec.argtypes = [c_char_p, c_char_p]
        crypt_library.LFSR_enc_dec.restype = c_char_p
        miwen = crypt_library.LFSR_enc_dec(c, mingwen)
        widgets.plainTextEdit_21.setPlainText(miwen.hex())

    def LSFR_decrypt(self):
        key = str.encode(widgets.plainTextEdit_23.toPlainText())
        miwen = str.encode(widgets.plainTextEdit_22.toPlainText())
        c_box = create_string_buffer(4)
        c = cast(c_box, c_char_p)
        crypt_library.LFSR_set_key.argtypes = [c_char_p, c_char_p]
        crypt_library.LFSR_set_key(c, key)
        crypt_library.LFSR_enc_dec.argtypes = [c_char_p, c_char_p]
        crypt_library.LFSR_enc_dec.restype = c_char_p
        mingwen = crypt_library.LFSR_enc_dec(c, binascii.unhexlify(miwen))
        widgets.plainTextEdit_21.setPlainText(bytes.decode(mingwen))

    # DES加密函数
    def DES_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_4.toPlainText())
        key = str.encode(widgets.lineEdit_2.text())
        crypt_library.DES_generateKeys.argtypes = [c_char_p]
        crypt_library.DES_generateKeys(key)
        crypt_library.DES_encrypt.argtypes = [c_char_p]
        crypt_library.DES_encrypt.restype = c_char_p
        miwen = crypt_library.DES_encrypt(mingwen)
        widgets.plainTextEdit_3.setPlainText(bytes.decode(miwen))

    # DES解密函数
    def DES_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_4.toPlainText())
        key = str.encode(widgets.lineEdit_2.text())
        crypt_library.DES_generateKeys.argtypes = [c_char_p]
        crypt_library.DES_generateKeys(key)
        crypt_library.DES_decrypt.argtypes = [c_char_p]
        crypt_library.DES_decrypt.restype = c_char_p
        mingwen = crypt_library.DES_decrypt(miwen)

        try:
            plain = bytes.decode(mingwen)
        except UnicodeDecodeError:
            plain = "Key Error"
        widgets.plainTextEdit_3.setPlainText(plain)

    # RSA
    def RSA_gen_key(self):
        e = c_int()  # (widgets.plainTextEdit_25.toPlainText())
        n = c_int()  # (widgets.plainTextEdit_24.toPlainText())
        d = c_int()  # (widgets.plainTextEdit_26.toPlainText())
        crypt_library.RSA_gen_key.argtypes = (
            POINTER(c_int), POINTER(c_int), POINTER(c_int))
        crypt_library.RSA_gen_key(pointer(e), pointer(d), pointer(n))
        widgets.plainTextEdit_25.setPlainText(str(e.value))
        widgets.plainTextEdit_24.setPlainText(str(n.value))
        widgets.plainTextEdit_26.setPlainText(str(d.value))
        widgets.plainTextEdit_27.setPlainText(str(n.value))

    def RSA_pubkey_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        e = int(widgets.plainTextEdit_25.toPlainText())
        n = int(widgets.plainTextEdit_24.toPlainText())
        crypt_library.RSA_pubkey_encrypt.argtypes = (c_char_p, c_int, c_int)
        crypt_library.RSA_pubkey_encrypt.restype = c_char_p
        miwen = crypt_library.RSA_pubkey_encrypt(mingwen, e, n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(miwen))

    def RSA_pubkey_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        e = int(widgets.plainTextEdit_25.toPlainText())
        n = int(widgets.plainTextEdit_24.toPlainText())
        crypt_library.RSA_pubkey_decrypt.argtypes = (c_char_p, c_int, c_int)
        crypt_library.RSA_pubkey_decrypt.restype = c_char_p
        mingwen = crypt_library.RSA_pubkey_decrypt(miwen, e, n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(mingwen))

    def RSA_privkey_encrypt(self):
        mingwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        d = int(widgets.plainTextEdit_26.toPlainText())
        n = int(widgets.plainTextEdit_27.toPlainText())
        crypt_library.RSA_privkey_encrypt.argtypes = (c_char_p, c_int, c_int)
        crypt_library.RSA_privkey_encrypt.restype = c_char_p
        miwen = crypt_library.RSA_privkey_encrypt(mingwen, d, n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(miwen))

    def RSA_privkey_decrypt(self):
        miwen = str.encode(widgets.plainTextEdit_6.toPlainText())
        d = int(widgets.plainTextEdit_26.toPlainText())
        n = int(widgets.plainTextEdit_27.toPlainText())
        crypt_library.RSA_privkey_decrypt.argtypes = (c_char_p, c_int, c_int)
        crypt_library.RSA_privkey_decrypt.restype = c_char_p
        mingwen = crypt_library.RSA_privkey_decrypt(miwen, d, n)
        widgets.plainTextEdit_7.setPlainText(bytes.decode(mingwen))

    def DH_connect(self):
        global new_socket, recv_thread, DH_class
        if recv_thread:
            widgets.plainTextEdit_16.appendPlainText("不允许重复的连接/监听")
            return
        ip = widgets.lineEdit_9.text()
        port = int(widgets.lineEdit_10.text())
        widgets.plainTextEdit_16.appendPlainText("尝试连接服务器......")
        try:
            new_socket.connect((ip,port))      # 连接服务器
            # Auth_DH_new
            crypt_library.Auth_DH_new.argtypes=[c_int]
            crypt_library.Auth_DH_new.restype=c_void_p
            DH_class=crypt_library.Auth_DH_new(new_socket.fileno())
            print("connect DH_class: " + hex(DH_class))
            widgets.plainTextEdit_16.appendPlainText("连接成功")
            # Auth_DH_client_exch_key
            crypt_library.Auth_DH_client_exch_key.argtypes=[c_void_p]
            crypt_library.Auth_DH_client_exch_key.restype=c_bool
            if(crypt_library.Auth_DH_client_exch_key(DH_class)):
                widgets.plainTextEdit_16.appendPlainText("协商成功")
            else:
                widgets.plainTextEdit_16.appendPlainText("协商失败")
                new_socket.close()
                return

        except ConnectionRefusedError:
            widgets.plainTextEdit_16.appendPlainText("连接失败")
            return

        recv_thread = threading.Thread(target=self.recv_msg_worker, args=(None,))
        recv_thread.start()


    def DH_listen(self):
        global recv_thread
        if recv_thread:
            widgets.plainTextEdit_16.appendPlainText("不允许重复的连接/监听")
            return
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = '0.0.0.0' # widgets.lineEdit_9.text()
        port = int(widgets.lineEdit_10.text())
        listen_socket.bind((ip,port))
        listen_socket.listen(5)
        recv_thread = threading.Thread(target=self.recv_msg_worker, args=(listen_socket,))
        recv_thread.start()

    def recv_msg_worker(self, listen_socket):
        global new_socket, thread_exit_flag, recv_thread, DH_class
        thread_exit_flag = False
        if listen_socket:
            widgets.plainTextEdit_16.appendPlainText('启动socket服务，等待客户端连接...')
            new_socket, _ = listen_socket.accept()     # 等待连接，此处自动阻塞
            # Auth_DH_new
            crypt_library.Auth_DH_new.argtypes=[c_int]
            crypt_library.Auth_DH_new.restype=c_void_p
            DH_class=crypt_library.Auth_DH_new(new_socket.fileno())
            print("listen DH_class: " + hex(DH_class))
            listen_socket.close()
            widgets.plainTextEdit_16.appendPlainText("客户端连接成功！")
            # Auth_DH_server_exch_key
            crypt_library.Auth_DH_server_exch_key.argtypes=[c_void_p]
            crypt_library.Auth_DH_server_exch_key.restype=c_bool
            if crypt_library.Auth_DH_server_exch_key(DH_class):
                widgets.plainTextEdit_16.appendPlainText("协商成功")
            else:
                widgets.plainTextEdit_16.appendPlainText("协商失败")
                new_socket.close()
                return
            
        while thread_exit_flag != True: 
            try:
                # client_data = new_socket.recv(1024).decode()      # 接收信息
                # replace to Auth_DH_recv
                crypt_library.Auth_DH_recv.argtypes=[c_void_p]
                crypt_library.Auth_DH_recv.restype=c_char_p
                dh_msg_bytes = crypt_library.Auth_DH_recv(DH_class) 
                if dh_msg_bytes is None:
                    raise BrokenPipeError("Remote connection shutdown")
                widgets.plainTextEdit_16.appendPlainText("来自远程的信息：%s" % dh_msg_bytes.decode())
            except BrokenPipeError:
                widgets.plainTextEdit_16.appendPlainText("连接已断开")
                # Auth_DH_free
                break
        recv_thread = None
        exit()

    def DH_disconnect(self):
        global new_socket, recv_thread, thread_exit_flag
        if recv_thread:
            thread_exit_flag = True
            new_socket.close()       # 关闭连接
            #recv_thread.join()
            new_socket = None
            widgets.plainTextEdit_16.appendPlainText("连接已断开")
            # Auth_DH_free
        else:
            widgets.plainTextEdit_16.appendPlainText("当前不存在连接")

    def DH_send(self):
        global new_socket, DH_class
        input = widgets.plainTextEdit_19.toPlainText()
        try:
            # new_socket.sendall(input.encode())
            # replace to Auth_DH_send
            crypt_library.Auth_DH_send.argtypes=[c_void_p,c_char_p]
            crypt_library.Auth_DH_send.restype=c_bool
            if(crypt_library.Auth_DH_send(DH_class ,input.encode())):
                widgets.plainTextEdit_16.appendPlainText("信息已发送：" + input)
            else:
                widgets.plainTextEdit_16.appendPlainText("信息发送失败")
        except BrokenPipeError:
            self.DH_disconnect()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

'''
无法正常关闭某个链接的原因：
    1. 父线程中设置了 exit flag，但是子线程无法获取到这个新设置的 exit flag ，因此子线程无法退出，以至于父线程在挂起等待
'''