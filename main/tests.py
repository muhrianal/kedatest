import json
from urllib import response
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from matplotlib.font_manager import json_dump

from .models import Supplier, Material

class TestMaterial(TestCase):
    def setUp(self):
        self.supplier_obj = Supplier.objects.create(
            supplier_name=" PT Keda"
        )
        self.material_obj = Material.objects.create(
            material_code="ABC123",
            material_name="Celana Jeans Panjang",
            material_type="Jeans",
            material_buy_price=45000,
            supplier = self.supplier_obj
        )

    def test_home_api_overview(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
        

    def test_get_materials(self):
        response = Client().get("/materials")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["material_code"], self.material_obj.material_code)
        

    def test_get_materials_with_filter(self):
        response = Client().get("/materials?material_type=Jeans")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["material_type"], "Jeans")
        

    def test_get_materials_empty(self):
        self.material_obj.delete()
        response = Client().get("/materials")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, dict())


    def test_create_material(self):
        self.valid_payload =  {
                "material_code": "DEF123",
                "material_name": "Kaos",
                "material_type": "Fabric",
                "supplier": 1,
                "material_buy_price": 3246
            }
        
        self.invalid_payload =  {
                "material_name": "Kaos",
                "material_type": "Fabric",
                "supplier": 1,
                "material_buy_price": 3246
            }
        
        # test proper creation
        response = Client().post(
            path="/material/create", 
            data=json.dumps(self.valid_payload),
            content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(Material.objects.get(pk=self.valid_payload["material_code"]))

        # test createion with invalid payload
        response = Client().post(
            path="/material/create", 
            data=json.dumps(self.invalid_payload),
            content_type="application/json")
        
        self.assertEqual(response.status_code, 400)

        # test createion material to the material_code that already existed
        response = Client().post(
            path="/material/create", 
            data=json.dumps(self.valid_payload),
            content_type="application/json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data[0], "This data already exists")


    def test_update_material(self):
        self.update_payload = {
            "material_code" : "ABC123",
            "material_name" : "Celana Chino",
            "material_type" : "Fabric",
            "material_buy_price" : 45000,
            "supplier" : 1
        }

        response = Client().put(
            path="/material/update/" + self.update_payload["material_code"],
            data=json.dumps(self.update_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, self.update_payload)
        
        # test update with incomplete payload
        self.update_payload.pop("material_type")

        response = Client().put(
            path="/material/update/" + self.update_payload["material_code"],
            data=json.dumps(self.update_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_material(self):
        # test delete if the data exist
        pk = "ABC123"

        self.assertIsNotNone(Material.objects.get(pk=pk))
        response = Client().delete("/material/delete/" + pk)
        
        self.assertEqual(response.status_code, 202)
        self.assertIsNone(Material.objects.filter(pk=pk).first())

        # test delete if the data doesn't exist
        invalid_pk = "WADIDAW123"
        response = Client().delete("/material/delete/" + invalid_pk)
        self.assertEqual(response.status_code, 404)

        




