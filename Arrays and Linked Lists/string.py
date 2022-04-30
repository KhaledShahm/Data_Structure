# #1-Reverse Strings
# # Code

# # def string_reverser(our_string):

# #     """
# #     Reverse the input string

# #     Args:
# #        our_string(string): String to be reversed
# #     Returns:
# #        string: The reversed string
# #     """
        
# #     # New empty string for us to build on
# #     out_string = ""
    
# #     for i in range (len(our_string)):
# #          # Grab the charecter from the back of the string and add them to the new string
# #         out_string += our_string[(len(our_string)-1)-i]

# #      # Return our solution
# #     return out_string

# # # Test Cases

# # print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
# # print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
# # print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")    



# # 2-Anagrams
# # Code

# # def anagram_checker(str1, str2):

# #    """
# #    Check if the input strings are anagrams of each other

# #    Args:
# #         str1(string), str2(string): strings to be checked  
# #    Returns:
# #         bool: Indicates whether strings are anagrams
# #    """

# #    if(len(str1) == len(str2)):
# #        # Cleaning Strings
# #        clean_str_1 = str1.replace(" ", "").lower()
# #        clean_str_2 = str2.replace(" ", "").lower()

# #        if sorted(clean_str_1) == sorted(clean_str_2):
# #            return True
   
# #    return False

# # print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
# # print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
# # print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
# # print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
# # print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")


# # Reverse the words in sentence
# # Code 

# # def word_flipper(our_string):

# #     """
# #     Flip the individual words in a sentence

# #     Args:
# #        our_string(string): String with words to flip
# #     Returns:
# #        string: String with words flipped
# #     """

# #     word_list = our_string.split(" ")

# #     for i in range(len(word_list)):
# #         word_list[i] = word_list[i][::-1]

# #     return" ".join(word_list)

# # # Test Cases

# # print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# # print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# # print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


# def hamming_distance(str1, str2):

#     """
#     Calculate the hamming distance of the two strings

#     Args:
#        str1(string),str2(string): Strings to be used for finding the hamming distance
#     Returns:
#        int: Hamming Distance
#     """

#     if len(str1) == len(str2):
#         count = 0

#         for char in range(len(str1)):
#             if str1[char] != str2[char]:
#                 count+=1

#         return count

#     return None



# print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
# print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
# print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
# print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
# print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")