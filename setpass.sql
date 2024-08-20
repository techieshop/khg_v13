#
#su - postgres
#psql
#\c KHG2022_DEMO_2
#
update res_users set password = 'test' where login in ('na@khg','ming@khg','donna@khg','ki@khg','suet@khg','hung@khg','man@khg','mui@khg','yiu@khg');