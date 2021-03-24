import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)핸들러란 내가 로깅한 정보가 출력되는 위치 설정하는 것


fh = logging.FileHandler(filename="run.log")
# fh.setLevel(logging.INFO)logging.FileHandler 클래스를 통해 객체를 만들어서 나의 로거에 추가

logger.addHandler(ch)
logger.addHandler(fh)

logger.critical("critical.")
logger.error("error.")
logger.warning("warning.")
logger.info("info.")
logger.debug("debug.")