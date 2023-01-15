from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
	path("", views.HomeView.as_view(), name="home"),
	path("gallery/", views.GalleryView.as_view(), name="gallery"),
	path("my-images/", views.MyImagesView.as_view(), name="my-images"),
	path("my-coordinates/", views.MyCoordinatesView.as_view(), name="my-coordinates"),
	path("select-file/", views.select_file, name="select-file"),
	path("submit-coordinates/<uuid:id>/", views.submit_coordinates, name="submit-coordinates"),
	path("create-json/<uuid:id>/", views.create_json, name="create-json"),
]