# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, _


class ProductExtractionType(models.Model):
    _name = 'product.extraction.type'

    name = fields.Char(
        required=True,
        translate=True,
    )
    product_ids = fields.One2many(
        'product.template',
        'product_extraction_type_id',
        string='Product',
    )
    task_ids = fields.One2many(
        'project.task',
        'product_extraction_type_id',
        string='Task',
    )
    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('The name must be unique')),
    ]