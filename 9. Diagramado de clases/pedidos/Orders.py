from Customers import Customers
from Employees import Employees


class Orders:

    id_order = 0

    # --- Método Constructor ---
    def __init__(self, customer_id, employee_id, order_date, required_date, shipped_date,
                 ship_via, freight, ship_name, ship_address, ship_city, ship_region,
                 ship_postal_code, ship_country):
        Orders.id_order += 1
        self._id_order = Orders.id_order
        self._customer_id = customer_id
        self._employee_id = employee_id
        self._order_date = order_date
        self._required_date = required_date
        self._shipped_date = shipped_date
        self._ship_via = ship_via
        self._freight = freight
        self._ship_name = ship_name
        self._ship_address = ship_address
        self._ship_city = ship_city
        self._ship_region = ship_region
        self._ship_postal_code = ship_postal_code
        self._ship_country = ship_country
        # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_order_date(self, order_date):
        self._order_date = order_date

    def set_required_date(self, required_date):
        self._required_date = required_date

    def set_shipped_date(self, shipped_date):
        self._shipped_date = shipped_date

    def set_ship_via(self, ship_via):
        self._ship_via = ship_via

    def set_freight(self, freight):
        self._freight = freight

    def set_ship_name(self, ship_name):
        self._ship_name = ship_name

    def set_ship_address(self, ship_address):
        self._ship_address = ship_address

    def set_ship_city(self, ship_city):
        self._ship_city = ship_city

    def set_ship_region(self, ship_region):
        self._ship_region = ship_region

    def set_ship_postal_code(self, ship_postal_code):
        self._ship_postal_code = ship_postal_code

    def set_ship_country(self, ship_country):
        self._ship_country = ship_country
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_customer_id(self):
        return self._customer_id

    def get_employee_id(self):
        return self._employee_id

    def get_order_date(self):
        return self._order_date

    def get_required_date(self):
        return self._required_date

    def get_shipped_date(self):
        return self._shipped_date

    def get_ship_via(self):
        return self._ship_via

    def get_freight(self):
        return self._freight

    def get_ship_name(self):
        return self._ship_name

    def get_ship_address(self):
        return self._ship_address

    def get_ship_city(self):
        return self._ship_city

    def get_ship_region(self):
        return self._ship_region

    def get_ship_postal_code(self):
        return self._ship_postal_code

    def get_ship_country(self):
        return self._ship_country
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Order N° {self._id_order}
            customer id: {self._customer_id}
            employee id: {self._employee_id}
            order_date: {self._order_date}
            required_date: {self._required_date}
            shipped_date: {self._shipped_date}
            ship_via: {self._ship_via}
            freight: {self._freight}
            ship_name: {self._ship_name}
            ship_address: {self._ship_address}
            ship_city: {self._ship_city}
            ship_region: {self._ship_region}
            ship_postal_code: {self._ship_postal_code}
            ship_country: {self._ship_country}
        """


if __name__ == "__main__":
    customer_prueba = Customers("calle 67 90-09", "New York", "Coca bit",
                                "contact name", "contact title", "EEUU", "fax", 5555098, 98765, "Norte")

    empleado1 = Employees("Estevez", "Juan", "Title", "Courtesy", "10/10/1978", "23/02/2001", "Calle 3 27 68",
                          "Bogotá", "Cundinamarca", "45678", "Colombia", "5465476296", "+57", "No hay notas", "Pepito Perez")

    orden1 = Orders(customer_prueba.get_contact_title(), empleado1.get_id_employee(), "27-05-2010", "28-05-2010",
                    "29-10-2017", "ship_via", "freight", "ship name", "dirección", "Bogotá", "norte", 987654, "colombia")

    print(orden1)
