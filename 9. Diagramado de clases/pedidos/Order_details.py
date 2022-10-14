class Order_Details:

    # --- Método Constructor ---
    def __init__(self, order_id, products_id, unit_price, quantity, discount):
        self._order_id = order_id
        self._products_id = list(products_id)
        self._unit_price = unit_price
        self._quantity = quantity
        self._discount = discount
    # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_order_id(self, order_id):
        self._order_id = order_id

    def set_products_id(self, products_id):
        self._products_id = products_id

    def set_unit_price(self, unit_price):
        self._unit_price = unit_price

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_discount(self, discount):
        self._discount = discount
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_order_id(self):
        return self._order_id

    def get_products_id(self):
        return self._products_id

    def get_unit_price(self):
        return self._unit_price

    def get_quantity(self):
        return self._quantity

    def get_discount(self):
        return self._discount
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Order Detail
            Order_id: {self._order_id}
            products: {self._products_id}
            unit_price: {self._unit_price}
            quantity: {self._quantity}
            discount: {self._discount}
        """

