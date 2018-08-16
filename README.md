# Python-Template
Creates port configs to a template from attributes in a csv file

----------------------------------------------------------------------------------------------------------------------------------------
															Windows
----------------------------------------------------------------------------------------------------------------------------------------

1.install Anaconda
	It is a virtual environment used to run Python. We cannot run it in windows cmd.
	https://www.anaconda.com/download/
	
2.install git
	this is used to clone python scripts from github into the local drive.
	in anaconda command line type - conda install git
	
3.cloning the scripts
	go to the repo and click "Clone or download". And copy the URL.
	
4.getting the script into the local directory
	in anaconda select the path where you want to store the program. And type - git clone """URL"""
	Example: git clone https://github.com/rapavin/Python-Template.git
	
5.create an attribute file
	the attribute file should be a CSV file in Excel.
	Example:
 	 Interface	  Name 	       tagged 	    untagged
 	 Int 1/1	  computer     1	        11
  	 Int 1/2	  phone   	   2	        22
  	 Int 1/3	  ap	       3	        33
  	 Int 1/4	  game	       4	        44
 	 Int 1/5	  phone        5	        55
  	 Int 1/6	  ap	       6	        66
	 ****** the template has been arrange in the following order. do not change the coloumn attributes.Meaning coloumn 1 should be 		               interfaces, coloumn 2 should be name etc....... ********
	 
	 how ever the program can be modified.
	 
6.Run the program.
    the python script should ask you for the file name of the attributes.
	Example:
		python jinja2-template.py
		Enter parameter-file to convert: XYZ.csv
		the output should be in the local directory.
