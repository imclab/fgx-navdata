
"""The application's model objects"""

from fgx_ajax_server.model.meta import  Session, metadata
#import sqlalchemy as sa
#from sqlalchemy.ext.sqlsoup import SqlSoup
from sqlalchemy import orm, Table, Column
from sqlalchemy import Boolean, SmallInteger, INTEGER, NUMERIC, Float, Text, CHAR, String, DateTime, Date


def init_model(engine):
	
	"""Call me before using any of the tables or classes in the model"""
	meta.Session.configure(bind=engine)
	#meta.db = SqlSoup(engine)

	
##=================================================================
## Airport
t_apt =  Table('apt', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False),
	Column(u'wkb_geometry', CHAR()),
	Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'apt_name', CHAR(length=38, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True)),
	Column(u'has_tower', NUMERIC(precision=1, scale=0, asdecimal=True)),
	Column(u'hgt_tower_m', NUMERIC(precision=8, scale=2, asdecimal=True)),
	Column(u'tower_name', CHAR(length=32, convert_unicode=False, assert_unicode=None, unicode_error=None))
)

class Apt(object):
	def dic(self):
		return {'ogc_fid': self.ogc_fid,
				'apt_icao': self.apt_icao.strip(),
				'apt_name': self.apt_name.strip(),
				'elevation_m': str(self.elevation_m),
				'has_tower': bool(self.has_tower),
				'tower_name': '' if self.tower_name == None else self.tower_name.strip(),
				'hgt_tower_m': str(self.hgt_tower_m)
		}
orm.mapper(Apt, t_apt)

##=================================================================
## Ils
t_ils =  Table('ils', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False),
	Column(u'wkb_geometry', String(length=255)),
	Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True)),
	Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True)),
	Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True)),
	Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True)),
)

class Ils(object):
	def dic(self):
		return {'ogc_fid': self.ogc_fid,
				'navaid_id': self.navaid_id.strip(),
				'apt_icao': self.apt_icao.strip(),
				'rwy_num': self.rwy_num.strip(),
				'freq_mhz': str(self.freq_mhz),
				'true_heading_deg': str(self.true_heading_deg),
				'range_km': str(self.range_km),
				'subtype': self.subtype,
				'elevation_m': str(self.elevation_m)
		}
orm.mapper(Ils, t_ils)   
    
    
    
##=================================================================
## RunwayThreshold
t_runway_threhold =  Table('runwaythreshold', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False),
	Column(u'wkb_geometry', String(length=255), primary_key=False),
	Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
	Column(u'surface', CHAR(length=11, convert_unicode=False, assert_unicode=None, unicode_error=None )),
	Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None )),
	Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True)),
	Column(u'centerline_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'distance_remaining_signs', NUMERIC(precision=1, scale=0, asdecimal=True)),
	Column(u'displaced_threshold_m', Float(precision=53, asdecimal=False)),
	Column(u'is_displaced', NUMERIC(precision=1, scale=0, asdecimal=True)),
	Column(u'stopway_length_m', Float(precision=53, asdecimal=False)),
	Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	Column(u'approach_lighting', CHAR(length=26, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	Column(u'touchdown_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	Column(u'reil', CHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	Column(u'length_m', Float(precision=53, asdecimal=False)),
	Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True)),    
)

class RunwayThreshold(object):
	
	def dic(self):
		return {'ogc_fid': self.ogc_fid,
				'apt_icao': self.apt_icao.strip(),
				'rwy_num': self.rwy_num.strip(),
				'length_m': self.length_m,
				'width_m': str(self.width_m),
				'true_heading_deg': str(self.true_heading_deg)
		}
orm.mapper(RunwayThreshold, t_runway_threhold)

