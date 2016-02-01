# pylint: disable=no-self-use, wildcard-import, unused-wildcard-import
from definitions import Parser
from test.fixtures import *


class ClassName:

    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2


class SubClassName(ClassName):

    def __init__(self, argument1, argument2):
        super().__init__(argument1, argument2)


class TestReadme:

    def test_intro(self):
        parser = Parser(filename('schema/readme_intro.yaml'))
        definition = parser(filename('definition/readme_intro.yaml'))
        assert definition.key1 == 'foo'
        assert isinstance(definition.key2, SubClassName)
        assert isinstance(definition.key3, ClassName)
        assert definition.key3.argument1 == 'foo'
        assert definition.key3.argument2 == 42
        assert isinstance(definition.key4, SubClassName)
        assert definition.key4.argument1 == 'foo'
        assert definition.key4.argument2 == 42
        assert definition.key5 == ['value1', 'value2', 'value3']

    def test_long(self):
        pass
