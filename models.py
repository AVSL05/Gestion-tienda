from datetime import datetime

class Product:
    CATEGORIES = [
        'Joyería',
        'Perfumería',
        'Calzado',
        'Bolsas',
        'Mochilas',
        'Cobertores',
        'Sábanas'
    ]

    def __init__(self, name, category, cost_price, selling_price, description="", quantity=1):
        self.name = name
        self.category = category
        self.cost_price = float(cost_price)
        self.selling_price = float(selling_price)
        self.description = description
        self.quantity = int(quantity)
        self.sold_quantity = 0
        self.sold = False
        self.created_at = datetime.now()

    def calculate_profit(self):
        return self.selling_price - self.cost_price

    def calculate_total_profit(self):
        """Calcula la ganancia total basada en cantidad vendida"""
        return (self.selling_price - self.cost_price) * self.sold_quantity

    def get_available_quantity(self):
        """Retorna la cantidad disponible para venta"""
        return self.quantity - self.sold_quantity

    def is_sold_out(self):
        """Verifica si el producto está agotado"""
        return self.sold_quantity >= self.quantity

    def sell_units(self, units_to_sell):
        """Vende una cantidad específica de unidades"""
        if units_to_sell <= self.get_available_quantity():
            self.sold_quantity += units_to_sell
            if self.sold_quantity >= self.quantity:
                self.sold = True
            return True
        return False

    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'cost_price': self.cost_price,
            'selling_price': self.selling_price,
            'description': self.description,
            'quantity': self.quantity,
            'sold_quantity': self.sold_quantity,
            'sold': self.sold,
            'created_at': self.created_at
        }