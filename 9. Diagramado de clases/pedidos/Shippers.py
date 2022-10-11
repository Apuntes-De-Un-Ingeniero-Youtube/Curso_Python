class Shippers:

    id_shipper = 0

    # --- Método Constructor ---
    def __init__(self, company_name, phone):
        Shippers.id_shipper += 1
        self._id_shipper = Shippers.id_shipper
        self._company_name = company_name
        self._phone = phone
        # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_company_name(self, company_name):
        self._company_name = company_name

    def set_phone(self, phone):
        self._phone = phone
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_company_name(self):
        return self._company_name

    def get_phone(self):
        return self._phone
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Shipper N° {self._id_shipper}
            company name: {self._company_name}
            phone: {self._phone}
        """


if __name__ == "__main__":
    shipper1 = Shippers("oracle", 9886765)
    print(shipper1)
