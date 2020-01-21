vidst = int(input("Яку відстань пробіг спротсмен (в метрах): "))
time = int(input("Час затрачений спортсменом (в секундах): "))

def sport_speed(vidst, time):
    vidst_time = vidst / time
    return round(vidst_time, 1)

vidst_time = sport_speed(vidst, time)
print("Швидкість спортсмена:",
      vidst_time, "м/сек.")
