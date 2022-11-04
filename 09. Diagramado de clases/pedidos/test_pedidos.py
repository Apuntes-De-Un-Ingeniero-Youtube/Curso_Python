from Order_details import Order_Details
from Orders import Orders
from Customers import Customers
from Employees import Employees
from Products import Products
from Supliers import Supliers
from Categories import Categories

# Creando un cliente
customer_prueba = Customers("calle 67 90-09", "New York", "Coca bit",
                            "contact name", "contact title", "EEUU", "fax", 5555098, 98765, "Norte")

# Creando un empleado
empleado1 = Employees("Estevez", "Juan", "Title", "Courtesy", "10/10/1978", "23/02/2001", "Calle 3 27 68",
                      "Bogotá", "Cundinamarca", "45678", "Colombia", "5465476296", "+57", "No hay notas", "Pepito Perez")


# Creando una orden de compra
order_1 = Orders(customer_prueba.get_id_customer(), empleado1.get_id_employee(), "27-05-2010", "28-05-2010",
                 "29-10-2017", "ship_via", "freight", "ship name", "dirección", "Bogotá", "norte", 987654, "colombia")

# Creando supplier
suplier_prueba = Supliers("calle 67 90-09", "New York", "Coca bit",
                          "contact name", "contact title", "EEUU", "fax", 5555098, 98765, "Norte", "home page")

# Creando categorias
category1 = Categories("Anime", "La mejor categoría de todas", "anime.png")
category2 = Categories("Camisas", "Camisa cara", "camisa.png")

# Creando productos
jabon = Products("Jabón Dove", suplier_prueba.get_id_supplier(
), category1.get_id_category(), 567, 80000, 1000, 87, "reorder level", False)

camisa = Products("JCamisa Gucci", suplier_prueba.get_id_supplier(
), category2.get_id_category(), 563, 700000, 1270, 7, "reorder level", False)

# Generación detalle de orden de compra
detail_order_1 = Order_Details(order_1.get_id_order(
), [jabon.get_product_name(), camisa.get_product_name()], 3987, 87, 0)

print(detail_order_1)
