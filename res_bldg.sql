select * from res_bldg a 
left join parcel_account b 
on a.major = b.major 
and a.minor = b.minor 
left join parcel c
on a.major = c.major
and a.minor = c.minor