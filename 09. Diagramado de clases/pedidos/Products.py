from Supliers import Supliers
from Categories import Categories


class Products:

    id_product = 0

    # --- Método Constructor ---
    def __init__(self, product_name, supplier_id, category_id, quantity_per_unit, unit_price,
                 units_in_stock, units_on_order, reorder_level, discontinued):
        Products.id_product += 1
        self._id_product = Products.id_product
        self._product_name = product_name
        self._supplier_id = supplier_id
        self._category_id = category_id
        self._quantity_per_unit = quantity_per_unit
        self._unit_price = unit_price
        self._units_in_stock = units_in_stock
        self._units_on_order = units_on_order
        self._reorder_level = reorder_level
        self._discontinued = discontinued
        # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_product_name(self, product_name):
        self._product_name = product_name

    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    def set_category_id(self, category_id):
        self._category_id = category_id

    def set_quantity_per_unit(self, quantity_per_unit):
        self._quantity_per_unit = quantity_per_unit

    def set_unit_price(self, unit_price):
        self._unit_price = unit_price

    def set_units_in_stock(self, units_in_stock):
        self._units_in_stock = units_in_stock

    def set_units_on_order(self, units_on_order):
        self._units_on_order = units_on_order

    def set_reorder_level(self, reorder_level):
        self._reorder_level = reorder_level

    def set_discontinued(self, discontinued):
        self._discontinued = discontinued
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_id_product(self):
        return self._id_product

    def get_product_name(self):
        return self._product_name

    def get_supplier_id(self):
        return self._supplier_id

    def get_category_id(self):
        return self._category_id

    def get_quantity_per_unit(self):
        return self._quantity_per_unit

    def get_unit_price(self):
        return self._unit_price

    def get_units_in_stock(self):
        return self._units_in_stock

    def get_units_on_order(self):
        return self._units_on_order

    def get_reorder_level(self):
        return self._reorder_level

    def get_discontinued(self):
        return self._discontinued
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Product N° {self._id_product}
            product_name: {self._product_name}
            supplier_id: {self._supplier_id}
            category_id: {self._category_id}
            quantity_per_unit: {self._quantity_per_unit}
            unit_price: {self._unit_price}
            units_in_stock: {self._units_in_stock}
            units_on_order: {self._units_on_order}
            discontinued: {self._discontinued}
        """


if __name__ == "__main__":
    suplier_prueba = Supliers("calle 67 90-09", "New York", "Coca bit",
                              "contact name", "contact title", "EEUU", "fax", 5555098, 98765, "Norte", "home page")

    category1 = Categories("Anime", "La mejor categoría de todas", "anime.png")

    producto1 = Products("Gorra de beisbol", suplier_prueba.get_id_supplier(
    ), category1.get_id_category(), 567, 80000, 1000, 87, "reorder level", False)

    print(producto1)
