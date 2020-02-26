{
    'name': 'To-Do Application',
    'description': 'Manage your personal Tasks with this module.',
    'author': 'Jorge Pastor',
    'depends': ['mail'],
    'data': ['views/todo_view.xml'],
    'data': [
        'views/todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml'
    ],
    'application': True,
}
