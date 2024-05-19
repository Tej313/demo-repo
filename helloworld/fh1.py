import os
with os.scandir('/Users/tej/Desktop/demo/helloworld/helloworld') as entries:
    for entry in entries:
        print(entry.name)
