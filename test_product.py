import products
import pytest


def test_create_normal_product():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_create_invalid_product():
    with pytest.raises(Exception):
        products.Product("MacBook Air M2", price=-1450, quantity=100)


def test_zero_quantity():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)
    assert product.quantity == 0
    assert not product.is_active()


def test_modify_quantity():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(3)
    assert product.quantity == 97


def test_buy_larger_quantity_than_exists():
    product = products.Product("MacBook Air M2", price=1450, quantity=100)

    with pytest.raises(ValueError):
        product.buy(105)


# ============ 5 passed in 0.03s =============
