from django.test import Client


def test_create_product():
    client = Client()

    with open("test.jpg", "rb") as image:
        response = client.post(
            "/api/products",
            {
                "name": "Test Product",
                "price": "10.00",
                "tags_ids": ["1", "2", "3"],
                "image": image,
            }
        )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.content.decode())