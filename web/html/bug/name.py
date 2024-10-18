import os
path = input("Enter folder: ")
files = os.listdir(os.path.expanduser(path))
for f in files:
    try:
        for index, file in enumerate(files):
            os.rename(os.path.join(path, file), os.path.join(path, 'e'.join([str(index), ''])))
    except FileNotFoundError:
        pass

# The output is not ordered as the input. This was to shorten names without changing the order.