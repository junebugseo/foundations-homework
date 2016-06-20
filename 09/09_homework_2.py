# PART THREE

import pandas as pd
import dateutil.parser

earthquakes_df = pd.read_csv("1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')

for earthquake in earthquakes:

    if earthquake['type']=='earthquake':

        def depth_to_words(earthquake):
            if earthquake['depth']<70:
                return "A shallow"
            if earthquake['depth']>300:
                return "A deep"
            else:
                return "An intermediate"

        def magnitude_to_words(earthquake):

            if earthquake['mag']<2:
                return "micro"
            if earthquake['mag']>=2 and earthquake['mag']<4:
                return "minor"
            if earthquake['mag']>=4 and earthquake['mag']<5:
                return "light"
            if earthquake['mag']>=5 and earthquake['mag']<6:
                return "strong"
            if earthquake['mag']>=6 and earthquake['mag']<7:
                return "major"
            if earthquake['mag']>=8:
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

        def eq_to_sentence(earthquake):
            return depth_to_words(earthquake)+', '+ magnitude_to_words(earthquake) +' '+ str(earthquake['mag']) + ' earthquake was reported ' + day_in_words(earthquake) + ' '+ time_in_words(earthquake) + ' on ' + date_in_words(earthquake) + ' '+ earthquake['place']

        print(eq_to_sentence(earthquake))

#    else:
#        def add_sentence(earthquake):
#            return ' There was also a magnitude ' + magnitude_to_words(earthquake) + ' ' + earthquake['type'] + ' on ' + date_in_words(earthquake) + ' '+ earthquake['place']
#        print (add_sentence(earthquake))
