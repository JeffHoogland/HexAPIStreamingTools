import SocketServer
import json

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = self.request.recv(1024).strip().split("\n")
            for l in data:
                if l[0] == "{":
                    #print l
                    datadict =  json.loads(l)
                    
                    f = open('apioutput.txt', 'a')
                    f.write("%s\n"%datadict)
                    f.close()
                    
                    print(datadict)
                    for d in datadict:
                        print("%s : %s"%(d, datadict[d]))

        except Exception, e:
            print "Exception wile receiving message: ", e

server = MyTCPServer(('127.0.0.1', 1234), MyTCPServerHandler)
print "Server running on 1234"
server.serve_forever()
