# -*- coding: utf-8 -*-
# Developed by nu-civilisation. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"
    # ...Be sure to only define "_inherit" field and not the "_name", since we are extending the base class "res.partner".

    admin_ids = fields.One2many(comodel_name="res.users", inverse_name="administrating", string="Admins")
    type_id = fields.Many2one(comodel_name="res.partner.types", string="Type")
    tag_ids = fields.Many2many(comodel_name="res.partner.tags", string="Tags")
    presentation_text = fields.Text(string="Presentation Text", translate=True)
    presentation_image = fields.Image(string="Presentation Image")
