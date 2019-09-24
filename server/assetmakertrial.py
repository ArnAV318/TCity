from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation
listy=["k20 pro","oneplus 7 pro",
]







arguments = {"keywords":",".join(x for x in listy),"limit":3,"print_urls":True,"aspect_ratio":"square","size":">4MP"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded imag