apt_sql = """
select a.*,b.addrline, b.citystate, b.zipcode as rpzip, b.taxvalreason, b.apprlandval, b.apprimpsval, c.*,d.*  from apt_complex a 
left join parcel_account b 
on a.major = b.major 
and a.minor = b.minor 
left outer join parcel c
on a.major = c.major
and a.minor = c.minor
left outer join unit_detail d
on a.major = d.major
and a.minor = d.minor
"""

condo_sql = 'select a.major, a.minor, a.unittype, a.unitquality, a.footage, a.nbrbedrooms, a.bathhalfcount, a.bath3qtrcount, a.bathfullcount, a.fireplace,b.addrline, b.citystate, b.zipcode as rpzip, b.taxvalreason, b.apprlandval, b.apprimpsval,c.complextype, c.nbrstories, c.projectlocation, c.projectappeal, c.constrclass, c.bldgquality, c.condition, c.yrbuilt, c.effyr, c.elevators, c.sectysystem, c.laundry, c.aptconversion, d.proptype, d.districtname, d.currentzoning, d.presentuse, d.sqftlot, d.watersystem, d.sewersystem, d.access, d.topography, d.streetsurface, d.inadequateparking, d.mtrainier, d.olympics, d.cascades, d.territorial, d.seattleskyline, d.pugetsound, d.lakewashington, d.lakesammamish, d.smalllakerivercreek, d.otherview, d.wfntlocation, d.wfntfootage, d.trafficnoise, d.powerlines, d.othernuisances, d.adjacentgolffairway, d.adjacentgreenbelt from condo_unit a  left join parcel_account b  on a.major = b.major  and a.minor = b.minor  left join condo_complex c on a.major = c.major inner join (select * from parcel where minor = \'0000\') d on c.major = d.major order by a.major,a.minor,bldgnbr,unitnbr'

res_sql = 'select  a.major, a.minor, a.bldgnbr, a.nbrlivingunits, a.stories, a.bldggrade, a.bldggradevar, a.sqfttotliving, a.sqftgaragebasement, a.sqftgarageattached, a.sqftfinbasement, a.heatsystem, a.heatsource, a.brickstone, a.bedrooms, a.bathhalfcount, a.bath3qtrcount, a.bathfullcount, a.yrbuilt, a.yrrenovated, a.condition, b.addrline, b.citystate, b.zipcode as rpzip, b.taxvalreason, b.apprlandval, b.apprimpsval, c.proptype, c.districtname, c.currentzoning, c.presentuse, c.sqftlot, c.watersystem, c.sewersystem, c.access, c.topography, c.streetsurface, c.inadequateparking, c.mtrainier, c.olympics, c.cascades, c.territorial, c.seattleskyline, c.pugetsound, c.lakewashington, c.lakesammamish, c.smalllakerivercreek, c.otherview, c.wfntlocation, c.wfntfootage, c.trafficnoise, c.powerlines, c.othernuisances, c.adjacentgolffairway, c.adjacentgreenbelt from res_bldg a left join parcel_account b  on a.major = b.major  and a.minor = b.minor  left join parcel c on a.major = c.major and a.minor = c.minor'

turnout_sql = """

with v1 as (select precinct,year,et_id,max(count) as ballots from results where counter like \'Times C%%\' group by precinct,year,et_id order by year, precinct), 
v2 as (select precinct,year,et_id,max(count) as voters from results where counter like \'Registered V%%\' group by precinct,year,et_id order by year, precinct) 
select  v1.precinct as name,  v1.year, case when v1.et_id = 1 then \'G\' else \'P\' end as type, ballots, voters 
from  v1 left join v2  on v1.precinct = v2.precinct  and v1.year = v2.year and v1.et_id = v2.et_id order by year, type, name 

"""

pp_sql = 'select major,minor,name,year from parcel_precinct where minor ~ \'^[0-9]\' group by major,minor,name,year order by minor desc'

valhist_sql = "select * from valhist"

mh_sql = 'select a.*,c.*, b.addrline, b.citystate, b.zipcode as rpzip, b.taxvalreason, b.apprlandval, b.apprimpsval from "EXTR_Accessory_V" a left join parcel c on a.major = c.major and a.minor = c.minor left join parcel_account b on a.major = b.major and a.minor = b.minor where accytype = \'24\''

dd = 'select * from dd'