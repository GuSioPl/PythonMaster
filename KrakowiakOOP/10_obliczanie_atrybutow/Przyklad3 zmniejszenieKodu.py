class Model3: #walidacja całkowita + usuwanie zmniejszeniekodu

    def __init__(self, y_true, y_pred):
        Model3._validate_input(y_true, 'y_true')
        Model3._validate_input(y_pred, 'y_pred')
        if not len(y_true) == len(y_pred):
            raise ValueError(f'Parameters should have same lenght')

        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    def _validate_input(iters, var_name):
        if not isinstance(iters, (list, tuple)):
            raise TypeError(f'They {var_name} object must have type of list or'
                            f' typle not {type(iters).__name__}')

    def _validate_value(self, value, var_name): ##On wrzuca walidacje z validate input tutaj jeszcze
        mapping = {'y_true': '_y_pred', 'y_pred' : '_y_true'}
        if not len(value) == len(getattr(self, mapping[var_name])):
            raise AttributeError(f"Lenght of {var_name} must have same lenght "
                                 f"{len(getattr(self, mapping[var_name]))}")

    @property
    def y_true(self):
        return self._y_true

    @property
    def y_pred(self):
        return self._y_pred

    @y_true.setter
    def y_true(self, value):
        Model3._validate_input(value, 'y_true')
        Model3._validate_value(self, value, 'y_true')
        self._y_true = value
        self._accuracy = None

    @y_true.deleter
    def y_true(self):
        print("Deleting true")
        del self._y_true

    @y_pred.setter
    def y_pred(self, value):
        Model3._validate_input(value, 'y_pred')
        Model3._validate_value(self, value, 'y_pred')
        self._y_pred = value
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

