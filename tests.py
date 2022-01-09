from xUnit import WasRun, TestCase

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert self.test.wasRun

TestCaseTest("testTemplateMethod").run()


