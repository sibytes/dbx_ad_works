
from ._table import BatchTable, AutoloaderTable


# register tables here and map them to a table Class
# if adding new properties then they must be added
# to the __init__ of the ._base_table.BaseTable
def tables():
  
  return {
    "hr_department": {
      "filename": "hr_department",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "department_id"
      ]
    },
    "hr_employee": {
      "filename": "hr_employee",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_ID"
      ]
    },
    "hr_employee_department_history": {
      "filename": "hr_employee_department_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "department_id",
        "shift_id",
        "start_date"
      ]
    },
    "hr_employee_pay_history": {
      "filename": "hr_employee_pay_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "rate_change_date"
      ]
    },
    "hr_job_candidate": {
      "filename": "hr_job_candidate",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "job_candidate_date"
      ]
    },
    "hr_shift": {
      "filename": "hr_shift",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "shift_id"
      ]
    },
    "person_address": {
      "filename": "person_address",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "address_id"
      ]
    },
    "person_address_type": {
      "filename": "person_address_type",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "address_type_id"
      ]
    },
    "person_business_entity": {
      "filename": "person_business_entity",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "person_business_entity_address": {
      "filename": "person_business_entity_address",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "address_id",
        "address_type_id"
      ]
    },
    "person_business_entity_contact": {
      "filename": "person_business_entity_contact",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "person_id",
        "contact_type_id"
      ]
    },
    "person_contact_type": {
      "filename": "person_contact_type",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "contact_type_id"
      ]
    },
    "person_country_region": {
      "filename": "person_country_region",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "country_region_code"
      ]
    },
    "person_email_address": {
      "filename": "person_email_address",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "email_address_id"
      ]
    },
    "person_password": {
      "filename": "person_password",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "person_person": {
      "filename": "person_person",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
    },
    "person_personp_phone": {
      "filename": "person_personp_phone",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "phone_number",
        "phone_number_type_id"
      ]
    },
    "person_phone_number_type": {
      "filename": "person_phone_number_type",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "phone_number_type_id"
      ]
    },
    "person_state_province": {
      "filename": "person_state_province",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "state_province_id"
      ]
    },
    "production_bill_of_materials": {
      "filename": "production_bill_of_materials",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "bill_of_materials_id"
      ]
    },
    "production_culture": {
      "filename": "production_culture",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "culture_id"
      ]
    },
    "production_document": {
      "filename": "production_document",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "document_node"
      ]
    },
    "production_illustration": {
      "filename": "production_illustration",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "illustration_id"
      ]
    },
    "production_location": {
      "filename": "production_location",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        
      ]
    },
    "production_product": {
      "filename": "production_product",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id"
      ]
    },
    "production_product_category": {
      "filename": "production_product_category",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_category_id"
      ]
    },
    "production_product_cost_history": {
      "filename": "production_product_cost_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id",
        "start_date"
      ]
    },
    "production_product_description": {
      "filename": "production_product_description",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        product_description_id
      ]
    },
    "production_product_document": {
      "filename": "production_product_document",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id",
        "document_node"
      ]
    },
    "production_product_inventory": {
      "filename": "production_product_inventory",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id",
        "location_id"
      ]
    },
    "production_product_list_price_history": {
      "filename": "production_product_list_price_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id",
        "start_date"
      ]
    },
    "production_product_model": {
      "filename": "production_product_model",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_model_id"
      ]
    },
    "production_product_model_illustration": {
      "filename": "production_product_model_illustration",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_model_id",
        "illustration_id"
      ]
    },
    "production_product_model_product_description_culture": {
      "filename": "production_product_model_product_description_culture",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_model_id",
        "product_description_id",
        "culture_id"
      ]
    },
    "production_product_photo": {
      "filename": "production_product_photo",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_photo_id"
      ]
    },
    "production_product_product_photo": {
      "filename": "production_product_product_photo",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_id"
        "product_photo_id"
      ]
    },
    "production_product_review": {
      "filename": "production_product_review",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_review_id"
      ]
    },
    "production_product_subcategory": {
      "filename": "production_product_subcategory",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "product_subcategory_id"
      ]
    },
    "production_scrap_reason": {
      "filename": "production_scrap_reason",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "scrap_reason_id"
      ]
    },
    "production_transaction_history": {
      "filename": "production_transaction_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "transaction_id"
      ]
    },
    "production_transaction_history_archive": {
      "filename": "production_transaction_history_archive",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "transaction_id"
      ]
    },
    "production_unit_measure": {
      "filename": "production_unit_measure",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "unit_measure_code"
      ]
    },
    "production_work_order": {
      "filename": "production_work_order",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "work_order_id"
      ]
    },
    "production_work_order_routing": {
      "filename": "production_work_order_routing",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "work_order_id",
        "product_id",
        "operation_sequence"
      ]
    },
    "purchasing_product_vendor": {
      "filename": "purchasing_product_vendor",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "purchasing_purchase_order_detail": {
      "filename": "purchasing_purchase_order_detail",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "purchase_order_detail",
        "purchase_order_detail_id"
      ]
    },
    "purchasing_purchase_order_header": {
      "filename": "purchasing_purchase_order_header",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "purchase_order_detail"
      ]
    },
    "purchasing_ship_method": {
      "filename": "purchasing_ship_method",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "ship_method_id"
      ]
    },
    "purchasing_vendor": {
      "filename": "purchasing_vendor",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "sales_country_region_currency": {
      "filename": "sales_country_region_currency",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "country_region_code"
        "currency_code"
      ]
    },
    "sales_credit_card": {
      "filename": "sales_credit_card",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "credit_card_id"
      ]
    },
    "sales_currency": {
      "filename": "sales_currency",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "currency_code"
      ]
    },
    "sales_currency_rate": {
      "filename": "sales_currency_rate",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "currency_rate_id"
      ]
    },
    "sales_customer": {
      "filename": "sales_customer",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "customer_id"
      ]
    },
    "sales_person_credit_card": {
      "filename": "sales_person_credit_card",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "credit_card_id"
      ]
    },
    "sales_sales_order_detail": {
      "filename": "sales_sales_order_detail",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "sales_order_id",
        "sales_order_detail_id"
      ]
    },
    "sales_sales_order_header": {
      "filename": "sales_sales_order_header",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "sales_order_id"
      ]
    },
    "sales_sales_order_header_sales_reason": {
      "filename": "sales_sales_order_header_sales_reason",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "sales_order_id",
        "sales_reason_id"
      ]
    },
    "sales_sales_person": {
      "filename": "sales_sales_person",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
    "sales_sales_person_quota_history": {
      "filename": "sales_sales_person_quota_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "quota_date"
      ]
    },
    "sales_sales_reason": {
      "filename": "sales_sales_reason",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "sales_reason_id"
      ]
    },
    "sales_sales_tax_rate": {
      "filename": "sales_sales_tax_rate",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "sales_tax_rate_id"
      ]
    },
    "sales_sales_territory": {
      "filename": "sales_sales_territory",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "tarritory_id"
      ]
    },
    "sales_sales_territory_history": {
      "filename": "sales_sales_territory_history",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id",
        "tarritory_id",
        "start_date"
      ]
    },
    "sales_shopping_cart_item": {
      "filename": "sales_shopping_cart_item",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "shopping_cart_item_id"
      ]
    },
    "sales_special_offer": {
      "filename": "sales_special_offer",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "special_offer_id"
      ]
    },
    "sales_special_offer_product": {
      "filename": "sales_special_offer_product",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "special_offer_id",
        "product_id"
      ]
    },
    "sales_store": {
      "filename": "sales_store",
      "default":BatchTable,
      "autoloader": AutoloaderTable,
      "primary_keys": [
        "business_entity_id"
      ]
    },
  }
