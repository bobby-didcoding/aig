# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.views.home import HomeView
from core.views.gallery import GalleryView
from core.views.my_images import MyImagesView
from core.views.my_coordinates import MyCoordinatesView
from core.views.select_file import select_file
from core.views.submit_coordinates import submit_coordinates
from core.views.create_json import create_json


__all__ = [
    HomeView,
    GalleryView,
    MyImagesView,
    MyCoordinatesView,
    select_file,
    submit_coordinates,
    create_json
    ]
