# python manage.py shell

# from airtrans.models import *

# Flight.objects.all()
# <QuerySet [<Flight: 1 - 10:35:36 - 10:35:37 - 1 - Шереметьево - Москва - 4 - Пулково - Санкт-Петербург>,
# <Flight: 5 - 11:00:00 - 11:00:00 - 4 - Пулково - Санкт-Петербург - 1 - Шереметьево - Москва>]>

# Seat.objects.all().filter(aircraft_code='2')
# <QuerySet [<Seat: 2 - Airbus A380 - 343>, <Seat: 2 - Airbus A380 - 45>, <Seat: 2 - Airbus A380 - 12>]>

# BoardingPasses.objects.all().filter(boarding_no='1')
# <QuerySet [<BoardingPasses: 1 - 1 - Airbus A220 - 255>]>

# nm = Ticket.objects.all()
# names = [nm[0].passenger_name, nm[1].passenger_name]
# names
# ['Василий Пупкин', 'Анна Васильева']

