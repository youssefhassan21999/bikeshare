import time
import pandas as pd
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("Which city would you like to choose? (Chicago, New york city, Washington)").lower()
        if city in cities:
            break
        else:
            print("\n Please enter one of the following cities (Chicago, New york city, Washington)")


    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
        month = input("Which month would you like to choose? (January, February, March, April, May, June)? or all of them? if all write All\n").title()
        if month in months:
            break
        else:
            print("\n Please enter one of the following months (January, February, March, April, May, June) or type All")

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = input("\n Which day of the week would you like to choose? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? type All, if you want all day \n").title()
        if day in days:
            break
        else:
            print("\n Please enter one of the following days, (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or type All if you want all days ")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_popular_month = months[most_popular_month - 1]
    print("{} is the most popular month".format(most_popular_month))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("{} is the most popular day is".format(most_common_day))

    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Start Hour'].mode()[0]
    print("{} is the most common start hour".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    print("{} is the most commonly used start station".format(most_used_start))

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    print("{} is the most commonly used end station".format(most_used_end))

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print("The total trip duration is {} hour {} minute {} second".format(hour, minute, second))

    # display mean travel time
    average_travel_time = round(df['Trip Duration'].mean())
    min, sec = divmod(average_travel_time, 60)

    if min > 60:
        hrs, min = divmod(min, 60)
        print("The total trip duration is {} hour {} minute {} second".format(hrs, min, sec))
    else:
        print("The total trip duration is {} minute {} second".format(min, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("There are {} user counts".format(user_types_count))

    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        counts_of_gender = df['Gender'].value_counts()
        print("There are {} gender counts".format(counts_of_gender))
    else:
        print("counts of gender couldn't be displayed for the chosen city")

    # Display earliest, most recent, and most common year of birth
    if city.title() == 'Chicago' or city.title() == 'New York City':
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("{} is the oldest date of birth".format(earliest_year_of_birth))

        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("{} is the most recent date of birth".format(most_recent_year_of_birth))

        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("{} is the most common date of birth".format(most_common_year_of_birth))
    else:
        print("counts of gender couldn't be displayed for the chosen city")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):

    while True:
        answer=['yes','no']
        question_answer= input("Would you like to see the first 5 rows of data? Type 'yes' or 'no'\n").lower()
        if question_answer in answer:
            if question_answer=='yes':
                start=0
                end=5
                data = df.iloc[start:end,:9]
                print(data)
            break
        else:
            print("Please enter a valid answer")
    if  question_answer=='yes':
            while True:
                other_answer= input("Would you like to see the next 5 rows of data? Type 'yes' or 'no'\n").lower()
                if other_answer in answer:
                    if other_answer=='yes':
                        start+=5
                        end+=5
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:
                        break
                else:
                    print("Please enter a valid answer")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
