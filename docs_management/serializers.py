from rest_framework import serializers
from django.core import exceptions
from docs_management.models import UploadedDoc, ExtractedDoc


class UploadedDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDoc
        fields = ("id", "uploaded_on", "storage_path", "status")



class UpdateStatusSerializer(serializers.ModelSerializer):
	status = serializers.IntegerField()
	class Meta:
		model = UploadedDoc
		fields = ["status"]

	def update_status(self, instance):
		instance.status = self.data["status"]

		return instance


class UpdateExtracedDocSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExtractedDoc
		# fields = ["invoice_number", "summary"]
		exclude = ["uploaded_doc"]


# class PurchaseItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     quantity = serializers.IntegerField(read_only=True)


# class PurchaseSerializer(serializers.Serializer):
#     items = PurchaseItemSerializer(many=True)

#     def update_inventory(self):
#         errors = []
#         objs = {
#             "passed": [],
#             "failed": [],
#         }

#         for item in self.data['items']:
#             try:
#                 item_obj = InventoryItem.objects.get(id=item["id"])
#                 item_obj.purchase(item["quantity"])
#                 objs["passed"].append({
#                     "status": True,
#                     "id": item_obj,
#                 })

#             except exceptions.ObjectDoesNotExist as err:
#                 errors.append({"id": item["id"], "error": "Invalid ID"})
#                 objs["failed"].append({
#                     "status": False,
#                     "id": item["id"],
#                 })

#             except Exception as err:
#                 errors.append({"id": item["id"], "error": str(err)})
#                 objs["failed"].append({
#                     "status": False,
#                     "id": item["id"],
#                 })

#         resp = {
#             "status": True,
#             "errors": [],
#         }

#         if not objs["failed"]:
#             resp["status"] = False
#             resp["errors"] = {
#                 "des": "Update failed",
#                 "errors": errors
#             }
#         else:
#             for obj in objs["passed"]:
#                 obj["id"].save()

#         return resp
