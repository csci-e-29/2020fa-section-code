'''

1) Context Managers
    - enter
    - exit
    - error handling

'''
from timeit import timeit

'''
Part 1a: Acquiring and returning resources
'''
# files=[]
# for x in range(100000):
#     print(x)
#     files.append(open('output.txt', 'w'))

'''
Part 1a FIXED: closing
'''
# files=[]
# for x in range(100000):
#     #files.append(
#     f=open('output.txt', 'w')
#     f.write('hello')
#     print(f)
#     f.close()
#     files.append(f)


'''
Part 1b: What about this issue?
'''
# files=[]
# for x in range(10):
#     f = open('foo.txt', 'w')
#     files.append(f)
#     if x==5: raise Exception('exception raised')
#     f.close()
   
# def check_closed(list_files):
#     print("There are {} files in the list".format(len(list_files)))
#     for i in range(len(list_files)):
#         if not list_files[i].closed:
#             print('File not closed: {}'.format(i))
#     print("Done!")
    
# check_closed(files)

'''
Part 1b FIXED: try-except-finally
'''

# files=[]
# for x in range(10):
#     try:
#         f = open('foo.txt', 'w')
#         files.append(f)
#         if x==5: raise Exception('exception raised')
#     except:
#         pass
#     finally:
#         f.close()

# for i in range(len(files)):
#     if not files[i].closed:
#         print('not closed: {}'.format(i))

'''
Could also fix 1b by using context manager in the try. Will close despite the Exception.
'''
# files=[]
# for x in range(10):
#     try:
#         with open('foo.txt', 'w') as f:
#             files.append(f)
#             if x==5: raise Exception('exception raised')
#     except:
#         pass

'''
Part 2: Writing to a file - help me use the "with" statement. Why might this be better?
'''
## delays things for 5 seconds
# from timeit import timeit
# files = []

# def sum_squares(n_squares=6):
#     squared = []
#     for i in range(n_squares):
#         squared.append(i**2)
#     summed_value = 0
#     for i in squared:
#         summed_value += i
#     return summed_value


# def write_value_to_file():
#     f = open('output.txt', 'w')
#     files.append(f)
#     time_it_took = timeit(sum_squares)
#     msg = 'The time to compute is {} seconds\n'.format(time_it_took)
#     print(msg)
#     f.write(msg)
#     f.close()

# write_value_to_file() 
# check_closed(files)

'''
Part 2 FIXED
'''
# from timeit import timeit
# files = []

# def sum_squares(n_squares=6):
#     squared = []
#     for i in range(n_squares):
#         squared.append(i**2)
#     summed_value = 0
#     for i in squared:
#         summed_value += i
#     return summed_value


# def write_value_to_file():
#     with open('output.txt', 'w') as f:
#         files.append(f)
#         time_it_took = timeit(sum_squares)
#         msg = 'The time to compute is {} seconds\n'.format(time_it_took)
#         print(msg)
#         f.write(msg)

# write_value_to_file() 
# check_closed(files)

'''
Part 3: Constructing our own Context Manager to do the same thing
http://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-class
'''
# files = []

# class File(object):
#     """Starter context manager
#     """
#     def __init__(self, file_name, method):
#         print('__init__')
#         self.file_obj = open(file_name, method)
#     def __enter__(self):
#         print('enter')
#         return self.file_obj
#     def __exit__(self, type, value, traceback):
#         print('exit')
#         self.file_obj.close()

# item_test=File('output.txt', 'w')

# with item_test as f:
#     files.append(f)
#     time_it_took = timeit(sum_squares) # 5 seconds after enter
#     msg = 'The time to compute is {} seconds\n'.format(time_it_took)
#     #raise Exception('exception')
#     print(msg)
#     f.write(msg)

# check_closed(files)

'''
Part 3: Comment out the Exception. How to handle it? 
ANSWER:
'''
#     def __exit__(self, type, value, traceback):
#         try:
#             if type is not None:  
#                 print("Handling exception during the write")
#                 print("type:", type)
#                 print("value:", value)
#                 print("traceback:", traceback)
#         except Exception as e:
#             print(e)
#         finally:
#             print('exit')
#             self.file_obj.close()
#             return True

'''
Part 4: Contextlib contextmanager
https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
'''

# from contextlib import contextmanager

# @contextmanager
# def open_file(path, mode):
#     the_file = open(path, mode)
#     yield the_file
#     the_file.close()

# files = []

# for x in range(10):
#     with open_file('foo.txt', 'w') as infile:
#         files.append(infile)

# check_closed(files)
