from threading import Timer
from tkinter import Frame, Checkbutton, IntVar

from _view.conveyor_canvas import ConveyorCanvas
from _view.remote_io_view import RemoteIOView


class Data:
    input_index = {'S1': 0, 'S2': 1, 'S3': 2}
    output_index = {'M1': 0, 'M2': 1, 'M3': 2}


class ErrorCheckBox(Frame):

    def __init__(self,
                 master=None,
                 error1_process=None,
                 error2_process=None,
                 error3_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.error1_var = IntVar()
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')
        self.error3_var = IntVar()
        self.error3 = Checkbutton(self, variable=self.error3_var, command=error3_process, text='Szalag 3 hiba')

        self.error1.grid(row=1, column=1)
        self.error2.grid(row=1, column=2)
        self.error3.grid(row=1, column=3)


class Conveyors(ConveyorCanvas):
    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 400

    CONVEYOR1_X_POSITION = 5
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH + 50
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    CONVEYOR1_Y_POSITION = 5
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION
    CONVEYOR3_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__conveyor1_motor_color = 'gray'
        self.__conveyor1_sensor_color = 'gray'
        self.__conveyor2_motor_color = 'gray'
        self.__conveyor2_sensor_color = 'gray'
        self.__conveyor3_motor_color = 'gray'
        self.__conveyor3_sensor_color = 'gray'

        self.__conveyor1_drawing()
        self.__conveyor2_drawing()
        self.__conveyor3_drawing()

    def conveyor1_change_motor_color(self, motor_color):
        if self.__conveyor1_motor_color != motor_color:
            self.__conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()

    def conveyor1_change_sensor_color(self, sensor_color):
        if self.__conveyor1_sensor_color != sensor_color:
            self.__conveyor1_sensor_color = sensor_color
            self.__conveyor1_drawing()

    def conveyor2_change_motor_color(self, motor_color):
        if self.__conveyor2_motor_color != motor_color:
            self.__conveyor2_motor_color = motor_color
            self.__conveyor2_drawing()

    def conveyor2_change_sensor_color(self, sensor_color):
        if self.__conveyor2_sensor_color != sensor_color:
            self.__conveyor2_sensor_color = sensor_color
            self.__conveyor2_drawing()

    def conveyor3_change_motor_color(self, motor_color):
        if self.__conveyor3_motor_color != motor_color:
            self.__conveyor3_motor_color = motor_color
            self.__conveyor3_drawing()

    def conveyor3_change_sensor_color(self, sensor_color):
        if self.__conveyor3_sensor_color != sensor_color:
            self.__conveyor3_sensor_color = sensor_color
            self.__conveyor3_drawing()

    def __conveyor1_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M1', circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S1', circle2_color=self.__conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S2', circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M2', circle2_color=self.__conveyor2_motor_color)

    def __conveyor3_drawing(self):
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR3_LENGTH, name='Szalag 3',
                             circle1_name='M3', circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S3', circle2_color=self.__conveyor3_sensor_color)


class App(RemoteIOView):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.name.configure(text='Szalag 1 Remote IO')

        self.conveyors = Conveyors(self.process_frame)
        self.error_check = ErrorCheckBox(self.process_frame,
                                         error1_process=self.s1_changed,
                                         error2_process=self.s2_changed,
                                         error3_process=self.s3_changed)

        self.conveyors.pack()
        self.error_check.pack()

    def loop(self):

        if self.remote_data.output_data_bit_is_change(Data.output_index['M1']):
            if self.remote_data.output_bits[Data.output_index['M1']]:
                self.conveyors.conveyor1_change_motor_color(motor_color='green')
                s1_delay = Timer(1.5, self.s1_changed)
                s1_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color(motor_color='gray')
                self.s1_changed()

        if self.remote_data.output_data_bit_is_change(Data.output_index['M2']):
            if self.remote_data.output_bits[Data.output_index['M2']]:
                self.conveyors.conveyor2_change_motor_color(motor_color='green')
                s2_delay = Timer(1.5, self.s2_changed)
                s2_delay.start()
            else:
                self.conveyors.conveyor2_change_motor_color(motor_color='gray')
                self.s2_changed()

        if self.remote_data.output_data_bit_is_change(Data.output_index['M3']):
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor3_change_motor_color(motor_color='green')
                s3_delay = Timer(1.5, self.s3_changed)
                s3_delay.start()
            else:
                self.conveyors.conveyor3_change_motor_color(motor_color='gray')
                self.s3_changed()

        super().loop()

    def s1_changed(self):
        if self.error_check.error1_var.get():
            self.conveyors.conveyor1_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S1']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M1']]:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S1']] = True
            else:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S1']] = False

    def s2_changed(self):
        if self.error_check.error2_var.get():
            self.conveyors.conveyor2_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S2']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M2']]:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S2']] = True
            else:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S2']] = False

    def s3_changed(self):
        if self.error_check.error3_var.get():
            self.conveyors.conveyor3_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S3']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S3']] = True
            else:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S3']] = False


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
