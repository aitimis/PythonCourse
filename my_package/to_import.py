def dummy_function():
    print('does nothing')


def test_module_import():
    print(__name__)
    print(__package__)

print('running "to import"')
test_module_import()