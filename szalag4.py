from _view.remote_io_view import RemoteIOView


class App(RemoteIOView):

    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.name.configure(text='Szalag 4 Remote IO')


if __name__ == '__main__':
    app = App()

    app.after(100, app.loop)

    app.mainloop()
