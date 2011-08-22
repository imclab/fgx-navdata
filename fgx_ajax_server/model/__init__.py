
"""The application's model objects"""

from fgx_ajax_server.model.meta import  Session, metadata
#import sqlalchemy as sa
#from sqlalchemy.ext.sqlsoup import SqlSoup
from sqlalchemy import orm, Table, Column
from sqlalchemy import Boolean, SmallInteger, INTEGER, NUMERIC, Float, Text, CHAR, DateTime, Date


def init_model(engine):
	
	"""Call me before using any of the tables or classes in the model"""
	meta.Session.configure(bind=engine)
	#meta.db = SqlSoup(engine)

	

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