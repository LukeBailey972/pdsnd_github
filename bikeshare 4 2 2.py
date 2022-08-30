import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago',
              'new york city': 'new_york_city',
              'washington': 'washington' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')

    # user input for city (chicago, new york city, washington).
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print('\nInvalid entry, please try again.')
            continue
        else:
            break

    # user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('\nWhich month would you like to filter by: January, February, March, April, May, or June? Alternatively, enter "all" to apply no month filter.\n').lower()
        if month not in months:
            print('Invalid entry, please try again.')
            continue
        else:
            break

    # user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('\nWhich day would you like to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Alternatively, enter "all" to apply no day filter.\n').lower()
        if day not in days:
            print('Invalid entry, please try again.')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converts the Start Time column to datetime and creates new month and day of week columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filters by month if applicable and creates new dataframe
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filters by day of week if applicable and creates new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    popular_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', common_day)

    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common starting hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    Start_Station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start)


    End_Station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end)

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, 'seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Count:\n', user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        print('\nGender Count: No data available.')
    # Display earliest, most recent, and most common year of birth

    try:

        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    """Displays raw data 5 rows at a time, if requested."""

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    if view_data != 'no':
        start_loc = 0
        keep_asking = True
        while (keep_asking):
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display == "no": 
               keep_asking = False



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
