
"""
def airport(code):
	
	airport = Session.query(Apt).filter_by(apt_icao=code).first()
	if airport:
		return airport.dic()
	return None
"""