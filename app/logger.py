import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)