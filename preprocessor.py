import pandas as pd
import re

def preprocess(data):
    # Print input data for debugging
    # print("Input data:")
    # print(data)

    # Updated regex pattern to match the 12-hour format with am/pm
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
    messages = re.split(pattern, data)[1:]  # Split based on the pattern
    dates = re.findall(pattern, data)  # Extract dates

    # # Print extracted messages and dates
    # print(f"Extracted Messages: {messages}")
    # print(f"Extracted Dates: {dates}")

    # Proceed only if we have messages
    if not messages or not dates:
        print("No messages or dates found. Returning empty DataFrame.")
        return pd.DataFrame(columns=['date', 'user', 'message', 'year', 'month', 'hour', 'minute', 'month_num', 'only_date', 'day_name', 'period'])

    df = pd.DataFrame({'User_message': messages, 'message_date': dates})

    # Handle date parsing
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p - ', errors='coerce')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['User_message']:
        entry = re.split('([\w\W]+?):\s', message, 1)  # Add maxsplit argument
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['User_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    
    # Calculate period
    df['period'] = df['hour'].apply(lambda hour: f"{hour:02d}-{(hour + 1) % 24:02d}")

    # print(df)  # Display the resulting DataFrame
    
    return df


