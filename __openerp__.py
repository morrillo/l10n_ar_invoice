# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{   'active': False,
    'author': 'OpenERP - Team de Localizacion Argentina',
    'category': 'Localization/Argentina',
    'data': [   'data/document_class.xml',
                'data/responsability.xml',
                'data/responsability_class.xml',
                'data/journal_class.xml',
                'data/document_type.xml',
                'data/partner.xml',
                'data/invoice_workflow.xml',
                'data/reports.xml',
                'data/country.xml',
                'data/res.currency.csv',
                'data/afip.journal_template.csv',
                'data/afip.concept_type.csv',
                'view/partner_view.xml',
                'view/country_view.xml',
                'view/afip_menuitem.xml',
                'view/afip_concept_type_view.xml',
                'view/afip_optional_type_view.xml',
                'view/afip_document_type_view.xml',
                'view/afip_document_class_view.xml',
                'view/afip_journal_class_view.xml',
                'view/afip_journal_template_view.xml',
                'view/afip_responsability_view.xml',
                'view/afip_responsability_class_view.xml',
                'view/afip_document_type_view.xml',
                'view/afip_journal_class_view.xml',
                'view/afip_responsability_view.xml',
                'view/afip_responsability_class_view.xml',
                'view/journal_view.xml',
                'view/invoice_view.xml',
                'view/invoice_config.xml',
                'view/res_config_view.xml',
                'security/l10n_ar_invoice_security.xml',
                'security/ir.model.access.csv'],
    'demo_xml': [],
    'depends': [   'base_setup',
                   'account_voucher',
                   'l10n_ar_base_vat',
                   'l10n_ar_chart_generic',
                   'l10n_ar_states'],
    'description': 'l10n_ar_invoice',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Argentina - Generador de Talonarios',
    'test': [   'test/products.yml',
                'test/partners.yml',
                'test/com_ri1.yml',
                'test/com_ri2.yml',
                'test/com_rm1.yml',
                'test/inv_ri2ri.yml',
                'test/inv_rm2ri.yml',
                'test/inv_ri2rm.yml',
                'test/bug_1042944.yml'],
    'version': '2.7.231',
    'website': 'https://launchpad.net/~openerp-l10n-ar-localization'}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
