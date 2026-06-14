"""Routes for asset tracker API"""

import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server_rest.db.database import get_db
from server_rest.schemas.asset_tracker import Asset, AssetResponse
from server_rest.schemas.common import GenericMessage
from server_rest.services.asset_tracker import add_asset_service, delete_asset_service, get_all_assets_service

# Local file logger
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/asset-tracker", tags=["asset tracker"])


@router.get("/all", response_model=list[AssetResponse])
def show_all_assets(db: Session = Depends(get_db)):
    logger.info("Retrieving all assets")
    return get_all_assets_service(db)


@router.post("/", response_model=GenericMessage)
def add_asset(asset: Asset, db: Session = Depends(get_db)):
    logger.info(f"Adding asset: {asset.asset_name}")
    return add_asset_service(db, asset)


@router.delete("/", response_model=GenericMessage)
def delete_asset(asset_id: str, db: Session = Depends(get_db)):
    logger.info(f"Deleting asset: {asset_id}")
    return delete_asset_service(db, asset_id)
