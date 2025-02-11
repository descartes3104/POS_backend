from pydantic import BaseModel
from typing import List, Optional

class ProductSchema(BaseModel):
    code: str
    name: str
    price: float

class TransactionDetailSchema(BaseModel):
    product_code: str
    product_name: str
    product_price: float

class PurchaseSchema(BaseModel):
    cashier_code: Optional[str] = "9999999999"
    store_code: str = "30"
    pos_id: str = "90"
    products: List[TransactionDetailSchema]
    # このコードは、購入情報を表すスキーマを定義しています。
    # PurchaseSchema クラスは、購入情報のスキーマを定義するために使用されます。
    # cashier_code はオプションの文字列フィールドで、デフォルト値は "9999999999" です。
    # store_code は文字列フィールドで、デフォルト値は "30" です。
    # pos_id は文字列フィールドで、デフォルト値は "90" です。
    # products は TransactionDetailSchema のリストで、購入した商品の詳細情報を含みます。
