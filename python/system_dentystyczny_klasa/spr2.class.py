import os
import datetime

class AppointmentManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        """Sprawdza czy number telefonu ma 9 cyfr."""
        return len(phone_number) == 9 and phone_number.isdigit()
    
    def check_file_exists(self) -> bool:
        """Sprawdza czy istnieje plik o podanej ścieżce"""
        return os.path.exists(self.file_path)

    def get_appointments_from_file(self) -> list:
        """Wczytuje zapisane wizyty z pliku."""
        if self.check_file_exists():
            with open(self.file_path, 'r') as file:
                return file.readlines()
        return []
    
    def check_availability(self, appointments: list, date: str) -> bool:
        """Sprawdza czy jest mniej niż 8 wiyt na daną datę."""
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Nieprawidłowy format daty. Oczekiwano YYYY-MM-DD")
            return False
        
        return sum(date in appt for appt in appointments) < 8
    
    def save_appointment(self, phone_number: str, date: str, time: str) -> bool:
        """Zapisuje nową wizytę, jeśli numer telefonu i data są poprawne."""
        if not self.validate_phone_number(phone_number):
            print("Nieprawidłowy numer telefonu.")
            return False

        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
            print("Brak wolnych terminów na ten dzień.")
            return False

        with open(self.file_path, 'a') as file:
            file.write(f"{phone_number};{date};{time}\n")
        print("Wizyta została napisana.")
        return True
    
    def show_available_hours(self, date: str) -> None:
        """Wyświetla dostępne godziny wizyt na podaną datę."""
        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
            print("Brak wolnych terminów na ten dzień.")
            return

        working_hours = [f"{hour}:00" for hour in range(9,17)]
        booked_hours = [appt.split(';')[2].strip() for appt in appointments if date in appt]
        available_hours = [hour for hour in working_hours if hour not in booked_hours]

        if available_hours:
            print("Dostępne godziny:", ", ".join(available_hours))
        else:
            print("Brak wolnych terminów na ten dzień.")

# Przykładowe użyie
file_path = "appointments.txt"
appointment_manager = AppointmentManager(file_path)
date = input("Podaj datę (YYYY-MM-DD): ")
appointment_manager.show_available_hours(date)