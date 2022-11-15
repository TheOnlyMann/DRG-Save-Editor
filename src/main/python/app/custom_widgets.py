
import PySide2
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtCore import QFile, QIODevice, Slot
from PySide2.QtGui import QColor, QCursor, QFocusEvent
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (QAction, QApplication, QFileDialog, QLineEdit,
                               QListWidgetItem, QMenu, QPlainTextEdit,
                               QTreeWidgetItem, QWidget)
from main.python.app.ui import UI_Singleton


class TextEditFocusChecking(QLineEdit):
    """
    Custom single-line text box to allow for event-driven updating of XP totals
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def focusOutEvent(self, e: QFocusEvent) -> None:
        from main.python.data.xp import XP_TABLE
        # check for blank text
        box = self.objectName()
        if self.text() == "":
            return super().focusOutEvent(e)
        season = False
        value = int(self.text())

        if box.startswith("driller"):
            dwarf = "driller"
        elif box.startswith("engineer"):
            dwarf = "engineer"
        elif box.startswith("gunner"):
            dwarf = "gunner"
        elif box.startswith("scout"):
            dwarf = "scout"
        elif box.startswith("season"):
            season = True
        else:
            print("abandon all hope, ye who see this message")
            return super().focusOutEvent(e)
        # print(dwarf)

        if season:
            if box.endswith("xp"):
                if value >= 5000:
                    UI_Singleton.widget.season_xp.setText("4999")
                elif value < 0:
                    UI_Singleton.widget.season_xp.setText("0")
            elif box.endswith("lvl_text"):
                if value < 0:
                    UI_Singleton.widget.season_lvl_text.setText("0")
                elif value > 100:
                    UI_Singleton.widget.season_lvl_text.setText("100")
                    UI_Singleton.widget.season_xp_.setText("0")
        else:
            # decide/calculate how to update based on which box was changed
            if box.endswith("xp"):  # total xp box changed
                # print('main xp')
                total = value
            elif box.endswith("text"):  # dwarf level box changed
                # print('level xp')
                xp, level, rem = UI_Singleton.get_dwarf_xp(dwarf)
                if XP_TABLE[value - 1] + rem == xp:
                    total = xp
                else:
                    total = XP_TABLE[value - 1]
            elif box.endswith("2"):  # xp for current level changed
                xp, level, rem = UI_Singleton.get_dwarf_xp(dwarf)
                total = XP_TABLE[level - 1] + value

            UI_Singleton.update_xp_fields(dwarf, total)  # update relevant xp fields

        return super().focusOutEvent(e)  # call any other stuff that might happen (?)
