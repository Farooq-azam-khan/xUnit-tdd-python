class TestCase: 
    
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None # should'nt it be False initinally
        self.wasSetUp = 1
        TestCase.__init__(self, name) 

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

