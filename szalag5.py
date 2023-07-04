from threading import Timer
from tkinter import Frame, Checkbutton, IntVar

from _view.conveyor_canvas import ConveyorCanvas
from _view.remote_io_view import RemoteIOView
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas


class Data:
    input_index = {'S1': 0, 'S2': 1, 'S3': 2, 'S4': 3}
    output_index = {'M1': 0, 'M2': 1, 'M3': 2, 'M4': 3}


class ErrorCheckBox(Frame):

    # noinspection PyDefaultArgument
    def __init__(self,
                 master=None,
                 silo1_process=None,
                 silo2_process=None,
                 error1_process=None,
                 error2_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.silo1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo1 = Checkbutton(self, variable=self.silo1_var, command=silo1_process, text='Siló 1 kifogyott')
        self.silo2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo2 = Checkbutton(self, variable=self.silo2_var, command=silo2_process, text='Siló 2 kifogyott')

        self.error1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')

        self.silo1.grid(row=1, column=1)
        self.silo2.grid(row=1, column=2)

        self.error1.grid(row=2, column=1)
        self.error2.grid(row=2, column=2)


class Conveyors(ConveyorCanvas, SiloCanvas, SensorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 400
    CONVEYOR2_LENGTH = 400

    SILO1_X_POSITION = 5
    SILO2_X_POSITION = SILO1_X_POSITION + SILO_WIDTH + 80
    SILO1_SENSOR_X_POSITION = SILO1_X_POSITION + 5
    SILO2_SENSOR_X_POSITION = SILO2_X_POSITION + 5
    CONVEYOR1_X_POSITION = SILO1_X_POSITION
    CONVEYOR2_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8
    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 20
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20

    FULL_WIDTH = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH
    FULL_HEIGHT = CONVEYOR2_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.silo1_motor_color = 'gray'
        self.silo2_motor_color = 'gray'
        self.silo1_sensor_color = 'red'
        self.silo2_sensor_color = 'red'
        self.conveyor1_motor_color = 'gray'
        self.conveyor1_sensor_color = 'gray'
        self.conveyor2_motor_color = 'gray'
        self.conveyor2_sensor_color = 'gray'

        self.__silo1_drawing()
        self.__silo2_drawing()
        self.__conveyor1_drawing()
        self.__conveyor2_drawing()

    def silo1_change_motor_color(self, motor_color):
        if self.silo1_motor_color != motor_color:
            self.silo1_motor_color = motor_color
            self.__silo1_drawing()

    def silo1_change_sensor_color(self, sensor_color):
        if self.silo1_sensor_color != sensor_color:
            self.silo1_sensor_color = sensor_color
            self.__silo1_drawing()

    def silo2_change_motor_color(self, motor_color):
        if self.silo2_motor_color != motor_color:
            self.silo2_motor_color = motor_color
            self.__silo2_drawing()

    def silo2_change_sensor_color(self, sensor_color):
        if self.silo2_sensor_color != sensor_color:
            self.silo2_sensor_color = sensor_color
            self.__silo2_drawing()

    def conveyor1_change_motor_color(self, motor_color):
        if self.conveyor1_motor_color != motor_color:
            self.conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()

    def conveyor1_change_sensor_color(self, sensor_color):
        if self.conveyor1_sensor_color != sensor_color:
            self.conveyor1_sensor_color = sensor_color
            self.__conveyor1_drawing()

    def conveyor2_change_motor_color(self, motor_color):
        if self.conveyor2_motor_color != motor_color:
            self.conveyor2_motor_color = motor_color
            self.__conveyor2_drawing()

    def conveyor2_change_sensor_color(self, sensor_color):
        if self.conveyor2_sensor_color != sensor_color:
            self.conveyor2_sensor_color = sensor_color
            self.__conveyor2_drawing()

    def __silo1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO1_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 1',
                         motor_name='M1', motor_color=self.silo1_motor_color)
        self.create_sensor(self.SILO1_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1', color=self.silo1_sensor_color)

    def __silo2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO2_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló 2',
                         motor_name='M2', motor_color=self.silo2_motor_color)
        self.create_sensor(self.SILO2_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S2', color=self.silo2_sensor_color)

    def __conveyor1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M3', circle1_color=self.conveyor1_motor_color,
                             circle2_name='S3', circle2_color=self.conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='M4', circle1_color=self.conveyor2_motor_color,
                             circle2_name='S4', circle2_color=self.conveyor2_sensor_color)


class App(RemoteIOView):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.name.configure(text='Szalag 5 Remote IO')
        self.error_check = ErrorCheckBox(self.process_frame,
                                         silo1_process=self.s1_changed,
                                         silo2_process=self.s2_changed,
                                         error1_process=self.s3_changed,
                                         error2_process=self.s4_changed)
        self.conveyors = Conveyors(self.process_frame)

        self.conveyors.pack()
        self.error_check.pack()

        self.remote_data.input_bits[Data.input_index['S1']] = True
        self.remote_data.input_bits[Data.input_index['S2']] = True

    def loop(self):
        if self.remote_data.output_data_bit_is_change(Data.output_index['M1']):
            if self.remote_data.output_bits[Data.output_index['M1']]:
                self.conveyors.silo1_change_motor_color(motor_color='green')
            else:
                self.conveyors.silo1_change_motor_color(motor_color='gray')

        if self.remote_data.output_data_bit_is_change(Data.output_index['M2']):
            if self.remote_data.output_bits[Data.output_index['M2']]:
                self.conveyors.silo2_change_motor_color(motor_color='green')
            else:
                self.conveyors.silo2_change_motor_color(motor_color='gray')

        if self.remote_data.output_data_bit_is_change(Data.output_index['M3']):
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor1_change_motor_color(motor_color='green')
                s3_delay = Timer(1.5, self.s3_changed)
                s3_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color(motor_color='gray')
                self.s3_changed()

        if self.remote_data.output_data_bit_is_change(Data.output_index['M4']):
            if self.remote_data.output_bits[Data.output_index['M4']]:
                self.conveyors.conveyor2_change_motor_color(motor_color='green')
                s4_delay = Timer(1.5, self.s4_changed)
                s4_delay.start()
            else:
                self.conveyors.conveyor2_change_motor_color(motor_color='gray')
                self.s4_changed()

        super().loop()

    def s1_changed(self):
        if self.error_check.silo1_var.get():
            self.conveyors.silo1_change_sensor_color(sensor_color='gray')
            self.remote_data.input_bits[Data.input_index['S1']] = False
        else:
            self.conveyors.silo1_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S1']] = True

    def s2_changed(self):
        if self.error_check.silo2_var.get():
            self.conveyors.silo2_change_sensor_color(sensor_color='gray')
            self.remote_data.input_bits[Data.input_index['S2']] = False
        else:
            self.conveyors.silo2_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S2']] = True

    def s3_changed(self):
        if self.error_check.error1_var.get():
            self.conveyors.conveyor1_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S3']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S3']] = True
            else:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S3']] = False

    def s4_changed(self):
        if self.error_check.error2_var.get():
            self.conveyors.conveyor2_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S4']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M4']]:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S4']] = True
            else:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S4']] = False


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
