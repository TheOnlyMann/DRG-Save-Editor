# functions that act as slots, attached to UI elements
from sys import platform

import PySide2
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtCore import QFile, QIODevice, Slot
from PySide2.QtGui import QColor, QCursor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QAction, QApplication, QFileDialog, QLineEdit,
                               QListWidgetItem, QMenu, QPlainTextEdit,
                               QTreeWidgetItem, QWidget)

from main.python.app.ui import UI_Singleton
from main.python.data.xp import XP
from main.python.save_reader import Reader_Singleton

if platform == "win32":
    import winreg

def ConnectSlots() -> None:
    # connect file opening function to menu item
    UI_Singleton.widget.actionOpen_Save_File.triggered.connect(open_file)
    # set column names for overclock treeview
    UI_Singleton.widget.overclock_tree.setHeaderLabels(["Overclock", "Status", "GUID"])

    # connect functions to buttons and menu items
    UI_Singleton.widget.actionSave_changes.triggered.connect(save_changes)
    UI_Singleton.widget.actionSet_All_Classes_to_25.triggered.connect(set_all_25)
    UI_Singleton.widget.actionAdd_overclock_crafting_materials.triggered.connect(add_crafting_mats)
    UI_Singleton.widget.actionReset_to_original_values.triggered.connect(reset_values)
    UI_Singleton.widget.combo_oc_filter.currentTextChanged.connect(filter_overclocks)
    UI_Singleton.widget.add_cores_button.clicked.connect(add_cores)
    UI_Singleton.widget.remove_all_ocs.clicked.connect(remove_all_ocs)
    UI_Singleton.widget.remove_selected_ocs.clicked.connect(remove_selected_ocs)
    UI_Singleton.widget.driller_promo_box.currentIndexChanged.connect(update_rank)
    UI_Singleton.widget.engineer_promo_box.currentIndexChanged.connect(update_rank)
    UI_Singleton.widget.gunner_promo_box.currentIndexChanged.connect(update_rank)
    UI_Singleton.widget.scout_promo_box.currentIndexChanged.connect(update_rank)

def get_steam_path() -> str:
    steam_path:str
    try:
        # find the install path for the steam version
        if platform == "win32":
            steam_reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam") # type: ignore
            steam_path = str(winreg.QueryValueEx(steam_reg, "SteamPath")[0]) # type: ignore
            steam_path += "/steamapps/common/Deep Rock Galactic/FSD/Saved/SaveGames"
        else:
            steam_path = "."
    except:
        steam_path = "."
        
    return steam_path

@Slot() # type: ignore
def open_file():
    filename:str = str(QFileDialog.getOpenFileName(
        None,
        "Open Save File...",
        get_steam_path(),
        "Player Save Files (*.sav);;All Files (*.*)",
    )[0])
    
    UI_Singleton.widget.setWindowTitle(f"DRG Save Editor - {filename}")  # window-dressing
    
    # make a backup of the save file in case of weirdness or bugs
    with open(f"{filename}.old", "wb") as backup:
        with open(filename, "rb") as f:
            backup.write(f.read())
       
    # initialize the reader and populate the text fields
    Reader_Singleton.read(filename)
    UI_Singleton.refresh_fields()
    update_rank()

    
    
    # TODO: finish when weaponoc data module is created
    # parse save file and categorize weapon overclocks
    
    # clear and initialize overclock tree view
    
    # populate list of unforged ocs
    
    ...

@Slot() # type: ignore
def filter_overclocks() -> None:
    item_filter = UI_Singleton.widget.combo_oc_filter.currentText()
    # forged_ocs, unacquired_ocs, unforged_ocs = get_overclocks(save_data, guid_dict)
    # print(item_filter)
    tree = UI_Singleton.widget.overclock_tree
    tree_root = tree.invisibleRootItem()

    for i in range(tree_root.childCount()):
        # print(tree_root.child(i).text(0))
        dwarf = tree_root.child(i)
        for j in range(dwarf.childCount()):
            weapon = dwarf.child(j)
            # print(f'\t{weapon.text(0)}')
            for k in range(weapon.childCount()):
                oc = weapon.child(k)
                # print(f'\t\t{oc.text(0)}')
                if oc.text(1) == item_filter or item_filter == "All":
                    oc.setHidden(False)
                else:
                    oc.setHidden(True)

@Slot() # type: ignore
def add_cores() -> None:
    # TODO: Implement when weapon OC module is made
    ...
    
@Slot() # type: ignore
def save_changes() -> None:
    # TODO: Implement when weapon OC module is made
    ...

@Slot() # type: ignore
def set_all_25() -> None:
    # TODO: implement after expanding functionality of xp module
    XP.update_xp("driller", 315000)
    XP.update_xp("engineer", 315000)
    XP.update_xp("gunner", 315000)
    XP.update_xp("scout", 315000)
    
    UI_Singleton.update_xp_fields()

    ...
    
@Slot() # type: ignore
def reset_values() -> None:
    Reader_Singleton.restore_from_backup()
    UI_Singleton.update_fields()
    
@Slot() # type: ignore
def add_crafting_mats() -> None:
    # TODO: implement after adding weapon OC module and expanding resources data module
    ...
    
@Slot() # type: ignore
def remove_selected_ocs() -> None:
    # TODO: implement after adding weapon oc module
    ...
    
@Slot() # type: ignore
def remove_all_ocs() -> None:
    # TODO: implement after adding weapon oc module
    ...

def update_rank():
    XP.update_promos(
        scout_index = UI_Singleton.scout_promo_box.currendIndex(),
        engineer_index = UI_Singleton.engineer_promo_box.currendIndex(),
        gunner_index = UI_Singleton.gunner_promo_box.currendIndex(),
        driller_index = UI_Singleton.driller_promo_box.currendIndex(),
    )
    
    UI_Singleton.widget.classes_group.setTitle(XP.get_rank_title())
    
    ...