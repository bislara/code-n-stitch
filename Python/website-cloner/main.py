from pywebcopy import save_webpage

kwargs = {'project_name': 'site folder'}

save_webpage(

    # url pf the website
    url=input("Paste the url here: "),
    # folder where the copy will be saved
    project_folder=input('Enter project path: '),
    **kwargs
)
