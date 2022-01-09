class TestCase: 
    
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None # should'nt it be False initinally
        TestCase.__init__(self, name) 

    def testMethod(self):
        self.wasRun = 1

    def run(self):
        method = getattr(self, self.name)
        method()#self.testMethod()


