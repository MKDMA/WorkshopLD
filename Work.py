#Declaring variables

a1="abc"
a2="def"
a3="ghi"

#Using find command

print "variable options \na1 \na2 \na3\n"

a00 = raw_input("enter the variable to search: ")
if a00 =="a1" or a00=="a2" or a00=="a3": #if anything else input script stops
    a01 = raw_input("enter the string to find: ")

    a11 = a00.find(a01)

    if a11 > 0:
        print "%s is at index %i\n\n" %(a01, a11)
    else:
        print "%s is not present\n\n" %a01
  
    
#String addition

    a06=a1+a2
    print "a1 + a2 = %s\n\n" %(a06)
    
    a4=3*a1[2]+4*a2[1]
    print "3*a1[2]+4*a2[1] = %s\n\n"%(a4)

# "read write with string files"

    print "read write with string files\n"

    a5 = open('D:/11Apr2015_PythonWorkshop/file1.txt', 'w')
    a5.write('This is the first file. ')

    a7=open('D:/11Apr2015_PythonWorkshop/file1.txt', 'a')
    a7.write("\nThis is first + second file. ")

    a8=open('D:/11Apr2015_PythonWorkshop/file1.txt', 'a')
    a8.write("\nThis is first + second + third file.")

    a9= open('D:/11Apr2015_PythonWorkshop/file1.txt', 'a')
    a9.write("\nThis is the joined fine")

    a5.close()
    a7.close()
    a8.close()
    a9.close()

    a10=open('D:/11Apr2015_PythonWorkshop/file1.txt', 'r')
    print a10.read() 
    print " \nAll three files are joined as file1.txt"

else:
    print "choose correct variable"










