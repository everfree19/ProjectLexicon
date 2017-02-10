import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'GODHAND'
#HOME_PAGE = 'http://creativeworks.tistory.com'
HOME_PAGE = 'http://www.mk.co.kr'
DOMAIN_NAME = get_site_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + 'crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)