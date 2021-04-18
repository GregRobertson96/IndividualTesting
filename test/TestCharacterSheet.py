import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.Entities.CharacterSheet import CharacterSheet
from src.Display.TestInput import TestInput

#Mocks
class TestMocks(unittest.TestCase):

    def mockTestTotalStats(self):
        mockTesting = CharacterSheet()
        mockTesting.totalStats = MagicMock(return_value=50)
        self.assertEqual(mockTesting.totalStats(), 50)


#Fakes
class TestFakes(unittest.TestCase):

    def fakeGetStats(self):
        fakeTesting = CharacterSheet
        fakeTestUserInput = TestInput()
        fakeTestUserInput.setInputList([5, 5, 5, 5, 5, 5, 5, 5])

        fakeStats = fakeTesting.characterStats(fakeTestUserInput)

        return fakeStats

    def testCharacterStats(self):
        fakeStats = self.fakeGetStats()
        fakeCharacterStats = fakeStats.characterStats()
        self.assertEqual(fakeCharacterStats, [5, 5, 5, 5, 5, 5, 5, 5])

#Stubs
class stubTests(CharacterSheet):

    def characterClassStub(self):
        raise NotImplementedError

    def characterPerksStub(self):
        raise NotImplementedError

