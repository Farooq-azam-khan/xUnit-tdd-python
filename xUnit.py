class TestCase: 
    
    def __init__(self, name):
        self.name = name

    def run(self):#, result):
        #result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def tearDown(self):
        pass 

    def setUp(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name) 

    def testMethod(self):
        self.wasRun = 1
        self.log += "testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "


