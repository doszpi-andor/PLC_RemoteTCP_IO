from tkinter import Tk, Label, Frame

from _socket import gethostbyname, gethostname

from _data.remote_data import RemoteData
from _tcp_connect.plc_tcp_connect import TCPConnect
from _threading.thread_loop import ThreadLoop


class RemoteIOView(Tk):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('Remote IO')

        self.resizable(False, False)

        self.name_frame = Frame(self)
        self.process_frame = Frame(self)
        self.connect_frame = Frame(self)

        self.name = Label(self.name_frame, text='Remote TCP', font=("Arial", 16))
        self.name.pack()

        self.server_label = Label(self.connect_frame, text='--')
        self.connect_label = Label(self.connect_frame, text='--')
        self.server_label.pack()
        self.connect_label.pack()

        self.name_frame.pack()
        self.process_frame.pack()
        self.connect_frame.pack()

        self.remote_data = RemoteData()

        self.plc_connect = TCPConnect(gethostbyname(gethostname()), 2000)
        self.plc_connect.bind()

        self.server_label.configure(text='Local address: %s:%i' %
                                         (self.plc_connect.server_host, self.plc_connect.server_port))

        self.transfer_loop = ThreadLoop(loop=self.data_transfer)
        self.transfer_loop.start()

    def destroy(self):
        self.plc_connect.close()
        self.transfer_loop.stop()
        self.transfer_loop.join()
        super().destroy()

    def data_transfer(self):
        self.plc_connect.send_data = self.remote_data.input_data
        self.plc_connect.transfer()
        self.remote_data.output_data = self.plc_connect.read_data

    def loop(self):
        if self.plc_connect.connect:
            self.connect_label.configure(text='PLC connected in ' + self.plc_connect.client_host, fg='black')
        else:
            self.connect_label.configure(text='PLC not connected', fg='red')

        self.after(100, self.loop)


if __name__ == '__main__':
    app = RemoteIOView()

    app.after(100, app.loop)

    app.mainloop()
