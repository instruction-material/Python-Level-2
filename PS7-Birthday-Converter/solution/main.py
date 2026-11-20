from datetime import date

MONTH_NAMES = {1: "January", 2: "February", 3: "March", 4: "April",
               5: "May", 6: "June", 7: "July", 8: "August",
               9: "September", 10: "October", 11: "November", 12: "December"}
ORDINAL_ENDINGS = {1: "st", 2: "nd", 3: "rd"}


def display_date(sample):
    parts = sample.strip().split("/")
    if [len(part) for part in parts] != [2, 2, 4] or not all(
        part.isascii() and part.isdecimal() for part in parts
    ):
        raise ValueError("Use mm/dd/yyyy.")
    month, day, year = [int(part) for part in parts]
    try:
        date(year, month, day)
    except ValueError:
        raise ValueError("This date does not exist.") from None

    ending = "th" if 11 <= day <= 13 else ORDINAL_ENDINGS.get(day % 10, "th")
    return f"{MONTH_NAMES[month]} {day}{ending}, {year:04d}"


if __name__ == "__main__":
    try:
        sample = input("Sample date (mm/dd/yyyy): ")
        print(f"Date: {display_date(sample)}")
    except ValueError as error:
        print(error)
    except EOFError:
        print("No date entered.")
