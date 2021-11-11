import importlib

if __name__ == '__main__':
    while True:
        module_name = input("Enter name of the module: ")
        module = importlib.import_module(module_name)
        print(module.__doc__)