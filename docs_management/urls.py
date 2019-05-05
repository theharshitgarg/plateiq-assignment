from django.conf.urls import url


from docs_management import views


urlpatterns = [
    url(r'list/(\d+)/update-status', views.update_status_view, name='update_status'),
    url(r'list/(\d+)/digitized', views.digitized_doc_details, name='list_docs'),
    url(r'upload-doc', views.upload_doc, name='upload_doc'),
    url(r'list', views.list_uploaded_docs, name='list_docs'),
    
    
    # API Views
    url(r'api/v1/list', views.UploadedDocListGenerics.as_view(), name='api_list_docs')
]
