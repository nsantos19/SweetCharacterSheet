from os import popen
import sys
from typing import Counter
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from loadNewPage import *
from PyQt5 import QtCore

import json
from loadAttackDialog import *
import random
from loadEquipDialog import *
from loadSpellDialog import *
from loadSpellInfoDialog import *
from spell import *


class Player():
    def __init__(self,playerDic):
        self.strength = playerDic['str']
        self.dex = playerDic['dex']
        self.con = playerDic['con']
        self.int = playerDic['int']
        self.wis = playerDic['wis']
        self.char = playerDic['char']
        self.hp = playerDic['hp']
        self.temphp = playerDic['temphp']
        self.ac = playerDic['ac']
        self.spd = playerDic['spd']
        self.profs = playerDic['profs']
        self.skills = playerDic['skills']
        self.equips = playerDic['equips']
        self.attks = playerDic['attks']
        self.name = playerDic['name']
        self.race = playerDic['race']
        self.clss = playerDic['clss']
        self.exp = playerDic['exp']
        self.ststrength = playerDic['ststr']
        self.stdex = playerDic['stdex']
        self.stcon = playerDic['stcon']
        self.stint = playerDic['stint']
        self.stwis = playerDic['stwis']
        self.stchr = playerDic['stchr']
        self.cbstrength = playerDic['cbstr']
        self.cbdex = playerDic['cbdex']
        self.cbcon = playerDic['cbcon']
        self.cbint = playerDic['cbint']
        self.cbwis = playerDic['cbwis']
        self.cbchr = playerDic['cbchr']
        self.acro = playerDic['acro']
        self.ahandling = playerDic['ahandling']
        self.arc = playerDic['arc']
        self.athl = playerDic['athl'] 
        self.decep = playerDic['decep']
        self.his = playerDic['his']
        self.insight = playerDic['insight']
        self.intim = playerDic['intim']
        self.invest = playerDic['invest']
        self.med = playerDic['med'] 
        self.nature = playerDic['nature'] 
        self.percep = playerDic['percep']
        self.perf = playerDic['perf'] 
        self.persuasion = playerDic['persuasion']
        self.relig = playerDic['relig']
        self.SOH = playerDic['SOH']
        self.stealth = playerDic['stealth']
        self.survival = playerDic['survival']
        self.cbacro = playerDic['cbacro']
        self.cbahandling = playerDic['cbahandling']
        self.cbarc = playerDic['cbarc']
        self.cbathl = playerDic['cbathl'] 
        self.cbdecep = playerDic['cbdecep']
        self.cbhis = playerDic['cbhis']
        self.cbinsight = playerDic['cbinsight']
        self.cbintim = playerDic['cbintimid']
        self.cbinvest = playerDic['cbinvest']
        self.cbmed = playerDic['cbmed'] 
        self.cbnature = playerDic['cbnature'] 
        self.cbpercep = playerDic['cbpercep']
        self.cbperf = playerDic['cbperform'] 
        self.cbpersuasion = playerDic['cbpersuasion']
        self.cbrelig = playerDic['cbrelig']
        self.cbSOH = playerDic['cbSOH']
        self.cbstealh = playerDic['cbstealh']
        self.cbsurvival = playerDic['cbsurvival'] 
        self.profec = playerDic['profec']
        self.attkRowCount = playerDic['attkRowCount']
        self.level = playerDic['level']
        self.Cspells = playerDic['Cspells']
        self.spells1 = playerDic['1spells']
        self.spells2 = playerDic['2spells']
        self.spells3 = playerDic['3spells']
        self.spells4 = playerDic['4spells']
        self.spells5 = playerDic['5spells']
        self.spells6 = playerDic['6spells']
        self.spells7 = playerDic['7spells']
        self.spells8 = playerDic['8spells']
        self.charInfo = playerDic['characterInfo']



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow,Player,Attack_Ui_Dialog,Equip_Ui_Dialog,Spell_Ui_Dialog,SpellInfo_Ui_Dialog):
    def __init__(self,playerDic,parent = None):
        super(MainWindow,self).__init__(parent= parent)
        super(Attack_Ui_Dialog,self).__init__()
        super(Equip_Ui_Dialog,self).__init__()
        super(Spell_Ui_Dialog,self).__init__()
        super(SpellInfo_Ui_Dialog,self).__init__()
        Player.__init__(self,playerDic)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.diceBrowser.setReadOnly(True)
        self.loadPlayer()


        '''ACTIONS'''




        # HP
        self.ui.hpVal.returnPressed.connect(self.changeHP)


        # TEMPHP
        self.ui.temphpVal.returnPressed.connect(self.changeTempHP)

        # ATTRIBUTES
        self.ui.strVAl.returnPressed.connect(lambda: self.changeAttributes(self.ui.strVAl,"str",self.strength))
        self.ui.dexVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.dexVal,"dex",self.dex))
        self.ui.conVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.conVal,"con",self.con))
        self.ui.intVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.intVal,"int",self.int))
        self.ui.wisVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.wisVal,"wis",self.wis))
        self.ui.charVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.charVal,"char",self.char))
            #saving throws
        self.ui.ststrLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.ststrLE,"ststr",self.ststrength))
        self.ui.stdexLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.stdexLE,"stdex",self.stdex))
        self.ui.stconLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.stconLE,"stcon",self.stcon))
        self.ui.stintLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.stintLE,"stint",self.stint))
        self.ui.stwisLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.stwisLE,"stwis",self.stwis))
        self.ui.stcharLE.returnPressed.connect(lambda: self.changeAttributes(self.ui.stcharLE,"stchr",self.stchr))
            #Saving throw checkboxes
        
        self.ui.strBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.strBox,'cbstr',self.cbstrength))
        self.ui.dexBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.dexBox,'cbdex',self.cbdex))
        self.ui.intBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.intBox,'cbint',self.cbint))
        self.ui.conBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.conBox,'cbcon',self.cbcon))
        self.ui.wisBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.wisBox,'cbwis',self.cbwis))
        self.ui.charBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.charBox,'cbchr',self.cbchr))


            #SKILLS
        self.ui.acrobaticsVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.acrobaticsVal,"acro",self.acro))
        self.ui.ahandlingVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.ahandlingVal,"ahandling",self.ahandling))
        self.ui.arcanaVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.arcanaVal,"arc",self.arc))
        self.ui.athleticsVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.athleticsVal,"athl",self.athl))
        self.ui.deceptionVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.deceptionVal,"decep",self.decep))
        self.ui.historyVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.historyVal,"his",self.his))
        self.ui.insightVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.insightVal,"insight",self.insight))
        self.ui.intimidationVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.intimidationVal,"intim",self.intim))
        self.ui.investigationVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.investigationVal,"invest",self.invest))
        self.ui.medicineVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.medicineVal,"med",self.med))
        self.ui.perceptionVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.perceptionVal,"percep",self.percep))
        self.ui.religionVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.religionVal,"relig",self.relig))
        self.ui.natureVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.natureVal,"nature",self.nature))
        self.ui.persuasionVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.persuasionVal,"persuasion",self.persuasion))
        self.ui.performanceVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.performanceVal,"perf",self.perf))
        self.ui.sohVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.sohVal,"SOH",self.SOH))
        self.ui.stealthVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.stealthVal,"stealth",self.stealth))
        self.ui.survivalVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.survivalVal,"survival",self.survival))
        self.ui.levelVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.levelVal,'level',self.level))

            #AC AND PROFEC
        self.ui.profecVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.profecVal,"profec",self.profec))
        self.ui.acVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.acVal,"ac",self.ac))


            # LOWER VALUES
        self.ui.nameVal.returnPressed.connect(lambda: self.changeStringAttributes(self.ui.nameVal,'name',self.name))
        self.ui.raceVal.returnPressed.connect(lambda: self.changeStringAttributes(self.ui.raceVal,'race',self.race))
        self.ui.classVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.classVal,'clss',self.clss))
        self.ui.expVal.returnPressed.connect(lambda: self.changeAttributes(self.ui.expVal,'exp',self.exp))

                #SKILL CHECKBOXES
        self.ui.acrobaticsBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.acrobaticsBox,'cbacro',self.cbacro))
        self.ui.ahandlingBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.ahandlingBox,'cbahandling',self.cbahandling))
        self.ui.arcanaBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.arcanaBox,'cbarc',self.cbarc))
        self.ui.athleticsBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.athleticsBox,'cbathl',self.cbathl))
        self.ui.deceptionBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.deceptionBox,'cbdecep',self.cbdecep))
        self.ui.historyBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.historyBox,'cbhis',self.cbhis))
        self.ui.insightBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.insightBox,'cbinsight',self.cbinsight))
        self.ui.intimidationBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.intimidationBox,'cbintimid',self.cbintim))
        self.ui.investigationBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.investigationBox,'cbinvest',self.cbinvest))
        self.ui.medicinBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.medicinBox,'cbmed',self.cbmed))
        self.ui.natureBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.natureBox,'cbnature',self.cbnature))
        self.ui.perceptionBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.perceptionBox,'cbpercep',self.cbpercep))
        self.ui.performanceBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.performanceBox,'cbperform',self.cbperf))
        self.ui.persusasionBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.persusasionBox,'cbpersuasion',self.cbpersuasion))
        self.ui.religionBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.religionBox,'cbrelig',self.cbrelig))
        self.ui.sohBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.sohBox,'cbSOH',self.cbSOH))
        self.ui.stealthBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.stealthBox,'cbstealth',self.cbstealh))
        self.ui.survivalBox.stateChanged.connect(lambda: self.chngCheckbox(self.ui.survivalBox,'cbsurvival',self.cbsurvival))


            # attribute context menues

    



        self.ui.acrobaticsBox.installEventFilter(self)
        self.ui.ahandlingBox.installEventFilter(self)
        self.ui.arcanaBox.installEventFilter(self)
        self.ui.athleticsBox.installEventFilter(self)
        self.ui.deceptionBox.installEventFilter(self)
        self.ui.historyBox.installEventFilter(self)
        self.ui.insightBox.installEventFilter(self)
        self.ui.intimidationBox.installEventFilter(self)
        self.ui.investigationBox.installEventFilter(self)
        self.ui.medicinBox.installEventFilter(self)
        self.ui.natureBox.installEventFilter(self)
        self.ui.perceptionBox.installEventFilter(self)
        self.ui.performanceBox.installEventFilter(self)
        self.ui.persusasionBox.installEventFilter(self)
        self.ui.religionBox.installEventFilter(self)
        self.ui.sohBox.installEventFilter(self)
        self.ui.stealthBox.installEventFilter(self)
        self.ui.survivalBox.installEventFilter(self)


            # Saving Throw context menu
        self.ui.strBox.installEventFilter(self)
        self.ui.dexBox.installEventFilter(self)
        self.ui.conBox.installEventFilter(self)
        self.ui.intBox.installEventFilter(self)
        self.ui.wisBox.installEventFilter(self)
        self.ui.charBox.installEventFilter(self)


        self.ui.strLable.installEventFilter(self)
        self.ui.dexLabel.installEventFilter(self)
        self.ui.conLabel.installEventFilter(self)
        self.ui.intLabel.installEventFilter(self)
        self.ui.wisLabel.installEventFilter(self)
        self.ui.charLabel.installEventFilter(self)

        # Equip

        self.ui.equipEdit.textChanged.connect(lambda: self.saveEdit('equips',self.equips,self.ui.equipEdit.toPlainText()))
        self.ui.euipButton.clicked.connect(self.equipPopup)

        #attack
        self.ui.attkButton.clicked.connect(self.attackPopup)
        self.ui.attackView.itemChanged.connect(self.changeAttack)
        self.ui.attackView.cellClicked.connect(self.rollAttack)

        #COMMAND
        self.ui.inputBox.returnPressed.connect(self.commandInputs)

        #SPELL BUTTON
        self.ui.spellButton.pressed.connect(self.spellPopup)

        #SpellView
        self.ui.cantripView.itemPressed.connect(self.spellInfoDialogCantrip)
        self.ui.lv1View.itemPressed.connect(self.spellInfoDialog1)
        self.ui.lv2View.itemPressed.connect(self.spellInfoDialog2)
        self.ui.lv3View.itemPressed.connect(self.spellInfoDialog3)
        self.ui.lv4View.itemPressed.connect(self.spellInfoDialog4)
        self.ui.lv5View.itemPressed.connect(self.spellInfoDialog5)
        self.ui.lv6View.itemPressed.connect(self.spellInfoDialog6)
        self.ui.lv7View.itemPressed.connect(self.spellInfoDialog7)
        self.ui.lv8View.itemPressed.connect(self.spellInfoDialog1)



        self.ui.characterEdit.textChanged.connect(lambda: self.saveEdit('characterInfo',self.charInfo,self.ui.characterEdit.toPlainText()))





        self.show()
    

    def commandInputs(self):
        item = self.ui.inputBox.text()
        try:
                noSpaceItem = item.replace(" ","")
                dicePlace = 0
                while True:
                    if noSpaceItem[dicePlace] == 'd' or dicePlace == len(item):
                        break
                    else:
                        dicePlace += 1
                diceAmount = int(noSpaceItem[:dicePlace])
                diceAmountPlace = dicePlace + 1
                dicePlace +=1
                while True:
                    if dicePlace == (len(noSpaceItem)) or noSpaceItem[dicePlace] == "+":
                        break
                    else:
                        dicePlace +=1
                diceSides = int(noSpaceItem[diceAmountPlace:dicePlace])
                try:
                    diceTotal = 0
                    diceAddition = int(noSpaceItem[dicePlace+1:])
                    for i in range(diceAmount):
                        diceTotal +=  (random.randint(1,diceSides))
                    diceTotal += diceAddition
                    self.consoleOut(item + "=" + str(diceTotal))
                except:
                    diceTotal = 0
                    for i in range(diceAmount):
                        diceTotal +=  random.randint(1,diceSides)
                    self.consoleOut(item + "=" + str(diceTotal))
        except:
            if item == 'clear':
                self.ui.diceBrowser.clear()

    def addEdit(self,item):
        self.ui.equipEdit.setPlainText(str(self.ui.equipEdit.toPlainText()) + '\n' + str(item) )
    # EVENT FILTER FOR ATTRIBUTES
    def eventFilter(self,source,event):
        if event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.RightButton:
            ## ALL SKILLS
            if source == self.ui.acrobaticsBox:
                self.boxRoller(self.ui.acrobaticsBox,self.ui.acrobaticsVal,self.ui.profecVal)
            if source == self.ui.ahandlingBox:
                self.boxRoller(self.ui.ahandlingBox,self.ui.ahandlingVal,self.ui.profecVal)
            if source == self.ui.arcanaBox:
                self.boxRoller(self.ui.arcanaBox,self.ui.arcanaVal,self.ui.profecVal)
            if source == self.ui.athleticsBox:
                self.boxRoller(self.ui.athleticsBox,self.ui.athleticsVal,self.ui.profecVal)
            if source == self.ui.deceptionBox:
                self.boxRoller(self.ui.deceptionBox,self.ui.deceptionVal,self.ui.profecVal)
            if source == self.ui.historyBox:
                self.boxRoller(self.ui.historyBox,self.ui.historyVal,self.ui.profecVal)
            if source == self.ui.insightBox:
                self.boxRoller(self.ui.insightBox,self.ui.insightVal,self.ui.profecVal)
            if source == self.ui.intimidationBox:
                self.boxRoller(self.ui.intimidationBox,self.ui.intimidationVal,self.ui.profecVal)
            if source == self.ui.investigationBox:
                self.boxRoller(self.ui.investigationBox,self.ui.investigationVal,self.ui.profecVal)
            if source == self.ui.medicinBox:
                self.boxRoller(self.ui.medicinBox,self.ui.medicineVal,self.ui.profecVal)
            if source == self.ui.natureBox:
                self.boxRoller(self.ui.natureBox,self.ui.natureVal,self.ui.profecVal)
            if source == self.ui.perceptionBox:
                self.boxRoller(self.ui.perceptionBox,self.ui.perceptionVal,self.ui.profecVal)
            if source == self.ui.performanceBox:
                self.boxRoller(self.ui.performanceBox,self.ui.performanceVal,self.ui.profecVal)
            if source == self.ui.persusasionBox:
                self.boxRoller(self.ui.persusasionBox,self.ui.persuasionVal,self.ui.profecVal)
            if source == self.ui.religionBox:
                self.boxRoller(self.ui.religionBox,self.ui.religionVal,self.ui.profecVal)
            if source == self.ui.sohBox:
                self.boxRoller(self.ui.sohBox,self.ui.sohVal,self.ui.profecVal)
            if source == self.ui.stealthBox:
                self.boxRoller(self.ui.stealthBox,self.ui.stealthBox,self.ui.profecVal)
            if source == self.ui.survivalBox:
                self.boxRoller(self.ui.survivalBox,self.ui.survivalVal,self.ui.profecVal)
            if source == self.ui.strBox:
                self.boxRoller(self.ui.strBox,self.ui.ststrLE,self.ui.profecVal)
            if source == self.ui.dexBox:
                self.boxRoller(self.ui.dexBox,self.ui.stdexLE,self.ui.profecVal)
            if source == self.ui.conBox:
                self.boxRoller(self.ui.conBox,self.ui.stconLE,self.ui.profecVal)
            if source == self.ui.intBox:
                self.boxRoller(self.ui.intBox,self.ui.stintLE,self.ui.profecVal)
            if source == self.ui.wisBox:
                self.boxRoller(self.ui.wisBox,self.ui.stwisLE,self.ui.profecVal)
            if source == self.ui.charBox:
                self.boxRoller(self.ui.charBox,self.ui.stcharLE,self.ui.profecVal)
            if source == self.ui.strLable:
                self.attributeRoller(self.ui.strVAl)
            if source == self.ui.dexLabel:
                self.attributeRoller(self.ui.dexVal)
            if source == self.ui.conLabel:
                self.attributeRoller(self.ui.conVal)
            if source == self.ui.intLabel:
                self.attributeRoller(self.ui.intVal)
            if source == self.ui.wisLabel:
                self.attributeRoller(self.ui.wisVal)
            if source == self.ui.charLabel:
                self.attributeRoller(self.ui.charVal)


        return super(MainWindow,self).eventFilter(source,event)

    # ROLLER FOR BOXES
    def boxRoller(self,boxName,attributeName,profecName):
        try:
            if boxName.isChecked():
                number = int(profecName.text()) + int(attributeName.text()) + (random.randint(1,20))
                self.consoleOut(profecName.text() + "+" + attributeName.text() + "+" + "1d20= " + str(number))
            else:
                number = int(attributeName.text()) + (random.randint(1,20))
                self.consoleOut(attributeName.text() + "+" + "1d20 = " + str(number))
        except:
            self.consoleOut("INVALID INPUT")
        
    def attributeRoller(self,attributeName):
        try:
            number = int(attributeName.text()) + (random.randint(1,20))
            self.consoleOut(attributeName.text() + "+1d20 =" + str(number))
        except:
            self.consoleOut("INVALID INPUT")

    def loadPlayer(self):
        self.ui.strVAl.setText(str(self.strength))
        self.ui.dexVal.setText(str(self.dex))
        self.ui.conVal.setText(str(self.con))
        self.ui.intVal.setText(str(self.int))
        self.ui.wisVal.setText(str(self.wis))
        self.ui.charVal.setText(str(self.char))
        self.ui.hpVal.setText(str(self.hp))
        self.ui.temphpVal.setText(str(self.temphp))
        self.ui.acVal.setText(str(self.ac))
        self.ui.spdVal.setText(str(self.spd))
        self.ui.nameVal.setText(self.name)
        self.ui.classVal.setText(self.clss)
        self.ui.raceVal.setText(self.race)
        self.ui.expVal.setText(str(self.exp))
        self.ui.profecVal.setText(str(self.profec))
        self.ui.levelVal.setText(str(self.level))

        # Saving throws
        self.ui.ststrLE.setText(str(self.ststrength))
        self.ui.stdexLE.setText(str(self.stdex))
        self.ui.stconLE.setText(str(self.stcon))
        self.ui.stintLE.setText(str(self.stint))
        self.ui.stwisLE.setText(str(self.stwis))
        self.ui.stcharLE.setText(str(self.char))

            # Saving Throw Checkboxes
        self.ui.strBox.setChecked(self.cbstrength)
        self.ui.dexBox.setChecked(self.cbdex)
        self.ui.intBox.setChecked(self.cbint)
        self.ui.conBox.setChecked(self.cbcon)
        self.ui.wisBox.setChecked(self.cbwis)
        self.ui.charBox.setChecked(self.cbchr)

        #SKILLS
        self.ui.acrobaticsVal.setText(str(self.acro))
        self.ui.ahandlingVal.setText(str(self.ahandling))
        self.ui.arcanaVal.setText(str(self.arc))
        self.ui.athleticsVal.setText(str(self.athl))
        self.ui.deceptionVal.setText(str(self.decep))
        self.ui.historyVal.setText(str(self.his))
        self.ui.insightVal.setText(str(self.insight))
        self.ui.intimidationVal.setText(str(self.intim))
        self.ui.investigationVal.setText(str(self.invest))
        self.ui.medicineVal.setText(str(self.med))
        self.ui.perceptionVal.setText(str(self.percep))
        self.ui.religionVal.setText(str(self.relig))
        self.ui.natureVal.setText(str(self.nature))
        self.ui.persuasionVal.setText(str(self.persuasion))
        self.ui.performanceVal.setText(str(self.perf))
        self.ui.sohVal.setText(str(self.SOH))
        self.ui.stealthVal.setText(str(self.stealth))
        self.ui.survivalVal.setText(str(self.survival))

            #SKILL CHECKBOXES
        self.ui.acrobaticsBox.setChecked(self.cbacro)
        self.ui.ahandlingBox.setChecked(self.cbahandling)
        self.ui.arcanaBox.setChecked(self.cbarc)
        self.ui.athleticsBox.setChecked(self.cbathl)
        self.ui.deceptionBox.setChecked(self.cbdecep)
        self.ui.historyBox.setChecked(self.cbhis)
        self.ui.insightBox.setChecked(self.cbinsight)
        self.ui.intimidationBox.setChecked(self.cbintim)
        self.ui.investigationBox.setChecked(self.cbinvest)
        self.ui.medicinBox.setChecked(self.cbmed)
        self.ui.perceptionBox.setChecked(self.cbpercep)
        self.ui.religionBox.setChecked(self.cbrelig)
        self.ui.natureBox.setChecked(self.cbnature)
        self.ui.persusasionBox.setChecked(self.cbpersuasion)
        self.ui.performanceBox.setChecked(self.cbperf)
        self.ui.sohBox.setChecked(self.cbSOH)
        self.ui.stealthBox.setChecked(self.cbstealh)
        self.ui.survivalBox.setChecked(self.cbsurvival)



        #Equip Editor
        self.ui.equipEdit.setPlainText(self.equips)

        #ATTACK POPULATOR
        self.populateAttacks(self.attks)

        #SPELL POPULATOR
        self.populateSpells()

        #CHAR EDITOR
        self.ui.characterEdit.setPlainText(self.charInfo)


    """ATTACK POPUP"""
    def attackPopup(self):
        popup = attackDialogClass(self)
        popup.attackDialog.addattkButton.clicked.connect(lambda: self.addAttk(popup.attackDialog.attkName.text(),popup.attackDialog.attkRTH.text(),popup.attackDialog.attkDR.text()))
    
        popup.attackDialog.addattkButton.released.connect(popup.accept)
        popup.exec()

    def addAttk(self,attkname,attkRTH,attkDMG):
        self.attkRowCount = len(self.attks)
        self.attkRowCount += 1
        self.attks.append([attkname,attkDMG,attkRTH])
        self.savePlayer('attkRowCount',self.attkRowCount)
        self.savePlayer('attks',self.attks)
        self.ui.attackView.setRowCount(self.attkRowCount)
        self.ui.attackView.setItem(self.attkRowCount-1,0,QTableWidgetItem(attkname))
        self.ui.attackView.setItem(self.attkRowCount-1,1,QTableWidgetItem(attkRTH))
        self.ui.attackView.setItem(self.attkRowCount-1,2,QTableWidgetItem(attkDMG))

    def populateAttacks(self,attkList):
        self.ui.attackView.setRowCount(self.attkRowCount)
        for i in range(len(attkList)):
            self.ui.attackView.setItem(i,0,QTableWidgetItem(attkList[i][0]))
            self.ui.attackView.setItem(i,1,QTableWidgetItem(attkList[i][1]))
            self.ui.attackView.setItem(i,2,QTableWidgetItem(attkList[i][2]))
    def changeAttack(self,item):
        row = item.row()
        column = item.column()
        if item.text() == "delete" or item.text() == 'd' or item.text() == 'Delete':
            self.ui.attackView.removeRow(row)
            self.attks.pop(row)
            self.attkRowCount -= 1
            self.savePlayer('attkRowCount',self.attkRowCount)
            self.savePlayer('attks',self.attks)
        else:
            self.attks[row][column] = item.text()
            self.savePlayer('attks',self.attks)

    def rollAttack(self,row,column):
        try:
            Tableitem = self.ui.attackView.item(row,column)
            item = Tableitem.text()
            if (column == 1 or column == 2) and row != 0:
                noSpaceItem = item.replace(" ","")
                dicePlace = 0
                while True:
                    if noSpaceItem[dicePlace] == 'd' or dicePlace == len(item):
                        break
                    else:
                        dicePlace += 1
                diceAmount = int(noSpaceItem[:dicePlace])
                diceAmountPlace = dicePlace + 1
                dicePlace +=1
                while True:
                    if dicePlace == (len(noSpaceItem)) or noSpaceItem[dicePlace] == "+":
                        break
                    else:
                        dicePlace +=1
                diceSides = int(noSpaceItem[diceAmountPlace:dicePlace])
                try:
                    diceTotal = 0
                    diceAddition = int(noSpaceItem[dicePlace+1:])
                    for i in range(diceAmount):
                        diceTotal +=  (random.randint(1,diceSides))
                    diceTotal += diceAddition
                    self.consoleOut(item + "=" + str(diceTotal))
                except:
                    diceTotal = 0
                    for i in range(diceAmount):
                        diceTotal +=  (random.randint(1,diceSides))
                    self.consoleOut(item + "=" + str(diceTotal))        
        except:
            self.consoleOut("INVALID DICE INPUT")
                


    """EQUIP POPUP"""
    
    def equipPopup(self):
        popupEquip = equipDialogClass(self)
        popupEquip.equipDialog.addattkButton.clicked.connect(lambda: self.addEdit(popupEquip.equipDialog.equipName.text()))
        popupEquip.equipDialog.addattkButton.released.connect(popupEquip.accept)
        popupEquip.exec()




            
    """SPELL POPUP"""
    def spellPopup(self):
        popupSpell = spellDialogClass(self)
        uiDialogRef = popupSpell.spellDialog
        popupSpell.spellDialog.addSpellButton.clicked.connect(lambda: self.addSpell(uiDialogRef.spellNmVal.text(),uiDialogRef.spellRngVal.text(),uiDialogRef.spellDescVal.toPlainText(),uiDialogRef.spellDamVal.text(),uiDialogRef.spellHiRollVal.text(),uiDialogRef.spellCstTmeVal.text(),uiDialogRef.spellLVVal.text()))
        popupSpell.spellDialog.addSpellButton.released.connect(popupSpell.accept)
        popupSpell.exec()

    def addSpell(self,name,range,desc,damage,hileveldamage,castTime,level):
        spellString = name
        if level == 'cantrip' or level == 'Cantrip':
            self.Cspells[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('Cspells',self.Cspells)
            self.ui.cantripView.addItem((spellString))
        if level == '1':
            self.spells1[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('1spells',self.spells1)
            self.ui.lv1View.addItem(spellString)
        if level == '2':
            self.spells2[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('2spells',self.spells2)
            self.ui.lv2View.addItem((spellString))
        if level == '3':
            self.spells3[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('3spells',self.spells3)
            self.ui.lv3View.addItem((spellString))
        if level == '4':
            self.spell4[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('4spells',self.spell4)
            self.ui.lv4View.addItem((spellString))
        if level == '5':
            self.spells5[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('5spells',self.spells5)
            self.ui.lv5View.addItem((spellString))
        if level == '6':
            self.spells6[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('6spells',self.spells6)
            self.ui.lv6View.addItem((spellString))
        if level == '7':
            self.spells7[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('7spells',self.spells7)
            self.ui.lv7View.addItem((spellString))
        if level == '8':
            self.spells8[name]=[name,range,desc,damage,hileveldamage,castTime,level]
            self.savePlayer('8spells',self.spells8)
            self.ui.lv8View.addItem((spellString))
    
    
    
    
    def spellInfoDialogCantrip(self,item):
        self.spellInfoDialog(item,self.Cspells,'Cspells',self.ui.cantripView)
    def spellInfoDialog1(self,item):
        self.spellInfoDialog(item,self.spells1,'1spells',self.ui.lv1View)
    def spellInfoDialog2(self,item):
        self.spellInfoDialog(item,self.spells2,'2spells',self.ui.lv2View)
    def spellInfoDialog3(self,item):
        self.spellInfoDialog(item,self.spells3,'3spells',self.ui.lv3View)
    def spellInfoDialog4(self,item):
        self.spellInfoDialog(item,self.spells4,'4spells',self.ui.lv4View)
    def spellInfoDialog5(self,item):
        self.spellInfoDialog(item,self.spells5,'5spells',self.ui.lv5View)
    def spellInfoDialog6(self,item):
        self.spellInfoDialog(item,self.spells6,'6spells',self.ui.lv6View)
    def spellInfoDialog7(self,item):
        self.spellInfoDialog(item,self.spells7,'7spells',self.ui.lv7View)
    def spellInfoDialog8(self,item):
        self.spellInfoDialog(item,self.spells8,'8spells',self.ui.lv8View)
        
    
    
    
    
    def spellInfoDialog(self,item,varRef,jsonRef,uiRef):
        spellName = item.text()
        spellPopup = spellInfoDialogClass()
        spellPopup.spellDialog.addSpellButton.setText("Roll?")
        spellPopup.spellDialog.addSpellALabel.setText(varRef[spellName][0])
        spellPopup.spellDialog.spellNmVal.setHidden(True)
        spellPopup.spellDialog.spellRngVal.setText("RANGE: " + varRef[spellName][1])
        spellPopup.spellDialog.spellDescVal.setPlainText("DESCRIPTION: \n" + varRef[spellName][2])
        spellPopup.spellDialog.spellDamVal.setText( varRef[spellName][3])
        spellPopup.spellDialog.spellHiRollVal.setText(varRef[spellName][4])
        spellPopup.spellDialog.spellCstTmeVal.setText("CAST TIME: " + varRef[spellName][5])
        spellPopup.spellDialog.spellLVVal.setText("LEVEL: "+ varRef[spellName][6])

        #HIDE DAMAGE IF NONE
        spellPopup.spellDialog.spellRngVal.returnPressed.connect(lambda: self.saveSpellPopup(jsonRef,1,spellName,varRef[spellName][1],spellPopup.spellDialog.spellRngVal.text()))
        spellPopup.spellDialog.spellDescVal.textChanged.connect(lambda: self.saveSpellPopup(jsonRef,2,spellName,varRef[spellName][2],spellPopup.spellDialog.spellDescVal.toPlainText()))
        spellPopup.spellDialog.spellDamVal.returnPressed.connect(lambda: self.saveSpellPopup(jsonRef,3,spellName,varRef[spellName][3],spellPopup.spellDialog.spellDamVal.text()))
        spellPopup.spellDialog.spellHiRollVal.returnPressed.connect(lambda: self.saveSpellPopup(jsonRef,4,spellName,varRef[spellName][4],spellPopup.spellDialog.spellHiRollVal.text()))
        spellPopup.spellDialog.spellCstTmeVal.returnPressed.connect(lambda: self.saveSpellPopup(jsonRef,5,spellName,varRef[spellName][5],spellPopup.spellDialog.spellCstTmeVal.text()))
        spellPopup.spellDialog.spellLVVal.returnPressed.connect(lambda: self.saveSpellPopup(jsonRef,6,spellName,varRef[spellName][6],spellPopup.spellDialog.spellLVVal.text()))

        spellPopup.spellDialog.deleteButton.pressed.connect(lambda: self.spellDelete(item,uiRef,spellName,varRef,jsonRef))
        spellPopup.spellDialog.deleteButton.released.connect(spellPopup.accept)

        spellPopup.spellDialog.addSpellButton.pressed.connect(lambda: spellRoller(varRef[spellName][3],varRef[spellName][4],spellPopup.spellDialog.spellHIRollSpellLE.text()))


        def spellRoller(damageRoll,hilvAddition,hilvtimes):
            noSpaceItem = damageRoll.replace(" ","")
            noSpaceHigherLevel = hilvAddition.replace(" ","")
            try:
                diceTotal = 0
                diceTotalAddition = 0
                dicePlace = 0
                while True:
                    if noSpaceItem[dicePlace] == 'd' or dicePlace == len(damageRoll):
                        break
                    else:
                        dicePlace += 1
                diceAmount = int(noSpaceItem[:dicePlace])
                diceAmountPlace = dicePlace + 1
                dicePlace +=1
                while True:
                    if dicePlace == (len(noSpaceItem)) or noSpaceItem[dicePlace] == "+":
                        break
                    else:
                        dicePlace +=1
                diceSides = int(noSpaceItem[diceAmountPlace:dicePlace])
                try:
                    diceTotal = 0
                    diceAddition = int(noSpaceItem[dicePlace+1:])
                    for i in range(diceAmount):
                        diceTotal +=  (random.randint(1,diceSides))
                    diceTotal += diceAddition
                except:
                    diceTotal = 0
                    for i in range(diceAmount):
                        diceTotal +=  (random.randint(1,diceSides))
                #HIGHER LEVEL
                if hilvAddition != "0" or hilvAddition != "" or hilvAddition != "HIGHER LEVEL UP?(0 for casting at same level)":
                    try:
                        for i in range(int(hilvtimes)):
                            noSpaceHigherLevel = hilvAddition.replace(" ","")
                            dicePlace = 0
                            while True:
                                if noSpaceHigherLevel[dicePlace] == 'd' or dicePlace == len(hilvAddition):
                                    break
                                else:
                                    dicePlace += 1
                            diceAmount = int(noSpaceHigherLevel[:dicePlace])
                            diceAmountPlace = dicePlace + 1
                            dicePlace +=1

                            diceTotalAddition = 0
                            for i in range(int(hilvtimes)):
                                for i in range(diceAmount):
                                    diceTotalAddition +=  (random.randint(1,diceSides))
                            spellPopup.spellDialog.rollLabel.setText(noSpaceItem + "+"+ "("+ noSpaceHigherLevel+")"+str(hilvtimes)+ "=" + str(diceTotalAddition + diceTotal))
                            
                    except:
                        spellPopup.spellDialog.rollLabel.setText(noSpaceItem + "=" +str(diceTotal))
                else:
                    spellPopup.spellDialog.rollLabel.setText(noSpaceItem + "=" +str(diceTotal))
            except:
                spellPopup.spellDialog.rollLabel.setText("INVALID ENTRY")



                        
        #except:
            self.consoleOut("INVALID DICE INPUT")



        spellPopup.exec()

    def saveSpellPopup(self,jsonSpellLevel,category,name,varRef,newVal):
        varRef = newVal
        playerDic[jsonSpellLevel][name][category] = varRef
        with open('D:\\pyqtProjects\\real\\playerStats.json',"w") as jsonfile:
            json.dump(playerDic,jsonfile)

    def spellDelete(self,item,uiReference,name,varRef,jsonSpellLevel):
        row = uiReference.row(item)
        uiReference.takeItem(row)
        varRef.pop(name)
        playerDic[jsonSpellLevel] = varRef
        with open('D:\\pyqtProjects\\real\\playerStats.json',"w") as jsonfile:
            json.dump(playerDic,jsonfile)

    def populateSpells(self):
        for key in self.Cspells:
            self.ui.cantripView.addItem(key)
        for key in self.spells1:
            self.ui.lv1View.addItem(key)
        for key in self.spells2:
            self.ui.lv2View.addItem(key)
        for key in self.spells3:
            self.ui.lv3View.addItem(key)
        for key in self.spells4:
            self.ui.lv4View.addItem(key)
        for key in self.spells5:
            self.ui.lv5View.addItem(key)
        for key in self.spells6:
            self.ui.lv6View.addItem(key)
        for key in self.spells7:
            self.ui.lv7View.addItem(key)
        for key in self.spells8:
            self.ui.lv8View.addItem(key)





    
        

        

    

    '''JSON SAVER'''
    def savePlayer(self,jsonReference,classReference):
        playerDic[str(jsonReference)] = classReference
        with open('D:\\pyqtProjects\\real\\playerStats.json',"w") as jsonfile:
            json.dump(playerDic,jsonfile)

    def saveEdit(self,jsonReference,classReference,value):
        classReference = value
        playerDic[str(jsonReference)] = classReference
        with open('D:\\pyqtProjects\\real\\playerStats.json',"w") as jsonfile:
            json.dump(playerDic,jsonfile)



    """CONSOLE OUT"""
    def consoleOut(self,input):
        self.ui.diceBrowser.append(input + "\n--------------")

    """HP METHOD"""
    def changeHP(self):
        try:
            if str(self.ui.hpVal.text())[0] == "-":
                self.hp += int(self.ui.hpVal.text())
                self.ui.hpVal.setText(str(self.hp))
                self.consoleOut("SUBTRACTION SUCCESSFUL") 
            else:
                self.hp = int(self.ui.hpVal.text())
                self.ui.hpVal.setText(str(self.hp))
                self.consoleOut("HP SET")
            self.savePlayer('hp',self.hp)
        except:
            self.ui.hpVal.setText(str(self.hp))
            self.consoleOut("INVALID INPUT")


    """TEMP HP METHOD"""
    def changeTempHP(self):
        try:
            if str(self.ui.temphpVal.text())[0] == "-":
                if self.temphp == 0 or self.temphp < 0:
                    self.consoleOut("TEMP HP ALREADY 0")
                else:
                    self.temphp += int(self.ui.temphpVal.text()) 
                    self.ui.temphpVal.setText(str(self.temphp))
                    self.savePlayer('temphp',self.temphp)
                    self.consoleOut("TEMP HP SET")
            else:
                self.temphp = int(self.ui.temphpVal.text())
                self.ui.temphpVal.setText(str(self.temphp))
                self.savePlayer('temphp',self.temphp)
                self.consoleOut("TEMP HP SET")
        except:
            self.ui.temphpVal.setText(str(self.temphp))
            self.consoleOut("INVALID TEMP HP")

    """ATTRIBUTE METHOD"""
    def changeAttributes(self,guiReference,jsonReference,classReference):
        try:
            classReference = int(guiReference.text())
            guiReference.setText(str(classReference))
            self.savePlayer(jsonReference,classReference)
            self.consoleOut(jsonReference + " OF " + str(classReference) + " SET")
        except:
            classReference = playerDic[jsonReference]
            guiReference.setText(str(classReference))
            self.consoleOut("INVALID VALUE")


    def changeStringAttributes(self,guiReference,jsonReference,classReference):
        try:
            classReference = guiReference.text()
            guiReference.setText(str(classReference))
            self.savePlayer(jsonReference,classReference)
            self.consoleOut(jsonReference + " OF " + str(classReference) + " SET")
        except:
            classReference = playerDic[jsonReference]
            guiReference.setText(str(classReference))
            self.consoleOut("INVALID VALUE")

        # ATTRIBUTE CHECKBOX METHOD

    def chngCheckbox(self,guiReference,jsonReference,classReference):
        classReference = guiReference.isChecked()
        self.savePlayer(jsonReference,classReference)
        self.consoleOut(jsonReference + " " + str(classReference) + " " + "SET")



        

class attackDialogClass(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.attackDialog = Attack_Ui_Dialog()
        self.attackDialog.setupUi(self)

class equipDialogClass(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.equipDialog = Equip_Ui_Dialog()
        self.equipDialog.setupUi(self)

class spellDialogClass(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.spellDialog = Spell_Ui_Dialog()
        self.spellDialog.setupUi(self)

class spellInfoDialogClass(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.spellDialog = SpellInfo_Ui_Dialog()
        self.spellDialog.setupUi(self)












            




        



    








        


if __name__ == "__main__":
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        print("USING HIGH DPI SCALING")
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        print("USING HIGH DPI PIXMAPS")
    

    with open('D:\\pyqtProjects\\real\\playerStats.json') as json_file:
            playerDic = json.load(json_file)
    

    app = QtWidgets.QApplication(sys.argv)
    dir_ = QtCore.QDir("clacon")
    _id = QtGui.QFontDatabase.addApplicationFont("fonts\\clacon2.ttf")
    print(QtGui.QFontDatabase.applicationFontFamilies(_id))
    app.setFont(QFont('Classic Console Neue'))
    w = MainWindow(playerDic)
    w.show()
    sys.exit(app.exec_())