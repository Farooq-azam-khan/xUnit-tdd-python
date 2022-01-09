class TestCase: 
    
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

    def tearDown(self):
        pass 

    def setUp(self):
        pass

class TestResult:
    
    def __init__(self):
        self.runCount = 0


    def testStarted(self):
        self.runCount = self.runCount+ 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"

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

    def testBrokenMethod(self):
        raise Exception


