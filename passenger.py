#!/bin/env python3
# IMPORTANT! THIS FILE ONLY CONTANINS GUI. IMPORTS ENCODER AND DECODER SEPARATELY.
# TODO READ EXTERNAL
# TODO GIT INTEGRATION
from PyQt5.QtWidgets import QAbstractItemView, QAction, QButtonGroup, QCheckBox, QComboBox, QDialog, QFileDialog, QGroupBox, QHeaderView, QMenu, QMessageBox, QRadioButton, QScrollArea, QShortcut, QTableWidget, QTableWidgetItem, QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap
from PyQt5.QtCore import Qt
from pyperclip import copy
from sys import exit, argv, platform
from base64 import b64decode
from random import choice
from os import popen, system, path
from json import load
from squirrel import StrBase
from io import StringIO
from pickle import loads
from os import popen
from endecode import en, de # encode/decode functions are here.
if "linux" in platform.lower():
    directory="/usr/share/Passenger"; currUsr=popen("echo $HOME").read().strip(); system(f"mkdir -pv {currUsr}/.passenger"); StrBaseDir=f"{currUsr}/.passenger/"
else:
    directory="."; currUsr=popen("echo %appdata%").read().strip(); system(f"if not exist '{currUsr}\\.passenger' mkdir {currUsr}\\.passenger"); StrBaseDir=f"{currUsr}\\.passenger\\"
try:
    with open(f"{directory}/Assets/language.json",encoding="UTF-8") as json_file:
        lang=load(json_file)
except:
    lang={
        "en":{
            "lang":"English",
            "appName":"Passenger",
            "willAdd":"will be added.",
            "willSkip":"will be skipped because already exists.",
            "willSkipSame":"will skip because same instance will already be add.",
            "willSkipKey":"will skip because key values cannot be same.",
            "totalAdd":"Total {} entry/entries will be added.",
            "mFile":"&File",
            "mEdit":"&Edit",
            "mConst":"&Constants",
            "mOptions":"&Options",
            "fQuit":"&Quit",
            "fImport":"&Import from browser",
            "fExport":"&Export to CSV file.",
            "eReset":"&Reset Password",
            "searchPW":"Search Passwords",
            "tbAdd":"Add Password",
            "tbEdit":"Edit Selected",
            "tbDel":"Delete Selected",
            "nothingToEdit":"There is no entry to edit. Select one first.",
            "nothingToDel":"There is no entry to delete. Select one first.",
            "ttlAdd":"Add New Entry",
            "colNames":[
                "Platform",
                "Username",
                "Password"
            ],
            "conNames":[
                "Key",
                "Value"
            ],
            "censor":"Censor",
            "genPW":"Generate",
            "maniPW":"Manipulate",
            "bAdd":"Add Entry",
            "fAdded":"added succesfully.",
            "fAlready":"This account is already exists.",
            "mFillBlanks":"Fill the blanks for adding new entry.",
            "errFatal":"Fatal Error",
            "errWTF":"What the hell are you doing?",
            "errRestricted":"This is the only protected platform key in this program and congratulations, you have written it as a platform. Did it take a lot of time to find?",
            "errFillAll":"Please fill all areas.",
            "ttlEdit":"Edit Entry",
            "gUpd":"Update Entry",
            "gDel":"Delete Entry",
            "bUpd":"Save Changes",
            "cUpd":"Update Confirmation",
            "clUpd":"Do you really want to update this entry?",
            "updAs":"'{}' updated as {} - {}",
            "errUpdExisted":"There is an entry with the same data as the data you are trying to change.",
            "sUpd":"'{}' updated successfully.",
            "errFillOne":"Please fill at least one area to make changes.",
            "cDel":"Delete Confirmation",
            "clDel":"Do you really want to delete the '{}' entry?",
            "sDel":"{} has been deleted.",
            "ttlLogin":"Enter Application Password",
            "bLogin":"Login",
            "showPW":"Show Passwords",
            "ePass":"Enter Password",
            "logDesc":"Enter your password to access your other passwords.",
            "logTWrong":"Wrong Password",
            "logDWrong":"The password you entered does not matched.",
            "regTitle":"Set Application Password",
            "regDesc":"Create a strong password to keep your other passwords safe. This will be required everytime.",
            "conUsage":"Constant usage: Define as Email, Use as $Email.",
            "regMinTen":"min 10 chars",
            "regRePass":"Re-enter Password",
            "regSuccess":"Registiration Successful",
            "regSucDesc":"Your password has been saved.",
            "savePW":"Save Password",
            "resTitle":"Reset Application Password",
            "resDesc":"Re-create your password. This will be required for next login actions.",
            "resNewPW":"Enter New Password",
            "resCurPW":"Enter Current Password",
            "resRePW":"Re-enter New Password",
            "stRes":"Password Change Successful!",
            "sdRes":"Your new password has been saved. You must use this password everytime you open this program.",
            "errLogic":"Logical Error",
            "errDLogic":"You cannot change your password with the same as your current password.",
            "errTWrongPW":"Wrong Password",
            "errDWrongPW":"Nice try. But you must enter current password correctly.",
            "optTitle":"Options",
            "language":"Language",
            "sLang":"Selected Language",
            "wrnLang":"Language changes will be applied after relaunch!",
            "sSecur":"Security",
            "sReEncrypt":"Re-encrypt on every quit. (Quitting will take longer.)",
            "expTImport":"Export Data",
            "expDesc":"Export your data to a CSV file. You can export both passwords and constants. Select one to export. Do not forget, when import a password file exported from here, select type as 'Passenger'. Do not show exported files to anybody.",
            "bExport":"Export",
            "impTImport":"Import Data",
            "impGSelect":"File Selection",
            "impDesc":"Description",
            "lPickDrag":"Pick or drag and drop a file to start.",
            "lSelect":"Select File",
            "impNoFile":"Not Selected.",
            "bImport":"Import",
            "lBrowserType":"Export your passwords from your web browser and select that file to import your password. But before, select your browser:",
            "firefox":"Firefox Based",
            "chromium":"Chromium Based",
            "csvTitle":"Select CSV File",
            "csvMeaning":"Comma Separated Values (*.csv)",
            "selectCsv":"Select a csv file to import passwords.",
            "impReady":"Ready to import.",
            "impApprove":"Approve Changes (Cannot Revert)",
            "impTSuccess":"Success",
            "impDSuccess":"Changes applied successfully.",
            "impTNothing":"Nothing To Add",
            "impDNothing":"There is nothing to add into database.",
            "errNotCsv":"File extension must be csv.",
            "apply":"Apply",
            "discard":"Discard",
            "copy":"Copy",
            "conAdd":"Add New",
            "conDel":"Delete Selected",
            "unqKeyReq":"Unique Key Required",
            "keyExists":"The key you entered already exists.",
            "lMode":"Select what data you import:",
            "modeSel":"Mode Select",
            "rPasswords":"Passwords",
            "rBrowser":"Browsers",
            "rConstants":"Constants",
            "tGEdit":"Edit Selected",
            "tConstants":"Your Constants",
            "newEmpty":"New empty constant added.",
            "fillEmpty":"Fill empy one before adding new one.",
            "conBlak":"Constants cannot be left blank.",
            "valBlank":"Value cannot be left blank.",
            "sameKey":"Same key is already used.",
            "conEdSuc":"Constant edited successfully.",
            "notPermitted":"Operation not permitted.",
            "sameCon":"Same constant is already declared.",
            "sureDel":"Are you sure to delete?",
            "doneDel":"Deletion successed.",
            "notDel":"Deletion cancelled.",
            "tWrongFile":"Wrong File",
            "dWrongFile":"This file does not fit to required format.",
            "ffoxWTitle":"Importing on Firefox",
            "ffoxDesc":"Due to Firefox removed import file option, you need to change a setting to re-add the imort option. To do this follow this instructions:\n1) Go to \"about:config\" adress.\n2) Search for \"signon.management.page.fileImport.enabled\"\n3) Change the value to true.\nThen you are ready to import with the file you exported.",
            "expDoneTitle":"Export Successful",
            "expDoneConsDesc":"Export to file completed successfully. You can export the file to passenger applications.",
            "expDoneDesc":"Export to file completed successfully. You can export the file to your browser or passenger applications.",
            "expForGT":"Export For",
            "expFor":"Browsers cannot handle Passenger's constant management. Passenger mode will keep constants, browsers mode will replaces values. So, export for:",
            "expWhat":"What do you want to export:",
            "expEmptyTitle":"Nothing to export.",
            "expEmptyDesc":"Database empty so file not created."
        }
    }
if path.exists(f"{StrBaseDir}P@5$WoRd"):
    content=""
    with open(f"{StrBaseDir}P@5$WoRd","r",encoding="UTF-8") as file:
        content=de(file.read())
    with StringIO(content) as file:
        passwords:StrBase=loads(b64decode(file.read()))
else:
    passwords:StrBase=StrBase(("941c011cc85761e2fcfda3d964675bf9","124fa2874881ece0bac366399800ec1b","",""),("941c011cc85761e2fcfda3d964675bf9","24f42031cfe4add6fd220122360c1039","1",""),("941c011cc85761e2fcfda3d964675bf9","c9dcfdcb58f864cbffe8937015ec42cf","en",""),colNames=("Platform","Username","Password","URL"))
if path.exists(f"{StrBaseDir}v@R1A8l£"):
    content=""
    with open(f"{StrBaseDir}v@R1A8l£","r",encoding="UTF-8") as file:
        content=de(file.read())
    with StringIO(content) as file:
        constants:StrBase=loads(b64decode(file.read()))
else:
    constants:StrBase=StrBase(colNames=("Key","Value"))
def commit(type=0):
    if type==0:
        with open(f"{StrBaseDir}P@5$WoRd","w",encoding="UTF-8") as file:
            file.write(en(passwords.saveToString()))
    else:
        with open(f"{StrBaseDir}v@R1A8l£","w",encoding="UTF-8") as file:
            file.write(en(constants.saveToString()))
try:
    language=lang[passwords[2][2]]
except KeyError:
    passwords.edit("en",2,2)
    commit()
    language=lang["en"]
columnNames=language["colNames"]
manipulate={"q":["Q","q"],"w":["W","m","M","w"],"e":["E","€","£","e"],"r":["R","r"],"t":["T","7","t"],"y":["Y","h","y"],"u":["U","u","n"],"i":["I","1","i"],"o":["O","0","o"],"p":["P","p"],"a":["A","4","@","a"],"s":["S","$","5","s"],"d":["D","d"],"f":["F",],"g":["G","6","9","g"],"h":["H","y","h"],"j":["J","j"],"k":["K","k"],"l":["L","l"],"z":["Z","2","z"],"x":["X","x"],"c":["C","c"],"v":["V","v"],"b":["B","3","8","b"],"n":["N","n","u"],"m":["M","W","w","m"],"0":["O","o","0"],"1":["i","1"],"2":["Z","z","2"],"3":["B","3"],"4":["A","4"],"5":["S","s","5"],"6":["G","6"],"7":["7","?","T"],"8":["B","8"],"9":["g","9"],"@":["A","a"],"$":["S","s","5"],"€":["E","e"],"£":["E","e"],"?":["7"]}
specials="@_."
lowers="abcdefghijklmnopqrstuvyz"
letters=lowers+lowers.upper()
numbers="0123456789"
chars=letters+numbers+specials
def passwordManipulater(string):
    pw=""
    def convert(s):
        return choice(manipulate[s.lower()]) if s.lower() in manipulate.keys() else s 
    for i in string:
        pw+=convert(i)
    return pw
def passwordGeneragor():
    pw="".join([choice(chars) for _ in range(15)])
    for i in specials:
        while i not in pw:
            rand=choice(pw)
            if rand not in specials:
                pw=pw.replace(rand,i,1)
    return pw
def browserImport(filePath:str,constant=False,isFirefox:bool=False):
    error=lambda:QMessageBox.warning(imp,language["tWrongFile"],language["dWrongFile"],QMessageBox.Yes)
    data=StrBase()
    data.addCsv(filePath)
    log=[]
    add=0
    addlist=StrBase()
    if constant:
        if data.columnCount>2:
            error()
        else:
            data=data.cloneFromColumnRange(0,1)
            for entry in data.clone():
                if [entry[0],entry[1]] not in constants:
                    if not addlist.fetchXOne([entry[0],entry[1]],[True,True],[True,True],[[0],[1]]):
                        if not addlist.query(entry[0],True,True,[0]):
                            log.append("✓ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willAdd"])
                            addlist.add(entry[0],entry[1])
                            add+=1
                        else:
                            log.append("✗ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willSkipKey"])
                    else:
                        log.append("✗ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willSkipSame"])
                else:
                    log.append("✗ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willSkip"])
            data=addlist
            log=[language["totalAdd"].format(add)]+sorted(log)
            return data,log
    else:
        if data.columnCount<4:
            error()
        else:
            cols=(0,2,3,1)
            if isFirefox:
                data.apply(lambda x:x.replace("\"",""))
                cols=(0,1,2,0)
            data=data.cloneFromColumns(*cols,newColumnNames=("Platform","Username","Password","URL"))
            data.apply(lambda x:x.split("www.")[-1].split("//")[-1].split(".com")[0].split(".net")[0].split(".gov")[0].split(".org")[0].split(".mil")[0].split(".edu")[0].split("?")[0],[0])
            data.apply(en,[2])
            for entry in data.clone():
                index=passwords.indexof(passwords.fetchXOne([entry[0],entry[1]],[True,True],[True,True],[[0],[1]]))
                if index==-1:
                    if not addlist.fetchXOne([entry[0],entry[1]],[True,True],[True,True],[[0],[1]]):
                        log.append("✓ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willAdd"])
                        addlist.add(entry[0],entry[1])
                        add+=1
                    else:
                        log.append("✗ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willSkipSame"])
                        data.delRow(data.indexof(data.fetchXOne([entry[0],entry[1]],[True,True],[True,True],[[0],[1]])))
                else:
                    log.append("✗ "+entry[0]+" ─ "+entry[1]+"\n └ "+language["willSkip"])
                    data.delRow(data.indexof(data.fetchXOne([entry[0],entry[1]],[True,True],[True,True],[[0],[1]])))
            log=[language["totalAdd"].format(add)]+sorted(log)
            return data,log
    return False
def reEncrypt():
    sec,lan=passwords[1][2],passwords[2][2]
    passwords.apply(de,[2])
    passwords.apply(en,[2])
    passwords.edit(sec,1,2)
    passwords.edit(lan,2,2)
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        if "win" in platform:
            self.setFixedSize(460,640)
        elif "lin" in platform:
            self.setMinimumSize(460,640)
        self.viewWidget=ViewWidget()
        self.setCentralWidget(self.viewWidget)
        self.setWindowTitle(language["appName"])
        self.menu=self.menuBar()
        self.setMenuBar(self.menu)
        self.fileMenu=QMenu(language["mFile"])
        self.fileImport=QAction(QIcon(f"{directory}/Assets/import.png"),language["fImport"],self)
        self.fileImport.triggered.connect(lambda:imp.show())
        self.fileImport.setShortcut(QKeySequence("Ctrl+I"))
        self.fileExport=QAction(QIcon(f"{directory}/Assets/export.png"),language["fExport"],self)
        self.fileExport.triggered.connect(lambda:exp.show())
        self.fileExport.setShortcut(QKeySequence("Ctrl+X"))
        self.fileQuit=QAction(QIcon(f"{directory}/Assets/quit.png"),language["fQuit"],self)
        self.fileQuit.triggered.connect(app.quit)
        self.fileQuit.setShortcut(QKeySequence("Ctrl+Q"))
        self.fileMenu.addActions([self.fileImport,self.fileExport,self.fileQuit])
        self.editMenu=QMenu(language["mEdit"])
        self.editOpt=QAction(QIcon(f"{directory}/Assets/config.png"),language["mOptions"])
        self.editOpt.setShortcut(QKeySequence("F2"))
        self.editOpt.triggered.connect(lambda:opt.show())
        self.editReset=QAction(QIcon(f"{directory}/Assets/passenger.png"),language["eReset"],self)
        self.editReset.triggered.connect(lambda:res.show())
        self.editReset.setShortcut(QKeySequence("Ctrl+R"))
        self.editMenu.addActions([self.editReset,self.editOpt])
        self.constMenu=QMenu(language["mConst"])
        self.constEdit=QAction(QIcon(f"{directory}/Assets/constants.png"),language["mEdit"],self)
        self.constEdit.triggered.connect(lambda:con.show())
        self.constEdit.setShortcut(QKeySequence("Ctrl+O"))
        self.constMenu.addAction(self.constEdit)
        self.menu.addMenu(self.fileMenu)
        self.menu.addMenu(self.editMenu)
        self.menu.addMenu(self.constMenu)
class ViewWidget(QWidget):
    def __init__(self):
        super(ViewWidget,self).__init__()
        self.layout=QGridLayout(self)
        self.addButton=QPushButton(language["tbAdd"])
        self.addButton.clicked.connect(self.openAddWindow)
        self.focusAddButton=QShortcut(QKeySequence("Ctrl+N"),self)
        self.focusAddButton.activated.connect(self.openAddWindow)
        self.editButton=QPushButton(language["tbEdit"])
        self.editButton.clicked.connect(self.openEditWindow)
        self.focusEditButton=QShortcut(QKeySequence("Ctrl+E"),self)
        self.focusEditButton.activated.connect(self.openEditWindow)
        self.delButton=QPushButton(language["tbDel"])
        self.delButton.clicked.connect(self.deleteSelected)
        self.focusDelButton=QShortcut(QKeySequence("Delete"),self)
        self.focusDelButton.activated.connect(self.deleteSelected)
        self.searchBar=QLineEdit()
        self.searchBar.setPlaceholderText(language["searchPW"])
        self.searchBar.textChanged.connect(self.reloadTable)
        self.focusSearchBar=QShortcut(QKeySequence("Ctrl+F"),self)
        self.focusSearchBar.activated.connect(lambda:[self.searchBar.setFocus(),self.searchBar.selectAll()])
        self.table=QTableWidget(self)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.contextMenu)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setColumnCount(len(columnNames))
        self.reloadTable()
        self.table.setHorizontalHeaderLabels(iter(columnNames))
        self.layout.addWidget(self.addButton,0,0)
        self.layout.addWidget(self.editButton,0,1)
        self.layout.addWidget(self.delButton,0,2)
        self.layout.addWidget(self.searchBar,1,0,1,3)
        self.layout.addWidget(self.table,2,0,1,3)
        self.searchBar.setFocus()
    def reloadTable(self):
        self.table.setRowCount(0)
        db=StrBase(*passwords[3:],colNames=("Platform","Username","Password"))
        db.sortByKey(lambda x:x[0].lower())
        db=db.query(self.searchBar.text(),False,False,[0,1])
        if db:
            for row,data in enumerate(db):
                self.table.setRowCount(self.table.rowCount()+1)
                exec(f"""pl=QTableWidgetItem("{data[0]}")
un=TButton("{data[1]}")
pw=TButton("{language["copy"]}")
un.clicked.connect(lambda:copy("{data[1]}" if not "{data[1]}".startswith("$") else (constants.fetchOne("{data[1]}".replace("$","",1),1,1,[0])[1] if constants.fetchOne("{data[1]}".replace("$","",1),1,1,[0]) else "{data[1]}")))
pw.clicked.connect(lambda:copy(de("{data[2]}")))
self.table.setItem(row,0,pl)
self.table.setCellWidget(row,1,un)
self.table.setCellWidget(row,2,pw)""")
    def openAddWindow(self):
        add.ePlatform.setText("")
        add.eUrlAdres.setText("")
        add.eUsername.setText("")
        add.ePassword.setText("")
        add.ePassword.setEchoMode(QLineEdit.Password)
        add.cCensor.setChecked(True)
        add.show()
    def openEditWindow(self):
        if self.table.currentRow()!=-1:
            selected=passwords.fetchXOne([self.table.item(self.table.currentRow(),0).text(),self.table.cellWidget(self.table.currentRow(),1).text()],[True,True],[True,True],[[0],[1]])
            edit.selected=passwords.indexof(selected) if len(selected)>0 else 0
            edit.showSelected()
            edit.ePassword.setEchoMode(QLineEdit.Password)
            edit.cCensor.setChecked(True)
            edit.show()
        else:
            win.statusBar().showMessage(language["nothingToEdit"])
    def deleteSelected(self):
        if self.table.currentRow()!=-1:
            selected=passwords.fetchXOne([win.viewWidget.table.item(win.viewWidget.table.currentRow(),0).text(),win.viewWidget.table.cellWidget(win.viewWidget.table.currentRow(),1).text()],[True,True],[True,True],[[0],[1]])
            selected=passwords.indexof(selected) if len(selected)>0 else 0
            old=f"{passwords[selected][0]} - {passwords[selected][1]}"
            if QMessageBox.warning(self,language["cDel"],language["clDel"].format(old),QMessageBox.No,QMessageBox.Yes)==QMessageBox.Yes:
                passwords.delRow(selected)
                commit()
                win.statusBar().showMessage(language["sDel"].format(old))
                win.viewWidget.reloadTable()
                win.viewWidget.table.selectRow(0)
        else:
            win.statusBar().showMessage(language["nothingToDel"])
    def contextMenu(self,pos):
        cMenu=QMenu()
        qAdd=cMenu.addAction(language["bAdd"])
        qEdit=cMenu.addAction(language["gUpd"])
        qDel=cMenu.addAction(language["gDel"])
        qAdd.triggered.connect(win.viewWidget.openAddWindow)
        qEdit.triggered.connect(win.viewWidget.openEditWindow)
        qDel.triggered.connect(win.viewWidget.deleteSelected)
        cMenu.exec_(self.mapToGlobal(pos))
class AddWindow(QDialog):
    def __init__(self)->None:
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(language["ttlAdd"])
        self.setFixedWidth(350)
        self.layout=QGridLayout(self)
        self.lPlatform=QLabel(language["colNames"][0])
        self.lUsername=QLabel(language["colNames"][1])
        self.lPassword=QLabel(language["colNames"][2])
        self.lUrlAdres=QLabel("URL")
        self.ePlatform=QLineEdit(self)
        self.eUrlAdres=QLineEdit(self)
        self.eUsername=QLineEdit(self)
        self.eUsername.textChanged.connect(lambda:self.eUsername.setStyleSheet("color:#d7aE53" if self.eUsername.text().startswith("$") else ""))
        self.ePassword=QLineEdit(self)
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.cCensor=QCheckBox(language["censor"])
        self.cCensor.clicked.connect(lambda:self.ePassword.setEchoMode(QLineEdit.Password if self.cCensor.isChecked() else QLineEdit.Normal))
        self.cCensor.setChecked(1)
        self.bManipulate=QPushButton(language["maniPW"])
        self.bManipulate.clicked.connect(lambda:self.ePassword.setText(passwordManipulater(self.ePassword.text())))
        self.bGenerate=QPushButton(language["genPW"])
        self.bGenerate.clicked.connect(lambda:self.ePassword.setText(passwordGeneragor()))
        self.bAdd=QPushButton(language["bAdd"],self)
        self.bAdd.clicked.connect(self.addPassword)
        self.layout.addWidget(self.lPlatform,0,0)
        self.layout.addWidget(self.ePlatform,0,1)
        self.layout.addWidget(self.lUrlAdres)
        self.layout.addWidget(self.eUrlAdres)
        self.layout.addWidget(self.lUsername)
        self.layout.addWidget(self.eUsername)
        self.layout.addWidget(self.lPassword)
        self.layout.addWidget(self.ePassword)
        self.layout.addWidget(self.cCensor,4,1)
        self.layout.addWidget(self.bManipulate,5,0)
        self.layout.addWidget(self.bGenerate,5,1)
        self.layout.addWidget(self.bAdd,6,0,1,2)
    def addPassword(self):
        pl=self.ePlatform.text()
        ln=self.eUrlAdres.text()
        un=self.eUsername.text()
        pw=self.ePassword.text()
        self.ePlatform.setFocus()
        if "" in (pl,un,pw,ln):
            win.statusBar().showMessage(language["errFillAll"])
        elif pl=="941c011cc85761e2fcfda3d964675bf9":
            win.statusBar().showMessage(language["errFatal"])
            QMessageBox.warning(self,language["errWTF"],language["errRestricted"])
        elif len(passwords.fetchXOne([pl,un],[True,True],[True,True],columns=[[0],[1]]))==0:
            passwords.add(pl,un,en(pw),ln)
            win.viewWidget.reloadTable()
            commit()
            self.close()
            win.statusBar().showMessage(f"{pl} - {un}, "+language["fAdded"])
        else:
            win.statusBar().showMessage(language["fAlready"])
class EditWindow(QDialog):
    def __init__(self)->None:
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(language["ttlEdit"])
        self.layout=QGridLayout(self)
        self.setFixedWidth(350)
        self.lPlatform=QLabel(language["colNames"][0])
        self.lUsername=QLabel(language["colNames"][1])
        self.lPassword=QLabel(language["colNames"][2])
        self.lUrlAdres=QLabel("URL")
        self.ePlatform=QLineEdit(self)
        self.eUrlAdres=QLineEdit(self)
        self.eUsername=QLineEdit(self)
        self.eUsername.textChanged.connect(lambda:self.eUsername.setStyleSheet("color:#d7aE53" if self.eUsername.text().startswith("$") else ""))
        self.ePassword=QLineEdit(self)
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.cCensor=QCheckBox(language["censor"])
        self.cCensor.clicked.connect(lambda:self.ePassword.setEchoMode(QLineEdit.Password if self.cCensor.isChecked() else QLineEdit.Normal))
        self.cCensor.setChecked(1)
        self.bManipulate=QPushButton(language["maniPW"])
        self.bManipulate.clicked.connect(lambda:self.ePassword.setText(passwordManipulater(self.ePassword.text())))
        self.bGenerate=QPushButton(language["genPW"])
        self.bGenerate.clicked.connect(lambda:self.ePassword.setText(passwordGeneragor()))
        self.bEdit=QPushButton(language["gUpd"],self)
        self.bEdit.clicked.connect(self.editPassword)
        self.layout.addWidget(self.lPlatform,0,0)
        self.layout.addWidget(self.ePlatform,0,1)
        self.layout.addWidget(self.lUrlAdres)
        self.layout.addWidget(self.eUrlAdres)
        self.layout.addWidget(self.lUsername)
        self.layout.addWidget(self.eUsername)
        self.layout.addWidget(self.lPassword)
        self.layout.addWidget(self.ePassword)
        self.layout.addWidget(self.cCensor,4,1)
        self.layout.addWidget(self.bManipulate,5,0)
        self.layout.addWidget(self.bGenerate,5,1)
        self.layout.addWidget(self.bEdit,6,0,1,2)
        self.selected=0
    def showSelected(self):
        self.ePlatform.setPlaceholderText(passwords[self.selected][0])
        self.eUsername.setPlaceholderText(passwords[self.selected][1])
        self.ePassword.setPlaceholderText("*"*len(passwords[self.selected][2]))
        self.eUrlAdres.setPlaceholderText(passwords[self.selected][3])
        self.ePlatform.setFocus()
    def editPassword(self):
        pl=self.ePlatform.text()
        ln=self.eUrlAdres.text()
        un=self.eUsername.text()
        pw=self.ePassword.text()
        if any([not pl,not un,not pw,not ln]):
            if QMessageBox.warning(self,language["cUpd"],language["clUpd"],QMessageBox.No,QMessageBox.Yes)==QMessageBox.Yes:
                old=f"{passwords[self.selected][0]} - {passwords[self.selected][1]}"
                if len(passwords.fetchXOne([pl,un],[True,True],[True,True],columns=[[0],[1]]))==0:
                    if pl!="":
                        passwords.edit(pl,self.selected,0)
                    if un!="":
                        passwords.edit(un,self.selected,1)
                    if pw!="":
                        passwords.edit(en(pw),self.selected,2)
                    if ln!="":
                        passwords.edit(ln,self.selected,3)
                    win.statusBar().showMessage(language["updAs"].format(old,passwords[self.selected][0],passwords[self.selected][1]))
                    win.viewWidget.reloadTable()
                    commit()
                    self.close()
                elif pl=="" and un=="" and pw!="" and ln=="":
                    passwords.edit(en(pw),self.selected,2)
                    win.statusBar().showMessage(language["sUpd"].format(old))
                    win.viewWidget.reloadTable()
                    self.close()
                else:
                    win.statusBar().showMessage(language["errUpdExisted"])
        else:
            win.statusBar().showMessage(language["errFillOne"])
    def delPassword(self):
        old=f"{passwords[self.selected][0]} - {passwords[self.selected][1]}"
        if QMessageBox.warning(self,language["cDel"],language["clDel"].format(old),QMessageBox.No,QMessageBox.Yes)==QMessageBox.Yes:
            passwords.delRow(self.selected)
            commit()
            self.close()
            win.statusBar().showMessage(language["sDel"].format("sDel"))
            win.viewWidget.reloadTable()
class TButton(QPushButton):
    def __init__(self,*argv,**kwargs)->None:
        super().__init__(*argv,**kwargs)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)
    def contextMenu(self,pos):
        cMenu=QMenu()
        qAdd=cMenu.addAction(language["bAdd"])
        qEdit=cMenu.addAction(language["gUpd"])
        qDel=cMenu.addAction(language["gDel"])
        qAdd.triggered.connect(win.viewWidget.openAddWindow)
        qEdit.triggered.connect(win.viewWidget.openEditWindow)
        qDel.triggered.connect(win.viewWidget.deleteSelected)
        cMenu.exec_(self.mapToGlobal(pos))
class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.show()
        self.setWindowTitle(language["ttlLogin"])
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(400,200)
        self.layout=QGridLayout(self)
        self.ePassword=QLineEdit(self)
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.ePassword.textChanged.connect(self.checkPassword)
        self.ePassword.returnPressed.connect(self.submitPassword)
        self.bSubmitPW=QPushButton(language["bLogin"])
        self.bSubmitPW.setDisabled(True)
        self.bSubmitPW.clicked.connect(self.submitPassword)
        self.cShowPW=QCheckBox(language["showPW"],self)
        self.cShowPW.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.cShowPW.stateChanged.connect(lambda:self.ePassword.setEchoMode(QLineEdit.Normal if self.cShowPW.isChecked() else QLineEdit.Password))
        self.aShowPw=QShortcut(QKeySequence("Alt+S"),self)
        self.aShowPw.activated.connect(lambda:self.cShowPW.setChecked(not self.cShowPW.isChecked()))
        self.iLogo=QLabel("")
        self.iLogo.setPixmap(QPixmap(f"{directory}/Assets/passenger.png").scaled(96,96,True))
        self.iLogo.setAlignment(Qt.AlignCenter)
        self.lMessage=QLabel(language["logDesc"])
        self.lMessage.setWordWrap(True)
        self.lMessage.setAlignment(Qt.AlignCenter)
        self.lEnter=QLabel(language["ePass"])
        self.layout.addWidget(self.iLogo,0,0)
        self.layout.addWidget(self.lMessage,0,1,1,5)
        self.layout.addWidget(self.cShowPW,2,4,1,2)
        self.layout.addWidget(self.lEnter,2,0,1,2)
        self.layout.addWidget(self.ePassword,3,0,1,6)
        self.layout.addWidget(self.bSubmitPW,4,2,1,2)
        self.checkPassword()
    def checkPassword(self):
        status=len(self.ePassword.text())>9
        self.ePassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;" if status else "border:1px solid red; padding:.2em; border-radius:5%;")
        self.bSubmitPW.setDisabled(not status)
    def submitPassword(self):
        if self.ePassword.text()==de(passwords[0][2]):
            win.show()
            self.close()
        else:
            QMessageBox.warning(self,language["logTWrong"],language["logDWrong"])
class RegisterWindow(QWidget):
    def __init__(self):
        super(RegisterWindow,self).__init__()
        self.show()
        self.setWindowTitle(language["regTitle"])
        self.setFixedSize(430,250)
        self.layout=QGridLayout(self)
        self.iLogo=QLabel("")
        self.iLogo.setPixmap(QPixmap(f"{directory}/Assets/passenger.png").scaled(48,48,True))
        self.iLogo.setAlignment(Qt.AlignCenter)
        self.lMessage=QLabel(language["regDesc"])
        self.lMessage.setWordWrap(True)
        self.lMessage.setAlignment(Qt.AlignVCenter)
        self.lEnter=QLabel(language["ePass"])
        self.lMin10=QLabel(language["regMinTen"])
        self.lMin10.setAlignment(Qt.AlignRight)
        self.lReEnter=QLabel(language["regRePass"])
        self.ePassword=QLineEdit(self)
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.ePassword.textChanged.connect(self.checkPasswords)
        self.eRePassword=QLineEdit(self)
        self.eRePassword.textChanged.connect(self.checkPasswords)
        self.eRePassword.setEchoMode(QLineEdit.Password)
        self.cShowPW=QCheckBox(language["showPW"],self)
        self.cShowPW.stateChanged.connect(self.toggleShowPassword)
        self.bSavePW=QPushButton(language["savePW"])
        self.bSavePW.clicked.connect(self.savePassword)
        self.bSavePW.setDisabled(True)
        self.layout.addWidget(self.iLogo,0,0)
        self.layout.addWidget(self.lMessage,0,1,1,5)
        self.layout.addWidget(self.lEnter,1,0,1,2)
        self.layout.addWidget(self.lMin10,1,4,1,2)
        self.layout.addWidget(self.ePassword,2,0,1,6)
        self.layout.addWidget(self.lReEnter,3,0,1,2)
        self.layout.addWidget(self.eRePassword,4,0,1,6)
        self.layout.addWidget(self.cShowPW,5,0,1,2)
        self.layout.addWidget(self.bSavePW,6,2,1,2)
        self.checkPasswords()
    def toggleShowPassword(self):
        if self.cShowPW.isChecked():
            self.ePassword.setEchoMode(QLineEdit.Normal)
            self.eRePassword.setEchoMode(QLineEdit.Normal)
        else:
            self.ePassword.setEchoMode(QLineEdit.Password)
            self.eRePassword.setEchoMode(QLineEdit.Password)
    def checkPasswords(self):
        if len(self.ePassword.text())>9:
            self.bSavePW.setDisabled(self.ePassword.text()!=self.eRePassword.text())
            if self.ePassword.text()==self.eRePassword.text():
                self.eRePassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;")
            else:
                self.eRePassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
            self.ePassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;")
        else:
            self.ePassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
    def savePassword(self):
        passwords.edit(en(self.ePassword.text()),0,2)
        commit()
        QMessageBox.information(self,language["regSuccess"],language["regSucDesc"])
        win.show()
        self.close()
class ResetPassword(QDialog):
    def __init__(self):
        super(ResetPassword,self).__init__()
        self.setWindowTitle(language["resTitle"])
        self.setFixedSize(430,360)
        self.setWindowModality(Qt.ApplicationModal)
        self.layout=QGridLayout(self)
        self.iLogo=QLabel("")
        self.iLogo.setPixmap(QPixmap(f"{directory}/Assets/passenger.png").scaled(48,48,True))
        self.iLogo.setAlignment(Qt.AlignCenter)
        self.lMessage=QLabel(language["resDesc"])
        self.lMessage.setWordWrap(True)
        self.lMessage.setAlignment(Qt.AlignVCenter)
        self.lNewEnter=QLabel(language["resNewPW"])
        self.lEnter=QLabel(language["resCurPW"])
        self.lMin10=QLabel(language["regMinTen"])
        self.lMin10.setAlignment(Qt.AlignRight)
        self.lReEnter=QLabel(language["resRePW"])
        self.eCurPassword=QLineEdit(self)
        self.eCurPassword.setEchoMode(QLineEdit.Password)
        self.eCurPassword.textChanged.connect(self.checkPasswords)
        self.ePassword=QLineEdit(self)
        self.ePassword.setEchoMode(QLineEdit.Password)
        self.ePassword.textChanged.connect(self.checkPasswords)
        self.eRePassword=QLineEdit(self)
        self.eRePassword.setEchoMode(QLineEdit.Password)
        self.eRePassword.textChanged.connect(self.checkPasswords)
        self.cShowPW=QCheckBox(language["showPW"],self)
        self.cShowPW.stateChanged.connect(self.toggleShowPassword)
        self.bSavePW=QPushButton(language["savePW"])
        self.bSavePW.clicked.connect(self.savePassword)
        self.bSavePW.setDisabled(True)
        self.layout.addWidget(self.iLogo,0,0)
        self.layout.addWidget(self.lMessage,0,1,1,5)
        self.layout.addWidget(self.lEnter,1,0,1,2)
        self.layout.addWidget(self.eCurPassword,2,0,1,6)
        self.layout.addWidget(self.lNewEnter,3,0,1,2)
        self.layout.addWidget(self.lMin10,3,4,1,2)
        self.layout.addWidget(self.ePassword,4,0,1,6)
        self.layout.addWidget(self.lReEnter,5,0,1,2)
        self.layout.addWidget(self.eRePassword,6,0,1,6)
        self.layout.addWidget(self.cShowPW,7,0,1,2)
        self.layout.addWidget(self.bSavePW,8,2,1,2)
        self.checkPasswords()
    def toggleShowPassword(self):
        if self.cShowPW.isChecked():
            self.eCurPassword.setEchoMode(QLineEdit.Normal)
            self.ePassword.setEchoMode(QLineEdit.Normal)
            self.eRePassword.setEchoMode(QLineEdit.Normal)
        else:
            self.eCurPassword.setEchoMode(QLineEdit.Password)
            self.ePassword.setEchoMode(QLineEdit.Password)
            self.eRePassword.setEchoMode(QLineEdit.Password)
    def checkPasswords(self):
        equal=self.ePassword.text()==self.eRePassword.text()
        if len(self.ePassword.text())>9:
            self.bSavePW.setDisabled(not equal)
            self.ePassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;")
            if equal:
                self.eRePassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;")
            else:
                self.eRePassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
        else:
            self.bSavePW.setDisabled(True)
            self.eRePassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
            self.ePassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
        if len(self.eCurPassword.text())>9:
            self.eCurPassword.setStyleSheet("border:1px solid green; padding:.2em; border-radius:5%;")
        else:
            self.bSavePW.setDisabled(True)
            self.eCurPassword.setStyleSheet("border:1px solid red; padding:.2em; border-radius:5%;")
    def savePassword(self):
        if self.eCurPassword.text()==de(passwords[0][2]):
            if self.eCurPassword.text()==self.ePassword.text():
                QMessageBox.warning(self,"Logical Error","You cannot change your password with the same as your current password.")
            else:
                passwords.edit(en(self.ePassword.text()),0,2)
                commit()
                QMessageBox.information(self,language["stRes"],language["sdRes"])
                self.eCurPassword.setText("")
                self.ePassword.setText("")
                self.eRePassword.setText("")
                self.cShowPW.setChecked(False)
                win.show()
                self.close()
        elif self.eCurPassword.text()==self.ePassword.text():
            QMessageBox.warning(self,language["errLogic"],language["errDLogic"])
        else:
            QMessageBox.warning(self,language["errTWrongPW"],language["errDWrongPW"])
class Options(QDialog):
    def __init__(self):
        super(Options,self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(language["optTitle"])
        self.setFixedSize(300,250)
        self.layout=QGridLayout(self)
        self.gLang=QGroupBox(language["language"],self)
        self.glLang=QGridLayout(self.gLang)
        self.lLang=QLabel(language["sLang"])
        self.cLang=QComboBox()
        self.cLang.addItems([lang[i]["lang"] for i in lang.keys()])
        self.cLang.setCurrentText(lang[passwords[2][2]]["lang"])
        self.cLang.currentTextChanged.connect(lambda x:[passwords.edit(self.langs[x],2,2),commit(),self.lWarn.setText(lang[self.langs[x]]["wrnLang"])])
        self.lWarn=QLabel(language["wrnLang"])
        self.lWarn.setWordWrap(True)
        self.glLang.addWidget(self.lLang)
        self.glLang.addWidget(self.cLang,0,1)
        self.glLang.addWidget(self.lWarn,1,0,2,2)
        self.gSecur=QGroupBox(language["sSecur"],self)
        self.glSecur=QGridLayout(self.gSecur)
        self.lEnc=QLabel(language["sReEncrypt"])
        self.lEnc.setWordWrap(True)
        self.cEnc=QCheckBox()
        self.cEnc.setChecked(passwords[1][2]=="True")
        self.cEnc.stateChanged.connect(lambda:[passwords.edit(str(self.cEnc.isChecked()),1,2),commit()])
        self.glSecur.addWidget(self.lEnc)
        self.glSecur.addWidget(self.cEnc,0,1,Qt.AlignCenter)
        self.layout.addWidget(self.gLang)
        self.layout.addWidget(self.gSecur)
        self.langs={}
        for key in lang.keys():
            self.langs[lang[key]["lang"]]=key
class ExportWindow(QDialog):
    def __init__(self):
        super(ExportWindow,self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(language["expTImport"])
        self.layout=QGridLayout(self)
        self.rMConstants=QRadioButton(language["rConstants"])
        self.rMPasswords=QRadioButton(language["rPasswords"])
        self.gMode=QButtonGroup()
        self.gMode.addButton(self.rMPasswords)
        self.gMode.addButton(self.rMConstants)
        self.gMode.buttonToggled.connect(self.setMode)
        self.rPassenger=QRadioButton(language["appName"])
        self.rBrowser=QRadioButton(language["rBrowser"])
        self.gFor=QButtonGroup()
        self.gFor.addButton(self.rPassenger)
        self.gFor.addButton(self.rBrowser)
        self.lExportFor=QLabel(language["expFor"],self)
        self.lExportFor.setWordWrap(True)
        self.lExport=QLabel(language["expDesc"])
        self.lExport.setWordWrap(True)
        self.lExport.setAlignment(Qt.AlignJustify)
        self.lExpWhat=QLabel(language["expWhat"])
        self.lExpWhat.setWordWrap(True)
        self.boxExportFor=QGroupBox(language["expForGT"],self)
        self.layExportFor=QGridLayout(self.boxExportFor)
        self.layExportFor.addWidget(self.lExportFor)
        self.layExportFor.addWidget(self.rPassenger)
        self.layExportFor.addWidget(self.rBrowser)
        self.bExport=QPushButton(language["bExport"])
        self.bExport.clicked.connect(self.exportFile)
        self.boxExpWhat=QGroupBox(language["modeSel"],self)
        self.layExpWhat=QGridLayout(self.boxExpWhat)
        self.layExpWhat.addWidget(self.lExpWhat)
        self.layExpWhat.addWidget(self.rMPasswords)
        self.layExpWhat.addWidget(self.rMConstants)
        self.boxExport=QGroupBox(language["expTImport"],self)
        self.layExport=QGridLayout(self.boxExport)
        self.layExport.addWidget(self.lExport)
        self.layExport.addWidget(self.boxExpWhat)
        self.layExport.addWidget(self.boxExportFor)
        self.layExport.addWidget(self.bExport)
        self.layout.addWidget(self.boxExport)
        self.rBrowser.setChecked(True)
        self.rMPasswords.setChecked(True)
    def exportFile(self):
        url=QFileDialog.getSaveFileName(self,language["expTImport"],filter=language["csvMeaning"],options=QFileDialog.DontUseNativeDialog)[0]
        if url[-4:]!=".csv":
            url=f"{url}.csv"
        if url!=".csv":
            if self.rMConstants.isChecked():
                csv=constants.clone()
                csv.renameColumns("Key","Value")
                empty=csv.queries([""],[True,True],[True,True],[[]])
                while empty:
                    empty=csv.queries([""],[True,True],[True,True],[[]])
                    csv.delRow(csv.indexof(["",""]))
                if csv:
                    csv.saveCsv(url)
                    QMessageBox.information(self,language["expDoneTitle"],language["expDoneConsDesc"],QMessageBox.Ok)
                else:
                    QMessageBox.information(self,language["expEmptyTitle"],language["expEmptyDesc"],QMessageBox.Ok)
            else:
                csv=passwords.clone() 
                for _ in range(3):
                    csv.delRow(0)
                csv.apply(lambda x:de(x),[2])
                if self.rBrowser.isChecked(): csv.apply(lambda x:x if not x.startswith("$") else (constants.fetchOne(x.replace("$","",1),True,True,[0])[1] if constants.fetchOne(x.replace("$","",1),True,True,[0]) else x),[1])
                csv=csv.cloneFromColumns(0,3,1,2)
                if csv:
                    csv.saveCsv(url)
                    QMessageBox.warning(self,language["ffoxWTitle"],language["ffoxDesc"],QMessageBox.Ok)
                    QMessageBox.information(self,language["expDoneTitle"],language["expDoneDesc"],QMessageBox.Ok)
                else:
                    QMessageBox.information(self,language["expEmptyTitle"],language["expEmptyDesc"],QMessageBox.Ok)
            self.close()
    def setMode(self):
        state=self.rMPasswords.isChecked()
        self.boxExportFor.setDisabled(not state)
class ImportWindow(QDialog):
    def __init__(self):
        super(ImportWindow,self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(language["impTImport"])
        self.layout=QGridLayout(self)
        self.boxMode=QGroupBox(language["impDesc"],self)
        self.layMode=QGridLayout(self.boxMode)
        self.lMode=QLabel(language["lMode"])
        self.rMPasswords=QRadioButton(language["rPasswords"])
        self.rMPasswords.setChecked(True)
        self.rMConstants=QRadioButton(language["rConstants"])
        self.gMode=QButtonGroup()
        self.gMode.addButton(self.rMPasswords)
        self.gMode.addButton(self.rMConstants)
        self.gMode.buttonToggled.connect(self.setMode)
        self.layMode.addWidget(self.lMode)
        self.layMode.addWidget(self.rMPasswords)
        self.layMode.addWidget(self.rMConstants)
        self.boxSettings=QGroupBox(language["modeSel"],self)
        self.laySettings=QGridLayout(self.boxSettings)
        self.boxFileSelect=QGroupBox(language["impGSelect"],self)
        self.layFileSelect=QGridLayout(self.boxFileSelect)
        self.lSettings=QLabel(language["lPickDrag"])
        self.lSettings.setWordWrap(True)
        self.bSelect=Button(language["lSelect"],self)
        self.bSelect.clicked.connect(self.selectFile)
        self.bSelect.setShortcut(QKeySequence("Ctrl+O"))
        self.eFileName=QLabel(language["impNoFile"])
        self.layFileSelect.addWidget(self.lSettings,0,0,1,3)
        self.layFileSelect.addWidget(self.bSelect,1,0)
        self.layFileSelect.addWidget(self.eFileName,1,1,1,2)
        self.bImport=QPushButton(language["bImport"],self)
        self.bImport.clicked.connect(self.importValues)
        self.bImport.setShortcut(QKeySequence("Ctrl+Enter"))
        self.lDesc=QLabel(language["lBrowserType"])
        self.lDesc.setWordWrap(True)
        self.rFirefox=QRadioButton(language["firefox"])
        self.rChromium=QRadioButton(language["chromium"])
        self.rPassenger=QRadioButton(language["appName"])
        self.rChromium.setChecked(True)
        self.laySettings.addWidget(self.lDesc)
        self.laySettings.addWidget(self.rChromium)
        self.laySettings.addWidget(self.rFirefox)
        self.laySettings.addWidget(self.rPassenger)
        self.lStatus=QLabel()
        self.layout.addWidget(self.boxMode,0,0,1,3)
        self.layout.addWidget(self.boxFileSelect,1,0,1,3)
        self.layout.addWidget(self.boxSettings,2,0,1,3)
        self.layout.addWidget(self.lStatus,3,0,1,3)
        self.layout.addWidget(self.bImport,4,1)
        self.file=""
        self.log=[]
        self.canImport()
    def selectFile(self):
        file=QFileDialog.getOpenFileName(self,language["csvTitle"],"",language["csvMeaning"],options=QFileDialog.DontUseNativeDialog)
        self.file=file[0]
        self.eFileName.setText(file[0].split("/")[-1] if file[0] else language["impNoFile"])
        self.canImport()
    def canImport(self):
        state=self.eFileName.text()==language["impNoFile"]
        self.bImport.setDisabled(state)
        if state:
            self.lStatus.setText(language["selectCsv"])
        else:
            self.lStatus.setText(language["impReady"])
    def importValues(self):
        global log
        results=browserImport(self.file,self.rMConstants.isChecked(),self.rFirefox.isChecked())
        if results:
            log=LogWindow(language["impApprove"],"\n".join(results[1]),lambda:self._exec(results))
            log.show()
    def _exec(self,results):
        if len(results[0])>0:
            if self.rMPasswords.isChecked():
                passwords.merge(results[0])
                commit()
                win.viewWidget.reloadTable()
            else:
                constants.merge(results[0])
                commit(1)
                con.reloadTable()
            self.file=""
            self.eFileName.setText(language["impNoFile"])
            QMessageBox.information(self,language["impTSuccess"],language["impDSuccess"])
        else:
            QMessageBox.warning(self,language["impTNothing"],language["impDNothing"])
        self.close()
        imp.close()
        log.close()
    def setMode(self):
        state=self.rMConstants.isChecked()
        self.boxSettings.setDisabled(state)
class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):
        if e.mimeData().hasUrls():
            e.accept()
        else:e.ignore()
    def dropEvent(self,e):
        if e.mimeData().text().strip()[-4:]==".csv":
            imp.eFileName.setText(e.mimeData().text().replace("%20"," ").strip().split("/")[-1])
            imp.file=e.mimeData().text().replace("%20"," ").strip().split("//"+("/" if "win" in platform else ""))[1]
        else:
            imp.lStatus.setText(language["errNotCsv"])
        imp.canImport()
class LogWindow(QWidget):
    def __init__(self,title:str,content:str,function):
        super(LogWindow,self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.minimumWidth(),self.minimumHeight())
        self.setWindowTitle(title)
        self.layout=QGridLayout(self)
        self.log=QLabel(content,self)
        self.log.setWordWrap(True)
        self.log.setAlignment(Qt.AlignTop)
        self.scrollArea=QScrollArea(self)
        self.scrollArea.setFixedSize(360,240)
        self.scrollArea.setWidget(self.log)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("background-color:#222; color:#ccc")
        self.apply=QPushButton(language["apply"],self)
        self.discard=QPushButton(language["discard"],self)
        self.apply.clicked.connect(function)
        self.discard.clicked.connect(self.close)
        self.layout.addWidget(self.scrollArea,0,0,1,2)
        self.layout.addWidget(self.apply,1,0)
        self.layout.addWidget(self.discard,1,1)
class ConstantWindow(QDialog):
    def __init__(self):
        super(ConstantWindow,self).__init__()
        self.setWindowTitle(language["appName"])
        self.setWindowModality(Qt.ApplicationModal)
        self.layout=QHBoxLayout(self)
        self.editGroup=QGroupBox(language["tGEdit"])
        self.editLayout=QGridLayout(self.editGroup)
        self.editLayout.setAlignment(Qt.AlignTop)
        self.lKey=QLabel("Key")
        self.eKey=QLineEdit()
        self.eKey.setPlaceholderText("Key")
        self.focusEKey=QShortcut(QKeySequence("F2"),self)
        self.focusEKey.activated.connect(lambda:self.eKey.setFocus())
        self.lValue=QLabel("Value")
        self.eValue=QLineEdit()
        self.eValue.setPlaceholderText("Value")
        self.bEdit=QPushButton(language["tbEdit"])
        self.bEdit.clicked.connect(self.editSelected)
        self.bDel=QPushButton(language["conDel"])
        self.bDel.clicked.connect(self.deleteSelected)
        self.status=QLabel("")
        self.status.setWordWrap(True)
        self.editLayout.addWidget(self.lKey,0,0,1,2)
        self.editLayout.addWidget(self.eKey,1,0,1,2)
        self.editLayout.addWidget(self.lValue,2,0,1,2)
        self.editLayout.addWidget(self.eValue,3,0,1,2)
        self.editLayout.addWidget(self.bEdit)
        self.editLayout.addWidget(self.bDel)
        self.editLayout.addWidget(self.status,5,0,1,2)
        self.tableGroup=QGroupBox(language["tConstants"])
        self.tableGroup.setMinimumSize(400,500)
        self.tableLayout=QGridLayout(self.tableGroup)
        self.desc=QLabel(language["conUsage"],self)
        self.desc.setAlignment(Qt.AlignJustify)
        self.desc.setWordWrap(True)
        self.table=QTableWidget(1,2,self)
        self.table.setHorizontalHeaderLabels(language["conNames"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.bAdd=QPushButton(language["conAdd"])
        self.bAdd.clicked.connect(self.addNewLine)
        self.tableLayout.addWidget(self.desc)
        self.tableLayout.addWidget(self.bAdd)
        self.tableLayout.addWidget(self.table)
        self.layout.addWidget(self.editGroup)
        self.layout.addWidget(self.tableGroup)
        self.table.currentCellChanged.connect(self.fillEditArea)
        self.reloadTable()
        self.table.selectRow(0)
    def addNewLine(self):
        if len(constants)>0:
            if ["",""] not in constants:
                constants.add("","")
                self.reloadTable()
                self.eKey.setFocus()
                self.status.setText(language["newEmpty"])
                self.table.selectRow(self.table.rowCount()-1) 
            else:
                self.status.setText(language["fillEmpty"])
                self.table.selectRow(constants.indexof(["",""]))
        else:
            self.table.setRowCount(1)
    def fillEditArea(self):
        self.eKey.setText(self.table.model().index(self.table.currentRow(),0).data(0))
        self.eValue.setText(self.table.model().index(self.table.currentRow(),1).data(0))
    def editSelected(self):
        key=self.eKey.text()
        val=self.eValue.text()
        row=self.table.currentRow()
        tabkey=self.table.model().index(row,0).data(0)
        tabval=self.table.model().index(row,1).data(0)
        if [key,val] in constants:
            if ["",""] in constants:
                if (tabkey,tabval)==("",""):
                    self.status.setText(language["conBlank"])
                else:
                    self.deleteSelected()
            else:
                self.status.setText(language["sameCon"])
        elif (val,key)==("",""):
            if (tabkey,tabval)==("",""):
                self.status.setText(language["conBlank"])
            else:
                self.deleteSelected()
        elif val=="":
            self.status.setText(language["valBlank"])
        elif key=="":
            self.status.setText(language["keyBlank"])
        elif constants.query(key,True,False,[0]) and tabkey!=key:
            self.status.setText(language["sameKey"])
        elif (tabkey,tabval)==("",""):
            constants.editRow((key,val),row)
            self.reloadTable()
            self.status.setText(language["conEdSuc"])
        elif QMessageBox.warning(self,language["ttlEdit"],language["clUpd"],QMessageBox.No,QMessageBox.Yes)==QMessageBox.Yes:
            constants.editRow((key,val),row)
            self.reloadTable()
            self.status.setText(language["conEdSuc"])
        else:
            self.status.setText(language["notPermitted"])
    def reloadTable(self):
        self.table.setRowCount(len(constants))
        if len(constants)<1:
            self.table.setRowCount(1)
            constants.add("","")
            self.table.setItem(0,0,QTableWidgetItem(""))
            self.table.setItem(0,1,QTableWidgetItem(""))
            self.table.selectRow(0)
        else:
            for row in range(len(constants)):
                for col in range(constants.columnCount):
                    self.table.setItem(row,col,QTableWidgetItem(constants[row][col]))
        commit(1)
    def deleteSelected(self):
        if QMessageBox.warning(self,language["cDel"],language["sureDel"],QMessageBox.No,QMessageBox.Yes)==QMessageBox.Yes:
            constants.delRow(self.table.currentRow())
            if len(constants)==1:
                self.eKey.setText("")
                self.eValue.setText("")
            self.reloadTable()
            self.status.setText(language["doneDel"])
        else:
            self.status.setText(language["notDel"])
app=QApplication(argv)
app.setWindowIcon(QIcon(f"{directory}/Assets/passenger.svg"))
app.lastWindowClosed.connect(lambda:[reEncrypt(),commit()] if passwords[1][2]=="True" else commit())
win=MainWin()
add=AddWindow()
edit=EditWindow()
res=ResetPassword()
opt=Options()
exp=ExportWindow()
imp=ImportWindow()
con=ConstantWindow()
if passwords[0][2]=="":
    reg=RegisterWindow()
else:
    LoginWindow()
exit(app.exec_())
