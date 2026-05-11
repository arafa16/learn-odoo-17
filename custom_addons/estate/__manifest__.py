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

        # templates
        'data/templates/example_email_template.xml',

        # views
        'views/menu.xml',
        'views/estate_property.xml',

        # load initial data
        'data/estate.property.csv',

         # Schedulers
        'views/schedulers/estate_property_scheduler.xml'
    ]
}