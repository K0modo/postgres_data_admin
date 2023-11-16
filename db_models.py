from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase, MappedAsDataclass):
    pass



class Claims(Base):
    __tablename__ = 't_claims'

    claim_trans: Mapped[int] = mapped_column( primary_key=True)
    claim_id: Mapped[int]
    claim_item: Mapped[int]
    mem_acct: Mapped[int]
    injury_disease_id: Mapped[int]  # = mapped_column(ForeignKey("t_injury_disease.id"), nullable=False)
    specialty_id: Mapped[int]       #= mapped_column(ForeignKey("t_specialty.id"), nullable=False)
    facility_id: Mapped[int]        #= mapped_column(ForeignKey("t_facility.id"), nullable=False)

    # Declare relationship between the 2 classes involved
    # Relationship() is a function that allows ORM mapped classes to refer to each other
    # Relationship() defines an abstraction on top of database foreign keys which indicate how table rows can refer
    # to each other
    # payment: Mapped[int['ClaimsPaid']] = relationship(back_populates='claims')

    def __repr__(self):
        return (
            f"Claims (claim_trans={self.claim_trans!r}, "
            f"claim_id={self.claim_id!r}, claim_item={self.claim_item!r}, mem_acct={self.mem_acct!r}, injury_disease={self.injury_disease_id!r},"
            f" specialty_id={self.specialty_id!r}, facility_id={self.facility_id!r}"
        )


class ClaimsPaid(Base):
    __tablename__ = "t_claims_paid"

    pay_trans: Mapped[str] =mapped_column(primary_key=True)
    claim_trans_id: Mapped[int]     #= mapped_column(ForeignKey("t_claims.claim_trans"), nullable=False)
    charge_allowed: Mapped[float]
    deduct_copay: Mapped[float]
    charge_paid_ins: Mapped[float]
    charge_trans_date: Mapped[datetime]
    period: Mapped[int]
    quarter: Mapped[str]

    # claims: Mapped['Claims'] = relationship(back_populates='payment')

    def __repr__(self):
        return (
            f"ClaimsPaid (pay_trans={self.pay_trans!r}, "
            f"claim_trans={self.claim_trans_id!r}, charge_allowed={self.charge_allowed!r}, deduct_copay"
            f"={self.deduct_copay!r}, charge_trans_date={self.charge_trans_date!r}, period={self.period!r}, quarter={self.quarter!r}"
        )


class InjuryDisease(Base):
    __tablename__ = 't_injury_disease'

    id: Mapped[int] = mapped_column(primary_key=True)
    injury_disease_name: Mapped[str]

    # claims = relationship('Claims', backref=backref('t_injury_disease_id'),
    #                       cascade="all, delete-orphan")


class Specialty(Base):
    __tablename__ = 't_specialty'

    id: Mapped[int] = mapped_column(primary_key=True)
    specialty_name: Mapped[str]

    # claims = relationship('Claims', backref=backref('t_specialty_id'),
    #                       cascade='all, delete-orphan')


class Facility(Base):
    __tablename__ = 't_facility'

    id: Mapped[int] = mapped_column(primary_key=True)
    facility_name: Mapped[str]

    # claims = relationship('Claims', backref=backref('t_facility_id'),
    #                       cascade='all, delete-orphan')


class DailyClaims(Base):
    __tablename__ = 'v_daily_claims'

    charge_trans_date: Mapped[datetime] = mapped_column(primary_key=True)
    period: Mapped[int]
    count: Mapped[int]

    def __repr__(self):
        return (
            f"ClaimsPaid  Date: {self.charge_trans_date!r}  Period: {self.period!r},   "
            f"Claims_Count: {self.count!r}"
        )


class PeriodClaims(Base):
    __tablename__ = 'v_period_claims'

    period: Mapped[int] = mapped_column(primary_key=True)
    day_count: Mapped[int]
    sum_count: Mapped[int]

    def __repr__(self):
        return (
            f"Claims  Period: {self.period!r}  Period_Days {self.day_count!r},   "
            f"Sum_Claims: {self.sum_count!r}"
        )

