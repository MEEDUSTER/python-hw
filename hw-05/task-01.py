class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"{self.model} увімкнено"

    def turn_off(self):
        self.is_on = False
        return f"{self.model} вимкнено"

    def info(self):
        state = "увімкнено" if self.is_on else "вимкнено"
        return f"{self.brand} {self.model}, {self.power} Вт, {state}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_ml=1000, beans_g=200):
        super().__init__(brand, model, power)
        self.water_ml = water_ml
        self.beans_g = beans_g

    def brew(self):
        if not self.is_on:
            return "Спочатку увімкніть кавомашину"
        if self.water_ml < 80 or self.beans_g < 15:
            return "Недостатньо води або зерен"
        self.water_ml -= 80
        self.beans_g -= 15
        return f"Каву приготовано. Залишилось: {self.water_ml} мл води, {self.beans_g} г зерен"

    def info(self):
        return (f"{super().info()} — вода: {self.water_ml} мл, "
                f"зерна: {self.beans_g} г")


class Blender(Device):
    def __init__(self, brand, model, power, max_speed=5):
        super().__init__(brand, model, power)
        self.max_speed = max_speed
        self.speed = 0

    def blend(self, speed=1):
        if not self.is_on:
            return "Спочатку увімкніть блендер"
        if speed < 1 or speed > self.max_speed:
            return f"Швидкість має бути від 1 до {self.max_speed}"
        self.speed = speed
        return f"Змішування на швидкості {self.speed}"

    def stop(self):
        self.speed = 0
        return "Блендер зупинено"

    def info(self):
        return f"{super().info()} — швидкість: {self.speed}/{self.max_speed}"


class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model, power)
        self.processed_kg = 0

    def grind(self, kg):
        if not self.is_on:
            return "Спочатку увімкніть м'ясорубку"
        if kg <= 0:
            return "Маса має бути більшою за 0"
        self.processed_kg += kg
        return f"Перемелено {kg} кг, усього: {self.processed_kg} кг"

    def info(self):
        return f"{super().info()} — перемелено: {self.processed_kg} кг"


coffee = CoffeeMachine("DeLonghi", "ECAM", 1450)
print(coffee.info())
print(coffee.brew())
print(coffee.turn_on())
print(coffee.brew())
print(coffee.info())
print()

blender = Blender("Bosch", "VitaPower", 800)
print(blender.turn_on())
print(blender.blend(3))
print(blender.info())
print(blender.stop())
print()

grinder = MeatGrinder("Philips", "HR2727", 500)
print(grinder.turn_on())
print(grinder.grind(2))
print(grinder.grind(1.5))
print(grinder.info())
print(grinder.turn_off())
