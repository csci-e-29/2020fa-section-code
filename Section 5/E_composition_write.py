# Here's an example of how composition can be useful
import io


class WriteSomething:
    def __init__(self, my_writer):
        self.my_writer = my_writer  # whatever my_writer is, it's stored in the attr my_writer
        print(f"my writer set: {self.my_writer}")

    def write(self):
        self.my_writer.write("I love writing")  # I assume that I can call the write method on the object


#  Modularity - It doesn't really matter what type of object gets sent up to constructor


with open('text_io.txt', 'w') as f1:
    WriteSomething(f1).write()

# This code implements a file-like class, StringIO, that reads and writes a string buffer (also known as memory files)
with io.StringIO() as f2:
    WriteSomething(f2).write()
