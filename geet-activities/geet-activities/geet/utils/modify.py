# import os
# from utils.data_structures.stack import ModifiedFilesStack
# from utils.status import list_files, read_file
# from utils.init import write_file


# def modify_files(path: str, extension: str, new_content: str) -> None:
#     modified_files_stack = ModifiedFilesStack()

#     files = list_files(path)

#     for file in files:
#         if file.endswith(extension):
#             file_path = path + file
#             original_content = read_file(file_path)
            
#             # Guardar el archivo original en la pila antes de modificarlo
#             modified_files_stack.push((file_path, original_content))

#             # Modificar el archivo con el nuevo contenido
#             write_file(file_path, new_content)

#     # Si es necesario, restaurar los archivos en el orden inverso
#     while not modified_files_stack.is_empty():
#         file_path, original_content = modified_files_stack.pop()
#         write_file(file_path, original_content)
