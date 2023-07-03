from socket import socket, AF_INET, SOCK_STREAM, timeout
from struct import unpack, pack


class TCPConnect:
    READ_BUFFER_SIZE = 1

    BYTE_FORMAT = 'B'

    __send_byte = b'\x00'
    __read_byte = b'\x00'

    def __init__(self, host, port):
        self.__client_socket = None
        self.__client_host = None
        self.__client_port = None
        self.__server_socket = socket(AF_INET, SOCK_STREAM)
        self.__server_host = host
        self.__server_port = port

    def bind(self):
        self.__server_socket.bind((self.__server_host, self.__server_port))
        self.__server_socket.listen(5)

    def transfer(self):
        if self.__client_socket is None:
            try:
                self.__client_socket, client_address = self.__server_socket.accept()
                self.__client_host = client_address[0]
                self.__client_port = client_address[1]
                self.__client_socket.settimeout(2)
            except OSError:
                pass
        else:
            try:
                self.__read_byte = self.__client_socket.recv(self.READ_BUFFER_SIZE)
                self.__client_socket.send(self.__send_byte)
            except timeout:
                self.__client_socket.close()
                self.__client_socket = None
                self.send_data = 0
                self.read_data = 0
            except OSError:
                pass

    def close(self):
        if self.__client_socket is not None:
            self.__client_socket.close()
            self.__client_socket = None
        self.__server_socket.close()

    def server_close(self):
        self.__server_socket.close()
        self.__server_socket = None

    @property
    def connect(self):
        if self.__client_socket is None:
            return False
        return True

    @property
    def server_host(self):
        return self.__server_host

    @property
    def server_port(self):
        return self.__server_port

    @property
    def client_host(self):
        return self.__client_host

    @property
    def send_data(self):
        return unpack(self.BYTE_FORMAT, self.__send_byte)[0]

    @send_data.setter
    def send_data(self, data):
        self.__send_byte = pack(self.BYTE_FORMAT, data)

    @property
    def read_data(self):
        return unpack(self.BYTE_FORMAT, self.__read_byte)[0]

    @read_data.setter
    def read_data(self, data):
        self.__read_byte = pack(self.BYTE_FORMAT, data)
