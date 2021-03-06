
"""The application's model objects"""

from fgx_ajax_server.model.meta import  Session, metadata, Base
#import sqlalchemy as sa
#from sqlalchemy.ext.sqlsoup import SqlSoup
from sqlalchemy import orm, Table, Column, Index, ForeignKey
from sqlalchemy import Boolean, SmallInteger, Integer, Numeric, Text, String, DateTime, Date
#from sqlalchemy.orm import relationship, backref

def init_model(engine):
	
	"""Call me before using any of the tables or classes in the model"""
	meta.Session.configure(bind=engine)
	#meta.db = SqlSoup(engine)

"""
		self.source = None
		self.source_id = None

		self.ident = ident
		self.type = None
		self.name = None
		
		self.gps_code = None
		self.iata_code = None
		
		self.lat = None
		self.lon = None
		self.elevation_ft = None
		self.elevation_m = None
		
		self.continent = None
		self.iso_country = None
		self.iso_region = None
"""

class AirportTypes(Base):
	__tablename__ = "airport_types"
	
	airport_type_id = Column(Integer(), primary_key=True, nullable=False)
	airport_type = Column(String(length=50), nullable=False)


##=================================================================
## Airport
"""
t_airports =  Table('airports', metadata,
    Column(u'airport_id', INTEGER(), primary_key=True, nullable=False),
    Column("source", String(length=50), nullable=False),
    Column("source_id", String(length=50), nullable=False),
	#Column(u'wkb_geometry', CHAR()),
	Column(u'ident', String(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'name', String(length=50, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True)),
	Column("lat", String(length=15), nullable=True),
	Column("lon", String(length=15), nullable=True),
	#Column(u'has_tower', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'hgt_tower_m', NUMERIC(precision=8, scale=2, asdecimal=True)),
	#Column(u'tower_name', CHAR(length=32, convert_unicode=False, assert_unicode=None, unicode_error=None))
)
"""
class Airport(Base):
	__tablename__ = "airports"
	
	airport_id = Column(Integer(), primary_key=True, nullable=False)
	source = Column(String(length=50), nullable=False)
	
	airport_code = Column(String(length=6), nullable=False)
	iata_code = Column(String(length=4), nullable=True)
	airport = Column(String(length=50), nullable=False)
	type = Column(String(length=50), nullable=False)
	
	elevation_m = Column( Numeric(precision=8, scale=2, asdecimal=True))
	elevation_ft = Column( Numeric(precision=8, scale=2, asdecimal=True))
	lat = Column( String(length=11), nullable=True)
	lon = Column( String(length=11), nullable=True)

	def dic(self):
		return {'source': self.source,
				'airport_code': self.airport_code,
				'airport': self.airport,
				'elevation_m': str(self.elevation_m),
				'elevation_ft': str(self.elevation_ft),
				'lat': self.lat,
				'lon': self.lon
		}
#orm.mapper(Airport, t_airports)

##=================================================================
## Ils
"""
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
""" 
    
##=================================================================
## RunwayThreshold
"""
t_runways =  Table('runways', metadata,
    Column(u'runway_id', Integer(), primary_key=True, nullable=False),
	Column(u'source', String(length=50)),
	Column(u'airport_code', String(length=5)),
	Column(u'runway', String(length=20)),
	Column(u'length_m', Float(precision=53, asdecimal=False)),
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
	#Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True)),    
)
"""
class RunwaySurfaces(Base):
	__tablename__ = "runway_surfaces"
	
	surface_id = Column(Integer(), primary_key=True, nullable=False)
	surface = Column( String(length=50), nullable=False)
	
	def dic(self):
		return {'surface_id': self.surface_id,
				'surface': self.surface
		}
	
	@staticmethod
	def reverse_lookup():
		dic = {}
		for ob in meta.Session.query(RunwaySurfaces).all():
			dic[ob.surface] = ob.surface_id
		return dic
		
Index('runway_surfaces_idx', RunwaySurfaces.surface_id, RunwaySurfaces.surface)



class Runway(Base):
	__tablename__ = "runways"
	
	runway_id = Column(Integer(), primary_key=True, nullable=False)
	source = Column( String(length=50), nullable=False)
	
	airport_code = Column(String(length=5), nullable=False)
	runway = Column( String(length=20), nullable=False)
	
	length_m = Column( Numeric(precision=8, scale=2, asdecimal=True))
	length_ft = Column( Numeric(precision=8, scale=2, asdecimal=True))
	width_m = Column( Numeric(precision=8, scale=2, asdecimal=True))
	width_ft = Column( Numeric(precision=8, scale=2, asdecimal=True))
	
	#surface_id = Column( String(length=11 ))
	#surface_id = relationship("RunwaySurfaces", backref=backref('surface_id', order_by=runway_id))
	surface_id = Column(Integer, ForeignKey('runway_surfaces.surface_id'))
	
	#shoulder = Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None )),
	#smoothness = Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True)),
	#centerline_lights = Column(u'centerline_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#edge_lighting = Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	#distance_remaining_signs = Column(u'distance_remaining_signs', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#displaced_threshold_m = Column( Numeric(precision=2, asdecimal=True)),
	#is_displaced = Column(u'is_displaced', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#stopway_length_m = Column(u'stopway_length_m', Float(precision=53, asdecimal=False)),
	#markings = Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	#Column(u'approach_lighting', CHAR(length=26, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	#Column(u'touchdown_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'reil', CHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	
	def __repr__(self):
		return "<Runway %s - %s >" % (self.airport_code, self.runway)
	
	def dic(self):
		return {'runway_id': self.runway_id,
				'source': self.source,
				'airport_code': self.airport_code,
				'runway': self.runway,
				'length_m': str(self.length_m),
				'length_ft': str(self.length_ft),
				'width_m': str(self.width_m), 
				'width_ft': str(self.width_ft)
		}
Index('runway_idx', Runway.source, Runway.airport_code, Runway.runway)


"""

    keyword_id = sa.Column(sa.types.Integer, sa.Sequence('keyword_id_seq', optional=True), primary_key=True)
    keyword = sa.Column(sa.types.String(256), default='')
    source = sa.Column(sa.types.String(25), index=True, default='')
    insert_date = sa.Column(sa.types.DateTime, index=True, default='')
    check_date = sa.Column(sa.types.DateTime, index=True)
    global_monthly = sa.Column(sa.types.Numeric, default='0')
    ngram_group = sa.Column(sa.types.String(250), default='')
    average_targeted_monthly = sa.Column(sa.types.Numeric, default='0')
    competition = sa.Column(sa.types.Numeric, default='0')
    total_search_results = sa.Column(sa.types.Numeric, default='0')
    keyword_type = sa.Column(sa.types.String(25), default='')
    upperclicksperday = sa.Column(sa.types.Numeric, default='0')
    lowerclicksperday = sa.Column(sa.types.Numeric, default='0')
    lowercpc = sa.Column(sa.types.Numeric, default='0')
    uppercpc = sa.Column(sa.types.Numeric, default='0')
    upperavgposition = sa.Column(sa.types.Numeric, default='0')
    loweravgposition = sa.Column(sa.types.Numeric, default='0')

sa.Index('idx_nggm', Keyphrases.ngram_group, Keyphrases.global_monthly)
"""

    
##=================================================================
## RunwayThreshold
"""
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
"""
class Threshold(Base):
	__tablename__ = "thresholds"
		
	threshold_id = Column( Integer(), primary_key=True, nullable=False)
	#Column(u'wkb_geometry', String(length=255), primary_key=False),
	source = Column( String(length=50), nullable=False)
	
	airport_code = Column( String(length=10), nullable=False)
	threshold = Column(String(length=5), nullable=False)
	
	lat = Column(String(length=11), nullable=True)
	lon = Column(String(length=11), nullable=True)
	
	elevation_m =  Column( Numeric(precision=6, scale=2, asdecimal=True), nullable=True)
	elevation_ft =  Column( Numeric(precision=6, scale=2, asdecimal=True), nullable=True)
	
	displaced_m = Column( Numeric(precision=6, scale=2, asdecimal=True), nullable=True)
	displaced_ft = Column( Numeric(precision=6, scale=2, asdecimal=True), nullable=True)
	
	#Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None )),
	#Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True)),
	#Column(u'centerline_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None)),
	#Column(u'distance_remaining_signs', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'displaced_threshold_m', Float(precision=53, asdecimal=False)),
	#Column(u'is_displaced', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'stopway_length_m', Float(precision=53, asdecimal=False)),
	#Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	#Column(u'approach_lighting', CHAR(length=26, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	#Column(u'touchdown_lights', NUMERIC(precision=1, scale=0, asdecimal=True)),
	#Column(u'reil', CHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, )),
	#Column(u'length_m', Float(precision=53, asdecimal=False)),
	
	true_heading = Column( Numeric(precision=6, scale=2, asdecimal=True))    
	
	def __repr__(self):
		return "<Runway %s - %s >" % (self.airport_code, self.threshold)
		
	def dic(self):
		return {'ogc_fid': self.ogc_fid,
				'apt_icao': self.apt_icao.strip(),
				'rwy_num': self.rwy_num.strip(),
				'length_m': self.length_m,
				'width_m': str(self.width_m),
				'true_heading_deg': str(self.true_heading_deg)
		}
#orm.mapper(RunwayThreshold, t_runway_threhold)
Index('thresh_apt', Threshold.source, Threshold.airport_code, Threshold.threshold)



##===========================================================
class SysLog(Base):
	__tablename__ = "syslog"
		
	log_id = Column( Integer(), primary_key=True, nullable=False)
	dated = Column( Date(), nullable=False)

	airport_code = Column( String(length=20), nullable=True)
	runway = Column( String(length=20), nullable=True)
	threshold = Column( String(length=20), nullable=True)
	
	event =  Column( String(length=20), nullable=False)
	log =  Column( Text(), nullable=True)
	
	#airport_code = Column( String(length=10), nullable=False)
	#threshold = Column(String(length=5), nullable=False)
	
Index('syslog_idx', SysLog.airport_code, SysLog.runway, SysLog.threshold)

