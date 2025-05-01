import pytest
from app import app, db, Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        # Seed with a sample product
        product = Product(name="Sample Product", price=9.99, image_url="https://example.com/image.png")
        db.session.add(product)
        db.session.commit()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sample Product" in response.data

def test_add_product(client):
    response = client.post('/add-product', data={
        'name': 'Test Product',
        'price': '19.99',
        'image_url': 'http://example.com/test.png'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Product" in response.data

def test_add_to_cart(client):
    response = client.post('/add-to-cart/1')
    assert response.status_code == 200
    assert response.get_json()['message'] == "Product 1 added to cart."
