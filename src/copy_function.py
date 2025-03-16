from os import path , listdir, mkdir
from shutil import copy, rmtree

def copy_function(copy_from, copy_to):

    if not path.exists(copy_to):
        mkdir(copy_to)
    elif copy_to == "public": 
        rmtree(copy_to)
        mkdir(copy_to)



    current_objects= listdir(copy_from)

    for object in current_objects:

        source_path = path.join(copy_from,object)
        dest_path = path.join(copy_to,object)

        if path.isfile(source_path):
            copy(source_path,dest_path)
        
        else:
            if not path.exists(dest_path):
                mkdir(dest_path)
            
            copy_function(source_path,dest_path)
            







copy_function("static","public")
