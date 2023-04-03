class User:

    def start(self):
        print('Starting...')

    def drink(self):
        print('Drinking...')

    def work(self):
        print('Working...')

    def end(self):
        print('Ending...')

    def make_session(self):
        print(f'--- {self.__class__.__name__.upper()} SESSION ---')
        self.start()
        self.drink()
        self.work()
        self.end()
        print(f'--- END SESSION ---\n')



class Player(User):

    def work(self):
        print('Playing...')

user = User()
user.make_session()
player = Player()
player.make_session()

class User:

    def start(self):
        print('Starting...')

    def drink(self):
        print('Drinking...')

    def work(self):
        print('Working...')

    def end(self):
        print('Ending...')

    def make_session(self):
        print(f'--- {self.__class__.__name__.upper()} SESSION ---')
        User.start(self)
        User.drink(self)
        User.work(self)
        User.end(self)
        print(f'--- END SESSION ---\n')



class Player(User):

    def work(self):
        print('Playing...')

user = User()
user.make_session()
player = Player()
player.make_session() ##tAK ZAKODZONE źle działa powinno być jak wyżej playing