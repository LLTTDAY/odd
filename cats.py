# data and functions for replacing king county assessor cateogory values



keep_rp = [
    'addrline',
    'citystate',
    'rpzip',
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
    'laundry'
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
    'bldgnbr',
    'nbrlivingunits',
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
    'yrrenovated',
    'condition'
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

keep_mh = [
    'major',	
    'minor',
    'accytype',
    'accydescr',
    'quantity',
    'size',
    'unit',
    'grade',
    'effyr',
    'pcntnetcondition',
    'accyvalue',
    'datevalued'
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

keep_apts = keep_units + keep_apt + keep_rp + keep_parcel
keep_condo = keep_con + keep_con_com + keep_rp + keep_parcel
keep_res = keep_rb + keep_rp + keep_parcel
keep_mhpad = keep_mh + keep_rp + keep_parcel

usedcols = {
    'res': {
        'condition': 83,
        'bldggrade': 82,
        'watersystem': 56,
        'sewersystem': 57,
        'presentuse' : 102,
        'access' : 55,
        'topography' : 59,
        'streetsurface': 60,
        'mtrainier': 58,
        'olympics': 58,
        'cascades': 58,
        'territorial': 58,
        'seattleskyline': 58,
        'pugetsound': 58,
        'lakewashington': 58,
        'lakesammamish': 58,
        'smalllakerivercreek': 58,
        'otherview': 58,
        'wfntlocation': 50,
        'trafficnoise': 95
    },
    'condo': {
        'unittype': 150,
        'unitquality': 151,
        'unitlocation': 152,
        'condition': 155,
        'viewmountain': 157,
        'viewlakeriver': 157,
        'viewcityterritorial': 157,
        'viewpugetsound': 157,
        'viewlakewasamm': 157,
        'complextype': 143,
        'projectlocation': 98,
        'projectappeal': 99,
        'constrclass': 97,
        'bldgquality': 96,
        'laundry': 89,
        'condolandtype': 145,
        'presentuse' : 102,
        'access' : 55,
        'topography' : 59,
        'watersystem': 56,
        'sewersystem': 57,
        'streetsurface': 60,
        'mtrainier': 58,
        'olympics': 58,
        'cascades': 58,
        'territorial': 58,
        'seattleskyline': 58,
        'pugetsound': 58,
        'lakewashington': 58,
        'lakesammamish': 58,
        'smalllakerivercreek': 58,
        'otherview': 58,
        'wfntlocation': 50,
        'trafficnoise': 95
    },
    'apt': {
        'projectlocation': 98,
        'projectappeal': 99,
        'constrclass': 97,
        'bldgquality': 96,
        'laundry': 89,
        'condition': 83,
        'presentuse' : 102,
        'access' : 55,
        'topography' : 59,
        'watersystem': 56,
        'sewersystem': 57,
        'streetsurface': 60,
        'mtrainier': 58,
        'olympics': 58,
        'cascades': 58,
        'territorial': 58,
        'seattleskyline': 58,
        'pugetsound': 58,
        'lakewashington': 58,
        'lakesammamish': 58,
        'smalllakerivercreek': 58,
        'otherview': 58,
        'wfntlocation': 50,
        'trafficnoise': 95,
        'unittypeitemid' : 29
    },
    'mh' : {
        'accytype' : 26
    }
}

housing_cols = ["access","acctnbr","addnlcost","address","addrline","adjacentgolffairway","adjacentgreenbelt","airportnoise","apprimpsval","apprlandval","aptconversion","area","attnline","avgunitsize","bath3qtrcount","bathfullcount","bathhalfcount","bedrooms","billyr","bldggrade","bldggradevar","bldgnbr","bldgquality","brickstone","buildingnumber","cascades","citystate","coalminehazard","complexdescr","complextype","condition","condolandtype","constrclass","contamination","criticaldrainage","currentusedesignation","currentzoning","date","daylightbasement","deedrestrictions","developmentrightspurch","directionprefix","directionsuffix","districtname","dnrlease","easements","effyr","elevators","endunit","erosionhazard","finbasementgrade","fireplace","floornbr","footage","fpadditional","fpfreestanding","fpmultistory","fpsinglestory","fraction","grade","hbuasifvacant","hbuasimproved","heatsource","heatsystem","historicsite","hundredyrfloodplain","id","inadequateparking","lakesammamish","lakewashington","landfillbuffer","landperunit","landslidehazard","laundry","length","levycode","lotdepthfactor","major","mhomedescr","minor","mtrainier","nativegrowthprotesmt","nbrbaths","nbrbedrooms","nbrbldgs","nbrbldgsites","nbrlivingunits","nbrstories","nbrthistype","nbrunits","newconstructionflag","obsolescence","olympics","otherdesignation","othernuisances","otherproblems","otherroom","otherview","pcntcomplete","pcntnetcondition","pcntownership","pcntunusable","pcntwithview","perspropacctnbr","pkgbasement","pkgbasementtandem","pkgcarport","pkggarage","pkggaragetandem","pkgopen","pkgothertype","platblock","platlot","platname","powerlines","presentuse","projectappeal","projectlocation","propname","proptype","pugetsound","quartersection","range","restrictiveszshape","seattleskyline","section","sectysystem","seismichazard","sensitiveareatract","sewersystem","smalllakerivercreek","specarea","speciesofconcern","specsubarea","sqft","sqft1stfloor","sqft2ndfloor","sqftdeck","sqftenclosedporch","sqftfinbasement","sqftgarageattached","sqftgaragebasement","sqfthalffloor","sqftlot","sqftopenporch","sqfttotbasement","sqfttotliving","sqftunfinfull","sqftunfinhalf","sqftupperfloor","steepslopehazard","stories","stream","streetname","streetsurface","streettype","subarea","taxableimpsval","taxablelandval","taxstat","taxvalreason","territorial","tidelandshoreland","topfloor","topography","township","trafficnoise","transpconcurrency","unbuildable","unitdescr","unitloc","unitnbr","unitofmeasure","unitquality","unittype","unittypeitemid","viewcityterritorial","viewlakeriver","viewlakewasamm","viewmountain","viewpugetsound","viewutilization","waterproblems","watersystem","wetland","wfntaccessrights","wfntbank","wfntfootage","wfntlocation","wfntpoorquality","wfntproximityinfluence","wfntrestrictedaccess","width","yrbuilt","yrrenovated","zipcode"]


def replacecats(lookup, df, table):
    """Replace encoded categorical values in a dataframe with actual category names."""
    for key, value in usedcols[table].items():
        # load the values to find and replace for each column
        x = lookup[lookup['lutype'] == value]['luitem'].tolist()
        y = lookup[lookup['lutype'] == value]['ludescription'].tolist()
        y = [z.replace(' ', '').replace('/', '').replace('(', '').replace(')','').replace('+', '').replace(',', '') for z in y]

        # apply to the current column if it exists
        try:
            df[key] = df[key].replace(x, y, inplace=True)
        except:
            pass


common_cols = ['proptype',
       'districtname', 'currentzoning', 'presentuse', 'watersystem',
       'sewersystem', 'access', 'topography', 'streetsurface',
       'inadequateparking', 'mtrainier', 'olympics', 'cascades', 'territorial',
       'seattleskyline', 'pugetsound', 'lakewashington', 'lakesammamish',
       'smalllakerivercreek', 'otherview', 'wfntlocation', 'wfntfootage',
       'trafficnoise', 'powerlines', 'othernuisances', 'adjacentgolffairway',
       'adjacentgreenbelt', 'yrbuilt', 'apprimpsval', 'apprlandval', 'taxvalreason', 'addrline', 'citystate',
       'sqftlot']


# note: condo has two condition and two fireplace fields and three zip fields

cond_extra = [
    'unittype',
    'unitquality',
    'footage',
    'complex_type',
    'nbrstories',
    'projectlocation',
    'projectappeal',
    'effyr',
    'elevators',
    'sectysystem',
    'laundry',
    'aptconversion',
    'constrclass',
    'bldgquality',
    'condition',
    'nbrbedrooms',
    'complextype',
    'bath3qtrcount',
    'bathhalfcount',
    'bathfullcount',
    'condo',
    'fireplace'
]

apt_extra = [
    'apt',
 'avgunitsize',
 'bldgquality',
 'condition',
 'constrclass',
 'effyr',
 'elevators',
 'fireplace',
 'laundry',
 'nbrbaths',
 'nbrbedrooms',
 'nbrbldgs',
 'nbrstories',
 'nbrthistype',
 'nbrunits',
 'pcntwithview',
 'projectappeal',
 'projectlocation',
 'sectysystem',
 'sqft',
 'unittypeitemid'
]

res_extra = [
 'bath3qtrcount',
 'bathfullcount',
 'bathhalfcount',
 'bedrooms',
 'bldggrade',
 'bldggradevar',
 'bldgnbr',
 'brickstone',
 'condition',
 'heatsource',
 'heatsystem',
 'major',
 'major',
 'major',
 'minor',
 'minor',
 'minor',
 'nbrlivingunits',
 'res',
 'sqftfinbasement',
 'sqftgarageattached',
 'sqftgaragebasement',
 'sqfttotliving',
 'stories',
 'yrrenovated',
 'zipcode',
 'zipcode'
]

# Present Use Filter
uses = [ '4Plex',
 'Apartment',
 'ApartmentCoop',
 'ApartmentMixed Use',
 'ApartmentSubsidized',
 'CondominiumM Home Pk',
 'CondominiumMixed Use',
 'CondominiumResidential',
 'Congregate Housing',
 'Duplex',
 'Farm',
 'Group Home',
 'Historic PropResidence',
 'Houseboat',
 'Marina',
 'Mobile Home',
 'Mobile Home Park',
 'Nursing Home',
 'Retirement Facility',
 'Rooming House',
 'Single FamilyCI Zone',
 'Single FamilyRes UseZone',
 'Townhouse Plat',
 'Triplex',
 'VacantMultifamily',
 'VacantSinglefamily',
 'FraternitySorority House',
 'Residence HallDorm']

house_types = [
    'single_family',
    'duplex',
    'triplex',
    'fourplex',
    'townhouse',
    'apartment',
    'condominium',
    'senior_housing',
    'student_housing',
    'mobile_home'
    ]

def rcats(df,table,cc,lu):
   for col in df.columns:
       if col in cc[table].keys():
           df[col] = df[col].replace(to_replace=lu[cc[table][col]])


### MODELING LISTS


dummify = [
    'projectlocation',
    'projectappeal',
    'constrclass',
    'bldgquality',
    'condition',
    'laundry',
    'taxvalreason',
    'proptype',
    'districtname',
    #'presentuse',
    'watersystem',
    'sewersystem',
    'access',
    'streetsurface',
    'mtrainier',
    'olympics',
    'cascades',
    'territorial',
    'seattleskyline',
    'lakewashington',
    'pugetsound',
    'lakesammamish',
    'smalllakerivercreek',
    'otherview',
    'wfntlocation',
    'heatsystem',
    'heatsource',
    'unittype',
    'unitquality',
    'complextype',
    'aptconversion',
    'unittypeitemid',
    'trafficnoise',
    'bldggrade',
    'RegZipCode',
    'site_type'
]