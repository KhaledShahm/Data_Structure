# # 1-Reverse String 
# def ReveseString(our_string):
#     """
#     Reverse the input string 
#     Args:
#         our_string(string): String to be reversed
#     Returns:
#         string: the reversed string 
#     """
#     #TODO: Write your solution here    
#     reverse_string = ""
#     for i in range(len(our_string)):
#         reverse_string += our_string[(len(our_string)-1)-i]
    
#     return reverse_string

# # Test cases
# print("Pass" if("retaw" == ReveseString("water")) else "Fail")
# print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == ReveseString('Practicing string manipulation!')) else "Fail")
# print ("Pass" if ('3432 :si edoc esuoh ehT' == ReveseString('The house code is: 2343')) else "Fail")



# # 2-Anagrams
# def AnagramChecker(str1, str2):
#     """
#     check if the input strings are anagrams of each other
#     Args:
#         str1(string), str2(string) : strings to be checked
#     Returns:
#         bool: Indicates whether strings are anagrams
#     """
#     if len(str1) != len(str2):

#         # Clean strings
#         clean_str_1 = str1.replace(" ", "").lower()
#         clean_str_2 = str2.replace(" ", "").lower()

#         if sorted(clean_str_2) == sorted(clean_str_1):
#             return True
#     return False

# print ("Pass" if not (AnagramChecker('water','waiter')) else "Fail")
# print ("Pass" if AnagramChecker('Dormitory','Dirty room') else "Fail")
# print ("Pass" if AnagramChecker('Slot machines', 'Cash lost in me') else "Fail")
# print ("Pass" if not (AnagramChecker('A gentleman','Elegant men')) else "Fail")
# print ("Pass" if AnagramChecker('Time and tide wait for no man','Notified madman into water') else "Fail")


# # 3- Word flipper
# def FlipWord(our_string):

#     """
#     Flip the individual words in a sentence

#     Args:
#        our_string(string): Strings to have individual words flip
#     Returns:
#        string: String with words flipped
#     """

#     word_list = our_string.split(" ")

#     for idx in range(len(word_list)):
#         word_list[idx] = word_list[idx][::-1]

#     return " ".join(word_list)


# print ("Pass" if ('retaw' == FlipWord('water')) else "Fail")
# print ("Pass" if ('sihT si na elpmaxe' == FlipWord('This is an example')) else "Fail")
# print ("Pass" if ('sihT si eno llams pets rof ...' == FlipWord('This is one small step for ...')) else "Fail")


def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) == len(str2):
        count = 0

        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count+=1

        return count

    return None



print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")

