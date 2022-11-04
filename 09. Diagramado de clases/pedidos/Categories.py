class Categories:

    id_category = 0

    # --- Método Constructor ---
    def __init__(self, category_name, description, image):
        Categories.id_category += 1
        self._id_category = Categories.id_category
        self._category_name = category_name
        self._description = description
        self._image = image
        # --- Fin Constructor de clase ---

    # --- Métodos Set ---
    def set_category_name(self, category_name):
        self._category_name = category_name

    def set_description(self, description):
        self._description = description

    def set_image(self, image):
        self._image = image
    # --- Fin Métodos Set ---

    # --- Métodos Get ---
    def get_id_category(self):
        return self._id_category

    def get_category_name(self):
        return self._category_name

    def get_description(self):
        return self._description

    def get_image(self):
        return self._image
    # --- Fin Métodos Get ---

    def __str__(self) -> str:
        return f"""
        Category N° {self._id_category}
            category name: {self._category_name}
            description: {self._description}
            image: {self._image}
        """


if __name__ == "__main__":
    category1 = Categories("Anime", "La mejor categoría de todas", "anime.png")
    print(category1)
