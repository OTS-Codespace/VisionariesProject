from rest_framework.test import APITestCase
from rest_framework import status
from galio.models import Category, SubCategory, Product

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample category for testing
        self.category = Category.objects.create(name="Electronics", description="Electronic items")
        self.valid_payload = {"name": "Books", "description": "Books and magazines"}
        self.invalid_payload = {"name": ""}  # Name is required

    def test_get_categories(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure categories are returned

    def test_create_category_valid(self):
        response = self.client.post('/categories/', data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_create_category_invalid(self):
        response = self.client.post('/categories/', data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_category_detail(self):
        response = self.client.get(f'/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        updated_payload = {"name": "Updated Electronics", "description": "Updated description"}
        response = self.client.put(f'/categories/{self.category.id}/', data=updated_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_payload['name'])

    def test_delete_category(self):
        response = self.client.delete(f'/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())


class SubCategoryAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample category and subcategory
        self.category = Category.objects.create(name="Electronics", description="Electronic items")
        self.subcategory = SubCategory.objects.create(name="Mobile Phones", category=self.category)
        self.valid_payload = {"name": "Laptops", "category": self.category.id}
        self.invalid_payload = {"name": "", "category": self.category.id}  # Name is required

    def test_get_subcategories(self):
        response = self.client.get('/subcategories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_subcategory_valid(self):
        response = self.client.post('/subcategories/', data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_create_subcategory_invalid(self):
        response = self.client.post('/subcategories/', data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_subcategory_detail(self):
        response = self.client.get(f'/subcategories/{self.subcategory.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.subcategory.name)

    def test_update_subcategory(self):
        updated_payload = {"name": "Tablets", "category": self.category.id}
        response = self.client.put(f'/subcategories/{self.subcategory.id}/', data=updated_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_payload['name'])

    def test_delete_subcategory(self):
        response = self.client.delete(f'/subcategories/{self.subcategory.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SubCategory.objects.filter(id=self.subcategory.id).exists())


class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample category, subcategory, and product
        self.category = Category.objects.create(name="Electronics", description="Electronic items")
        self.subcategory = SubCategory.objects.create(name="Mobile Phones", category=self.category)
        self.product = Product.objects.create(
            name="iPhone 14", description="Latest Apple iPhone", price=999.99, stock=50,
            category=self.category, subcategory=self.subcategory
        )
        self.valid_payload = {
            "name": "MacBook Pro", "description": "Apple Laptop", "price": 1299.99, "stock": 20,
            "category": self.category.id, "subcategory": self.subcategory.id
        }
        self.invalid_payload = {
            "name": "", "description": "Invalid product", "price": -100, "stock": -5,
            "category": self.category.id, "subcategory": self.subcategory.id
        }

    def test_get_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_product_valid(self):
        response = self.client.post('/products/', data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_create_product_invalid(self):
        response = self.client.post('/products/', data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_product_detail(self):
        response = self.client.get(f'/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        updated_payload = {
            "name": "iPhone 15", "description": "Updated Apple iPhone", "price": 1099.99, "stock": 40,
            "category": self.category.id, "subcategory": self.subcategory.id
        }
        response = self.client.put(f'/products/{self.product.id}/', data=updated_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_payload['name'])

    def test_delete_product(self):
        response = self.client.delete(f'/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
