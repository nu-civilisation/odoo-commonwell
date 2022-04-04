# -*- coding: utf-8 -*-
# Developed by nu-civilisation. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo import models


class PartnerTags(models.Model):
    _name = "res.user.tags"
    _description = "User Tags"

    name = fields.Char(string="Tag", translate=True, required=True, index=True)
    color = fields.Integer(string="Color")
