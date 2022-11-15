# handles all the data used by the application, called by main

import sys

from main.python.app.ui import UI_Singleton
from main.python.app.slots import ConnectSlots

class Application:
    def __init__(
        self,
    ) -> None:
        # initialize the app
        self.ui = UI_Singleton
        
        # connect slots 
        ConnectSlots()
        
        
        pass