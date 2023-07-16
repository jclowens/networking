import locale
import socket #import socket to switch the hex to ip addresses
'''
Python Lab #1: Numbers, Math Operators, Strings, and Lists
These labs are meant to familiarize yourself with the topics discussed in class.
'''

#Use the following list for questions 1-7.
list1 = [5, '3.2', 'python', 9.8, 'rocks', 2]

#1. Assign the integer 5 to the variable a
a = list1[0]
print(a)

#2. Slice the list to only contain '3.2', 'python', and 9.8
#copying list2 to make list 2
slicedlist = list1[1:4]
print(slicedlist)

#3. Using the values contained in the list, print five to the second power
power = list1[0] ** list1[5]
print(power)

#4. Create a string that states 'python rocks'
rocks = list1[2] + ' ' + list1[4]
print(rocks)

#5. Add 2 to 3.2 to get 5.2
addition = list1[-1] + float(list1[1])
print(addition)

#6 Create the string '9.825'
number1 = str(list1[3]) + str(list1[-1]) + str(list1[0])
print(number1)

#7. What is the data type of '3.2' in list1? Assign this to a new variable but make the data type a float.
dtype = float(list1[1])
print(dtype)

#8. Manipulate the two strings to create one string that prints "The Earth is ROUND"
b = "       The Earth is flat"
c = 'A sphere is round'
bandc = b[7:20] + c[12:17].upper()
print(bandc)

#9 What does the following string decode to? (Use UTF-8 to decode)
bytesObj = b'\x68\x65\x6C\x6C\x6F'
bytesObj.decode()
print(bytesObj)

#Use the following string and list to answer questions 10-11
list2 = [580, 'latptop', 1999, 'PC', 450, 'console']

#10. Format a string that prints "This PC costs $1999.00". Make sure the price has two decimal places.
sentence = 'This ' + list2[3] + ' costs ' + "${:,.2f}".format(list2[2])
print(sentence)

#11. Assign list2 to a new variable, list3. Now change 580 in list2 to 600. What is the first value in list3? Make a
# copy of list3 called list4, make sure list4 is not linked to list3.
list3 = list2 #these lists are now the same
list2[0] = 600 #change index 0 to 600

list4 = list3.copy() #copying makes completely separate list
list4[0] = 50000
print(list3)
print(list4)
#12. What is the result of an exclusive OR between 10111011 and 00110111? Print the result twice, the first in binary,
# and the second in hex.
num1 = 0b10111011
num2 = 0b00110111

result = num1 ^ num2

print(bin(result))  # Output: '0b10001100' (binary representation)
print(hex(result))  # Output: '0x8C' (hexadecimal representation)

#Use the following dictionary to answer questions 13-16.
dictionary1 = {'attackBox': 'kali', 'redirector': 'centOS', 'target': 'solaris'}

#13. Assign all the dictionary keys to a new variable called keys, and print it.
keys = dictionary1.keys() #assigning and printing all keys
print(keys)

#14. Change the value of the target key to 'Windows 7', and then print the all the key:value pairs.
dictionary1['target'] = 'Windows 7' #changing target keys value to Windows 7 
print(dictionary1)

#15. Add a new key to the dictionary called networkIPs, the corresponding value will the list ['10.10.10.1', '10.10.10.254']
dictionary1.update({'networkIPs': ['10.10.10.1', '10.10.10.254']})
print(dictionary1)

#16. Assign dictionary1 to a new variable, dictionary2. In dictionary1, change the value of the redirector key to 'freeBSD'.
# Print dictionary2, did your change in dictionary1 carry over to dictionary2? If so, why? If you wanted to make an un-linked
# copy of a dictionary, what command would you use?
dictionary2 = dictionary1
dictionary1['redirector'] = 'freeBSD' #still linked copy
print(dictionary2)
# dictionary2 = dictionary1.copy() to make unlinked copy

# Given the following list, answer questions 17-19.
nestedList = [[1, 2, 3], [4, 5, 6], [7, [8, 9]], [10, [11, [12, 13]]]]

#17. Print the value 10
nvalue = nestedList[3][0]
print(nvalue)

#18. Print the values 5, 8, and 11
avalue = nestedList[1][1] #indexing at list 2 spot 1
bvalue = nestedList[2][1][0] #indexing at list 2, list 1, then spot 0
cvalue = nestedList[3][1][0]

print(avalue)
print(bvalue)
print(cvalue)

#19. Print the value 13
dvalue = nestedList[3][1][1][1]
print(dvalue)

'''
Practical Example: Below is a hex dump from a packet capture in the format of a string. By using slicing, we can assign
bytes to their corresponding variables, which are listed below. An example is provided of how to slice the hex dump and 
convert the hexadecimal characters into an easy to read format for the source IP. 
'''

hexDump = '78d2 94a6 75b1 147d da12 34dc 0800 4500 ' \
          '0059 0000 4000 4006 1287 c0a8 010f c0a8 ' \
          '0101 f87c 01bb 5087 e285 2849 991d 8018 ' \
          'ffff fdc3 0000 0101 080a 77cb d864 2c59 ' \
          '6086 1703 0300 20bb 6b4a 14a0 035f 1328 ' \
          'd698 b300 4991 9a48 a150 7aef 3b58 682a ' \
          'f343 fc6b 2fe2 67'

#Ethernet Header
destMac = hexDump[0:14]
sourceMac = hexDump[15:29]

#IP Header
ipVersion = hexDump[35:36]
headerLength = hexDump[36:37]
totalLength = hexDump[40:44]
flagsAndOffset = hexDump[50:54]
ttl = hexDump[55:57]
ipProtocol = hexDump[57:59]
checksum = hexDump[60:64]
sourceIP = hexDump[65:74] #format(int(sourceIP[0:2], 16), int(sourceIP[2:4], 16), int(sourceIP[5:7], 16), int(sourceIP[7:9], 16)))

destIP = hexDump[75:84]

#TCP Header
sourcePort = format(int(hexDump[85:89], 16)) #changed formatting
destPort = format(int(hexDump[90:94], 16))
dataOffset = hexDump[115:119]



print("The IP address is {}.{}.{}.{}".format(int(sourceIP[0:2], 16), int(sourceIP[2:4], 16), int(sourceIP[5:7], 16), int(sourceIP[7:9], 16)))

#20. Use the example to create a format string that will take any hex dump, formatted like the one above, and print the
# IP address and port the traffic is coming from, and the IP address and port it is going.
print("The Source IP address is {}.{}.{}.{}".format(int(sourceIP[0:2], 16), int(sourceIP[2:4], 16), int(sourceIP[5:7], 16), int(sourceIP[7:9], 16)))
print("The Source port is " + sourcePort)
print("The Destination IP address is {}.{}.{}.{}".format(int(destIP[0:2], 16), int(destIP[2:4], 16), int(destIP[5:7], 16), int(destIP[7:9], 16)))
print("The Destination port is " + destPort)

#21. Create a dictionary called networkDictionary with keys 'source', 'destination', and 'ipProtocol'. Assign them the
# correct values.

# i imported sockets for this
networkDictionary = {}

# Assign values for Ethernet Header
networkDictionary['source'] = hexDump[0:14]
networkDictionary['destination'] = hexDump[15:29]

# Assign values for IP Header
networkDictionary['source'] = socket.inet_ntoa(bytes.fromhex(sourceIP))
networkDictionary['destination'] = socket.inet_ntoa(bytes.fromhex(destIP))

# Assign values for IP Protocol
networkDictionary['ipProtocol'] = hexDump[57:59]

print(networkDictionary)
