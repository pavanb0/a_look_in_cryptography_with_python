#createad by pavan in april 2022
#after taking insperation from WW2 enigma machine
#follow me github pavanb0
import re
class enigma:

    def split_list(self,alist, wanted_parts=1):
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    def list_to_str(self,li):
        listToStr = ' '.join([str(elem) for elem in li])
        return listToStr

    def convert(self,list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return (res)

    def string_to_list(self,des):
        rs = ''.join(format(i, '08b') for i in bytearray(des, encoding='utf-8'))
        res = [int(x) for x in str(rs)]
        return res
    def encrypt (self,code,key,key2):
        if key=="root":
            res = self.string_to_list(code)
            for i in range(len(res)):
                if res[i]==1:
                    res[i]=0
                else:
                    res[i]=1
            if len(res)%2!=0:
                res.append(8)
            size = int(len(res)/8)
            length=len(res)
            li=self.split_list(res,wanted_parts=size)
            new_list=[]
            for i in range(size):
                new=self.convert(li[i])
                ks=new/key2
                new_list.append(ks)
                new_list.append("&")
            o=self.list_to_str(new_list)
            return [li,new_list,o]
        else:
            return "invalid key"

class concord:
    def int_to_list(self,n):
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        return l


    def binary_to_result(self,bits):
        n = int(bits, 2)
        result=n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        return result

    def convert(self,list):
        res = sum(d * 10 ** i for i, d in enumerate(list[::-1]))
        return (res)


    def maybeMakeNumber(self,s):
        if not s:
            return s
        try:
            f = float(s)
            i = int(f)
            return i if f == i else f
        except ValueError:
            return s


    def int_to_list(self,n):
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        return l


    def creat_binary(self,list):
        newlist = []
        for i in range(len(list)):
            eg = self.int_to_list(list[i])
            for k in range(8):
                if eg[k] == 0:
                    newlist.append(1)
                else:
                    newlist.append(0)
        return newlist


    def decryptor(self,code,key, key2):
        if key=="root":
            lie=[]
            x=0
            code2 = code[:-1]
            cod = re.split("&", code2)
            converted = list(map(self.maybeMakeNumber, cod))
            pl = int(key2)
            my_new_list = [i * key2 for i in converted]
            lie=self.creat_binary(my_new_list)
            lie2=(self.convert(lie))
            w3schools_is_my_love=str(lie2)
            if lie[0]==0:
                "0"+w3schools_is_my_love
            elif lie[1]==0:
                "0" + w3schools_is_my_love
            return [lie,lie2,w3schools_is_my_love]
        else:
            return "invalid syntax"

f=enigma()
#resone not to inheriting class because fuction overloading
def ask_credential():
    key = str(input("enter valid key :"))
    key2=int(input("enter password only intiger :"))
    return [key,key2]
q=""
while True:
    code = ""
    key = ""
    key2 = 0
##################################### encoding
    while True:
        q=str(input("what you want to do encode/decode\n==: "))
        q.lower()
        break
    while q=="encode":
        message = str(input("enter message to encrypt : "))
        key = str(input("enter valid key :"))
        key2=int(input("enter password only intiger :"))
        c=f.encrypt(message,key,key2)
        out=c[2]
        print("this is your encrypted messeage copy:  ",out)
        ws = str(input("want to encode again!! yes/no :"))
        ws.lower()
        if ws == "no":
            break
#################################################### decoding
    while q=="decode":
        c = concord()
        code=str(input("enter message to decrypt :"))
        key = str(input("enter valid key :"))
        key2=int(input("enter password only intiger :"))
        d = c.decryptor(code, key,key2)
        x="0"+d[2]
        print("your decrypted code = ",'"',c.binary_to_result(x),'"')
        ws=str(input("want to continue yes/no :"))
        ws.lower()
        if ws=="no":
            break
    cx = str(input("want to exit yes/no :"))
    cx.lower()
    if cx == "yes":
        break
##################################################################################