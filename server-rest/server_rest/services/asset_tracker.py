import uuid

from sqlalchemy.orm import Session

from server_rest.exceptions.asset_tracker import (
    AssetAddException,
    AssetAlreadyExistsException,
    AssetDeleteException,
    AssetRetrieveException,
)
from server_rest.models.asset_tracker import AssetTracker
from server_rest.repository.asset_tracker import add_asset, delete_asset, get_all_assets
from server_rest.schemas.asset_tracker import Asset, AssetResponse
from server_rest.schemas.common import GenericMessage


def add_asset_service(db: Session, asset_data: Asset) -> GenericMessage:
    """Service function to add a new asset to the database.
    Args:
        db (Session): Database session.
        asset_data (Asset): Data for the asset to be added.
    Returns:
        GenericMessage: A generic message indicating the result of the operation.
    """
    asset_table_row = AssetTracker(
        asset_name=asset_data.asset_name,
        asset_value=asset_data.asset_value,
        asset_owner=asset_data.asset_owner,
        asset_id=uuid.uuid4().hex,
    )
    try:
        added_asset = add_asset(db, asset_table_row)
        return GenericMessage(message=f"Asset '{added_asset.asset_name}' added successfully.")
    except AssetAddException as e:
        return GenericMessage(message=f"Failed to add asset: {str(e)}")
    except AssetAlreadyExistsException as e:
        return GenericMessage(message=f"Asset already exists: {str(e)}")


def delete_asset_service(db: Session, asset_id: str) -> GenericMessage:
    """Service function to delete an asset from the database by its ID.
    Args:
        db (Session): Database session.
        asset_id (str): ID of the asset to be deleted.
    Returns:
        GenericMessage: A generic message indicating the result of the operation.
    """
    try:
        delete_asset(db, asset_id)
        return GenericMessage(message=f"Asset with ID '{asset_id}' deleted successfully.")
    except AssetDeleteException as e:
        return GenericMessage(message=f"Failed to delete asset with ID '{asset_id}': {str(e)}")


def get_all_assets_service(db: Session) -> list[AssetResponse]:
    """Service function to retrieve all assets from the database.
    Args:
        db (Session): Database session.
    Returns:
        list[AssetResponse]: A list of all assets in the database.
    """
    try:
        asset_rows = get_all_assets(db)
        return [
            AssetResponse(
                asset_id=asset.asset_id,
                asset_name=asset.asset_name,
                asset_value=asset.asset_value,
                asset_owner=asset.asset_owner,
            )
            for asset in asset_rows
        ]
    except AssetRetrieveException:
        return []
