{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'ara fa adri',
    'category': 'App',
    'description': """This is a real estate management module.""",
    'application': True,
    'data': [

        # security
        'security/ir.model.access.csv',

        # views
        'views/menu.xml',
        'views/estate_property.xml',

        # load initial data
        'data/estate.property.csv',
    ]
}