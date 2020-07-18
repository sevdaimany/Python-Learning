from zipfile import ZipFile

filename =input('Enter a zip file name: ')

#opening the zip file in READ mode
with  ZipFile(filename, 'r') as zip :
    zip.printdir()

    #extracing all the files 
    print('extracing all the files now..')
    zip.extractall()
    print('Done')