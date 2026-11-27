from database import Database


class ProductRepository:
    def __init__(self, database=None):
        self.database = database or Database()

    def find_active(self, product_id):
        rows = self.database.get_data_to_dict(
            "SELECT ProductID, ProductName, Stock, Price FROM Products WHERE ProductID = %s AND State = 1",
            (product_id,),
        )
        return rows[0] if rows else None
