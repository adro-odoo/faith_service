{
  'name': 'Faith Service',
  'category':'customizations',
  'author':'Odoo PSIN',
  'version': '17.0.1.0.0',
  'license' : 'LGPL-3',
    'depends': [
        'base',
        'base_automation',
        'stock',
        'approvals',
        'mrp',
    ],
    'data':[
        'data/fields_approval_type.xml',
        'data/base_automation.xml',
        'views/stock_picking_view.xml',
        ],
  'installable': True,
  'application':True,
  'sequence':1,
}
