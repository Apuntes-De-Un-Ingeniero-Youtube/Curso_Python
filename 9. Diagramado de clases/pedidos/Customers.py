class Customers:

    id_customer = 0

    # --- Método Constructor ---
    def __init__(self, company_name, contact_name, contact_title, address,
                 city, region, postal_code, country, phone, fax):
        Customers.id_customer += 1
        self._id_customer = Customers.id_customer
        self._company_name = company_name
        self._contact_name = contact_name
        self._contact_title = contact_title
        self._address = address
        self._city = city
        self._region = region
        self._postal_code = postal_code
        self._country = country
        self._phone = phone
        self._fax = fax
        # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_company_name(self, company_name):
        self._company_name = company_name

    def set_contact_name(self, contact_name):
        self._contact_name = contact_name

    def set_contact_title(self, contact_title):
        self._contact_title = contact_title

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

    def set_phone(self, phone):
        self._phone = phone

    def set_fax(self, fax):
        self._fax = fax
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_id_customer(self):
        return self._id_customer

    def get_company_name(self):
        return self._company_name

    def get_contact_name(self):
        return self._contact_name

    def get_contact_title(self):
        return self._contact_title

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

    def get_phone(self):
        return self._phone

    def get_fax(self):
        return self._fax
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Customer N° {self._id_customer}
            company_name: {self._company_name}
            contact_name: {self._contact_name}
            contact_title: {self._contact_title}
            address: {self._address}
            City: {self._city}
            Region: {self._region}
            Postal Code: {self._postal_code}
            Country: {self._country}
            Phone: {self._phone}
            fax: {self._fax}
        """


if __name__ == "__main__":
    customer_prueba = Customers("calle 67 90-09", "New York", "Coca bit",
                                "contact name", "contact title", "EEUU", "fax", 5555098, 98765, "Norte")
    customer_prueba.set_address("calle 67 90-09 1")
    customer_prueba.set_city("New York 1")
    customer_prueba.set_company_name("Coca bit 1")
    customer_prueba.set_contact_name("contact name 1")
    customer_prueba.set_contact_title("contact title 1")
    customer_prueba.set_country("EEUU 1")
    customer_prueba.set_fax("fax 1")
    customer_prueba.set_phone(55550981)
    customer_prueba.set_postal_code(987651)
    customer_prueba.set_region("Norte 1")
    print(customer_prueba)
