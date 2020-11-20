# data and functions for replacig king county assessor cateogory values


keep_rp = [
    'addrline',
    'citystate',
    'zipcode',
    'taxvalreason',
    'apprlandval',
    'apprimpsval'
    ]

keep_apt = [
    'major',
    'minor',
    'nbrbldgs',
    'nbrstories',
    'nbrunits',
    'avgunitsize',
    'projectlocation',
    'projectappeal',
    'pcntwithview',
    'constrclass',
    'bldgquality',
    'condition',
    'yrbuilt',
    'effyr',
    'elevators',
    'sectysystem',
    'fireplace',
    'laundry',
    'address'
    ]

keep_units = [
    'unittypeitemid',
    'nbrthistype',
    'sqft',
    'nbrbedrooms',
    'nbrbaths'
    ]

keep_parcel = [
    'proptype',
    'districtname',
    'currentzoning',
    'presentuse',
    'sqftlot',
    'watersystem',
    'sewersystem',
    'access',
    'topography',
    'streetsurface',
    'inadequateparking',
    'mtrainier',
    'olympics',
    'cascades',
    'territorial',
    'seattleskyline',
    'pugetsound',
    'lakewashington',
    'lakesammamish',
    'smalllakerivercreek',
    'otherview',
    'wfntlocation',
    'wfntfootage',
    'trafficnoise',
    'powerlines',
    'othernuisances',
    'adjacentgolffairway',
    'adjacentgreenbelt'
    ]

keep_rb = [
    'major',
    'minor',
    'stories',
    'bldggrade',
    'bldggradevar',
    'sqfttotliving',
    'sqftgaragebasement',
    'sqftgarageattached',
    'sqftfinbasement',
    'heatsystem',
    'heatsource',
    'brickstone',
    'bedrooms',
    'bathhalfcount',
    'bath3qtrcount',
    'bathfullcount',
    'yrbuilt',
    'yrrenovated'
]

keep_con = [
    'major',
    'minor',
    'unittype',
    'unitquality',
    'footage',
    'nbrbedrooms',
    'bathhalfcount',
    'bath3qtrcount',
    'bathfullcount',
    'fireplace'
]

keep_con_com = [
    'complextype',
    'nbrstories',
    'projectlocation',
    'projectappeal',
    'constrclass',
    'bldgquality',
    'condition',
    'yrbuilt',
    'effyr',
    'elevators',
    'sectysystem',
    'laundry',
    'aptconversion'
]

usedcols = {
    'res': {
        'Condition': 83,
        'BldgGrade': 82,
        'WaterSystem': 56,
        'SewerSystem': 57,
        'StreetSurface': 60,
        'MtRainier': 58,
        'Olympics': 58,
        'Cascades': 58,
        'Territorial': 58,
        'SeattleSkyline': 58,
        'PugetSound': 58,
        'LakeWashington': 58,
        'LakeSammamish': 58,
        'SmallLakeRiverCreek': 58,
        'OtherView': 58,
        'WfntLocation': 50,
        'TrafficNoise': 95
    },
    'condo': {
        'UnitType': 150,
        'UnitQuality': 151,
        'UnitLocation': 152,
        'Condition': 155,
        'ViewMountain': 157,
        'ViewLakeRiver': 157,
        'ViewCityTerritorial': 157,
        'ViewPugetSound': 157,
        'ViewLakeWaSamm': 157,
        'ComplexType': 143,
        'ProjectLocation': 98,
        'ProjectAppeal': 99,
        'ConstrClass': 97,
        'BldgQuality': 96,
        'Laundry': 89,
        'CondoLandType': 145,
        'WaterSystem': 56,
        'SewerSystem': 57,
        'StreetSurface': 60,
        'MtRainier': 58,
        'Olympics': 58,
        'Cascades': 58,
        'Territorial': 58,
        'SeattleSkyline': 58,
        'PugetSound': 58,
        'LakeWashington': 58,
        'LakeSammamish': 58,
        'SmallLakeRiverCreek': 58,
        'OtherView': 58,
        'WfntLocation': 50,
        'TrafficNoise': 95
    },
    'apt': {
        'ProjectLocation': 98,
        'ProjectAppeal': 99,
        'ConstrClass': 97,
        'BldgQuality': 96,
        'Laundry': 89,
        'Condition': 83,
        'WaterSystem': 56,
        'SewerSystem': 57,
        'StreetSurface': 60,
        'MtRainier': 58,
        'Olympics': 58,
        'Cascades': 58,
        'Territorial': 58,
        'SeattleSkyline': 58,
        'PugetSound': 58,
        'LakeWashington': 58,
        'LakeSammamish': 58,
        'SmallLakeRiverCreek': 58,
        'OtherView': 58,
        'WfntLocation': 50,
        'TrafficNoise': 95,
        'unittypeitemid' : 29
    }
}

usedcols = { k : { x.lower() : y for x,y in v.items() } for k,v in usedcols.items()}

def replacecats(df, table):
    """Replace encoded categorical values in a dataframe with actual category names."""
    for key, value in usedcols[table].items():
        # load the values to find and replace for each column
        x = lookup[lookup['lutype'] == value]['luitem'].tolist()
        y = lookup[lookup['lutype'] == value]['ludescription'].tolist()
        y = [z.replace(' ', '').replace('/', '').replace('(', '').replace(')',
                                                                          '').replace('+', '').replace(',', '') for z in y]

        # apply to the current column if it exists
        try:
            df[key] = df[key].replace(x, y)
        except:
            pass