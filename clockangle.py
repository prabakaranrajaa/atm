def clockangle(hour, minutes):
  if 00 <= hour <= 24 and 00 <= minutes <= 60:
    if hour > 12:
      hour = hour - 12
    if minutes == 60:
      hour = hour + 1
      minutes = 00
    hour = hour + minutes / 60
    handiff = abs(hour - minutes / 5)
    preangle = handiff * 30
    postangle = min(preangle, 360 - preangle)
    angle=format(postangle,".2f")
    print(angle + "°")
  else:
    print("Enter correctly again")
    #print("\n")
  # print("In case you don't know, the clock has a 24 hour format")


clockangle(int(input("Enter here Hour: ")), int(input("Enter here Minutes: ")))