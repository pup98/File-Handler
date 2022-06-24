# File-Handler
This is a python script which handles files. 
* I have used Os module and watchdog library to implement this. 
Watchdog is an open-source python API library that is a cross-platform API to monitor file system events. You can specify a folder or a directory to watchdog observer, which keeps monitoring the folder for any changes like file creation, modification, deletion, or moving of files from one folder to another.
* The program monitors a folder using the Oberver class under watchog.observer, and filters all the text files and puts all these into a new destination folder using the os.rename method. 
