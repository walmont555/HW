from address import Address
from mailing import Mailing

mailing = Mailing(Address("12345", "Москва", "Первая", "1",
                       "27"),Address("772901", "Санкт-Петербург", "Монетная", "71",
                       "12"), 67,127621)
print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
