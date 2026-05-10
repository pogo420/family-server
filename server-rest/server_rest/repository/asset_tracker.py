import logging

from sqlalchemy.orm import Session

from server_rest.exceptions.asset_tracker import (
    AssetAddException,
    AssetAlreadyExistsException,
    AssetDeleteException,
    AssetRetrieveException,
)
from server_rest.models.asset_tracker import AssetTracker

# Local file logger
logger = logging.getLogger(__name__)


def get_all_assets(db: Session) -> list[AssetTracker]:
    """Retrieve all assets from the database.
    Args:
        db (Session): Database session.
    Returns:
        list[AssetTracker]: List of all assets in the database.
    Raises:
        AssetRetrieveException: If there is an error during the database operation.
    """
    try:
        assets = db.query(AssetTracker).all()
        return assets
    except Exception as e:
        logger.error(f"Error retrieving all assets: {e}")
        raise AssetRetrieveException() from e


def add_asset(db: Session, asset: AssetTracker) -> AssetTracker:
    """Add a new asset to the database.
    Args:
        db (Session): Database session.
        asset (AssetTracker): Asset data to be added.
    Returns:
        AssetTracker: The added asset if successful.
    Raises:
        AssetAddException: If there is an error adding the asset.
        AssetAlreadyExistsException: If an asset with the same ID already exists.
    """
    try:
        db.add(asset)
        db.commit()
        db.refresh(asset)
        return asset
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding asset: {e}")
        if "violates unique constraint" in str(e):
            raise AssetAlreadyExistsException() from e
        raise AssetAddException() from e


def delete_asset(db: Session, asset_id: str) -> None:
    """Delete an asset from the database by its ID.
    Args:
        db (Session): Database session.
        asset_id (str): ID of the asset to be deleted.
    Raises:
        AssetDeleteException: If there is an error deleting the asset.
    """
    try:
        asset = db.query(AssetTracker).filter(AssetTracker.asset_id == asset_id).first()
        if asset:
            db.delete(asset)
            db.commit()
        else:
            logger.warning(f"Asset with ID {asset_id} not found for deletion.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting asset with ID {asset_id}: {e}")
        raise AssetDeleteException() from e
