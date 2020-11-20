select * from condo_unit a 
left join parcel_account b 
on a.major = b.major 
and a.minor = b.minor 
left join condo_complex c
on a.major = c.major
inner join (select * from parcel where minor = '0000') d
on c.major = d.major
order by a.major,a.minor,bldgnbr,unitnbr