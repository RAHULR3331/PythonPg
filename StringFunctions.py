name="Rahul";
print(name);
print(len(name));
print(name[2]);

# printing character by character using for loop

for i in name:
    print(i);

# for printing it in same line 

for i in name:
    print(i,end="");

# Slicing 
# In between  
print(name[0:3]);

# from begining to the known end 
print(name[:3]);

# from the known brgining to the end of the string 
print(name[0:2]); 

# METHODS 

#  for print in UpperCase 
print(name.upper());

# for print in lowercase 
print(name.lower());

# for find a perticular character the String'
    # Find()
print(name.find('l'));
    #index()    
print(name.index('l'));

# converting a String to the list (The letter by letter the value will be Strored in the list)
x=name.split(" ");
print(x);

# FOR REPALCE A STRING WORD OR CHARACTER USING THE  REPLACE ()
print(name.replace('R','A'));

# String Concatination 
str1='good';
str2='morning';
str3= str1+" "+str2;
print(str3);


















