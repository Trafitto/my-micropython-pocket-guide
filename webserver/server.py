import network
import time
import gc
from machine import Pin
try:
    import usocket as socket
except:
    import socket


D4 = Pin(2, Pin.OUT)
D4.on()  # pin off
gc.collect()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


class StatusCode(object):
    def __init__(self, code, reason):
        self.code = code
        self.reason = reason


STATUS_MAP = {
    '200': StatusCode(200, 'OK')
}


class Connection():
    def __init__(self, socket):
        self.socket = socket.accept()

    @property
    def connection(self):
        if not hasattr(self, '_connection'):
            self.get_connection()
        return self._connection

    @property
    def address(self):
        if not hasattr(self, '_address'):
            self.get_connection()
        return self._address

    def get_connection(self):
        self._connection, self._address = self.socket.accept()

    def close(self):
        self.connection.close()
        delattr(self, '_connection')
        delattr(self, '_address')

 
class Response():
    send_buffer_size = 1024
    http_version = 'HTTP/1.0'

    def __init__(self, status_code=204, body='', headers={}):
          self.status_code = str(status_code)
          self.headers = headers.copy()
          
          self.body = json.dumps(body).encode()
          self.headers['Content-Type'] = 'application/json'
          
    def write(self, connection):
          connection.send('{http_version} {status_code} {reason} \r\n'.format(
            http_version=self.http_version,
            status_code=STATUS_MAP[self.status_code].code,
            reason=STATUS_MAP[self.status_code].reason
          ))
          connection.sendall(self.body)

          



def mini_blink(pin):
    pin.off()
    time.sleep(2)
    pin.on()

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    mini_blink(D4)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Connection: close\n\n')
    conn.sendall('{"status": "ok"}')
    conn.close()
