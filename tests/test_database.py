import pandas as pd
from sqlalchemy import create_engine, text

def test_specific_value_exists():
    engine = create_engine("sqlite:///:memory:")

    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE products (name TEXT)"))
        conn.execute(text("INSERT INTO products VALUES ('Laptop'), ('Phone')"))
        conn.commit()

    data = pd.read_sql("SELECT * FROM products", engine)

    assert "Laptop" in data["name"].values
