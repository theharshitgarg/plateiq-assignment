# How to run
1. Go to the main project folder
2. Run `python install -r requirements.txt`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver` 

# Assignment Details
1. Upload New PDF Doc : A user  can upload a new PDF
2. Uploaded Docs List View : 
	- Show list of uploaded docs
	- User can update the status of the docs from the view itself
3. Update Extracted Docs : User can update the existing fields of an extracted doc, created from the uploaded doc.


# Note:
1. The UI is not given much attention.
2. Creation of Extraced Doc from Uploaded doc happens in the background job, and is not implemened
