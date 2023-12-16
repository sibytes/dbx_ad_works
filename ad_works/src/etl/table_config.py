
from ._table import BatchTable

PROJECT = "ad_works"
# register tables here and map them to a table Class
# if adding new properties then they must be added
# to the __init__ of the ._base_table.BaseTable
def tables():
  
  return {
    "hr_department": {
      "project": PROJECT,
      "filename": "hr_department",
      "default": BatchTable,
      "primary_keys": [
        "department_id"
      ]
    },
    "hr_employee": {
      "project": PROJECT,
      "filename": "hr_employee",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_ID"
      ]
    },
    "hr_employee_department_history": {
      "project": PROJECT,
      "filename": "hr_employee_department_history",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "department_id",
        "shift_id",
        "start_date"
      ]
    },
    "hr_employee_pay_history": {
      "project": PROJECT,
      "filename": "hr_employee_pay_history",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "rate_change_date"
      ]
    },
    "hr_job_candidate": {
      "project": PROJECT,
      "filename": "hr_job_candidate",
      "default": BatchTable,
      "primary_keys": [
        "job_candidate_date"
      ]
    },
    "hr_shift": {
      "project": PROJECT,
      "filename": "hr_shift",
      "default": BatchTable,
      "primary_keys": [
        "shift_id"
      ]
    },
    "person_address": {
      "project": PROJECT,
      "filename": "person_address",
      "default": BatchTable,
      "primary_keys": [
        "address_id"
      ]
    },
    "person_address_type": {
      "project": PROJECT,
      "filename": "person_address_type",
      "default": BatchTable,
      "primary_keys": [
        "address_type_id"
      ]
    },
    "person_business_entity": {
      "project": PROJECT,
      "filename": "person_business_entity",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "person_business_entity_address": {
      "project": PROJECT,
      "filename": "person_business_entity_address",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "address_id",
        "address_type_id"
      ]
    },
    "person_business_entity_contact": {
      "project": PROJECT,
      "filename": "person_business_entity_contact",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "person_id",
        "contact_type_id"
      ]
    },
    "person_contact_type": {
      "project": PROJECT,
      "filename": "person_contact_type",
      "default": BatchTable,
      "primary_keys": [
        "contact_type_id"
      ]
    },
    "person_country_region": {
      "project": PROJECT,
      "filename": "person_country_region",
      "default": BatchTable,
      "primary_keys": [
        "country_region_code"
      ]
    },
    "person_email_address": {
      "project": PROJECT,
      "filename": "person_email_address",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "email_address_id"
      ]
    },
    "person_password": {
      "project": PROJECT,
      "filename": "person_password",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "person_person": {
      "project": PROJECT,
      "filename": "person_person",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "person_personp_phone": {
      "project": PROJECT,
      "filename": "person_personp_phone",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "phone_number",
        "phone_number_type_id"
      ]
    },
    "person_phone_number_type": {
      "project": PROJECT,
      "filename": "person_phone_number_type",
      "default": BatchTable,
      "primary_keys": [
        "phone_number_type_id"
      ]
    },
    "person_state_province": {
      "project": PROJECT,
      "filename": "person_state_province",
      "default": BatchTable,
      "primary_keys": [
        "state_province_id"
      ]
    },
    "production_bill_of_materials": {
      "project": PROJECT,
      "filename": "production_bill_of_materials",
      "default": BatchTable,
      "primary_keys": [
        "bill_of_materials_id"
      ]
    },
    "production_culture": {
      "project": PROJECT,
      "filename": "production_culture",
      "default": BatchTable,
      "primary_keys": [
        "culture_id"
      ]
    },
    "production_document": {
      "project": PROJECT,
      "filename": "production_document",
      "default": BatchTable,
      "primary_keys": [
        "document_node"
      ]
    },
    "production_illustration": {
      "project": PROJECT,
      "filename": "production_illustration",
      "default": BatchTable,
      "primary_keys": [
        "illustration_id"
      ]
    },
    "production_location": {
      "project": PROJECT,
      "filename": "production_location",
      "default": BatchTable,
      "primary_keys": [
        
      ]
    },
    "production_product": {
      "project": PROJECT,
      "filename": "production_product",
      "default": BatchTable,
      "primary_keys": [
        "product_id"
      ]
    },
    "production_product_category": {
      "project": PROJECT,
      "filename": "production_product_category",
      "default": BatchTable,
      "primary_keys": [
        "product_category_id"
      ]
    },
    "production_product_cost_history": {
      "project": PROJECT,
      "filename": "production_product_cost_history",
      "default": BatchTable,
      "primary_keys": [
        "product_id",
        "start_date"
      ]
    },
    "production_product_description": {
      "project": PROJECT,
      "filename": "production_product_description",
      "default": BatchTable,
      "primary_keys": [
        "product_description_id"
      ]
    },
    "production_product_document": {
      "project": PROJECT,
      "filename": "production_product_document",
      "default": BatchTable,
      "primary_keys": [
        "product_id",
        "document_node"
      ]
    },
    "production_product_inventory": {
      "project": PROJECT,
      "filename": "production_product_inventory",
      "default": BatchTable,
      "primary_keys": [
        "product_id",
        "location_id"
      ]
    },
    "production_product_list_price_history": {
      "project": PROJECT,
      "filename": "production_product_list_price_history",
      "default": BatchTable,
      "primary_keys": [
        "product_id",
        "start_date"
      ]
    },
    "production_product_model": {
      "project": PROJECT,
      "filename": "production_product_model",
      "default": BatchTable,
      "primary_keys": [
        "product_model_id"
      ]
    },
    "production_product_model_illustration": {
      "project": PROJECT,
      "filename": "production_product_model_illustration",
      "default": BatchTable,
      "primary_keys": [
        "product_model_id",
        "illustration_id"
      ]
    },
    "production_product_model_product_description_culture": {
      "project": PROJECT,
      "filename": "production_product_model_product_description_culture",
      "default": BatchTable,
      "primary_keys": [
        "product_model_id",
        "product_description_id",
        "culture_id"
      ]
    },
    "production_product_photo": {
      "project": PROJECT,
      "filename": "production_product_photo",
      "default": BatchTable,
      "primary_keys": [
        "product_photo_id"
      ]
    },
    "production_product_product_photo": {
      "project": PROJECT,
      "filename": "production_product_product_photo",
      "default": BatchTable,
      "primary_keys": [
        "product_id"
        "product_photo_id"
      ]
    },
    "production_product_review": {
      "project": PROJECT,
      "filename": "production_product_review",
      "default": BatchTable,
      "primary_keys": [
        "product_review_id"
      ]
    },
    "production_product_subcategory": {
      "project": PROJECT,
      "filename": "production_product_subcategory",
      "default": BatchTable,
      "primary_keys": [
        "product_subcategory_id"
      ]
    },
    "production_scrap_reason": {
      "project": PROJECT,
      "filename": "production_scrap_reason",
      "default": BatchTable,
      "primary_keys": [
        "scrap_reason_id"
      ]
    },
    "production_transaction_history": {
      "project": PROJECT,
      "filename": "production_transaction_history",
      "default": BatchTable,
      "primary_keys": [
        "transaction_id"
      ]
    },
    "production_transaction_history_archive": {
      "project": PROJECT,
      "filename": "production_transaction_history_archive",
      "default": BatchTable,
      "primary_keys": [
        "transaction_id"
      ]
    },
    "production_unit_measure": {
      "project": PROJECT,
      "filename": "production_unit_measure",
      "default": BatchTable,
      "primary_keys": [
        "unit_measure_code"
      ]
    },
    "production_work_order": {
      "project": PROJECT,
      "filename": "production_work_order",
      "default": BatchTable,
      "primary_keys": [
        "work_order_id"
      ]
    },
    "production_work_order_routing": {
      "project": PROJECT,
      "filename": "production_work_order_routing",
      "default": BatchTable,
      "primary_keys": [
        "work_order_id",
        "product_id",
        "operation_sequence"
      ]
    },
    "purchasing_product_vendor": {
      "project": PROJECT,
      "filename": "purchasing_product_vendor",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "purchasing_purchase_order_detail": {
      "project": PROJECT,
      "filename": "purchasing_purchase_order_detail",
      "default": BatchTable,
      "primary_keys": [
        "purchase_order_detail",
        "purchase_order_detail_id"
      ]
    },
    "purchasing_purchase_order_header": {
      "project": PROJECT,
      "filename": "purchasing_purchase_order_header",
      "default": BatchTable,
      "primary_keys": [
        "purchase_order_detail"
      ]
    },
    "purchasing_ship_method": {
      "project": PROJECT,
      "filename": "purchasing_ship_method",
      "default": BatchTable,
      "primary_keys": [
        "ship_method_id"
      ]
    },
    "purchasing_vendor": {
      "project": PROJECT,
      "filename": "purchasing_vendor",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "sales_country_region_currency": {
      "project": PROJECT,
      "filename": "sales_country_region_currency",
      "default": BatchTable,
      "primary_keys": [
        "country_region_code"
        "currency_code"
      ]
    },
    "sales_credit_card": {
      "project": PROJECT,
      "filename": "sales_credit_card",
      "default": BatchTable,
      "primary_keys": [
        "credit_card_id"
      ]
    },
    "sales_currency": {
      "project": PROJECT,
      "filename": "sales_currency",
      "default": BatchTable,
      "primary_keys": [
        "currency_code"
      ]
    },
    "sales_currency_rate": {
      "project": PROJECT,
      "filename": "sales_currency_rate",
      "default": BatchTable,
      "primary_keys": [
        "currency_rate_id"
      ]
    },
    "sales_customer": {
      "project": PROJECT,
      "filename": "sales_customer",
      "default": BatchTable,
      "primary_keys": [
        "customer_id"
      ]
    },
    "sales_person_credit_card": {
      "project": PROJECT,
      "filename": "sales_person_credit_card",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "credit_card_id"
      ]
    },
    "sales_sales_order_detail": {
      "project": PROJECT,
      "filename": "sales_sales_order_detail",
      "default": BatchTable,
      "primary_keys": [
        "sales_order_id",
        "sales_order_detail_id"
      ]
    },
    "sales_sales_order_header": {
      "project": PROJECT,
      "filename": "sales_sales_order_header",
      "default": BatchTable,
      "primary_keys": [
        "sales_order_id"
      ]
    },
    "sales_sales_order_header_sales_reason": {
      "project": PROJECT,
      "filename": "sales_sales_order_header_sales_reason",
      "default": BatchTable,
      "primary_keys": [
        "sales_order_id",
        "sales_reason_id"
      ]
    },
    "sales_sales_person": {
      "project": PROJECT,
      "filename": "sales_sales_person",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "sales_sales_person_quota_history": {
      "project": PROJECT,
      "filename": "sales_sales_person_quota_history",
      "default": BatchTable,
      "primary_keys": [
        "business_entity_id",
        "quota_date"
      ]
    },
    "sales_sales_reason": {
      "project": PROJECT,
      "filename": "sales_sales_reason",
      "default": Batch,
      "primary_keys": [
        "sales_reason_id"
      ]
    },
    "sales_sales_tax_rate": {
      "project": PROJECT,
      "filename": "sales_sales_tax_rate",
      "default": Batch,
      "primary_keys": [
        "sales_tax_rate_id"
      ]
    },
    "sales_sales_territory": {
      "project": PROJECT,
      "filename": "sales_sales_territory",
      "default": Batch,
      "primary_keys": [
        "tarritory_id"
      ]
    },
    "sales_sales_territory_history": {
      "project": PROJECT,
      "filename": "sales_sales_territory_history",
      "default": Batch,
      "primary_keys": [
        "business_entity_id",
        "tarritory_id",
        "start_date"
      ]
    },
    "sales_shopping_cart_item": {
      "project": PROJECT,
      "filename": "sales_shopping_cart_item",
      "default": Batch,
      "primary_keys": [
        "shopping_cart_item_id"
      ]
    },
    "sales_special_offer": {
      "project": PROJECT,
      "filename": "sales_special_offer",
      "default": Batch,
      "primary_keys": [
        "special_offer_id"
      ]
    },
    "sales_special_offer_product": {
      "project": PROJECT,
      "filename": "sales_special_offer_product",
      "default": Batch,
      "primary_keys": [
        "special_offer_id",
        "product_id"
      ]
    },
    "sales_store": {
      "project": PROJECT,
      "filename": "sales_store",
      "default": Batch,
      "primary_keys": [
        "business_entity_id"
      ]
    },
  }
