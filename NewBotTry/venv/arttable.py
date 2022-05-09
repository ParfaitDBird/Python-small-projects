class artf:


    def __init__(self):
        self._autor = 'name'
        self._url = 'enlace'
    @property
    def get_autor(self):
        return self._autor

    @get_autor.setter
    def set_autor(self, autor):
        self._autor = autor

    @property
    def get_enlace(self):
        return _url

    @get_enlace.setter
    def set_enlace(self, url):
        self._url = url
