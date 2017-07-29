from __future__ import division, print_function
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, SmallInteger, create_engine

engine = create_engine('sqlite:///anomalies.db', echo=False)
Base = declarative_base()

########################################################################

class Data(Base):
    __tablename__ = 'Data'
    hexo_timestamp = Column(Integer, primary_key=True, nullable=False)
    data = Column(Integer, nullable=False)
    datatype = Column(Integer, nullable=False)

    def __repr__(self):
        return ("<Data('%s', '%s' ,'%s')>"
                % (self.hexo_timestamp, self.data, self.datatype))

    def __init__(self, hexo_timestamp, data,
                 datatype):
        self.hexo_timestamp = hexo_timestamp
        self.data = data
        self.datatype = datatype
# ----------------------------------------------------------------------------

class AtrFibAlarms(Base):
    __tablename__ = 'AtrFibAlarms'
    start_hexo_timestamp = Column(Integer, primary_key=True, nullable=False)
    end_hexo_timestamp = Column(Integer, nullable=False)
    doe = Column(DateTime, nullable=False)
    num_of_NEC = Column(SmallInteger, nullable=False)
    data_reliability = Column(SmallInteger, nullable=False)
    window_size = Column(SmallInteger, nullable=False, default=64)

    def __repr__(self):
        return ("<AtrFibAlarms('%s', '%s', '%s', '%s', '%s')>"
                % (self.start_hexo_timestamp, self.end_hexo_timestamp,
                   self.doe, self.num_of_NEC, self.data_reliability))

    def __init__(self, start_hexo_timestamp, end_hexo_timestamp,
                 doe, num_of_NEC, data_reliability, window_size):
        self.start_hexo_timestamp = start_hexo_timestamp
        self.end_hexo_timestamp = end_hexo_timestamp
        self.doe = doe
        self.num_of_NEC = num_of_NEC
        self.data_reliability = data_reliability
        self.window_size = window_size
# ----------------------------------------------------------------------------


class VenTacAlarms(Base):
    __tablename__ = 'VenTacAlarms'
    start_hexo_timestamp = Column(Integer, primary_key=True, nullable=False)
    end_hexo_timestamp = Column(Integer, nullable=False)
    doe = Column(DateTime, nullable=False)
    data_reliability = Column(SmallInteger, nullable=False)

    def __repr__(self):
        return ("<AtrFibAlarms('%s', '%s', '%s', '%s')>"
                % (self.start_hexo_timestamp, self.end_hexo_timestamp,
                   self.doe, self.data_reliability))

    def __init__(self, start_hexo_timestamp, end_hexo_timestamp,
                 doe, data_reliability):
        self.start_hexo_timestamp = start_hexo_timestamp
        self.end_hexo_timestamp = end_hexo_timestamp
        self.doe = doe
        self.data_reliability = data_reliability
# ----------------------------------------------------------------------------


class APCAlarms(Base):
    __tablename__ = 'APCAlarms'
    RRPeak_hexo_timestamp = Column(Integer, primary_key=True,
                                   nullable=False, default=datetime.now())
    RR_Quality = Column(SmallInteger, nullable=False)
    doe = Column(DateTime, nullable=False)
    PVC_from = Column(SmallInteger, nullable=False)

    def __repr__(self):
        return ("<APCAlarms('%s', '%s', '%s', '%s')>"
                % (self.RRPeak_hexo_timestamp, self.RR_Quality,
                   self.doe, self.PVC_from))

    def __init__(self, RRPeak_hexo_timestamp, RR_Quality,
                 doe, PVC_from):
        self.RRPeak_hexo_timestamp = RRPeak_hexo_timestamp
        self.RR_Quality = RR_Quality
        self.doe = doe
        self.PVC_from = PVC_from


# create tables
Base.metadata.create_all(engine)
