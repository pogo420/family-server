"""Schema for asset tracker API"""

from pydantic import BaseModel, Field


class Asset(BaseModel):
    """Schema for an asset, payload for adding asset to the tracker"""

    asset_name: str = Field(..., min_length=1, max_length=255, description="Name of the asset")
    asset_owner: str = Field(..., min_length=1, max_length=255, description="Owner of the asset")
    asset_value: int = Field(..., ge=0, description="Value of the asset")


class AssetResponse(BaseModel):
    """Schema for asset response"""

    asset_id: str = Field(..., min_length=1, max_length=255, description="ID of the asset")
    asset_name: str = Field(..., min_length=1, max_length=255, description="Name of the asset")
    asset_owner: str = Field(..., min_length=1, max_length=255, description="Owner of the asset")
    asset_value: int = Field(..., ge=0, description="Value of the asset")
