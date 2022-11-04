class Employees:

    id_employee = 0

    # --- Constructor de clase ---
    def __init__(self, last_name, first_name, title, title_of_courtesy, birth_date, hire_date,
                 address, city, region, postal_code, country, home_phone, extension, notes, reports_to):
        Employees.id_employee += 1
        self._id_employee = Employees.id_employee
        self._last_name = last_name
        self._first_name = first_name
        self._title = title
        self._title_of_courtesy = title_of_courtesy
        self._birth_date = birth_date
        self._hire_date = hire_date
        self._address = address
        self._city = city
        self._region = region
        self._postal_code = postal_code
        self._country = country
        self._home_phone = home_phone
        self._extension = extension
        self._notes = notes
        self._reports_to = reports_to
    # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_title(self, title):
        self._title = title

    def set_title_of_courtesy(self, title_of_courtesy):
        self._title_of_courtesy = title_of_courtesy

    def set_birth_date(self, birth_date):
        self._birth_date = birth_date

    def set_hire_date(self, hire_date):
        self._hire_date = hire_date

    def set_address(self, address):
        self._address = address

    def set_city(self, city):
        self._city = city

    def set_region(self, region):
        self._region = region

    def set_postal_code(self, postal_code):
        self._postal_code = postal_code

    def set_country(self, country):
        self._country = country

    def set_home_phone(self, home_phone):
        self._home_phone = home_phone

    def set_extension(self, extension):
        self._extension = extension

    def set_notes(self, notes):
        self._notes = notes

    def set_reports_to(self, reports_to):
        self._reports_to = reports_to
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_id_employee(self):
        return self._id_employee

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_title(self):
        return self._title

    def get_title_of_courtesy(self):
        return self._title_of_courtesy

    def get_birth_date(self):
        return self._birth_date

    def get_hire_date(self):
        return self._hire_date

    def get_address(self):
        return self._address

    def get_city(self):
        return self._city

    def get_region(self):
        return self._region

    def get_postal_code(self):
        return self._postal_code

    def get_country(self):
        return self._country

    def get_home_phone(self):
        return self._home_phone

    def get_extension(self):
        return self._extension

    def get_notes(self):
        return self._notes

    def get_reports_to(self):
        return self._reports_to
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Empleado N° {self._id_employee}
            LastName: {self._last_name}
            FirstName: {self._first_name}
            Title: {self._title}
            Title Of Courtesy: {self._title_of_courtesy}
            BirthDate: {self._birth_date}
            HireDate: {self._hire_date}
            Address: {self._address}
            City: {self._city}
            Region: {self._region}
            Postal Code: {self._postal_code}
            Country: {self._country}
            Home Phone: {self._home_phone}
            Extension: {self._extension}
            Notes: {self._notes}
            Reports To: {self._reports_to}
        """


if __name__ == "__main__":
    empleado1 = Employees("Estevez", "Juan", "Title", "Courtesy", "10/10/1978", "23/02/2001", "Calle 3 27 68",
                          "Bogotá", "Cundinamarca", "45678", "Colombia", "5465476296", "+57", "No hay notas", "Pepito Perez")
    print(empleado1)
