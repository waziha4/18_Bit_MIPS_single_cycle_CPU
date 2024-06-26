def convertBinToHex(bin):
    hex = " "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex

# For 18 bit isa
# ADD   r3    r4     r5
# 000001  0011  0100   0101
# 1     3      4      5
# 1345

def checkInstruction(inst):
    convertInstruction = " "
    if inst == "beq":
        convertInstruction = "000000"
    elif inst == "add":
        convertInstruction = "000001"
    elif inst == "and":
        convertInstruction = "000010"
    elif inst == "sw":
        convertInstruction = "000011"
    elif inst == "addi":
        convertInstruction = "000100"
    elif inst == "nop":
        convertInstruction = "000101"
    elif inst == "sub":
        convertInstruction = "000110"
    elif inst == "slt":
        convertInstruction = "000111"
    elif inst == "j":
        convertInstruction = "001000"
    elif inst == "lw":
        convertInstruction = "001001"
    elif inst == "sll":
        convertInstruction = "001010"

    else:
        convertInstruction = "Invalid instructions"
    return convertInstruction


def checkRegister(reg):
    convertReg = ""
    if reg == "r0":
        convertReg = "0000"
    elif reg == "r1":
        convertReg = "0001"
    elif reg == "r2":
        convertReg = "0010"
    elif reg == "r3":
        convertReg = "0011"
    elif reg == "r4":
        convertReg = "0100"
    elif reg == "r5":
        convertReg = "0101"
    elif reg == "r6":
        convertReg = "0110"
    elif reg == "r7":
        convertReg = "0111"
    elif reg == "r8":
        convertReg = "1000"
    elif reg == "r9":
        convertReg = "1001"
    elif reg == "r10":
        convertReg = "1010"
    elif reg == "r11":
        convertReg = "1011"
    elif reg == "r12":
        convertReg = "1100"
    elif reg == "r13":
        convertReg = "1101"
    elif reg == "r14":
        convertReg = "1110"
    elif reg == "r15":
        convertReg = "1111"
    else:
        convertReg == "Invalid Register"

    return convertReg


def decimalToBinary(num):
    if (num < 0):
        num = 16 + num

    ext = ""
    result = ""

    while (num > 0):
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        # result = (num%2 == 0 ? "0" : "1") + result
        num = num // 2

    for i in range(4 - len(result)):
        ext = "0" + ext

    result = ext + result

    return result


# a[1,6,7,8]
# for(i=0, i<4, i++ )
#    {
#        a[i];
#    }

# a = ['apple', 'ball', 'cat', 'dog']
# for i in a:
#    i

readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

# A quick brown fox jumped over a lazy dog

# print(f.readline())
for i in readf:
    splitted = i.split()

    if (splitted[0] == "add" or splitted[0] == "sub" or splitted[0] == "and" or splitted[
        0] == "sll" or splitted[0] == "slt" or splitted[0] == "nop"):

        conv_inst = convertBinToHex(checkInstruction(splitted[0])[-4:])
        conv_rs = convertBinToHex(checkRegister(splitted[1]))
        conv_rt = convertBinToHex(checkRegister(splitted[2]))
        conv_rd = convertBinToHex(checkRegister(splitted[3]))

        out = conv_inst + conv_rs + conv_rt + conv_rd
        print(out)
        writef.write(out + "\n")

    elif (splitted[0] == "lw" or splitted[0] == "sw" or splitted[0] == "beq" or splitted[0] == "addi"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0])[-4:])
        conv_rs = convertBinToHex(checkRegister(splitted[1]))
        conv_rt = convertBinToHex(checkRegister(splitted[2]))
        conv_im = convertBinToHex(decimalToBinary(int(splitted[3])))

        out = conv_inst + conv_rs + conv_rt + conv_im
        print(out)
        writef.write(out + "\n")

    elif (splitted[0] == "j"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0])[-4:])
        # conv_target = convertBinToHex(decimalToBinary(int(splitted[1])))
        hexval = hex(int(splitted[1]))
        exF2 = hexval[2:]
        ext = ""
        for i in range(3 - len(exF2)):
            ext = "0" + ext

        conv_target = ext + exF2

        out = conv_inst + conv_target
        print(out)
        writef.write(out + "\n")