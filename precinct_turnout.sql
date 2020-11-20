with v1 as (select precinct,year,et_id,max(count) as ballots from results where counter like 'Times C%' group by precinct,year,et_id order by year, precinct),
v2 as (select precinct,year,et_id,max(count) as voters from results where counter like 'Registered V%' group by precinct,year,et_id order by year, precinct)
select 
v1.precinct as name, 
v1.year,
case when v1.et_id = 1 then 'G' else 'P' end as type,
case when ballots > voters then 1 else case when voters != 0 then ballots::decimal/voters::decimal else 0 end end as turnout
from 
v1 left join v2 
on v1.precinct = v2.precinct 
and v1.year = v2.year
and v1.et_id = v2.et_id
order by year, type, name