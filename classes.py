# class Person:
#
#     def __init__(self, name: str, age: int, salary: int,
#                  food_money: int, petrol_money: int = 0,
#                  rent_money: int = 0, add_money: int = 0) -> None:
#         self.name = name
#         self.age = age
#         self.food_money = food_money
#         self.petrol_money = petrol_money
#         self.rent_money = rent_money
#         self.salary = salary
#         self.add_money = add_money
#
#     def _calculate_food_money(self) -> int:
#         return self.food_money
#
#     def _calculate_petrol_money(self) -> int:
#         return self.petrol_money
#
#     def _calculate_rent_money(self) -> int:
#         return self.rent_money
#
#     def _additional_money(self) -> int:
#         return self.add_money
#
#     def spend_money_in_month(self) -> int:
#         food_money = self._calculate_food_money()
#         petrol_money = self._calculate_petrol_money()
#         rent_money = self._calculate_rent_money()
#         additional_money = self._additional_money()
#         total_money = food_money + petrol_money + rent_money
#         money = self.salary - total_money
#         money_in_month = additional_money + money
#         return money_in_month
#
#
# class Doctor(Person):
#     pass
#
#
# class Developer(Person):
#     pass
#
#
# d1 = Doctor(name="Айболот", age=34, salary=80000, food_money=10000, add_money=53000)
#
# print(d1.spend_money_in_month())
