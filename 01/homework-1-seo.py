#June Jeongwon Seo
#05/23/2016
#Homework1



yearborn = input ("Year of birth:")

age = 2016-int(yearborn)
print ("You are approximately " + str(age) + " years old.")

#
#Human: 80 beats per minute, 42,000,000 beats per year.
#Blue whale: 10 beats per minute, 525,000 beats per year.
#Rabbit: 150 beats per minute, 78,000,000 beats per year.

heartbeat = 42000000 * age
if heartbeat >= 1000000000:
    print ("Your heart has beaten " + str(heartbeat/1000000000) + " billion times.")
else:
    print ("Your heart has beaten " + str(heartbeat) + " times.")

bluewhale = 525000 * age
if bluewhale >= 1000000000:
    print ("A blue whale's heart has beaten " + str(bluewhale/1000000000) + " billion times.")
else:
    print ("A blue whale's heart has beaten " + str(bluewhale) + " times.")
rabbit = 78000000 * age
if rabbit >= 1000000000:
    print ("A rabbit's heart has beaten " + str(rabbit/1000000000) + " billion times.")
else:
    print ("A rabbit's heart has beaten " + str(rabbit) + " times.")

#
#A Venus year is 224 days.
#A Neptune year is 165 years.
venus = age * 365 / 224
neptune = age / 165
print ("You are " + str(venus) + " Venus years old.")
print ("You are " + str(neptune) + " Neptune years old.")

#
if age == 28:
    print ("You are 1 year older than me.")
elif age == 26:
    print ("You are 1 year younger than me.")
elif age > 27:
    print ("You are " + str(age-27) + " years older than me.")
elif age < 27:
    print ("You are " + str(27-age) + " years younger than me.")
else:
    print ("We are same age.")

#
if (yearborn%2 == 0):
    print ("You born in an even year.")
else:
    print ("You born in an odd year.")

#
if yearborn>=1901 and yearborn<1909:
    uspresi = "Theodore Roosevelt"
elif yearborn>=1909 and yearborn<1913:
    uspresi = "William Howard Taft"
elif yearborn>=1913 and yearborn<1921:
    uspresi = "Woodrow Wilson"
elif yearborn>=1921 and yearborn<1923:
    uspresi = "Warren G. Harding"
elif yearborn>=1923 and yearborn<1929:
    uspresi = "Calvin Coolidge"
elif yearborn>=1929 and yearborn<1933:
    uspresi = "Herbert Hoover"
elif yearborn>=1933 and yearborn<1945:
    uspresi = "Franklin D. Roosevelt"
elif yearborn>=1945 and yearborn<1953:
    uspresi = "Harry S. Truman"
elif yearborn>=1953 and yearborn<1961:
    uspresi = "Dwight D. Eisenhower"
elif yearborn>=1961 and yearborn<1963:
    uspresi = "John F. Kennedy"
elif yearborn>=1963 and yearborn<1969:
    uspresi = "Lyndon B. Johnson"
elif yearborn>=1969 and yearborn<1974:
    uspresi = "Richard Nixon"
elif yearborn>=1974 and yearborn<1977:
    uspresi = "Gerald Ford"
elif yearborn>=1977 and yearborn<1981:
    uspresi = "Jimmy Carter"
elif yearborn>=1981 and yearborn<1989:
    uspresi = "Ronald Reagan"
elif yearborn>=1989 and yearborn<1993:
    uspresi = "George H. W. Bush"
elif yearborn>=1993 and yearborn<2001:
    uspresi = "Bill Clinton"
elif yearborn>=2001 and yearborn<2009:
    uspresi = "George W. Bush"
elif yearborn>=2009 and yearborn<2017:
    uspresi = "Barack Obama"
print (str(uspresi) + " was in office when you were born.")
