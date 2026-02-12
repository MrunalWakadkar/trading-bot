import logging
from .validators import validate_side, validate_order_type, validate_quantity

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = self.client.place_order(**params)

        logger.info(f"Order response: {response}")
        return response
