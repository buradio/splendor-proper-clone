from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Roy\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Roy\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6"

setup(
    name = "Splendor" ,
    options = {"build_exe":{"packages":["pygame"],
                           "include_files":['board.py','button.py','control.py',
                                       'data.py','drawboard.py','endgame.py','gamelogic.py',
                                       'gameplay.py','menu.py','objects.py','asset/','cardslist/']}
              },
    version = "0.01a" ,
    description = "this is our first game by burad.io team" ,
    executables = [Executable("main.py")] ,
    ) 
