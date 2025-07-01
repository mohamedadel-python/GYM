{
    'name': "GymMaster",
    'author': "Mohamad Adel",
    'category': 'Tools',
    'version': '17.0.0.1.0',
    'depends': ['base','mail'],
    'data': ["security/ir.model.access.csv",
             "views/base.xml",
             "views/GymMaster.xml",
             "views/gym_trainer_view.xml",
             "views/gym_subscription_view.xml",
             "views/gym_weekday_view.xml"
    ],
    "assets": {
    'web.assets_backend': [

    ],
},

    'application': True,

}