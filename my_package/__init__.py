# __init__ - transforma folderul intr un pachet de sine statator

from my_package.to_import import test_module_import

def test_package_import():
    print(__name__) # valoarea __name__ este tot timpul numele pachetului
