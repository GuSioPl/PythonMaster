class Model:

    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
        self._accuracy = None

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'Model accuracy: {self._accuracy:.4f}')

model = Model([0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]) #ale jeszcze nie liczy ponownie jak zmieni się to
model.accuracy #policzuyło
model.accuracy #tu już nie

class Model2:

    def __init__(self, y_true, y_pred):
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
        self._y_true = value
        self._accuracy = None

    @y_pred.setter
    def y_pred(self, value):
        self._y_pred = value
        self._accuracy = None

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'{Model2.__name__} accuracy: {self._accuracy:.4f}')

model2 = Model2([0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]) #ale jeszcze nie liczy ponownie jak zmieni się to
model2.accuracy #policzuyło
model2.accuracy #tu już nie
print(model2.__dict__)
model2.y_true = [0, 0, 1, 0, 0, 1, 1]
model2.accuracy ##i tu liczy
model2.y_pred = [0, 0, 1, 0, 0, 1, 0]
model2.accuracy ##i tu liczy
print(model2.__dict__)
model2.y_pred = "[0, 0, 1, 0, 0, 1, 0]"
print(model2.__dict__)
model2.accuracy

class Model3: #walidacja całkowita

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
        self._y_true = value
        self._accuracy = None

    @y_pred.setter
    def y_pred(self, value):
        self._y_pred = value
        self._accuracy = None

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'{Model2.__name__} accuracy: {self._accuracy:.4f}')

model3 = Model3([0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0])
