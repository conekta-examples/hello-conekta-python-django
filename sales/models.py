from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import conekta
import json

class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)

        conekta.api_key = settings.CONEKTA_PRIVATE_KEY

    def charge(self, price_in_cents, token_id):
        try:
            charge = conekta.Charge.create({
              "description":"Stogies",
              "amount": price_in_cents,
              "currency":"MXN",
              "reference_id":"9839-wolf_pack",
              "card": token_id,
              "details": {
                "name": "Arnulfo Quimare",
                "phone": "403-342-0642",
                "email": "logan@x-men.org",
                "line_items": [{
                  "name": "Box of Cohiba S1s",
                  "description": "Imported From Mex.",
                  "unit_price": price_in_cents,
                  "quantity": 1,
                  "sku": "cohb_s1",
                  "category": "food"
                }],
                "shipment": {
                    "carrier":"estafeta",
                    "service":"international",
                    "price": price_in_cents,
                    "address": {
                      "street1": "250 Alexis St",
                      "street2": "Interior 303",
                      "street3": "Col. Condesa",
                      "city":"Red Deer",
                      "state":"Alberta",
                      "zip":"T4N 0B8",
                      "country":"Canada"
                    }
                  }
              }
            })
            return json.dumps(charge.__dict__)
        except conekta.ConektaError as e:
            return e.message
