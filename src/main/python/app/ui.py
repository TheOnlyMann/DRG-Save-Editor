# handles the UI for the application
import sys
import PySide2
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtCore import QFile, QIODevice, Slot
from PySide2.QtGui import QColor, QCursor, QFocusEvent
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QAction, QApplication, QFileDialog, QLineEdit,
                               QListWidgetItem, QMenu, QPlainTextEdit,
                               QTreeWidgetItem, QWidget)
from main.python.app.custom_widgets import TextEditFocusChecking
from main.python.data.xp import XP

from main.python.save_reader import Reader_Singleton

class __UI:
    def __init__(self) -> None:
        self.appctext: ApplicationContext 
        self.widget: QWidget
        
        # specify and open the UI
        ui_file_name:str = "editor.ui"
        self.appctext = ApplicationContext()
        ui_file: QFile = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
            
        # load the UI and do a basic check
        loader: QUiLoader = QUiLoader()
        loader.registerCustomWidget(TextEditFocusChecking)
        self.widget = loader.load(ui_file, None)
        ui_file.close()
        if not self.widget:
            print(loader.errorString())
            sys.exit(-1)
        
        # populate fields
        self.__populate_fields()
        
    def __populate_fields(self) -> None:
        ...
        
    def update_fields(self) -> None:
        self.update_xp_fields()
        ...
        
    def update_xp_fields(self) -> None:
        # updates the xp fields for all dwarfs
        driller = XP.get_xp("driller")
        engineer = XP.get_xp("engineer")
        gunner = XP.get_xp("gunner")
        scout = XP.get_xp("scout")
        
        total, level, remainder = driller if driller else (0,0,0)
        self.widget.driller_xp.setText(str(total))
        self.widget.driller_lvl_text.setText(str(level))
        self.widget.driller_xp_2.setText(str(remainder))
        
        total, level, remainder = engineer if engineer else (0,0,0)
        self.widget.engineer_xp.setText(str(total))
        self.widget.engineer_lvl_text.setText(str(level))
        self.widget.engineer_xp_2.setText(str(remainder))
        
        total, level, remainder = gunner if gunner else (0,0,0)
        self.widget.gunner_xp.setText(str(total))
        self.widget.gunner_lvl_text.setText(str(level))
        self.widget.gunner_xp_2.setText(str(remainder))
        
        total, level, remainder = scout if scout else (0,0,0)
        self.widget.scout_xp.setText(str(total))
        self.widget.scout_lvl_text.setText(str(level))
        self.widget.scout_xp_2.setText(str(remainder))

        self.widget.classes_group.setTitle(XP.get_rank_title())
        ...
    
UI_Singleton:__UI = __UI()
