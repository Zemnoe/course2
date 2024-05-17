str = "The quick brown fox jumps over the lazy dog"


print(str)


print(len(str))


print(str.upper())

print(str.lower())

print(str.title())

reverse_str = str[::-1]
print(reverse_str)

reverse_str = str[::-1]
print(reverse_str.title())

print(str.count("a"))

print(str.count("the"))

print(str.replace("the","a"))



#create dictionary to store key value
dict = {}
for i in str:
    #if i  exist as key in dict, icrement the count
    if i in dict:
        dict[i] += 1
        #else if i appears for the first time, add else
    else:
        dict[i]=1
        print(dict)




people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

x=  zip(people, sex, age)
print(people, sex ,age)
for people,sex,age in zip (people,sex,age):
    print(f"{people} the {sex} is {age} years old")





