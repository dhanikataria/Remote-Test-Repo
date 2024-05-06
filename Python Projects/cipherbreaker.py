#hello
from operator import xor
from collections import Counter
from heapq import nlargest

bin_s_box = {"0000": "1110", "0001": "0100", "0010": "1101", "0011": "0001", "0100": "0010", "0101": "1111",
             "0110": "1011", "0111": "1000", "1000": "0011", "1001": "1010", "1010": "0110", "1011": "1100",
             "1100": "0101", "1101": "1001", "1110": "0000", "1111": "0111"}
print()
key1 = int(input("[*] Enter the key 1 as 16-bit binary string: "),2)
print()
key2 = int(input("[*] Enter the key 2 as 16-bit binary string: "),2)
print()
key3 = int(input("[*] Enter the key 3 as 16-bit binary string: "),2)
print()
key4 = int(input("[*] Enter the key 4 as 16-bit binary string: "),2)
print()
key5 = int(input("[*] Enter the key 5 as 16-bit binary string. This Key will be Brute Forced: "),2)
print()


def keymixing1(Combinedpickp1):
    Splittedkeymixed1=[]
    tempmix1 = int(Combinedpickp1, 2)
    keymixed1IntegerForm=(xor(tempmix1,key1))
    keymixed1StringBinary=binbits(keymixed1IntegerForm,16)
    for rr in range(0, len(keymixed1StringBinary),4):
        tempkeysplit_output = keymixed1StringBinary[rr:rr + 4]
        Splittedkeymixed1.append(tempkeysplit_output)
    return Splittedkeymixed1

def keymixing2(Combinedpickp1):
    Splittedkeymixed1=[]
    tempmix1 = int(Combinedpickp1, 2)
    keymixed1IntegerForm=(xor(tempmix1,key2))
    keymixed1StringBinary=binbits(keymixed1IntegerForm,16)
    for rr in range(0, len(keymixed1StringBinary),4):
        tempkeysplit_output = keymixed1StringBinary[rr:rr + 4]
        Splittedkeymixed1.append(tempkeysplit_output)
    return Splittedkeymixed1

def keymixing3(Combinedpickp1):
    Splittedkeymixed1=[]
    tempmix1 = int(Combinedpickp1, 2)
    keymixed1IntegerForm=(xor(tempmix1,key3))
    keymixed1StringBinary=binbits(keymixed1IntegerForm,16)
    for rr in range(0, len(keymixed1StringBinary),4):
        tempkeysplit_output = keymixed1StringBinary[rr:rr + 4]
        Splittedkeymixed1.append(tempkeysplit_output)
    return Splittedkeymixed1

def keymixing4(Combinedpickp1):
    Splittedkeymixed1=[]
    tempmix1 = int(Combinedpickp1, 2)
    keymixed1IntegerForm=(xor(tempmix1,key4))
    keymixed1StringBinary=binbits(keymixed1IntegerForm,16)
    for rr in range(0, len(keymixed1StringBinary),4):
        tempkeysplit_output = keymixed1StringBinary[rr:rr + 4]
        Splittedkeymixed1.append(tempkeysplit_output)
    return Splittedkeymixed1

def keymixing5(Combinedpickp1):
    Splittedkeymixed1=[]
    tempmix1 = int(Combinedpickp1, 2)
    keymixed1IntegerForm=(xor(tempmix1,key5))
    keymixed1StringBinary=binbits(keymixed1IntegerForm,16)
    for rr in range(0, len(keymixed1StringBinary),4):
        tempkeysplit_output = keymixed1StringBinary[rr:rr + 4]
        Splittedkeymixed1.append(tempkeysplit_output)
    return Splittedkeymixed1

def filter_cipher(ciphertext):
    splitted_ciphertext=[]
    filteredciphertext=[]
    for cc in range (0,5000,1):
        temp4=ciphertext[cc]
        for dd in range(0, len(temp4),4):
            tempciphersplit_output=temp4[dd:dd+4]
            splitted_ciphertext.append(tempciphersplit_output)

        if((splitted_ciphertext[0]=="0000") and (splitted_ciphertext[2]=="0000")):
            temp55 = "".join(splitted_ciphertext)
            filteredciphertext.append(temp55)
            splitted_ciphertext.clear()
        else:
            splitted_ciphertext.clear()

    return filteredciphertext

def convertFunction(ToConvert):
    splitted_ciphertext = []
    integerList=[]
    for dd in range(0, len(ToConvert), 4):
        tempciphersplit_output = ToConvert[dd:dd + 4]
        splitted_ciphertext.append(tempciphersplit_output)
    integerList.append(int(splitted_ciphertext[0], 2))
    integerList.append(int(splitted_ciphertext[1], 2))
    integerList.append(int(splitted_ciphertext[2], 2))
    integerList.append(int(splitted_ciphertext[3], 2))
    return integerList





def encryptionSPN(plaintext1):
    cipherofplaintext1 = []

    for p1count in range(0, 5000, 1):
        pickp1 = plaintext1[p1count]
        keymixing1FunctionoutputSplitted = keymixing1(pickp1)
        # print(keymixing1FunctionoutputSplitted)
        finr1encrypt = []
        for r1encrypt in range(0, 4):
            temp_sbox_outputround1encrypt = bin_s_box[str(keymixing1FunctionoutputSplitted[r1encrypt])]
            finr1encrypt.append(temp_sbox_outputround1encrypt)
        # print(finr1encrypt)
        # Round 1 Permutation
        finr1encryptCombined = "".join(finr1encrypt)
        binary_string_e1 = finr1encryptCombined
        temp_e1 = permutation(binary_string_e1)
        permutedString_e1 = "".join(temp_e1)  # Combined Permuted String
        # Print(permutedString_e1) #Cobined Output After Round 1 Permutation
        SplittedPermutedString_e1 = []
        for u_e1 in range(0, len(permutedString_e1), 4):
            temp_output2_e1 = permutedString_e1[u_e1:u_e1 + 4]
            SplittedPermutedString_e1.append(temp_output2_e1)
        # print(SplittedPermutedString_e1) #Splitted Output After Round 1 Permutation
        # print(permutedString_e1)
        # Round 2 Key Mixing
        keymixing2FunctionoutputSplitted = keymixing2(permutedString_e1)
        # print(keymixing2FunctionoutputSplitted)
        # Round 2 Substitution
        finr2encrypt = []
        for r2encrypt in range(0, 4):
            temp_sbox_outputround2encrypt = bin_s_box[str(keymixing2FunctionoutputSplitted[r2encrypt])]
            finr2encrypt.append(temp_sbox_outputround2encrypt)
        # print(finr2encrypt) #Splitted Output of Round 2 Substitution
        # Round 2 Permutation
        finr2encryptCombined = "".join(finr2encrypt)
        binary_string_e2 = finr2encryptCombined
        temp_e2 = permutation(binary_string_e2)
        permutedString_e2 = "".join(temp_e2)  # Combined Permuted String
        # print(permutedString_e2)
        # print(permutedString_e1) #Combined Output After Round 2 Permutation
        SplittedPermutedString_e2 = []
        for u_e2 in range(0, len(permutedString_e2), 4):
            temp_output2_e2 = permutedString_e2[u_e2:u_e2 + 4]
            SplittedPermutedString_e2.append(temp_output2_e2)
        # print(SplittedPermutedString_e2)  # Splitted Output After Round 2 Permutation
        # print(permutedString_e2)
        # Round 3 Key Mixing
        keymixing3FunctionoutputSplitted = keymixing3(permutedString_e2)
        # print(keymixing3FunctionoutputSplitted)
        # Round 3 Substitution
        finr3encrypt = []
        for r3encrypt in range(0, 4):
            temp_sbox_outputround3encrypt = bin_s_box[str(keymixing3FunctionoutputSplitted[r3encrypt])]
            finr3encrypt.append(temp_sbox_outputround3encrypt)
        # print(finr3encrypt)  # Splitted Output of Round 3 Substitution
        # Round 3 Permutation
        finr3encryptCombined = "".join(finr3encrypt)
        binary_string_e3 = finr3encryptCombined
        temp_e3 = permutation(binary_string_e3)
        permutedString_e3 = "".join(temp_e3)  # Combined Permuted String

        SplittedPermutedString_e3 = []
        for u_e3 in range(0, len(permutedString_e3), 4):
            temp_output2_e3 = permutedString_e3[u_e3:u_e3 + 4]
            SplittedPermutedString_e3.append(temp_output2_e3)
        # print(SplittedPermutedString_e3)  # Splitted Output After Round 2 Permutation
        # print(permutedString_e3)
        # Round 4 Key Mixing
        keymixing4FunctionoutputSplitted = keymixing4(permutedString_e3)
        # print(keymixing4FunctionoutputSplitted)
        # Round 4 Substitution
        finr4encrypt = []
        for r4encrypt in range(0, 4):
            temp_sbox_outputround4encrypt = bin_s_box[str(keymixing4FunctionoutputSplitted[r4encrypt])]
            finr4encrypt.append(temp_sbox_outputround4encrypt)
        # print(finr4encrypt)  # Splitted Output of Round 4 Substitution
        finr4encryptCombined = "".join(finr4encrypt)
        # Last Key Mixing
        keymixing5FunctionoutputSplitted = keymixing5(finr4encryptCombined)
        # print(keymixing5FunctionoutputSplitted)
        keymixing5FunctionoutputCombined = "".join(keymixing5FunctionoutputSplitted)

        #print(keymixing5FunctionoutputCombined)
        cipherofplaintext1.append(keymixing5FunctionoutputCombined)
    return(cipherofplaintext1)

def s_box(value):
    dict = {0:14,1:4,2:13,3:1,4:2,5:15,6:11,7:8,8:3,9:10,10:6,11:12,12:5,13:9,14:0,15:7}
    return dict[value]
def reverse_s_box(value):
    dict = {14:0,4:1,13:2,1:3,2:4,15:5,11:6,8:7,3:8,10:9,6:10,12:11,5:12,9:13,0:14,7:15}
    return dict[value]

#def bin_s_box(value):
    #dict = {"0000":"1110","0001":"0100","0010":"1101","0011":"0001","0100":"0010","0101":"1111","0110":"1011","0111":"1000","1000":"0011","1001":"1010","1010":"0110","1011":"1100","1100":"0101","1101":"1001","1110":"0000","1111":"0111"}


def MaxOccurrancesInList(value1):
    temp=[]
    temp2={}
    count= Counter(value1)  # Sorted (max count first in dictionary) Dictionary of all deltaY:ItsCount
    temp2=count.most_common() # Converts the each key-value pair into list of tuples [(deltaY,count), (deltaY,count)]
    temp=temp2[0:2] # Slice to take top two tuples
    return temp

def binbits(x,n):

    if(type(x) == str):
        x = int(x,2)

    bits = bin(x).split('b')[1]
    if len(bits) < n:
        return '0' * (n - len(bits)) + bits
    else:
        return bits

def partiallyDecrypt(cipherToDecrypt,candidatekey):

    Splitted_xored_temp7_binString = []
    splitted_temp100_output=[]
    sbox_output2_xored_temp7_binString=[]
    temp7 = int(cipherToDecrypt,2)
    xored_temp7_integer=xor(temp7,candidatekey)
    xored_temp7_binString=binbits(xored_temp7_integer,16)
    for k in range(0, len(xored_temp7_binString), 4):
        temp_output = xored_temp7_binString[k:k + 4]
        Splitted_xored_temp7_binString.append(temp_output)
    for kk1 in range(0, 4):
        temp_sbox_output2_xored_temp7_binString = getSboxReverseValue(str(Splitted_xored_temp7_binString[kk1]))
        sbox_output2_xored_temp7_binString.append(temp_sbox_output2_xored_temp7_binString)

    return sbox_output2_xored_temp7_binString

def getSboxReverseValue(sBoxValueToGet):
    for key,value in bin_s_box.items():
        if value == sBoxValueToGet:
            return key



def permutation(StringToPermuted):
    bits = list(StringToPermuted)  # Extracting Bits from the string
    new_string = []
    new_string.append(bits[0])
    new_string.append(bits[4])
    new_string.append(bits[8])
    new_string.append(bits[12])
    new_string.append(bits[1])
    new_string.append(bits[5])
    new_string.append(bits[9])
    new_string.append(bits[13])
    new_string.append(bits[2])
    new_string.append(bits[6])
    new_string.append(bits[10])
    new_string.append(bits[14])
    new_string.append(bits[3])
    new_string.append(bits[7])
    new_string.append(bits[11])
    new_string.append(bits[15])
    return new_string


deltaXList=[]
deltaYList=[]

# Generating Difference Distribution Table

additional_dict={}
for deltaX in range (0,16,1):
    deltaXList.append(deltaX)
    for normalX in range (0,16,1):
        XplusdeltaX= xor(normalX,deltaX)
        normalY=s_box(normalX)
        YplusdeltaY=s_box(XplusdeltaX)
        deltaY= xor(normalY,YplusdeltaY)
        deltaYList.append(deltaY)
    additional_dict[deltaX]=deltaYList    # additional_dict={0:[all deltaY],1:[all deltaY].....}
    deltaYList=[]

#Printing All Differential Pair Values

print()
print("[*] Following are all the possible values of deltaY corresponding to each deltaX")
print()

#Calculating Frequency Table

frequency_dictionary={}
frequency_temp=[]
for zz in range (0,16,1):
    frequency_temp=additional_dict[zz]     # Takes out deltaY from list
    frequency_temp2=MaxOccurrancesInList(frequency_temp) # Sends deltaY list to MaxOccurrances list
    frequency_dictionary[zz]=frequency_temp2 # {deltaX:[(deltaY,count),(deltaY,count)}
for printing_additional_dict in additional_dict.keys():
  print("For deltaX = ",printing_additional_dict," ","Corresponding deltaY Values = ",additional_dict[printing_additional_dict]," ","[(Maximum Occuring deltaY, Occurance Count)]","---->",frequency_dictionary[printing_additional_dict])
print()

print("[*]Select the Differential Pairs for selecting S-Box S12, S23, S32 & S33 as suggested in the Tutorial")
print("   Enter the chosen value for deltaX ",end='');ChosenDeltaX=input();binary_chosenDeltaX=ChosenDeltaX;ChosenDeltaX=int(ChosenDeltaX)
print("   Enter the chosen value for deltaY ",end='');ChosenDeltaY=input()
print("Enter 3 more pairs of deltaX and deltaY")
binary_chosenDeltaX=binbits(ChosenDeltaX,4)
binary_chosenDeltaY=binbits(int(ChosenDeltaY),4)

diffrential_dict = {binary_chosenDeltaX:binary_chosenDeltaY}
temp_key=[]
temp_key.append(ChosenDeltaX)
for i in range(0,3):
    key = int(input("Enter deltaX: "))
    temp_key.append(key) # list of 4 deltaX entered by User (will use in calculating probability)
    key=binbits(key,4)
    value = int(input("Enter deltaY: "))
    value =binbits(value,4)
    diffrential_dict[key] = value # Binary Dictionary of User entered values

# Calculating Probability

j=1
for b in range (0,4):
    temp_key_value=frequency_dictionary[temp_key[b]] #Input frequency dictionary = {deltaX:[(deltaY,count),(deltaY,count)]}
    temp_key_value2=temp_key_value[0]   #temp_key_value2= (deltaY,count)
    temp_key_value3=list(temp_key_value2) # Converts to list [deltaY,count]
    temp_probability=((temp_key_value3[1])*j) # Extracting the count for probability
    j=temp_probability
probability=((temp_probability)/(16*16*16*16))
print()
print("The Probability for Occurance of the selected Differential Pairs = ",probability)
print()
print("[*] Calculating Differential Characteristic - The following process shows the output of each round of SPN Network")
print()
print("[Round 1] of SPN Network For Calculating Differential Characteristic")
ChosenDeltaX=ChosenDeltaX << 8 #
ChosenDeltaX=binbits(ChosenDeltaX,16)

#print(ChosenDeltaX)

SplittedInputDiffrential=[]
for k in range(0,len(ChosenDeltaX),4):
    temp_output=ChosenDeltaX[k:k+4]
    SplittedInputDiffrential.append(temp_output)

#print(SplittedInputDiffrential,end='');print("----->"+"Splitted Version of 16 bit Differential Input")

# Substitution Round 1 for Calculating Differential Characteristic
sboxoutputRound1=[]
for sboxcount in range (0,4):
    if (SplittedInputDiffrential[sboxcount]=='0000'):
        sboxoutputRound1.append('0000')
    else:
        temp_sbox_output=diffrential_dict[str(SplittedInputDiffrential[sboxcount])]
        sboxoutputRound1.append(temp_sbox_output)

print(sboxoutputRound1,end='');print("----->"+"Round 1 S-Box Output While Calculating Differential Characteristic")
CombinedsboxoutputRound1="".join(sboxoutputRound1)
#print(CombinedsboxoutputRound1)
#IntegerCombinedsboxoutputRound1=int(CombinedsboxoutputRound1,2) //Not needed so far

#Permutation Round 1 for Calculating Differential Characteristic
binary_string = CombinedsboxoutputRound1
temp=permutation(binary_string)
permutedString="".join(temp)
#print(permutedString,end='');print("----->"+"Round 1 Permuted Output ")

SplittedPermutedString=[]
for u in range(0,len(permutedString),4):
    temp_output2=permutedString[u:u+4]
    SplittedPermutedString.append(temp_output2)

print(SplittedPermutedString,end='');print("----->"+"Round 1 Permuted Output While Calculating Differential Characteristic")
print()
print("[Round 2] of SPN Network For Calculating Diffrential Characteristic")
#Substitution Round 2 for Calculating Differential Characteristic
sboxoutputRound2=[]
for sboxcount2 in range (0,4):
    if (SplittedPermutedString[sboxcount2]=='0000'):
        sboxoutputRound2.append('0000')
    else:
        temp_sbox_output1=diffrential_dict[str(SplittedPermutedString[sboxcount2])]
        sboxoutputRound2.append(temp_sbox_output1)

print(sboxoutputRound2,end='');print("----->"+"Round 2 S-Boxes Output While Calculating Differential Characteristic")
CombinedsboxoutputRound2="".join(sboxoutputRound2)
#print(CombinedsboxoutputRound2)

#Permutation Round 2 for Calculating Differential Characteristic
binary_string2 = CombinedsboxoutputRound2
temp2=permutation(binary_string2)
permutedString2="".join(temp2)
#print(permutedString2,end='');print("----->"+"Round 2 Permuted Output While Calculating Differential Characteristic")

SplittedPermutedString2=[]
for y in range(0,len(permutedString2),4):
    temp_output3=permutedString2[y:y+4]
    SplittedPermutedString2.append(temp_output3)

print(SplittedPermutedString2,end='');print("----->"+"Round 2 Permuted Output While Calculating Differential Characteristic")
print()
#Substitution Round 3 for Calculating Differential Characteristic
print("[Round 3] of SPN Network For Calculating Differential Characteristic")
sboxoutputRound3=[]
for sboxcount3 in range (0,4):
    if (SplittedPermutedString2[sboxcount3]=='0000'):
        sboxoutputRound3.append('0000')
    else:
        temp_sbox_output2=diffrential_dict[str(SplittedPermutedString2[sboxcount3])]
        sboxoutputRound3.append(temp_sbox_output2)

print(sboxoutputRound3,end='');print("----->"+"Round 3 S-Boxes Output While Calculating Differential Characteristic")
CombinedsboxoutputRound3="".join(sboxoutputRound3)
#print(CombinedsboxoutputRound3)

#Permutation Round 3 for Calculating Differential Characteristic
binary_string3 = CombinedsboxoutputRound3
temp3=permutation(binary_string3)
permutedString3="".join(temp3)
#print(permutedString3,"THISSSSSSSSSSSS")
#print(permutedString3,end='');print("----->"+"Round 3 Permuted Output")
IntegerValueForDifferential=int(permutedString3,2)

SplittedPermutedString3=[]
for z in range(0,len(permutedString3),4):
    temp_output4=permutedString3[z:z+4]
    SplittedPermutedString3.append(temp_output4)

print(SplittedPermutedString3,end='');print("----->"+"Round 3 Permuted Output While Calculating Differential Characteristic")
print()

print("Round 3 Permuted Output is the Differential Characteristic = ", SplittedPermutedString3)
print("The Differential Value ",SplittedPermutedString3," occurs with Probability = ", probability)

IntegerValueFor0110=int(SplittedPermutedString3[1],2)
#print(IntegerValueFor0110)
#=====================================================================================================================



# Choosing plaintext1 and plaintext2
plaintext1=[]
for p1 in range (0,5000,1):
    m1=binbits(p1,16)
    plaintext1.append(m1)

plaintext2=[]
for p2 in range (0,5000,1):
    plaintext1integervalue=int(plaintext1[p2],2)
    m2=xor(plaintext1integervalue,2816)
    m3=binbits(m2,16)
    plaintext2.append(m3)


encryptedplaintext1=encryptionSPN(plaintext1)
encryptedplaintext2=encryptionSPN(plaintext2)

#filtered_encrypted_ciphers1=filter_cipher(encryptedplaintext1)
#filtered_encrypted_ciphers2=filter_cipher(encryptedplaintext2)
#print(len(filtered_encrypted_ciphers2))
#print(len(filtered_encrypted_ciphers1))
filtered_encrypted_ciphers1 = encryptedplaintext1
filtered_encrypted_ciphers2 = encryptedplaintext2
#print(filtered_encrypted_ciphers1[199],"THUISSSSSS")
print()

print("[*] Brute Force Attack in progress to retrieve sub-bits of key 5")

key_keycount = {}
partialDecrypted1=[]
partialDecrypted2=[]
final_diff_of_both_ciphers_in_integers=[]
temp_integers_conv=[]
temp_integers_conversion1=[]
temp_integers_conversion2=[]
all_binary1_splitted=[]
all_binary2_splitted=[]

candidateKey=[]
temp_list111=[]
temp_list222=[]
list786=['0000','0000','0000','0000']
for ie in range (0,16,1): # Generate two lists each containing all 4 bits possible values in binary
    temp_list111.append(binbits(ie,4))
    temp_list222.append(binbits(ie,4))

for je in range(0,16,1):
    list786[1]=temp_list111[je]
    for asd in range (0,16,1):
        list786[3]=temp_list222[asd]
        combiningallthese="".join(list786)
        candidateKey.append(combiningallthese) # Candidate Key is list of 256 keys. each key is combined string


for iterations in range (0, 256, 1):
    integervalue_of_CandidateKey=int(candidateKey[iterations],2)
    key_keycount[integervalue_of_CandidateKey] = 0  # key_keycount is dictionary

    for pp in range (0,len(filtered_encrypted_ciphers2),1):  # filtered_encrypted_ciphers2=5000
        partialDecrypted1 = partiallyDecrypt(filtered_encrypted_ciphers1[pp], integervalue_of_CandidateKey)
        partialDecrypted2 = partiallyDecrypt(filtered_encrypted_ciphers2[pp], integervalue_of_CandidateKey)
        CombinedPartialDecrypted1 = "".join(partialDecrypted1)
        CombinedPartialDecrypted2 = "".join(partialDecrypted2)
        Integer_value_of_CombinedPartialDecrypted1 = int(CombinedPartialDecrypted1,2)
        Integer_value_of_CombinedPartialDecrypted2 = int(CombinedPartialDecrypted2, 2)
        Final_Differential_of_two_Ciphertext=xor(Integer_value_of_CombinedPartialDecrypted1,Integer_value_of_CombinedPartialDecrypted2)
        Binary_String_Final_Differential_of_two_Ciphertext=binbits(Final_Differential_of_two_Ciphertext,16)

        if(Binary_String_Final_Differential_of_two_Ciphertext==str(permutedString3)): #permutedString3=calculated differential characteristic
            key_keycount[integervalue_of_CandidateKey] += 1  # Key_Keycount={candidatekey:counter,}

max_value = max(key_keycount, key=key_keycount.get)
# print(max_value)
print("Guessed Subkey Bits from Key 5 are" + "-->",binbits(max_value,16))















