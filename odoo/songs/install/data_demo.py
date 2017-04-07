# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from pkg_resources import resource_stream

import anthem
from anthem.lyrics.loaders import load_csv_stream
from ..common import req

""" File for demo data

These songs will be called when the mode is 'demo', we should import only
excerpt of data, while the full data is only imported in the 'full' mode.

"""


@anthem.log
def import_customers(ctx):
    """ Importing customers from csv """
    content = resource_stream(req, 'data/demo/customers.csv')
    load_csv_stream(ctx, 'res.partner', content, delimiter=',')


@anthem.log
def import_employee(ctx):
    """ Importing employee from csv """
    content = resource_stream(req, 'data/demo/hr.employee.csv')
    load_csv_stream(ctx, 'hr.employee', content, delimiter=',')


@anthem.log
def import_partner_contact(ctx):
    """ Importing partner_contact from csv """
    content = resource_stream(req, 'data/demo/res.partner.contact.csv')
    load_csv_stream(ctx, 'res.partner', content, delimiter=',')


@anthem.log
def import_partner(ctx):
    """ Importing partner from csv """
    content = resource_stream(req, 'data/demo/res.partner.csv')
    load_csv_stream(ctx, 'res.partner', content, delimiter=',')


@anthem.log
def import_users(ctx):
    """ Importing users from csv """
    content = resource_stream(req, 'data/demo/res.users.csv')
    load_csv_stream(ctx, 'res.users', content, delimiter=',')


@anthem.log
def import_projects(ctx):
    """ Importing projects from csv """
    content = resource_stream(req, 'data/demo/project.project.csv')
    load_csv_stream(ctx, 'project.project', content, delimiter=',')


@anthem.log
def import_project_tasks(ctx):
    """ Importing project tasks from csv """
    content = resource_stream(req, 'data/demo/project.task.csv')
    load_csv_stream(ctx, 'project.task', content, delimiter=',')


@anthem.log
def main(ctx):
    """ Loading demo data """
    import_users(ctx)
    import_partner(ctx)
    import_partner_contact(ctx)
    import_employee(ctx)
    import_projects(ctx)
    import_project_tasks(ctx)
