# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv, fields

class retention_retention(osv.osv):
    """Objeto que define las retenciones que pueden utilizarse

       Configura las retenciones posibles. Luego a partir de estos objetos
       se crean las retention.tax que serian retenciones aplicadas a un recibo;
       las retention.tax toman la configuracion de la retention.retention que la
       genera y se le agrega la informacion del impuesto en si, como por ejemplo,
       monto, base imponible, nro de certificado, etc."""
    _name = "retention.retention"
    _description = "Retention Configuration"

    #TODO: Tal vez haya lo mejor es hacer desaparecer este objeto y agregarle
    # el par de campos (jurisdiccion y state_id) a account.tax y listo
    _columns = {
            'name': fields.char('Retention', required=True, size=64),
            'tax_id': fields.many2one('account.tax', 'Tax', required=True, help="Tax configuration for this retention"),
            'type_tax_use': fields.related('tax_id', 'type_tax_use', type='char', string='Tax Application', readonly=True),
            'state_id': fields.many2one('res.country.state', 'State/Province', domain="[('country_id','=','Argentina')]"),
            'type': fields.selection([('vat', 'VAT'),
                                      ('gross_income', 'Gross Income'),
                                      ('profit', 'Profit'),
                                      ('other', 'Other')], 'Type', required=True),

            'jurisdiccion': fields.selection([('nacional', 'Nacional'),
                                              ('provincial', 'Provincial'),
                                              ('municipal', 'Municipal')], 'Jurisdiccion'),
            }

    _defaults = {
            'jurisdiccion': 'nacional',
            }

retention_retention()


