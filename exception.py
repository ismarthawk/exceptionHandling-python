# The exceptions can be handled in order
# try : 

# except e1: 

# except e2 : 


# except Exception as e : 

# else : 


# finally : 




if __name__ == "__main__" : 
	try : 
		a = 100 / 0
	except NameError : 
		print("Name Error")
	except Exception as exp : 
		print("The Exception arised is : ", type(exp).__name__)