"""
A simple HandlerClass for getting raw data the Hex API serves up
"""

import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from HexAPI import HexAPI

class HexHandler(BaseHTTPRequestHandler):
    def handle_request(self):
        try:
            self.send_response(200)
            self.end_headers()
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        #f = open('apioutput.txt', 'a')
        #f.write("%s\n"%post_body)
        #f.close()
        HexAPI().newCall(post_body)

def main():
    PORT = 1234
    try:
        server = HTTPServer(('', PORT), HexHandler)
        print 'started httpserver on port %s...'%PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print 'received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
