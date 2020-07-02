import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit_student",
host = "108.167.140.122",
database = ""
)

cursor = con.cursor() #cursor object to navigate through the table

word = input("Enter a word: ")

#
query = cursor.execute("SELECT * FORM Dictionary WHERE Expression = '%s' " % word)
# The method you use to print
results = cursor.fetchall()

if results:
    for result in results:   #打印每一个，一个单词可能有很多种解释
        print(result[1])
else:
    print("No word found, haha")