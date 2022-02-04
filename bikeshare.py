import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = ''
    while (city not in ['chicago','new york city','washington']):
        city = input('name of the city to analyze:')
        city=city.lower()
        if city  in ('chicago','new york city ','washington'):
            break
        else:
            print("Sorry you entered a wrong city, Enter city names as chicago,new york city, washington")


    # TO DO: get user input for month (all, january, february, ... , june)
    
    month=''
    while (month not in ['january', 'february', 'march', 'april', 'may', 'june']):
        month = input('name of the month:')
        month=month.lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print("Enter month upto june")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    date=''
    while (date not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
        date = input('enter the day')
        date=date.lower()
        if date in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print("Sorry you enter a wrong day please enter correct day")


    print('-'*40)
    return city,month,date

    
    
#******************************************************************************************************************************************************************************   


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df =df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df



#******************************************************************************************************************************************************************************



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    print(" The Most Common Month was", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The Most Common Day of Week was", df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(" The most common hour was", df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time()-start_time))
    print('-'*40)
    


    
    
#******************************************************************************************************************************************************************************
    
    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Common_Start_Station :\n',popular_startstation)
    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('Common_Start_Station\n',popular_endstation)
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station']+ ','+df['End Station']).mode()[0]
    print('Most frequent start and end station:\n',common_start_end)
    
    df['stations'] = df['Start Station'] + ' / ' + df['End Station']
    print('The most common station is {}'.format(df['stations'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#******************************************************************************************************************************************************************************
    
    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    print("Total Traveltime:\n",df['Trip Duration'].sum() / 3600.0)
    # TO DO: display mean travel time
    print("Total avgtime:\n",df['Trip Duration'].mean() / 3600.0)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
#******************************************************************************************************************************************************************************
    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print("Count of each user_type:\n",df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Count of each Gender:\n",df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest year:\n",df['Birth Year'].min())
        print("Most Recent Year:\n",df['Birth Year'].max())
        print("Most Common year:\n",df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
def raw_data(df):
    raw_data = input('Would you like to see the first 5 rows of data? Answer yes or no:')
    i = 0
    while True:
         if raw_data.lower() == 'yes':
             print(df.iloc[i:i+5])
             i += 5
             raw_data = input('Would you like to see additional 5 rows of data? Answer yes or no.').lower()
                               

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

