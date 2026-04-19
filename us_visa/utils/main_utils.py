import os 
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import UsVisaException
from us_visa.logger import logging

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise UsVisaException(e,sys) from e    
    
def write_yaml_file(file_path:str,content:object, replace:bool=False)->None:
    """
    Writes content to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        content (object): The content to be written to the YAML file.
        replace (bool, optional): Whether to replace the existing file. Defaults to False.

    Raises:
        UsVisaException: If an error occurs while writing to the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)    

    except Exception as e:
        raise UsVisaException(e,sys) from e

def load_object(file_path:str)->object:
    """
    Loads an object from a file using dill.

    Args:
        file_path (str): The path to the file containing the object.    

    Returns:
        object: The object loaded from the file.

     """
    logging.info("Entered the load_object method of utils")

    try:
        with open(file_path, 'rb') as file_obj:
            obj= dill.load(file_obj)

        logging.info("Exited the load_object method of utils")
        return obj       
    except Exception as e:
        raise UsVisaException(e,sys) from e

def save_numpy_array_data(file_path:str, array:np.array):
    """
    Saves a NumPy array to a file.

    Args:
        file_path (str): The path to the file where the array will be saved.
        array (np.ndarray): The NumPy array to be saved.

    Raises:
        UsVisaException: If an error occurs while saving the array.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise UsVisaException(e, sys) from e

def load_numpy_array_data(file_path:str)->np.array:
    """
    Loads a NumPy array from a file.

    Args:
        file_path (str): The path to the file containing the NumPy array.
    Returns:
        np.ndarray: The NumPy array loaded from the file.
     """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise UsVisaException(e, sys) from e
    
def save_object(file_path:str, obj:object)->None:
    """
    Saves an object to a file using dill.

    Args:
        file_path (str): The path to the file where the object will be saved.
        obj (object): The object to be saved.

    Raises:
        UsVisaException: If an error occurs while saving the object.
    """
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")    
    except Exception as e:
        raise UsVisaException(e,sys) from e    
    
def drop_columns(df:DataFrame, columns:list)->DataFrame:
    """
    Drops specified columns from a DataFrame.

    Args:
        df (DataFrame): The input DataFrame.
        columns (list): A list of column names to be dropped.

    Returns:
        DataFrame: A new DataFrame with the specified columns dropped.
    """
    try:
        df=df.drop(columns=columns,axis=1)
        logging.info("Existed the drop_columns method of utils" )
        return df
    except Exception as e:
        raise UsVisaException(e,sys) from e