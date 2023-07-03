from _view.conveyor_canvas import ConveyorCanvas
from _view.indicator_canvas import IndicatorCanvas
from _view.remote_io_view import RemoteIOView
from _view.sensor_canvas import SensorCanvas
from _view.silo_camvas import SiloCanvas


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

    def conveyor1_change_color(self, motor_color, left_color, right_color):
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
        if self.__conveyor1_left_color != sensor_color:
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
        self.create_delta_indicator(self.DIRECTION2_INDICATOR_X_POSITION,
                                    self.DIRECTION2_INDICATOR_Y_POSITION,
                                    name='M2_JOBB',
                                    direction='right',
                                    color=self.__conveyor1_right_color)

    def __conveyor1_drawing(self):
        self.create_conveyor(self.CONVEYOR1_X_POSITION,
                             self.CONVEYOR1_Y_POSITION,
                             length=self.CONVEYOR1_LENGTH, name='Szalag 1',
                             circle1_name='M2',
                             circle1_color=self.__conveyor1_motor_color,
                             circle2_name='S2',
                             circle2_color=self.__conveyor1_sensor_color)

    def __conveyor2_drawing(self):
        self.create_conveyor(self.CONVEYOR2_X_POSITION,
                             self.CONVEYOR2_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 2',
                             circle1_name='S3',
                             circle1_color=self.__conveyor2_sensor_color,
                             circle2_name='M3',
                             circle2_color=self.__conveyor2_motor_color)

    def __conveyor3_drawing(self):
        self.create_conveyor(self.CONVEYOR3_X_POSITION,
                             self.CONVEYOR3_Y_POSITION,
                             length=self.CONVEYOR2_LENGTH, name='Szalag 3',
                             circle1_name='M4',
                             circle1_color=self.__conveyor3_motor_color,
                             circle2_name='S4',
                             circle2_color=self.__conveyor3_sensor_color)


class App(RemoteIOView):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.name.configure(text='Szalag 4 Remote IO')

        self.conveyors = Conveyors(self.process_frame)

        self.conveyors.pack()


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
