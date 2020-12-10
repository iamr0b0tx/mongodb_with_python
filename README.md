# MongoDB with Python
Trying out MongoDB with python using PyMongo. Working with PyMongo by cretaaing a class that implements CRUD functionalities on MongoDB.

# Project Structure
- main.py
    - contains usage of the `mongo_db.MongoDB` class
    
- mongo_db.py
    - contains the MongoDB class which intefaces with PyMongo APIs
    
- test_mongo_db.ipynb
    - A jupyter notebook that contains unittests for the MongoDB class
    
- requirements.txt
    - a txt files containing the python requirements
    
# Set up
1. update your pip
    ```
        python -m pip install pip --upgrade
    ```

2. Set up virtual environment. This is optional

    ```
        python -m pip
        virtualenv venv
        source venv/bin/activate #linux users
        venv/Scripts/activate #windows users
    ```
3. install all the requirements
    ```
        pip install -r requirements.txt
    ```
4. run main.py
    ```
        python main.py
    ```
5. run test_mongo_db.ipynb
    ```
        jupyter notebook
    ```

