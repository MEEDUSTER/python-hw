class Ship:
    def __init__(self, name, displacement, crew, max_speed):
        self.name = name
        self.displacement = displacement
        self.crew = crew
        self.max_speed = max_speed
        self.speed = 0

    def move(self, speed):
        if speed > self.max_speed:
            return f"Максимальна швидкість — {self.max_speed} вузлів"
        self.speed = speed
        if speed == 0:
            return f"{self.name} зупинено"
        return f"{self.name} рухається зі швидкістю {speed} вузлів"

    def stop(self):
        self.speed = 0
        return f"{self.name} зупинено"

    def info(self):
        return (f"{self.name} — {self.displacement} т, екіпаж {self.crew} ос., "
                f"швидкість {self.speed}/{self.max_speed} вузлів")


class Frigate(Ship):
    def __init__(self, name, displacement, crew, max_speed, missiles=8):
        super().__init__(name, displacement, crew, max_speed)
        self.missiles = missiles

    def launch_missile(self):
        if self.missiles <= 0:
            return "Ракет немає"
        self.missiles -= 1
        return f"Запущено ракету, залишилось: {self.missiles}"

    def info(self):
        return f"{super().info()} — фрегат, ракет: {self.missiles}"


class Destroyer(Ship):
    def __init__(self, name, displacement, crew, max_speed, torpedoes=10):
        super().__init__(name, displacement, crew, max_speed)
        self.torpedoes = torpedoes

    def fire_torpedo(self):
        if self.torpedoes <= 0:
            return "Торпед немає"
        self.torpedoes -= 1
        return f"Запущено торпеду, залишилось: {self.torpedoes}"

    def info(self):
        return f"{super().info()} — есмінець, торпед: {self.torpedoes}"


class Cruiser(Ship):
    def __init__(self, name, displacement, crew, max_speed, aircraft=2):
        super().__init__(name, displacement, crew, max_speed)
        self.aircraft = aircraft

    def launch_aircraft(self):
        if self.aircraft <= 0:
            return "Немає літаків на борту"
        self.aircraft -= 1
        return f"Літак злетів, на борту залишилось: {self.aircraft}"

    def info(self):
        return f"{super().info()} — крейсер, літаків: {self.aircraft}"


frigate = Frigate("Гетьман Сагайдачний", 3200, 180, 32)
print(frigate.info())
print(frigate.move(20))
print(frigate.launch_missile())
print(frigate.launch_missile())
print(frigate.info())
print(frigate.stop())
print()

destroyer = Destroyer("Безстрашний", 4500, 250, 30)
print(destroyer.info())
print(destroyer.move(25))
print(destroyer.fire_torpedo())
print(destroyer.info())
print()

cruiser = Cruiser("Україна", 12000, 500, 32)
print(cruiser.info())
print(cruiser.launch_aircraft())
print(cruiser.launch_aircraft())
print(cruiser.launch_aircraft())
print(cruiser.info())
