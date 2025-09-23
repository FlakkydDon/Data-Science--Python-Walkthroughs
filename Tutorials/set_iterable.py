# Manipulating the list
myset = {50, 20, 80, 40, 50, True, 1}
your_set = {50, 20, 80, 40, 50, False, 0}
print(myset)
print(your_set)
print(type(your_set))  # finding out the data type
your_set.add('baby')  # add new item to your_set
print(your_set)

# update a set to a list in order to append the list
your_set = [50, 20, {80, 40, 50}, False, 0]
my_list = [list(x) if isinstance(x, set) else x for x in your_set]
you_set = [50, 20, {80, 40, 50}, False, 0]
myList = list(you_set[2])
print(myList)
print(type(myList))
my_list1 = [list(x) if isinstance(x, set) else x for x in your_set]

print(my_list1)

my_list[2].append(36)
print(my_list)
print(type(my_list1))

#  JOINS
#  Unions: used to join set to multiple set or iterable
# while a set | is used to join a set with another set
t = {5, 8, 9, 10}  # set data type
z = {"love", "ball", "games"}  # set datatype
u = {34, "red", "leg", "arm"}  # a set datatype
k = (14, 29, 30, 23)  # tuple data type

# Union of the set creates a new variable
w = t.union(z)  # method 1 using .union()
print(w)
y = t | u  # method 2 using the |
print(y)

j = t.union(k)  # Adding a tuple data type to a set data type
print(j)

#  Update is used to join set to multiple iterable
# != used to join a set to a set, this only changes the later set e.g
z.update(k)
print(z)

# k |= z NOTE: This notation cannot be used to join a tuple to a set

t |= z
print(t)

# Interception (&)
# Example I : Finding the unique items between sweet and full
sweet = {"junks", "yummy", "cool"}
full = {"yummy", "cool", "wow", "chicken"}
s_f = full & sweet
print(s_f)


# Example II
wip = {"calendar", "cool", "junks", "yummy"}

# Finding the intercept between all 3 sets
swip = full & sweet & wip
print(swip)

# Using the keyword intersection
rap = {"jokes", "junks", "calendar", 'grape', "yummy"}

s_j = full.intersection(sweet, wip, rap)  # Note this keyword can also be used for update
print(s_j)

#  Intersection_Update
rap.intersection_update(wip, sweet)  # retains only items common in both set a
print(wip)
print(sweet)
print(rap)


# Using the interception_update notation(&=)
wip &= sweet
print(wip)  # Accepts only one argument

# Difference (-): outputs the difference between the 2 sets with reference to set1
sweet = {"junks", "yummy", "cool"}
jk = {"jokes", "junks", "calendar", 'grape', "yummy"}
duh = jk.difference(sweet, full) # takes multiple arguments
print(duh)

# Difference_update (-=)
jk.difference_update(sweet, wip)
print(jk)  # note no new objects are created it only

wip -= rap
print(wip)

# Symmetric Difference (^)
egg = {"bread", "dinner", "breakfast", "yummy", "jokes"}
sy_d = egg.symmetric_difference(duh) # Note: takes only one argument
print(sy_d)

# Symmetric_difference_update (^=)
sy_d.symmetric_difference_update(sweet)
print(sy_d)


#  Isdisjoint: this is outputs a boolean (True/ False)
#  When they have items in common = False
#  When there is no common items = True

#  Example I
g = {3, 2, 8, 9, 10, 5, 6}
u = {28, 3, 9, 1, "fly"}
j = {4, 9, 2, 8, "red", "dog", "gok"}
t2 = {"hide", "seek", "test"}
t = {5, 8, 9, 10}


o_d = g.isdisjoint(u)
dd = u.isdisjoint(j)
jd = u.isdisjoint(t2)
print(o_d)
print(dd)
print(jd)

# Issubset
kd = g.issubset(u)
print(kd)

# Issuperset
hum = j. issuperset(t2)
print(hum)

# Proper subset (<)
sej = u < t
print(sej)

#  Proper superset(>)
gut = u > t
print(gut)

#  Set Methods: remove, discard, pop, clear and delete
#  DISCARD will not give an error even when an
#  item is not present, on the contrast remove will.
#  POP removes an item at random and return it as an object
# e.g:
v = {4, 5, 7, 8, 10}
k = {3, 8, 6,1}
w = v.pop()
print(v)
print(w)

# Clear is used to empty the set and return an empty set
k.clear()
print(k)

# Using delete, you cannot print out the set,
# it raises a NameError.
# del c- remember no dot, just del and name of the set
# using del deletes the entire set from record
# unlike when using list[] and tuple() which you can index.


