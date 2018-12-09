import subprocess
import requests
import json
import time

import os
import time
import uuid
import logging
import subprocess
from distutils.spawn import find_executable


logger = logging.getLogger(__name__)


class NgrokTunnel:

    def __init__(self):

        assert find_executable("ngrok"), "ngrok command must be installed, see https://ngrok.com/"

    def start(self):
        """
        :return: the tunnel URL which is now publicly open for your localhost port
        """

        logger.debug("Starting ngrok tunnel")

        self.p = subprocess.Popen(["ngrok","http", "8000"], stdout=subprocess.PIPE)

        time.sleep(3)
        localhost_url = "http://localhost:4040/api/tunnels"
        tunnel_url = requests.get(localhost_url).text
        j = json.loads(tunnel_url)

        tunnel_url = j['tunnels'][1]['public_url']
        return tunnel_url

    def stop(self):
        self.p.kill()
        print("ngrok dies")




if __name__ == "__main__":
    ngrok = NgrokTunnel()
    print(ngrok.start())
    time.sleep(10)
