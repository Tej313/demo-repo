import os
with os.scandir('/Users/tej/Desktop/demo/helloworld') as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
