from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schemas import ProductSchema

router = APIRouter()

@router.get("/{code}", response_model=ProductSchema)
def get_product(code: str, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.CODE == code).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")





    # このコードは、FastAPIを使用して特定の製品コードに基づいて製品情報を取得するエンドポイントを定義しています。
    # @router.get("/{code}", response_model=ProductSchema) デコレーターは、HTTP GETリクエストを処理するエンドポイントを定義します。
    # {code} はURLパスパラメータで、取得したい製品のコードを指定します。
    # get_product 関数は、製品コードを引数として受け取り、データベースセッションを依存関係として取得します。
    # db.query(Product).filter(Product.CODE == code).first() は、データベースから指定された製品コードに一致する製品を検索します。
    # 一致する製品が見つからない場合、HTTP 404エラーを発生させます。
    # 一致する製品が見つかった場合、その製品情報を返します。
