class Context:

    def __init__(self):
        print('Init')

    def __enter__(self):
        print('Entered')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Done')


with Context() as cont:
    print('Do something')

# f = open('my.txt', "w")
# f.write('Regular mode\n')
# f.close()
#
# with open('my.txt', 'a') as f:
#     f.write('Written in context')
