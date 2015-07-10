from version import VERSION

# BrowserMob imports
from browsermobproxy import Server

class BrowserMobLibrary():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        self.isServerStarted = False
        self.activeProxy = None
        self.server = None
        self.proxies = []

    def _proxy(self):
        if self.activeProxy is None:
            raise Exception("No proxy has been created")
        return self.activeProxy

    def start_browsermob(self, browsermob_path):
        self.server = Server(browsermob_path)
        self.server.start()
        self.isServerStarted = True

    def stop_browsermob(self):
        self.server.stop()
        self.server = None
        self.isServerStarted = False

    def create_proxy(self):
        self.activeProxy = self.server.create_proxy
        self.proxies.append(self.activeProxy)
        return self.server.create_proxy()

    def close_proxy(self, proxy):
        self.proxies.remove(proxy)
        proxy.close()

    def close_active_proxy(self):
        self.close_proxy(self.activeProxy)

    def set_active_proxy(self, proxy):
        self.activeProxy = proxy

    def get_active_proxy(self):
        return self.activeProxy

    def get_all_proxies(self):
        return self.proxies

    def close_all_proxies(self):
        for proxy in self.proxies:
            proxy.close()

    def capture_traffic(self, reference=None, **options):
        return self._proxy().new_har(reference, options)

    def get_captured_traffic(self):
        return self._proxy().har

    def set_capture_reference(self, reference=None):
        return self._proxy().new_page(reference)

    def ignore_all_traffic_matching(self, regexp, status_code):
        return self._proxy().blacklist(regexp, status_code)

    def only_capture_traffic_matching(self, regexp, status_code):
        return self._proxy().whitelist(regexp, status_code)

    def use_basic_authentication(self, domain, username, password):
        return self._proxy().basic_authentication(domain, username, password)

    def set_headers(self, headers, ):
        return self._proxy().headers(headers)

    def set_response_interceptor(self, js, ):
        return self._proxy().response_interceptor(js)

    def set_request_interceptor(self, js, ):
        return self._proxy().request_interceptor(js)

    def set_bandwith_limits(self, **options):
        return self._proxy().limits(options)

    def set_proxy_timeouts(self, **options):
        return self._proxy().timeouts(options)

    def remap_hosts(self, address, ip_address):
        return self._proxy().remap_hosts(address, ip_address)

    def wait_for_traffic_to_stop(self, quiet_period, timeout):
        return self._proxy().wait_for_traffic_to_stop(quiet_period, timeout)

    def clear_proxy_dns_cache(self):
        return self._proxy().clear_dns_cache()

    def rewrite_url(self, match, replace):
        return self._proxy().rewrite_url(match, replace)
