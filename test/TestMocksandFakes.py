import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.Entities.CharacterSheet import CharacterSheet
from src.Display.TestInput import TestInput

#Mocks
class TestMocks(unittest.TestCase):

    def mockTest(self):
        mockTesting = CharacterSheet()
        mockTesting.characterStats = MagicMock(return_value=50)
        self.assertEqual(mockTesting.characterStats(), 50)

#Fakes
class TestFakes(unittest.TestCase):

    def fakeGetCharacterStats(self):
        fakeTestUserInput = TestInput()