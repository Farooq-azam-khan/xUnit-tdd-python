class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase: 
    
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.testStarted()
        self.setUp()
        try: 
            method = getattr(self, self.name)
            method()
        except Exception as e:
            print(f"{self.name} Failed")
            print(e)
            result.testFailed()

        self.tearDown()
        return result

    def tearDown(self):
        pass 

    def setUp(self):
        pass

class TestResult:
    
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0 

    def testFailed(self):
        self.errorCount += 1


    def testStarted(self):
        self.runCount = self.runCount+ 1

    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"

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


