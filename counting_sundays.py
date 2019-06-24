def is_leap_year(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  else:
    return False

def get_to_sunday(starting_index, number_of_days_in_week):
  if starting_index != 0:
    new_date = number_of_days_in_week - starting_index + 1
    return new_date
  else:
    return starting_index

def count_sundays(starting_year, starting_day):
  year = starting_year
  month_index = 0
  number_of_sundays_at_beginning_of_month = 0
  jan = mar = may = jul = aug = oct = dec = 31
  apr = jun = sep = nov = 30
  feb = 29 if is_leap_year(starting_year) else 28
  week = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
  months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
  number_of_days_in_week = len(week)
  number_of_months_in_year = len(months)
  starting_day_of_week_index = week.index(starting_day)
  date = get_to_sunday(starting_day_of_week_index, number_of_days_in_week)
  while(year < starting_year + 100):
    date += 7
    if date > months[month_index]:
      if date == months[month_index] + 1:
        number_of_sundays_at_beginning_of_month += 1
      date -= months[month_index]
      month_index += 1
      if month_index == number_of_months_in_year:
        month_index -= number_of_months_in_year
        year += 1
  return number_of_sundays_at_beginning_of_month
  
print(count_sundays(1901, 'tue'))
