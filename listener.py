import SimpleHTTPServer
import SocketServer
import string,cgi,time
import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from decklist import deckFormater

class MyHandler(BaseHTTPRequestHandler):

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
        #print post_body
        #f = open('apioutput.txt', 'a')
        #f.write("%s\n"%post_body)
        #f.close()
        if post_body["Message"] == "DeckSave":
            print(post_body)
            deckFormater().generateImage(post_body)

def main():
    PORT = 1234
    try:
        server = HTTPServer(('', PORT), MyHandler)
        print 'started httpserver on port %s...'%PORT
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
