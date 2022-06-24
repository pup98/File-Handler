
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os


'''To handle the different file system events, we will implement 
a sub-class of watchdog.events.FileSystemEventHandler.
The subclass will handle events like

on_created() for creation of new files/folders
on_modified() for updating a files
on_deleted() for deletion of files in a folder
on_moved() for moving files from a folder
on_any_event() for any event for the folder.'''

class Myhandler(FileSystemEventHandler):
    
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track): # tracking root folder
            if filename.endswith(('.txt')): # for txt files
                src = folder_to_track + '/' + filename          
                new_destination = folder_destination + '/' + filename
                os.rename(src, new_destination) # moves the file to the destination folder 
        
        print(event.src_path, event.event_type)


folder_to_track = 'C:/Users/Ujjwal/Desktop/root_folder'
folder_destination = 'C:/Users/Ujjwal/Desktop/dest_folder'


if __name__ == '__main__':

    event_handler  = Myhandler()
    '''
    Next, create an instance of Observer that will monitor the specified folder for
     any events.
    To watch the folder for any of the events, schedule the monitoring of the folder path
    with the observer 
    instance and the event handler sub-class.
    By default, watchdog.observers.Observer does not monitor the sub-folders. If you want 
    to monitor the sub-folders, 
    then you have to set the recursive flag to true '''

    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True )
    print('Monitoring Started')
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        print('Monitoring Terminated')