help()  # gives you details on a function
dir()   # lists all functions of a type or module
type()  # gives the type of an object ex. type('kenny') = class 'str'
print() # prints to console
input() # recivres input from console/user
 
while True: # while something is true looks will continue to run
for i in x: # will iterate over something
 
break    # stops the loop at any point
continue # continues a loop
 
"{}".format() # print variable/ replaces {} with the variable in the () ex "Hi my name is {}".format(name)
 
 
len()  # gives length of a container
list() # takes a string and breaks it up into a list.
 
for index, data in enumerate(test_list):  # returns a touple of data with a auto-incramenting
    print('{}: {}'.format(index, data))
 
for index in enumerate(test_list):     
    print('{}: {}'.format(index[0], index[1]))  # accesable by index
 
for index in enumerate(test_list):     # auto unpacking of data with *index
    print('{}: {}'.format(*index))
 
test_list.split()  #splits lists by delimiter ex. test_list.split(",")
' '.join(test_list) # joins list with delimiter between '' MUST BE STRING NO NUMBERS   ex1. ' '.join(test_list)  ex.2 '_'.join(test_list)
test_list.append(new_item) # adds new_item as list to the end of test_list ex. [test, [new_item]]
test_list.extend([x,y,z]) # extend adds x,y,z to the end of test_list
test_list.insert(index, data) # adds data to test_list at index given as paramater
test_list.index('x') # returns the index position of 'x' in test_list
test_list[1] # returns item at index 1 of test_list
test_list.remove('x') # will remove the first instance of 'x' from test_list
test_list.pop(index) # deletes index from test_list and returns the value. Can be stored in a variable. if no index is given will delete last item
test_list.sort() # sorts the list
 
test.strip() # strips surrounding white space
test.lower() # makes item lower case
test.upper() # makes item ALL CAPS
text.title() # makes first letter of each word capital
test.capitalize() # capitalizes the first letter of test
 
 
iter # key word for iterable type
str
dict
int
 
None
 
ValueError # Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
TypeError  # Raised when an operation or function is applied to an object of inappropriate type.
IndexError # RRaised when a sequence subscript is out of range.
 
random.randint(a, b) # MUST IMPORT! selects random int between a and b ex.random.randint(1,10) selects random number between 1 and 10
random.choice([a,b]) # choses a random element of given list. can also use a variable list.
 
sys.exit()  # exits the program. belongs to sys and MUST BE IMPORTED.
range(1, 10) # prints list of ints 1 to 9. returns its own kind of object. convert to list.DOES NOT INCLUDE 10 ex. list(range(1,10))
 
 
del test_list[1] # deletes item at index 1 in test_list. ex.2 del test_list will delete test_list completely
del test_list[0:2] # deletes first and 2nd index of the list.
test[2] # prints char in 2 index of test. WORKS ON STRINGS AND LISTS. RETURNS CHAR OR INT
test[-1] # counts index from other end. can be used at any point in a slice.
test[0:5] # prints chars in 0-4 indexs. DOES NOT INCLUDE INDEX 5. WORKS ON STRINGS AND LISTS. RETURNS LIST.
test[:5] # exact same as above. if you exclude the starting point it defaults to 0.
test[0:] # if you exclude ending point it defaults to the end of the list.
test[0:len(test)] # exact same as above len of list will include all items because index starts at 0.
test[:len(test)] # same as above
test[:] # defaults as whole list
test[:5:2] # 0-4 indexes steped by 2
test[0::2] # start from 0 to end of list stepped by 2
test[::2] # whole list steped by 2
"String"[::-1] # works on strings, can also negitive step to reverse
test[5:0:-1] # remember to start at the last index and stop at the first w/ negitive step
test[4:7] = ['e', 'f'] # replaces 4,5,6 indexes with e and f
 
 
test_dict = {names: {first: kenneth, last: gabbara}} #dicts are nestable
test_dict = ['key'] # prints out value connected to key
test_dict = ['key']['subkey'] # acceses subkey data withing key dict.
test_dict['key'] = data # assigns data to key inside test_dict
del test_dict['key'] # deletes key and assosiated data
test_dict.update({'newkey': newdata}) #update function can add multiple key:data to dict at once.
test_dict.values() # access to just values
test_dict.items() # allows you to loop thoughs keys and values. i.e. for key, value in test_dict.items():
 
test_string= "Hi my name is {name}!" # example string with named placeholder
test_string.format('name':'Kenny')   # example of manual formatting
test_dict = {'name': 'Kenny'}        # example dict
test_string.format(**test_dict)      # example of automated genertiion of data from a dict to string formatting.
print(mydict[key]) # need [key] to access key
 
 
test_tuple = (1, 2, 3) # sample tuple creation
test_tuple[1] # accesing an index of tuple
test_tuple = tuple([1, 2, 3]) # tuple function makes tuple out of iterable type
 
a, b = 1, 2     # assigns a= 1, b = 2
c = (3, 4)      # assigns c = (3,4)
d, e = c        # assigns d = 3, e = 4
a, b = b, a     # swaps values of a and b
 
 
 
 
#-----------------------------------class--------------------------------------
class Test:   # class names start with a capital letter. classes contain data that defines a type of object
    def __init__(self, attribute1=1, attribute2=1): #method init takes att1 and att2 as arguments at init stage & sets 1 as default(this is optional).
        self.attribute1 = attribute1
        self.attribute2 = attribute2
 
    def addAtt(self):                      # classes can have functions inside them called methods
        addAttNum =attribute1 + attribute1 # can only be called to a instance of the class not the class itself.
        return addAttNum                   # ex. test1.addAtt()
 
class Test():
    def __init__(self, **kwargs):
        self.attribute1 = kwargs.get(attribute1, 1)  # Test atributes can be initiated at instance creation
        self.attribute2 = kwargs.get(attribute2, 1)  # if not, they will default to 1
 
class Test(inheritance): # this example shows a class Test that inherits inheritance
    attribute1 = x
    attribute2 = y       # attributes assigned to class Test.
 
Test.attribute # Class.attribute will return the value of the atribute inside the class Test. does not requite () at the end.
 
test1 = Test() # initiates a test1 instance of the Test class.
test1.attribute = x # changes the value of atribute in test1 to x. DOES NOT CHANGE CLASS, ONLY INSTANCE.
del test1 # deletes instance test1 of Test class
 
#----------------------------example-------------------------------------------
 
import random
 
COLORS = ['yellow', 'red', 'blue', 'green']
 
 
class Monster():  # class defualts are set here. use object in paramater to make compatible with python 2 and 3 at the same time.
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'
 
    def __init__(self, **kwargs):  # makes it possible to set atrubutes during instance creation. see bottom of section for example.
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)
 
        for key, value in kwargs.items():
            setattr(self, key, value)  # setattr is a function that sets a atribute. takes 3 arguments: instance (self), item, and the value to pass in
 
 
    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)
 
    def battlecry(self):
        return self.sound.upper()
 
 
class Dragon(Monster): # if atribute is not expressed in this class, it is inherited from the Monster class.
    min_experience = 5  # if 'pass' is used it uses all Monster's defaults/
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
 
 
jabberwock - Monster(color='blue', sound='wiffling', hit_points=500, adjective ='manxsome') # Monster instance that overrides some sefaults and adds a new attrabute
drogon = Dragon(color='red', hit_points=2000) # if class in other file have to use dot notation. ex. drogon = reference.Dragon() replace reference with file name.
 
 
# ----------------------------------class instance method example------------------------------------
 
class Character():
    experience = 0
    hit_points = 10
 
    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
 
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif: weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.get_weapon()
 
    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()
 
        for key, value in kwargs.items():
            setattr(self, key, value)
