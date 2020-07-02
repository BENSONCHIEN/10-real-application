#import libraries
import json
from difflib import get_close_matches

#open file
data = json.load(open('data.json')) # as a dictionary datatype

#write the fuction
def translate(word):
    #solve upper case problem
    word = word.lower()
    #To detect the word exit or not
    if word in data.keys():
        return data[word]

    # To find the close match word
    # 改进：可以选择最符合的3个
    elif len(get_close_matches(word,data.keys())) > 0:
        answer = input("Did you mean %s instead? Choose one if it have, or enter N if no: " % get_close_matches(word, data.keys()))
        if answer == "1":  #这里要用引号，因为input到yn的是string，没有引号则是变量
            return data[get_close_matches(word,data.keys())[0]]
        elif answer == "2":
            return data[get_close_matches(word, data.keys())[1]]
        elif answer == "3":
            return data[get_close_matches(word, data.keys())[2]]
        elif yn == "N":
            return "My dictionary does not have the word"
        else:
            return "Look at What you entered"
    else:
        return "My dictionary does not have the word"

the_word_input = input("Enter a word: ") # the variable name cannot be called as input
output = translate(the_word_input)

#output出来的有括号[]，不够美观（因为是list）
#把list 变为string
if type(output) == list:
    for letter in output:
        print(letter)
else:
    print(output)