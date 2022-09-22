import pytest
from carts.models import CartLine


pytestmark = pytest.mark.django_db


def test_returns_empty_cart(client):
    response = client.get("/cart/")

    assert response.status_code == 200
    assert response.json() == {"lines": []}


def test_returns_cart_with_one_product(client):
    CartLine.objects.create(sku="50776", quantity=5)

    response = client.get("/cart/")

    assert response.status_code == 200
    assert response.json() == {"lines": [{"sku": "50776", "quantity": 5}]}


@pytest.mark.skip
def test_adds_product_to_cart_when_product_not_in_cart(client):
    # Arrange (?)
    # Act (post a quantity to any sku)
    # Assert (check status_code and response of the new cart state)
    pass


@pytest.mark.skip
def test_adds_product_to_cart_when_product_in_cart(client):
    CartLine.objects.create(sku="50776", quantity=5)
    # Act (post a quantity to the 50776 sku)
    # Assert (check status_code and response of the new cart state)
    pass


@pytest.mark.skip
def test_substracts_quantity(client):
    CartLine.objects.create(sku="50776", quantity=5)
    # Act (post a quantity substraction to the 50776 sku)
    # Assert (check status_code and response of the new cart state)
    pass
    

@pytest.mark.skip
def test_removes_product_when_substracting_greater_quantity_than_the_carts_has(client):
    CartLine.objects.create(sku="50776", quantity=5)
    # Act (substract more than 5 units to the 50776 sku)
    # Assert (check status_code and response of the new cart state)
    pass


@pytest.mark.skip
def test_does_nothing_when_product_does_not_exists(client):
    # Arrange (?)
    # Act (substract any quantity to any sku)
    # Assert (check status_code and response of the new cart state)
    pass

