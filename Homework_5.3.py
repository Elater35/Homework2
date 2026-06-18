#  Перетворити рядок на hashtag.

import string
# print(string.punctuation)

hashtag_str = ""

while hashtag_str == "":
    hashtag_str = input("Enter non-empty string for hashtag: ")

print(hashtag_str)

hashtag_str = hashtag_str.title()
# print(hashtag_str)

hashtag_lst = hashtag_str.split()
# print(hashtag_lst)

hashtag_str = "".join(hashtag_lst)
# print(hashtag_str)

hashtag_res = hashtag_str
# print(hashtag_res)

for item in hashtag_str:
    if item in string.punctuation:
        hashtag_res = hashtag_res.replace(item, "")

hashtag_res = "#" + hashtag_res
# print(hashtag_res)

if len(hashtag_res) > 140:
    hashtag_res = hashtag_res[:140]
print(hashtag_res)
