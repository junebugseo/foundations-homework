# JUNE SEO
# Homework 9
# 06-20-2016

# PART ZERO

import dateutil.parser
earthquake = {
      'rms': '1.85',
      'updated': '2014-06-11T05:22:21.596Z',
      'type': 'earthquake',
      'magType': 'mwp',
      'longitude': '-136.6561',
      'gap': '48',
      'depth': '10',
      'dmin': '0.811',
      'mag': '5.7',
      'time': '2014-06-04T11:58:58.200Z',
      'latitude': '59.0001',
      'place': '73km WSW of Haines, Alaska',
      'net': 'us',
      'nst': '',
      'id': 'usc000rauc'}

# PART ONE

def depth_to_words(earthquake):
    if int(earthquake['depth'])<70:
        return "A shallow"
    if int(earthquake['depth'])>300:
        return "A deep"
    else:
        return "An intermediate"

def magnitude_to_words(earthquake):
    if float(earthquake['mag'])<2:
        return "micro"
    if float(earthquake['mag'])>=2 and float(earthquake['mag'])<4:
        return "minor"
    if float(earthquake['mag'])=>4 and float(earthquake['mag'])<5:
        return "light"
    if float(earthquake['mag'])=>5 and float(earthquake['mag'])<6:
        return "strong"
    if float(earthquake['mag'])=>6 and float(earthquake['mag'])<7:
        return "major"
    if float(earthquake['mag'])>=8:
        return "great"

def day_in_words(earthquake):
    return dateutil.parser.parse(earthquake['time']).strftime('%A')

def time_in_words(earthquake):
    times = dateutil.parser.parse(earthquake['time']).strftime('%H')
    if int(times) <= 0 and int(times) <12:
        return "morning"
    if int(times) <= 12 and int(times) >17:
        return "afternoon"
    if int(times) <=17 and int(times) >21:
        return "evening"
    else:
        return "night"

def date_in_words(earthquake):
    return dateutil.parser.parse(earthquake['time']).strftime('%B %d')

# PART TWO
def eq_to_sentence(earthquake):
    return depth_to_words(earthquake)+', '+ magnitude_to_words(earthquake) +' '+ earthquake['mag'] + ' earthquake was reported ' + day_in_words(earthquake) + ' '+ time_in_words(earthquake) + ' on ' + date_in_words(earthquake) + ' '+ earthquake['place']
print (eq_to_sentence(earthquake))

# PART THREE
