

# reads file and returns a list that are inside the file
def read_file(filename):
    #try to open the file and read it
  try:
      with open(filename, 'r') as file:
          return [line.strip().split(',') for line in file if line.strip()]
    #expect any error that may occur
  except FileNotFoundError:
      return []    
  except Exception as e:
      print(f"An error occurred while reading '{filename}': {e}")
      return [] 


#save data by writing in to the file
def save_data(filename, data):
 # open the file in write mode 
  try:
      with open(filename, "w") as file:
          for item in data:
              file.write(str(item) + "\n")
 #expect any error that may occur
  except Exception as e:
      print(f"An error occurred while saving data to '{filename}': {e}")


# this function is to add the data into the file
def append_data(filename, data):
    # open the file in append mode
  try:
      with open(filename, 'a') as file:
          for item in data:
              file.write(",".join(str(x) for x in item) + "\n")
  except FileNotFoundError:
      print(f"File '{filename}' not found.")
  except Exception as e:
      print(f"An error occurred: {e}")





