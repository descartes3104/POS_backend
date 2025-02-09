import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import urllib.parse

# 環境変数をロード
load_dotenv()

# 環境変数を取得
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
SSL_CA = os.getenv("SSL_CA")

# パスワードをURLエンコード
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}?ssl_ca={SSL_CA}"

# SQLAlchemyの設定
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DBセッションを取得する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("接続成功:", result.scalar() == 1)
    except Exception as e:
        print("接続失敗:", e)
        print("接続情報を確認してください。")

if __name__ == "__main__":
    test_connection()
    # デバッグ用の出力は開発環境でのみ行う
    if os.getenv("ENV") == "development":
        print("データベース接続情報:")
        print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

