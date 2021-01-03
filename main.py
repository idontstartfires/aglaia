from weather import Report


if __name__ == '__main__':
    report = Report()
    for datetime, conditions in report.hourly.items():
        print(f'{datetime.strftime("%a, %b %d %Y [%H:%M]")}:    {conditions}')
