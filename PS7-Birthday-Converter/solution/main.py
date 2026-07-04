month_to_string = {
  1: "January",
  2: "February",
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December"
}

day_suffix = {
  0: "th",
  1: "st",
  2: "nd",
  3: "rd",
  4: "th",
  5: "th",
  6: "th",
  7: "th",
  8: "th",
  9: "th"
}

date = input("Enter your birthday in the form \"mm/dd/yyyy\": ")

month = 10 * int(date[0]) + int(date[1])
day = 10 * int(date[3]) + int(date[4])
year = 1000 * int(date[6]) + 100 * int(date[7]) + 10 * int(date[8]) + int(date[9])

month_string = month_to_string[month]
day_string = str(day) + day_suffix[day % 10]

# special cases for 11th, 12th, 13th
if day == 11 or day == 12 or day == 13:
  day_string = str(day) + "th"

print("You were born on " + month_string + " " + day_string + ", " + str(year))