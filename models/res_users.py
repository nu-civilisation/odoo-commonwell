# -*- coding: utf-8 -*-
# Developed by nu-civilisation. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo import models


class Users(models.Model):
    _inherit = "res.users"
    # ...Be sure to only define "_inherit" field and not the "_name", since we are extending the base class "res.users".

    caring = fields.Many2one(comodel_name="res.partner", string="Caring")
    tag_ids = fields.Many2many(comodel_name="res.user.tags", string="Tags")
