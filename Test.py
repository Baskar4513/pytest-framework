import os
print(f"Current working directory: {os.getcwd()}")
print(f"Script directory (__file__): {os.path.abspath(__file__) if '__file__' in globals() else 'No __file__'}")
