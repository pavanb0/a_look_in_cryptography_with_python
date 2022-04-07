# a_look_in_cryptography_with_python
enter valid key = root 
set password from 1-100 
if enterd zero it will give zero division error 
if password value exced 100 may be give garbage value
########################################################
                  HOW CODE WORKS!!
encryption:
    1)take message in string 
    2)convert into binary list example ['1,','0','1,','0','1','0','1','0','1,','0','1,','0','1','0','1','0']
    3)replace 1 with 0 vice versa example ['1,','0','1,','0','1','0','1','0','1,','0','1,','0','1','0','1','0']
    4)split list into 8-8-8 part example [['1,','0','1,','0','1','0','1','0'],['1,','0','1,','0','1','0','1','0']]
    5)take list[0] item in lis convert it into int form exapmle 10101010
    6)divide by key2 append &
    7)return encrypted list
    
decryption:
    1)take encrypted string "1666685.0 & 1668333.3333333333 & 1666835.0 &
    2)remov last most &
    3)split list by & using re and return list of digits
    4)process list to numbers and multiply by key2
    5)creat into 1011101010101010 form
    6)replace 1 with 0 vice versa example
    7)binary to text 
    8)return text
##########################done###########################
