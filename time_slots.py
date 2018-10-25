from datetime import datetime, timedelta

appointments = [(datetime(2012, 5, 22, 10), datetime(2012, 5, 22, 10, 30)),
                (datetime(2012, 5, 22, 12), datetime(2012, 5, 22, 13)),
                (datetime(2012, 5, 22, 15, 30), datetime(2012, 5, 22, 17, 10))]

hours = (datetime(2012, 5, 22, 9), datetime(2012, 5, 22, 18))


def get_slots(hours, appointments, duration=timedelta(hours=1)):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
        assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
            print("{:%H:%M} - {:%H:%M}".format(start, start + duration))
            start += duration


if __name__ == "__main__":
    get_slots(hours, appointments)
