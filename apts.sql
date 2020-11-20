select * from apt_complex a 
left join unit_detail d on
a.major = d.major and
a.minor = d.minor
left join parcel_account b 
on a.major = b.major 
and a.minor = b.minor 
left join parcel c
on a.major = c.major
and a.minor = c.minor