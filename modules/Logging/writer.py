import logging

from modules.Settings import WRITER_FILEMODE, WRITER_FORMAT, WRITER_FILE, WRITER_LEVEL

writer = logging.getLogger("writer")

writer_handler = logging.FileHandler(filename=WRITER_FILE, mode=WRITER_FILEMODE)
writer_handler.setFormatter(logging.Formatter(WRITER_FORMAT))
writer.setLevel(level=WRITER_LEVEL)
writer.addHandler(writer_handler)
