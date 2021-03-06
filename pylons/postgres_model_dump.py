# -*- coding: utf-8 -*-
## File autogenerated by SQLAutoCode
## see http://code.google.com/p/sqlautocode/

from sqlalchemy import *
from sqlalchemy.databases.postgresql import *

metadata = MetaData()


spatial_ref_sys =  Table('spatial_ref_sys', metadata,
    Column(u'srid', INTEGER(), primary_key=True, nullable=False),
            Column(u'auth_name', VARCHAR(length=256, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'auth_srid', INTEGER(), primary_key=False),
            Column(u'srtext', VARCHAR(length=2048, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'proj4text', VARCHAR(length=2048, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index('spatial_ref_sys_pkey', spatial_ref_sys.c.srid, unique=True)


geometry_columns =  Table('geometry_columns', metadata,
    Column(u'f_table_catalog', VARCHAR(length=256, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
            Column(u'f_table_schema', VARCHAR(length=256, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
            Column(u'f_table_name', VARCHAR(length=256, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
            Column(u'f_geometry_column', VARCHAR(length=256, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=True, nullable=False),
            Column(u'coord_dimension', INTEGER(), primary_key=False, nullable=False),
            Column(u'srid', INTEGER(), primary_key=False, nullable=False),
            Column(u'type', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False, nullable=False),
    
    
    )
Index('geometry_columns_pk', geometry_columns.c.f_table_catalog, geometry_columns.c.f_table_schema, geometry_columns.c.f_table_name, geometry_columns.c.f_geometry_column, unique=True)


waterrunwaypolygon =  Table('waterrunwaypolygon', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".waterrunwaypolygon_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num1', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num2', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'has_buoys', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'waterrunwaypolygon_geom_idx', waterrunwaypolygon.c.wkb_geometry, unique=False)


waterrunwaythreshold =  Table('waterrunwaythreshold', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".waterrunwaythreshold_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'has_buoys', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'waterrunwaythreshold_geom_idx', waterrunwaythreshold.c.wkb_geometry, unique=False)


helipad =  Table('helipad', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".helipad_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'helipad_name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'surface', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'helipad_geom_idx', helipad.c.wkb_geometry, unique=False)


apt =  Table('apt', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".apt_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'apt_name', CHAR(length=38, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'has_tower', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'hgt_tower_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'tower_name', CHAR(length=32, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'apt_geom_idx', apt.c.wkb_geometry, unique=False)


helipadpolygon =  Table('helipadpolygon', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".helipadpolygon_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'helipad_name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'surface', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'helipadpolygon_geom_idx', helipadpolygon.c.wkb_geometry, unique=False)


runwaypolygon =  Table('runwaypolygon', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".runwaypolygon_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num1', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num2', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'surface', CHAR(length=11, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'centerline_lights', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'distance_remaining_signs', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'runwaypolygon_geom_idx', runwaypolygon.c.wkb_geometry, unique=False)


taxiwayrectangle =  Table('taxiwayrectangle', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".taxiwayrectangle_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'surface', CHAR(length=11, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'edge_lighting', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
    
    
    )
Index(u'taxiwayrectangle_geom_idx', taxiwayrectangle.c.wkb_geometry, unique=False)


pavement =  Table('pavement', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".pavement_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', VARCHAR(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'surface', VARCHAR(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'texture_heading', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'pavement_geom_idx', pavement.c.wkb_geometry, unique=False)


runwaythreshold =  Table('runwaythreshold', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".runwaythreshold_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'width_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'surface', CHAR(length=11, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'shoulder', CHAR(length=8, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'smoothness', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
            Column(u'centerline_lights', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'edge_lighting', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'distance_remaining_signs', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'displaced_threshold_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'is_displaced', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'stopway_length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'markings', CHAR(length=22, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'approach_lighting', CHAR(length=26, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'touchdown_lights', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'reil', CHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'length_m', Float(precision=53, asdecimal=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'runwaythreshold_geom_idx', runwaythreshold.c.wkb_geometry, unique=False)


aptlinearfeature =  Table('aptlinearfeature', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".aptlinearfeature_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', VARCHAR(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'aptlinearfeature_geom_idx', aptlinearfeature.c.wkb_geometry, unique=False)


atcfreq =  Table('atcfreq', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".atcfreq_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'atc_type', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'freq_name', CHAR(length=32, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
    
    
    )
Index(u'atcfreq_geom_idx', atcfreq.c.wkb_geometry, unique=False)


aptboundary =  Table('aptboundary', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".aptboundary_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', VARCHAR(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'aptboundary_geom_idx', aptboundary.c.wkb_geometry, unique=False)


fix =  Table('fix', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".fix_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'fix_name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'fix_geom_idx', fix.c.wkb_geometry, unique=False)


aptlightbeacon =  Table('aptlightbeacon', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".aptlightbeacon_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', CHAR(length=28, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'color', CHAR(length=18, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'aptlightbeacon_geom_idx', aptlightbeacon.c.wkb_geometry, unique=False)


aptwindsock =  Table('aptwindsock', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".aptwindsock_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', CHAR(length=79, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'is_illuminated', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
    
    
    )
Index(u'aptwindsock_geom_idx', aptwindsock.c.wkb_geometry, unique=False)


vasi_papi_wigwag =  Table('vasi_papi_wigwag', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".vasi_papi_wigwag_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'type', CHAR(length=18, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'visual_glide_deg', NUMERIC(precision=4, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'vasi_papi_wigwag_geom_idx', vasi_papi_wigwag.c.wkb_geometry, unique=False)


ils =  Table('ils', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".ils_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'ils_geom_idx', ils.c.wkb_geometry, unique=False)


taxiwaysign =  Table('taxiwaysign', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".taxiwaysign_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'text', VARCHAR(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'size', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
    
    
    )
Index(u'taxiwaysign_geom_idx', taxiwaysign.c.wkb_geometry, unique=False)


vor =  Table('vor', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".vor_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'navaid_name', CHAR(length=29, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'slaved_variation_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'vor_geom_idx', vor.c.wkb_geometry, unique=False)


startuplocation =  Table('startuplocation', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".startuplocation_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'name', CHAR(length=38, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'startuplocation_geom_idx', startuplocation.c.wkb_geometry, unique=False)


airwaysegment =  Table('airwaysegment', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".airwaysegment_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'segment_name', CHAR(length=6, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'point1_name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'point2_name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'is_high', NUMERIC(precision=1, scale=0, asdecimal=True), primary_key=False),
            Column(u'base_fl', NUMERIC(precision=3, scale=0, asdecimal=True), primary_key=False),
            Column(u'top_fl', NUMERIC(precision=3, scale=0, asdecimal=True), primary_key=False),
    
    
    )
Index(u'airwaysegment_geom_idx', airwaysegment.c.wkb_geometry, unique=False)


ndb =  Table('ndb', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".ndb_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'navaid_name', CHAR(length=32, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_khz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
    
    
    )
Index(u'ndb_geom_idx', ndb.c.wkb_geometry, unique=False)


dme =  Table('dme', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".dme_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'navaid_name', CHAR(length=31, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'bias_km', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'dme_geom_idx', dme.c.wkb_geometry, unique=False)


gs =  Table('gs', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".gs_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
            Column(u'glide_slope', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'gs_geom_idx', gs.c.wkb_geometry, unique=False)


marker =  Table('marker', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".marker_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'subtype', CHAR(length=10, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'true_heading_deg', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'marker_geom_idx', marker.c.wkb_geometry, unique=False)


airwayintersection =  Table('airwayintersection', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".airwayintersection_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'name', CHAR(length=5, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
    
    
    )
Index(u'airwayintersection_geom_idx', airwayintersection.c.wkb_geometry, unique=False)


dmeils =  Table('dmeils', metadata,
    Column(u'ogc_fid', INTEGER(), primary_key=True, nullable=False, default=text(u'nextval(\'"public".dmeils_ogc_fid_seq\'::regclass)')),
            Column(u'wkb_geometry', NullType(), primary_key=False),
            Column(u'navaid_id', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'apt_icao', CHAR(length=4, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'rwy_num', CHAR(length=3, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), primary_key=False),
            Column(u'elevation_m', NUMERIC(precision=8, scale=2, asdecimal=True), primary_key=False),
            Column(u'freq_mhz', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'range_km', NUMERIC(precision=7, scale=3, asdecimal=True), primary_key=False),
            Column(u'bias_km', NUMERIC(precision=6, scale=2, asdecimal=True), primary_key=False),
    
    
    )
Index(u'dmeils_geom_idx', dmeils.c.wkb_geometry, unique=False)

