from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base
import datetime

class Product(Base):
    __tablename__ = "m_product_inoue_master"

    PRD_ID = Column(Integer, primary_key=True, autoincrement=True, index=True)  # 商品一意キー
    CODE = Column(String(13), unique=True, nullable=False, index=True)      # 商品コード（重複不可）
    NAME = Column(String(50), nullable=False)                               # 商品名称
    PRICE = Column(Integer, nullable=False)                                 # 商品単価

class Transaction(Base):
    __tablename__ = "m_product_inoue_transaction"

    TRD_ID = Column(Integer, primary_key=True, autoincrement=True, index=True)  # 取引一意キー
    DATETIME = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))  # UTCで現在時刻を取得
    EMP_CD = Column(String(10), nullable=False)                                 # レジ担当者コード
    STORE_CD = Column(String(5), nullable=False)                                # 店舗コード
    POS_NO = Column(String(3), nullable=False)                                  # POS機ID
    TOTAL_AMT = Column(Float, nullable=False)  # ここをFloatに変更し、nullable=Falseを追加

class TransactionDetail(Base):
    __tablename__ = "m_product_inoue_transaction_detail"

    TRD_ID = Column(Integer, ForeignKey("m_product_inoue_transaction.TRD_ID"), nullable=False, index=True)
    DTL_ID = Column(Integer, primary_key=True, autoincrement=True, index=True)  # 取引明細一意キー
    PRD_ID = Column(Integer, ForeignKey("m_product_inoue_master.PRD_ID"), nullable=False)  # 商品一意キー（FK）
    PRD_CODE = Column(String(13), nullable=False)  # 商品コード（冗長データ）
    PRD_NAME = Column(String(50), nullable=False)  # 商品名称（冗長データ）
    PRD_PRICE = Column(Integer, nullable=False)  # 商品単価（冗長データ）
    transaction = relationship("Transaction", back_populates="details")
    product = relationship("Product")
    Transaction.details = relationship("TransactionDetail", back_populates="transaction")


