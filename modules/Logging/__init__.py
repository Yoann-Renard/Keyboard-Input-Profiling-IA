from os import stat

from .logger import *
from .writer import *

from modules.Settings import WRITER_FILE

if stat(WRITER_FILE).st_size == 0:
    with open(WRITER_FILE, 'a') as f:
        f.write("character_chain, intervals\n")
        f.close()
