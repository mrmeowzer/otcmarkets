# coding: utf-8
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Numeric,
    Text,
    text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Stock(Base):
    __tablename__ = "Stock"

    id = Column(BigInteger, primary_key=True, unique=True)
    symbol = Column(Text, unique=True)
    name = Column(Text)
    stateofincorporation = Column(Text)
    authorizedshares = Column(BigInteger, server_default=text("'0'::bigint"))
    outstandingshares = Column(BigInteger, server_default=text("'0'::bigint"))
    unrestrictedshares = Column(BigInteger, server_default=text("'0'::bigint"))
    restrictedshares = Column(BigInteger, server_default=text("'0'::bigint"))
    float = Column(BigInteger, server_default=text("'0'::bigint"))
    dtcshares = Column(BigInteger, server_default=text("'0'::bigint"))
    tier = Column(Text, server_default=text("'Unknown'::text"))
    reportingstandard = Column(Text, server_default=text("'Unknown'::text"))
    marketcap = Column(BigInteger, server_default=text("'0'::bigint"))
    bidprice = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    askprice = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    bidsize = Column(BigInteger, server_default=text("'0'::bigint"))
    asksize = Column(BigInteger, server_default=text("'0'::bigint"))
    volume = Column(BigInteger, server_default=text("'0'::bigint"))
    thirtydayavgvolume = Column(
        Numeric(20, 10), server_default=text("'0'::numeric"))
    fiftytwoweeklow = Column(
        Numeric(20, 10), server_default=text("'0'::numeric"))
    fiftytwoweekhigh = Column(
        Numeric(20, 10), server_default=text("'0'::numeric"))
    mark = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    open = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    low = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    high = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    change = Column(Numeric(20, 10), server_default=text("'0'::numeric"))
    iscavetemptor = Column(Boolean)
    istransferagentverified = Column(Boolean)
    lastsize = Column(BigInteger, server_default=text("'0'::bigint"))
    insertdate = Column(DateTime(True))
    updatedate = Column(DateTime(True))
    otcupdatedate = Column(DateTime(True))

