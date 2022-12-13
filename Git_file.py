import os
import shutil
import zipfile

# Делаем обход всего дерева каталога:

#for folderName, subfolders, filenames in os.walk("/Users/valeriyamekhonina/PycharmProjects/PythonPY1104/Занятие3/"
                                              #"Практические_задания"):
    #print("Текущая папка" + folderName)
    #for subfolder in subfolders:
        #print("ПОДПАПКА ПАПКИ" + folderName + ":" + subfolder)
    #for filename in filenames:
        #print("ФАЙЛ в ПАПКЕ" + folderName + ":" + filename)

    #print(" ")


# Делаем копию папки Практические занятия:

#source = "/Users/valeriyamekhonina/PycharmProjects/PythonPY1104/Занятие3/Практические_задания"
#destination = "/Users/valeriyamekhonina/Desktop/Practice_3_copy"
#dest = shutil.copytree(source, destination, dirs_exist_ok=True)
#print(dest)


#Создаем zip файл из папки Практические занятия:

#newZip = zipfile.ZipFile("practice_3.zip", "w")
#newZip.write("/Users/valeriyamekhonina/Desktop/Practice_3_copy", compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()

# Отправляем practice_3.zip на Github