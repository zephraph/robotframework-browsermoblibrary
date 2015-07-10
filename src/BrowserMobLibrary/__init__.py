from version import VERSION

# BrowserMob imports
from browsermobproxy import Server

class BrowserMobLibrary():

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = VERSION

	def __init__(self):
		self.isServerStarted = False

	def start_browsermob(self, browsermob_path):
		self.server = Server(browsermob_path)
		self.server.start()
		self.isServerStarted = True

	def stop_browsermob(self):
		self.server.stop()
		self.server = None
		self.isServerStarted = False

	def create_proxy(self):
		return self.server.create_proxy()
