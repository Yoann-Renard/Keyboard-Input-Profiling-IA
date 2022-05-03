import logging

from modules.Settings import WRITER_FILEMODE, WRITER_FORMAT, WRITER_FILE

writer = logging.getLogger("writer")

writer_handler = logging.FileHandler(filename=WRITER_FILE, mode=WRITER_FILEMODE)
writer_handler.setFormatter(logging.Formatter(WRITER_FORMAT))
writer.addHandler(writer_handler)