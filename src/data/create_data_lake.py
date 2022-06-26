from functools import partial
import os
import sys

def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
   
raise NotImplementedError("Implementar esta función")


os.mkdir('data_lake')
root_directory = 'data_lake/'

list = ["landing", "raw", "cleansed", "business"]

concat_root_path = partial(os.path.join, root_directory)
make_directory = partial(os.makedirs, exist_ok=True)

for path_items in map(concat_root_path, list):
    make_directory(path_items)

root_b = 'data_lake/business'
list_b = ["reports", "figures", "features", "forecasts"]

concat_root_path_b = partial(os.path.join, root_b)
make_directory = partial(os.makedirs, exist_ok=True)

for path_items in map(concat_root_path_b, list_b):
    make_directory(path_items)

root_r = 'data_lake/business/reports'
list_r = ["figures"]

concat_root_path_r = partial(os.path.join, root_r)
make_directory = partial(os.makedirs, exist_ok=True)

for path_items in map(concat_root_path_r, list_r):
    make_directory(path_items)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
