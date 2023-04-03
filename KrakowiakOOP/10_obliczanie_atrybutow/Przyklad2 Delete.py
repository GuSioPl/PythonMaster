class Model3: #walidacja całkowita + usuwanie

    def __init__(self, y_true, y_pred):

        if not isinstance(y_true, (list,tuple)):
            raise TypeError(f'They y_true object must have type of list or typle not {type(y_true).__name__}')
        if not isinstance(y_pred, (list,tuple)):
            raise TypeError(f'They _y_pred object must have type of list or typle not {type(y_pred).__name__}')

        if not len(y_true) == len(y_pred):
            raise ValueError(f'Parameters should have same lenght')

        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    @property
    def y_true(self):
        return self._y_true

    @property
    def y_pred(self):
        return self._y_pred

    @y_true.setter
    def y_true(self, value):
        if isinstance(value, (list,tuple)):
            if len(self._y_pred) == len(value):
                self._y_true = value
            else:
                raise ValueError(f"The y_true object beed to be of lenght"
                                 f'{len(self._y_pred)}')
        else:
            raise TypeError(f"object neet to be tuple or list instead"
                            f" {type(self._y_true).__name__}")
        self._accuracy = None

    @y_true.deleter
    def y_true(self):
        print("Deleting true")
        del self._y_true

    @y_pred.setter
    def y_pred(self, value):
        if isinstance(value, (list,tuple)):
            if len(value) == len(self._y_true):
                self._y_pred = value
            else:
                raise ValueError(f"The y_pred object beed to be of lenght"
                                 f'{len(self._y_true)}')
        else:
            raise TypeError(f"object neet to be tuple or list instead"
                            f" {type(self._y_pred).__name__}")
        self._accuracy = None

    @y_pred.deleter
    def y_pred(self):
        print("Deleting pred")
        del self._y_pred

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'{Model3.__name__} accuracy: {self._accuracy:.4f}')

model3 = Model3([0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0])
model3.y_true = (0, 0, 1, 0, 1, 0, 0)
del model3.y_true ##wyskakuje deleting true
model3.y_true = (0, 0, 1, 0, 1, 0, 0)
model3.accuracy
