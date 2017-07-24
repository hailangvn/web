# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
import anthem
from ...common import load_csv


@anthem.log
def load_mt_crm_teams(ctx):
    """ Importing CRM teams from CSV """
    model = ctx.env['crm.team'].with_context({'tracking_disable': 1})
    load_csv(ctx, 'data/install/mte/crm.team.csv', model)


@anthem.log
def main(ctx):
    """ Configuring MT CRM """
    load_mt_crm_teams(ctx)
