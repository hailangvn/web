# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from ..common import load_csv


@anthem.log
def load_warehouses(ctx):
    """ Importing warehouses from CSV """
    load_csv(ctx, 'data/install/stock.warehouse.csv', 'stock.warehouse')


@anthem.log
def main(ctx):
    load_warehouses(ctx)
