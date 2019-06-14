"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#I think this function will create an array title "some_words" with elements: what, does, this, line, do and?
some_words = ['what', 'does', 'this', 'line', 'do', '?']#returned nothing, but stored respective string elements in some_words list

#this function creates a loop of the print function for every element in the "some_words" array
for word in some_words:
    print(word) #printed each element of the list named some_words

#this loop function will do the same except the name of the variable moving through the array is x
for x in some_words:
    print(x) #did the same thing

#this will print every element in the array?
print(some_words) #it printed the list as a while, not each element

#this conditional statement will test whether the length of the array is greater than 3, if so print the string
if len(some_words) > 3:
    print('some_words contains more than 3 words') #condition was met so string was printed

#platform.uname from the link must release the system information such as this might show windows, DESKTOP-NTSFHD0, Win10, AMD64, Intel i7
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #I guessed some of them  but but didn't get the release number: 10.0.17134 and processor name:Intel64 Family 6 Model 158 Stepping 9, Genuine Intel

usefulFunction()
