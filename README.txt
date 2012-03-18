______ _____       ______      _          _____                          
|  ___|  __ \      |  _  \    | |        /  ___|                         
| |_  | |  \/_  __ | | | |__ _| |_ __ _  \ `--.  ___ _ ____   _____ _ __ 
|  _| | | __\ \/ / | | | / _` | __/ _` |  `--. \/ _ \ '__\ \ / / _ \ '__|
| |   | |_\ \>  <  | |/ / (_| | || (_| | /\__/ /  __/ |   \ V /  __/ |   
\_|    \____/_/\_\ |___/ \__,_|\__\__,_| \____/ \___|_|    \_/ \___|_|   


The intention of this site is to do all the "data calls" and return in various formats.


==== Introduction ====
If your building a web service for FlightGear, then you will need to do all sorts
of tricks to aqquire data such as:

* Nav Data: finding fixes, ILS, airport search etc
* Multiplayers Online - making a remote telnet call peroidically
* Metars - fetching metars from various sources

So this site is intended to consolidate all these services together, 
and return the data in a reliable and usefule form, primarily json. 

At this stage of the game, this is experimntal code to test the concept.

--Contents
* dev_docs/ - is dev odumentation and spec WIP
* pylons/ - is a legacy (already) ap with some queries left and other bits to extract


==== Development ====

Design idea is in the dev_docs

