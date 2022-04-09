# after taking insperation from WW2 enigma machine
# createad by pavan in april 2022
# follow me github pavanb0
# update now code can directly encrypt decrypt files
import re
import os
import time


class enigma:

    def split_list(self, alist, wanted_parts=1):
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    def list_to_str(self, li):
        listToStr = ' '.join([str(elem) for elem in li])
        return listToStr

    def convert(self, list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return (res)

    def string_to_list(self, des):
        rs = ''.join(format(i, '08b') for i in bytearray(des, encoding='utf-8'))
        res = [int(x) for x in str(rs)]
        return res

    def encrypt(self, code, key, key2):
        if key == "root":
            res = self.string_to_list(code)
            for i in range(len(res)):
                if res[i] == 1:
                    res[i] = 0
                else:
                    res[i] = 1
            if len(res) % 2 != 0:
                res.append(8)
            size = int(len(res) / 8)
            length = len(res)
            li = self.split_list(res, wanted_parts=size)
            new_list = []
            for i in range(size):
                new = self.convert(li[i])
                ks = new / key2
                new_list.append(ks)
                new_list.append("&")
            o = self.list_to_str(new_list)
            return [li, new_list, o]
        else:
            return "invalid key"


class concord:
    def int_to_list(self, n):
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        return l

    def binary_to_result(self, bits):
        n = int(bits, 2)
        result = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        return result

    def convert(self, list):
        res = sum(d * 10 ** i for i, d in enumerate(list[::-1]))
        return (res)

    def maybeMakeNumber(self, s):
        if not s:
            return s
        try:
            f = float(s)
            i = int(f)
            return i if f == i else f
        except ValueError:
            return s

    def int_to_list(self, n):
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        return l

    def creat_binary(self, list):
        newlist = []
        for i in range(len(list)):
            eg = self.int_to_list(list[i])
            for k in range(8):
                if eg[k] == 0:
                    newlist.append(1)
                else:
                    newlist.append(0)
        return newlist

    def decryptor(self, code, key, key2):
        try:
            if key == "root":
                lie = []
                x = 0
                code2 = code[:-1]
                cod = re.split("&", code2)
                converted = list(map(self.maybeMakeNumber, cod))
                pl = int(key2)
                my_new_list = [i * key2 for i in converted]
                lie = self.creat_binary(my_new_list)
                lie2 = (self.convert(lie))
                w3schools_is_my_love = str(lie2)
                if lie[0] == 0:
                    "0" + w3schools_is_my_love
                elif lie[1] == 0:
                    "0" + w3schools_is_my_love
                return [lie, lie2, w3schools_is_my_love]
            else:
                return [0, 0, "invalid syntax"]
        except Exception:
            print("errors occured during execution")


f = enigma()

# resone not to enherit class because function overloading

q = ""
while True:
    code = ""
    key = ""
    key2 = 0
    ##################################### encoding
    q = str(input("what you want to do encode/decode\n==: "))
    q.lower()

    while q == "encode":
        user_input = str(input("encode text file or text on consol consol/textfile :"))
        user_input.lower()
############################### encoding consol ##################################
        if user_input == "consol":
            message = str(input("enter message to encrypt : "))
            key = str(input("enter valid key :"))
            key2 = int(input("enter password only intiger :"))
            c = f.encrypt(message, key, key2)
            out = c[2]
            print("this is your encrypted messeage copy:  ", out)
            ws = str(input("want to encode again!! yes/no :"))
            ws.lower()
            if ws == "no":
                break
########################### encoding text file ############################
        elif user_input == "textfile":
            message = str(input("enter textfile path to encrypt : "))
            key = str(input("enter valid key :"))
            key2 = int(input("enter password only intiger :"))
            messageout = message + "out"
            message_escapeseq = re.escape(message)
            message_escapese = re.escape(messageout)
            message_escapeseq_inp = message_escapeseq + ".txt"
            message_escapese_out = message_escapese + ".txt"
            file1 = open(message_escapese_out, 'w')
            with open(message_escapeseq_inp) as d:
                contents = d.read()
                c = f.encrypt(contents, key, key2)
                out = c[2]
                file1 = open(message_escapese_out, "a")  # append mode
                file1.write(out)
            file1.close()
            print("this is your encrypted file is saved on desktop:  ")
            ws = str(input("want to encode again!! yes/no :"))
            ws.lower()
            if ws == "no":
                break
#################################################### decoding##########################
    while q == "decode":
        user_input = str(input("decode text file or text on consol consol/textfile :"))
        user_input.lower()
  ##################################### decoding consol ##########################
        if user_input == "consol":
            try:
                c = concord()
                code = str(input("enter message to decrypt :"))
                key = str(input("enter valid key :"))
                key2 = int(input("enter password only intiger :"))
                d = c.decryptor(code, key, key2)
                x = "0" + d[2]
                print("your decrypted code = ", '"', c.binary_to_result(x), '"')
                ws = str(input("want to continue yes/no :"))
                ws.lower()
                if ws == "no":
                    break
            except Exception:
                print("errors")
########################################## decoding textfile ################################
        elif user_input == "textfile":
            try:
                ac = concord()
                message = str(input("enter textfile path to decrypt : "))
                key = str(input("enter valid key :"))
                key2 = int(input("enter password only intiger :"))
                messageout = message + "new"
                message_escapeseq = re.escape(message)
                message_escapese = re.escape(messageout)
                message_escapeseq_inp = message_escapeseq + ".txt"
                message_escapese_out = message_escapese + ".txt"
                file1 = open(message_escapese_out, 'w')
                time1 = time.time()
                with open(message_escapeseq_inp) as d:
                    contents = d.read()
                    ds = ac.decryptor(contents, key, key2)
                    x = "0" + ds[2]
                    out = ac.binary_to_result(x)
                # print(out) optional only
                file1 = open(message_escapese_out, "a")  # append mode
                file1.write(out)
                file1.close()
                time2 = time.time()
                tim = time2 - time1
                print("this is your encrypted file is saved on desktop:  \n that took ", tim, " seconds")
                ws = str(input("want to encode again!! yes/no :"))
                ws.lower()
                if ws == "no":
                    break
            except Exception:
                print("errors")
    cx = str(input("want to exit yes/no :"))
    cx.lower()
    if cx == "yes":
        break
################################# pleas gui #################################################