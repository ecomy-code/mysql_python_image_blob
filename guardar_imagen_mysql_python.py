import mysql.connector



def convercion_aBinaryText(archivo_text_binaname):
    with open(archivo_text_binaname, 'rb') as archivo_text_bina:
        binaryData = archivo_text_bina.read()
    return binaryData

def insertar_archivoX(emp_id, name, photo, biodataarchivo_text_bina):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='productos',
                                             user='root',
                                             password='azby')

        cursor = connection.cursor()
        insertar_blobarchivo_text_bina = """ INSERT INTO prueba
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        image_text_bina = convercion_aBinaryText(photo)
        archivo_text_bina = convercion_aBinaryText(biodataarchivo_text_bina)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, image_text_bina, archivo_text_bina)
        result = cursor.execute(insertar_blobarchivo_text_bina, insert_blob_tuple)
        connection.commit()
        print("Image and archivo_text_bina inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



try:

    insertar_archivoX(1, "Eric",   "./asd.png",  "./asd.png")
    insertar_archivoX(2, "Scott", "./Sin título.png",  "./Sin título.png")

except Exception as e:
    print(str(e))