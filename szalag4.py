from threading import Timer
from tkinter import Checkbutton, IntVar, Frame

from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.remote_io_view import RemoteIOView
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas


class Data:
    input_index = {'S1': 0, 'S2': 1, 'S3': 2, 'S4': 3}
    # noinspection SpellCheckingInspection
    output_index = {'M1': 0, 'M2_Bal': 1, 'M2_Jobb': 2, 'M3': 3, 'M4': 4}


class ErrorCheckBox(Frame):

    # noinspection PyDefaultArgument
    def __init__(self,
                 master=None,
                 silo_process=None,
                 error1_process=None,
                 error2_process=None,
                 error3_process=None,
                 cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.silo_var = IntVar()
        # noinspection SpellCheckingInspection
        self.silo = Checkbutton(self, variable=self.silo_var, command=silo_process, text='Siló kifogyott')

        self.error1_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error1 = Checkbutton(self, variable=self.error1_var, command=error1_process, text='Szalag 1 hiba')
        self.error2_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error2 = Checkbutton(self, variable=self.error2_var, command=error2_process, text='Szalag 2 hiba')
        self.error3_var = IntVar()
        # noinspection SpellCheckingInspection
        self.error3 = Checkbutton(self, variable=self.error3_var, command=error3_process, text='Szalag 3 hiba')

        self.silo.grid(row=1, column=1, columnspan=3)

        self.error1.grid(row=2, column=1)
        self.error2.grid(row=2, column=2)
        self.error3.grid(row=2, column=3)


class Conveyors(SiloCanvas, ConveyorCanvas, SensorCanvas, IndicatorCanvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 150

    INDICATOR_WIDTH = 25

    CONVEYOR_WIDTH = 45

    CONVEYOR1_LENGTH = 300
    CONVEYOR2_LENGTH = 300
    CONVEYOR3_LENGTH = 300

    CONVEYOR2_X_POSITION = 5
    CONVEYOR1_X_POSITION = CONVEYOR2_X_POSITION + CONVEYOR2_LENGTH * 2 // 3
    CONVEYOR3_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH * 2 // 3

    DIRECTION1_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION - 60
    DIRECTION2_INDICATOR_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH - 30

    SILO_X_POSITION = CONVEYOR1_X_POSITION + CONVEYOR1_LENGTH // 2 - SILO_WIDTH // 2
    SILO_SENSOR_X_POSITION = SILO_X_POSITION + 5

    SILO_Y_POSITION = 5
    SILO_SENSOR_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT * 7 // 8

    CONVEYOR1_Y_POSITION = SILO_Y_POSITION + SILO_HEIGHT + 40
    CONVEYOR2_Y_POSITION = CONVEYOR1_Y_POSITION + CONVEYOR_WIDTH + 20
    CONVEYOR3_Y_POSITION = CONVEYOR2_Y_POSITION

    DIRECTION1_INDICATOR_Y_POSITION = CONVEYOR1_Y_POSITION - INDICATOR_WIDTH - 10
    DIRECTION2_INDICATOR_Y_POSITION = DIRECTION1_INDICATOR_Y_POSITION

    FULL_WIDTH = CONVEYOR3_X_POSITION + CONVEYOR3_LENGTH
    FULL_HEIGHT = CONVEYOR3_Y_POSITION + CONVEYOR_WIDTH

    # noinspection PyDefaultArgument
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, width=self.FULL_WIDTH, height=self.FULL_HEIGHT, **kw)

        self.__silo_motor_color = 'gray'
        self.__silo_sensor_color = 'red'

        self.__conveyor1_motor_color = 'gray'
        self.__conveyor1_left_color = 'gray'
        self.__conveyor1_right_color = 'gray'
        self.__conveyor1_sensor_color = 'gray'
        self.__conveyor2_motor_color = 'gray'
        self.__conveyor2_sensor_color = 'gray'
        self.__conveyor3_motor_color = 'gray'
        self.__conveyor3_sensor_color = 'gray'

        self.__silo_drawing()
        self.__conveyor1_drawing()
        self.__conveyor2_drawing()
        self.__conveyor3_drawing()
        self.__direction_left_drawing()
        self.__direction_right_drawing()

    def silo_change_motor_color(self, motor_color):
        if self.__silo_motor_color != motor_color:
            self.__silo_motor_color = motor_color
            self.__silo_drawing()

    def silo_change_sensor_color(self, sensor_color):
        if self.__silo_sensor_color != sensor_color:
            self.__silo_sensor_color = sensor_color
            self.__silo_drawing()

    def conveyor1_change_motor_color(self, motor_color, left_color, right_color):
        if self.__conveyor1_motor_color != motor_color:
            self.__conveyor1_motor_color = motor_color
            self.__conveyor1_drawing()
        if self.__conveyor1_left_color != left_color:
            self.__conveyor1_left_color = left_color
            self.__direction_left_drawing()
        if self.__conveyor1_right_color != right_color:
            self.__conveyor1_right_color = right_color
            self.__direction_right_drawing()

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

    def __silo_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_silo(self.SILO_X_POSITION,
                         self.SILO_Y_POSITION,
                         silo_name='Siló',
                         motor_name='M1', motor_color=self.__silo_motor_color)
        self.create_sensor(self.SILO_SENSOR_X_POSITION,
                           self.SILO_SENSOR_Y_POSITION,
                           line_length=self.SILO_WIDTH,
                           name='S1', color=self.__silo_sensor_color)

    def __direction_left_drawing(self):
        self.create_delta_indicator(self.DIRECTION1_INDICATOR_X_POSITION,
                                    self.DIRECTION1_INDICATOR_Y_POSITION,
                                    name='M2_BAL',
                                    direction='left',
                                    color=self.__conveyor1_left_color)

    def __direction_right_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_delta_indicator(self.DIRECTION2_INDICATOR_X_POSITION,
                                    self.DIRECTION2_INDICATOR_Y_POSITION,
                                    name='M2_JOBB',
                                    direction='right',
                                    color=self.__conveyor1_right_color)

    def __conveyor1_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M2',
                             circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S2',
                             circle2_color=self.__conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S3',
                             circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M3',
                             circle2_color=self.__conveyor2_motor_color)

    def __conveyor3_drawing(self):
        # noinspection SpellCheckingInspection
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 3',
                             circle1_name='M4',
                             circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S4',
                             circle2_color=self.__conveyor3_sensor_color)


class App(RemoteIOView):

    # noinspection PyPep8Naming
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # noinspection SpellCheckingInspection
        self.name.configure(text='Szalag 4 Remote IO')

        self.error_check = ErrorCheckBox(self.process_frame,
                                         silo_process=self.s1_changed,
                                         error1_process=self.s2_changed,
                                         error2_process=self.s3_changed,
                                         error3_process=self.s4_changed)
        self.conveyors = Conveyors(self.process_frame)

        self.conveyors.pack()
        self.error_check.pack()

        self.remote_data.input_bits[Data.input_index['S1']] = True

    def loop(self):
        if self.remote_data.output_data_bit_is_change(Data.output_index['M1']):
            if self.remote_data.output_bits[Data.output_index['M1']]:
                self.conveyors.silo_change_motor_color(motor_color='green')
            else:
                self.conveyors.silo_change_motor_color(motor_color='gray')

        if self.remote_data.output_data_bit_is_change(Data.output_index['M2_Bal']):
            if self.remote_data.output_bits[Data.output_index['M2_Bal']]:
                self.conveyors.conveyor1_change_motor_color(motor_color='green', left_color='green', right_color='gray')
                s2_left_delay = Timer(1.5, self.s2_changed)
                s2_left_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color(motor_color='gray', left_color='gray', right_color='gray')
                self.s2_changed()

        # noinspection SpellCheckingInspection
        if self.remote_data.output_data_bit_is_change(Data.output_index['M2_Jobb']):
            # noinspection SpellCheckingInspection
            if self.remote_data.output_bits[Data.output_index['M2_Jobb']]:
                self.conveyors.conveyor1_change_motor_color(motor_color='green', left_color='gray', right_color='green')
                s2_right_delay = Timer(1.5, self.s2_changed)
                s2_right_delay.start()
            else:
                self.conveyors.conveyor1_change_motor_color(motor_color='gray', left_color='gray', right_color='gray')
                self.s2_changed()

        if self.remote_data.output_data_bit_is_change(Data.output_index['M3']):
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor2_change_motor_color(motor_color='green')
                s3_delay = Timer(1.5, self.s3_changed)
                s3_delay.start()
            else:
                self.conveyors.conveyor2_change_motor_color(motor_color='gray')
                self.s3_changed()

        if self.remote_data.output_data_bit_is_change(Data.output_index['M4']):
            if self.remote_data.output_bits[Data.output_index['M4']]:
                self.conveyors.conveyor3_change_motor_color(motor_color='green')
                s4_delay = Timer(1.5, self.s4_changed)
                s4_delay.start()
            else:
                self.conveyors.conveyor3_change_motor_color(motor_color='gray')
                self.s4_changed()

        super().loop()

    def s1_changed(self):
        if self.error_check.silo_var.get():
            self.conveyors.silo_change_sensor_color(sensor_color='gray')
            self.remote_data.input_bits[Data.input_index['S1']] = False
        else:
            self.conveyors.silo_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S1']] = True

    def s2_changed(self):
        if self.error_check.error1_var.get():
            self.conveyors.conveyor1_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S2']] = False
        else:
            # noinspection SpellCheckingInspection
            if self.remote_data.output_bits[Data.output_index['M2_Bal']] or \
                    self.remote_data.output_bits[Data.output_index['M2_Jobb']]:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S2']] = True
            else:
                self.conveyors.conveyor1_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S2']] = False

    def s3_changed(self):
        if self.error_check.error2_var.get():
            self.conveyors.conveyor2_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S3']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M3']]:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S3']] = True
            else:
                self.conveyors.conveyor2_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S3']] = False

    def s4_changed(self):
        if self.error_check.error3_var.get():
            self.conveyors.conveyor3_change_sensor_color(sensor_color='red')
            self.remote_data.input_bits[Data.input_index['S3']] = False
        else:
            if self.remote_data.output_bits[Data.output_index['M4']]:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='green')
                self.remote_data.input_bits[Data.input_index['S4']] = True
            else:
                self.conveyors.conveyor3_change_sensor_color(sensor_color='gray')
                self.remote_data.input_bits[Data.input_index['S4']] = False


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
