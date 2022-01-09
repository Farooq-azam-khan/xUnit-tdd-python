from xUnit import WasRun, TestCase
'''
test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
'''
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")


    def testRunning(self):
        #test = WasRun("testMethod")
        #assert (not test.wasRun)
        self.test.run()
        assert self.test.wasRun

    
    def testSetUp(self):
        #test = WasRun("testMethod")
        self.test.run()
        assert self.test.wasSetUp

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()


