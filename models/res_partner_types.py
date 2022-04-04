# -*- coding: utf-8 -*-
# Developed by nu-civilisation. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo import models


class PartnerTypes(models.Model):
    _name = "res.partner.types"
    _description = "Contact Types"

    name = fields.Char(string="Type", translate=True, required=True, index=True)
