def format_currency(amount):
    """Formatea una cantidad como moneda"""
    return f"${amount:.2f}"

def validate_price(price):
    """Valida que el precio sea un número positivo"""
    try:
        price = float(price)
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        return price
    except ValueError:
        raise ValueError("El precio debe ser un número válido")