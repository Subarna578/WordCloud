def upload():
	_upload_widget=fileupload.FileUploadWidget()
	
	def _cb(change):
		global file_contents
		
		decoded=io.StringIO(change['owner'].data.decode('utf-8'))
		
		filename=change['owner'].filename
		
		print("Uploaded '{}' ({:.2f} KB)".format(filename, len(decoded.read())/2 **10))
		
		file_contents=decoded.getvalue()
		
	_upload_widget.observe(_cb, names='data')
	
	display(_upload_widget)
	

