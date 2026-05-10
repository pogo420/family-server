"""Asset tracker model, Table definition for event tracker API"""

from sqlalchemy import Column, Numeric, String, UniqueConstraint

from server_rest.db.database import Base

# Custom data types
Currency = Numeric(12, 2)
Percentage = Numeric(3, 1)


class AssetTracker(Base):
    __tablename__ = "asset_tracker"

    asset_id = Column(String(36), primary_key=True, index=True)
    asset_name = Column(String(255), nullable=False)
    asset_value = Column(Currency, nullable=False)
    asset_owner = Column(String(255), nullable=False)
    annual_investment = Column(Currency, nullable=False)
    annual_return = Column(Percentage, nullable=False)  # Percentage return, e.g., 5.0 for 5%
    annual_step_up = Column(Percentage, nullable=False)  # Percentage step-up, e.g., 2.0 for 2%

    __table_args__ = (UniqueConstraint("asset_name", "asset_owner", name="uq_asset_tracker_name_owner"),)
