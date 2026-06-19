# Конвертер із числа в дату.

input_str = input("Enter the number of seconds from 0 to 8640000: ")

days_ = int(input_str) // (24*60*60)
hours_ = (int(input_str) % (24*60*60)) // (60*60)
minutes_ = ((int(input_str) % (24*60*60)) % (60 * 60)) // 60
seconds_ = ((int(input_str) % (24*60*60)) % (60 * 60)) % 60

print(days_, " days, ", str(hours_).zfill(2), ":", str(minutes_).zfill(2), ":", str(seconds_).zfill(2), ".", sep = "")

# або

days_ = divmod(int(input_str), 24*60*60)[0]
hours_ = divmod(divmod(int(input_str), 24*60*60)[1], 60*60)[0]
minutes_ = divmod(divmod(divmod(int(input_str), 24*60*60)[1], 60*60)[1], 60)[0]
seconds_ = divmod(divmod(divmod(int(input_str), 24*60*60)[1], 60*60)[1], 60)[1]

print(days_, " days, ", str(hours_).zfill(2), ":", str(minutes_).zfill(2), ":", str(seconds_).zfill(2), ".", sep = "")