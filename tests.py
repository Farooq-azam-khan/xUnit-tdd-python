from xUnit import WasRun, TestCase

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert self.test.wasRun

    
    def testSetUp(self):
        self.test.run()
        assert "setUp testMethod " == self.test.log

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testSetUp").run()


