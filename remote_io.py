from tkinter import Frame, Label, Checkbutton, IntVar, DISABLED

from _view.remote_io_view import RemoteIOView


class InputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Remote Input').grid(row=1, column=1, columnspan=8)
        self.input1_var = IntVar()
        self.input1 = Checkbutton(self, variable=self.input1_var)
        self.input1.grid(row=2, column=1)
        Label(self, text='0').grid(row=3, column=1)
        self.input2_var = IntVar()
        self.input2 = Checkbutton(self, variable=self.input2_var)
        self.input2.grid(row=2, column=2)
        Label(self, text='1').grid(row=3, column=2)
        self.input3_var = IntVar()
        self.input3 = Checkbutton(self, variable=self.input3_var)
        self.input3.grid(row=2, column=3)
        Label(self, text='2').grid(row=3, column=3)
        self.input4_var = IntVar()
        self.input4 = Checkbutton(self, variable=self.input4_var)
        self.input4.grid(row=2, column=4)
        Label(self, text='3').grid(row=3, column=4)
        self.input5_var = IntVar()
        self.input5 = Checkbutton(self, variable=self.input5_var)
        self.input5.grid(row=2, column=5)
        Label(self, text='4').grid(row=3, column=5)
        self.input6_var = IntVar()
        self.input6 = Checkbutton(self, variable=self.input6_var)
        self.input6.grid(row=2, column=6)
        Label(self, text='5').grid(row=3, column=6)
        self.input7_var = IntVar()
        self.input7 = Checkbutton(self, variable=self.input7_var)
        self.input7.grid(row=2, column=7)
        Label(self, text='6').grid(row=3, column=7)
        self.input8_var = IntVar()
        self.input8 = Checkbutton(self, variable=self.input8_var)
        self.input8.grid(row=2, column=8)
        Label(self, text='7').grid(row=3, column=8)


class OutputView(Frame):

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        Label(self, text='Remote Output').grid(row=1, column=1, columnspan=8)
        self.output1_var = IntVar()
        self.output1 = Checkbutton(self, variable=self.output1_var, state=DISABLED)
        self.output1.grid(row=2, column=1)
        Label(self, text='0').grid(row=3, column=1)
        self.output2_var = IntVar()
        self.output2 = Checkbutton(self, variable=self.output2_var, state=DISABLED)
        self.output2.grid(row=2, column=2)
        Label(self, text='1').grid(row=3, column=2)
        self.output3_var = IntVar()
        self.output3 = Checkbutton(self, variable=self.output3_var, state=DISABLED)
        self.output3.grid(row=2, column=3)
        Label(self, text='2').grid(row=3, column=3)
        self.output4_var = IntVar()
        self.output4 = Checkbutton(self, variable=self.output4_var, state=DISABLED)
        self.output4.grid(row=2, column=4)
        Label(self, text='3').grid(row=3, column=4)
        self.output5_var = IntVar()
        self.output5 = Checkbutton(self, variable=self.output5_var, state=DISABLED)
        self.output5.grid(row=2, column=5)
        Label(self, text='4').grid(row=3, column=5)
        self.output6_var = IntVar()
        self.output6 = Checkbutton(self, variable=self.output6_var, state=DISABLED)
        self.output6.grid(row=2, column=6)
        Label(self, text='5').grid(row=3, column=6)
        self.output7_var = IntVar()
        self.output7 = Checkbutton(self, variable=self.output7_var, state=DISABLED)
        self.output7.grid(row=2, column=7)
        Label(self, text='6').grid(row=3, column=7)
        self.output8_var = IntVar()
        self.output8 = Checkbutton(self, variable=self.output8_var, state=DISABLED)
        self.output8.grid(row=2, column=8)
        Label(self, text='7').grid(row=3, column=8)


class App(RemoteIOView):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.input_view = InputView(self.process_frame)
        self.output_view = OutputView(self.process_frame)

        self.input_view.pack()
        self.output_view.pack()

    def loop(self):
        self.remote_data.input_bits[0] = self.input_view.input1_var.get()
        self.remote_data.input_bits[1] = self.input_view.input2_var.get()
        self.remote_data.input_bits[2] = self.input_view.input3_var.get()
        self.remote_data.input_bits[3] = self.input_view.input4_var.get()
        self.remote_data.input_bits[4] = self.input_view.input5_var.get()
        self.remote_data.input_bits[5] = self.input_view.input6_var.get()
        self.remote_data.input_bits[6] = self.input_view.input7_var.get()
        self.remote_data.input_bits[7] = self.input_view.input8_var.get()

        if self.remote_data.output_data_bit_is_change(0):
            self.output_view.output1_var.set(self.remote_data.output_bits[0])

        if self.remote_data.output_data_bit_is_change(1):
            self.output_view.output2_var.set(self.remote_data.output_bits[1])

        if self.remote_data.output_data_bit_is_change(2):
            self.output_view.output3_var.set(self.remote_data.output_bits[2])

        if self.remote_data.output_data_bit_is_change(3):
            self.output_view.output4_var.set(self.remote_data.output_bits[3])

        if self.remote_data.output_data_bit_is_change(4):
            self.output_view.output5_var.set(self.remote_data.output_bits[4])

        if self.remote_data.output_data_bit_is_change(5):
            self.output_view.output6_var.set(self.remote_data.output_bits[5])

        if self.remote_data.output_data_bit_is_change(6):
            self.output_view.output7_var.set(self.remote_data.output_bits[6])

        if self.remote_data.output_data_bit_is_change(7):
            self.output_view.output8_var.set(self.remote_data.output_bits[7])

        super().loop()


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
