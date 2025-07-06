from datetime import datetime, timedelta
import pytz

print("🌍 You can enter any valid timezone (e.g., Asia/Hong_Kong, Europe/London, America/New_York).")
print("If unsure, check the list here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\n")

# User inputs
departure_str = input("Enter departure time (YYYY-MM-DD HH:MM): ")
from_zone_str = input("Enter departure timezone: ")
to_zone_str = input("Enter arrival timezone: ")

# Flight duration input
duration_hours = input("Enter flight duration hours (e.g., 18): ")
duration_minutes = input("Enter flight duration minutes (e.g., 30): ")

try:
    # Validate and create timezone objects
    if from_zone_str not in pytz.all_timezones:
        raise ValueError(f"Invalid departure timezone: {from_zone_str}") #raise: stops the program with an error, different from print 
    if to_zone_str not in pytz.all_timezones:
        raise ValueError(f"Invalid arrival timezone: {to_zone_str}")

    # converting & creating objects
    # Now from_zone and to_zone are full timezone-aware objects that pytz can apply to your datetime values.
    from_zone = pytz.timezone(from_zone_str)  
    to_zone = pytz.timezone(to_zone_str)

    # Parse user input into naive datetime
    departure_naive = datetime.strptime(departure_str, "%Y-%m-%d %H:%M")

    # Localize naive datetime to from_zone (make it timezone-aware)
    departure_aware = from_zone.localize(departure_naive)

    # Create timedelta for flight duration
    duration = timedelta(hours=int(duration_hours), minutes=int(duration_minutes))

    # Calculate arrival time in departure timezone
    arrival_aware_departure_tz = departure_aware + duration

    # Convert arrival time to arrival timezone
    arrival_time = arrival_aware_departure_tz.astimezone(to_zone)

    # Display results
    print("\n✅ Time Conversion Successful:")
    print("🛫 Departure:", departure_aware.strftime("%Y-%m-%d %H:%M %Z%z"))
    print(f"⏳ Flight duration: {duration_hours} hours and {duration_minutes} minutes")
    print("🛬 Arrival:  ", arrival_time.strftime("%Y-%m-%d %H:%M %Z%z"))

except Exception as e:
    print("\n❌ Error:", e)
