# Конвертер із числа в дату.

input_str = input("Enter the number of seconds from 0 to 8640000: ")

days_ = int(input_str) // (24*60*60)
hours_ = (int(input_str) % (24*60*60)) // (60*60)
minutes_ = ((int(input_str) % (24*60*60)) % (60 * 60)) // 60
seconds_ = ((int(input_str) % (24*60*60)) % (60 * 60)) % 60

if str(days_)[-1] == "1" and str(days_).zfill(2)[-2] != "1":
    days_word = " день, "

elif str(days_)[-1] in "2, 3, 4" and str(days_).zfill(2)[-2] != "1":
    days_word = " дні, "

else:
    days_word = " днів, "

print(days_, days_word, str(hours_).zfill(2), ":", str(minutes_).zfill(2), ":", str(seconds_).zfill(2), ".", sep = "")
