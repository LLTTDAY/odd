select major,minor,name,year from parcel_precinct where minor ~ '^[0-9]' group by major,minor,name,year order by minor desc 
