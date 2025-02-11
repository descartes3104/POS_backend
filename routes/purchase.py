from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Transaction, TransactionDetail, Product
from ..schemas import PurchaseSchema

router = APIRouter()

@router.post("/purchase")
def create_transaction(purchase: PurchaseSchema, db: Session = Depends(get_db)):
    # 1-1 取引テーブルへ登録
    new_transaction = Transaction(
        EMP_CD=purchase.cashier_code,
        STORE_CD=purchase.store_code,
        POS_NO=purchase.pos_id,
        TOTAL_AMT=0
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    transaction_id = new_transaction.TRD_ID
    total_amount = 0
    
    # 1-2 取引明細テーブルへ登録
    for item in purchase.products:
        product = db.query(Product).filter(Product.CODE == item.product_code).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_code} not found")
        
        new_detail = TransactionDetail(
            transaction_id=transaction_id,
            product_id=product.PRD_ID,
            product_code=item.product_code,
            product_name=item.product_name,
            product_price=item.product_price
        )
        db.add(new_detail)
        total_amount += item.product_price

    # 1-4 取引テーブルを更新
    new_transaction.TOTAL_AMT = int(total_amount)
    db.commit()

    return {"success": True, "total_amount": total_amount}
