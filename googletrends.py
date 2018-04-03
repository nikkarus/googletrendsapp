from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

#This section asks for the inputs for the program to run
kw_list = []
enter_info = input("Enter in up to 5 keywords you would like to enter into Google Trends(separated by commas):",)
weeks = input("Now enter how many weeks back you would like to see:",)
kw_list = enter_info.split(',')

#This section pulls the data from the API and then enters it into a dataframe based on prior parameters
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='US', gprop='')
df = pytrends.interest_over_time()
tail_calc_for_csv = pd.DataFrame.tail(df,int(weeks))
df.plot()

#Printing the dataframe to see if it looks correct
print(pd.DataFrame.tail(df,int(weeks)))


#This section asks if the user would like to print to a .csv in the root directory
csv_choice = input("Would you like to export to a csv? (yes or no):")
if csv_choice == "yes":
    file_name = " -".join(kw_list)
    tail_calc_for_csv.to_csv(file_name + ' trends data.csv')
else:
    print("Ok, done!")
