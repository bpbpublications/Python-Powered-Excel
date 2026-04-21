# Time-Zone Manipulations ___________________________________________________

# Naive and Aware time zone ------------------------

from datetime import datetime, timezone

# Naive date-time
naive_time = datetime.now()
print(f'Naive Time: {naive_time}, TimeZone: {naive_time.tzname()}')

# Aware date-time
aware_time = datetime.now(tz = timezone.utc)
print(f'Aware Time: {aware_time}, TimeZone: {aware_time.tzname()}')


# Using dateutil library  ------------------------

from dateutil import tz

current_time = datetime.now()
print(f'current_time: {current_time}, TimeZone: {current_time.tzname()}')

# Aware Object_Get the current time in the local time zone   ---------
local_now = datetime.now(tz=tz.tzlocal())
print(f"Local time: {local_now}, TimeZone: {local_now.tzname()}")

local_now.tzname() # 'India Standard Time'
local_now.tzinfo # tzlocal()

tz.tzlocal() # it doesn’t directly give you the name of the timezone
# But sets it to your machine's local timezone


# Get the current time in the UTC time zone   ---------
utc_now = datetime.now(tz=tz.UTC)
print(f'UTC time now: {utc_now}')

utc_now.tzname() # UTC
utc_now.tzinfo # tzutc

# Get the current time in the AEDT/australia time zone   ---------
aus_tz = tz.gettz("Australia/Sydney")
aus_now = datetime.now(tz=aus_tz)
print(f'Australia time now: {aus_now}')

aus_now.tzname() # AEDT
aus_now.tzinfo # tzfile('Australia/ACT')


# Create Aware Objects  in different time zones    ---------
local_time = datetime(2025, 3, 4, 15, 0, 0, tzinfo = tz.tzlocal())
utc_time = datetime(2025, 3, 4, 15, 0, 0, tzinfo = tz.UTC)

# Australia time (Sydney)
aus_tz = tz.gettz("Australia/Sydney")
# aus_now = datetime.now(tz=aus_tz)
aus_time = datetime(2025, 3, 4, 15, 0, 0, tzinfo = aus_tz)

print(local_time)
print(utc_time)
print(aus_time)

# Converting time zones   -------------------------------

# Create specific date (local time zone)
local_zone = tz.tzlocal()  # System's local timezone
local_time = datetime(2025, 3, 4, 10, 0, 0, tzinfo=local_zone)
print("Local Time:", local_time)

# Convert to America/New_York time
ny_zone = tz.gettz("America/New_York")
ny_time = local_time.astimezone(ny_zone)
print("New York Time:", ny_time)

# Convert to Australia/Sydney time
sydney_zone = tz.gettz("Australia/Sydney")
sydney_time = local_time.astimezone(sydney_zone)
print("Sydney Time:", sydney_time)

# Convert to US/Eastern time
eastern_now = local_now.astimezone(tz.gettz('US/Eastern'))
print(f"Eastern Time: {eastern_now}")

# Convert to Asia/Tokyo
tokyo_now = local_now.astimezone(tz.gettz('Asia/Tokyo'))
print(f"Tokyo Time: {tokyo_now}")


# Print all available time zones
import zoneinfo
print(list(zoneinfo.available_timezones()))