import argparse

def update_server_conf(filepath,parameter_to_update,updated_value):

    
    with open (filepath,"r") as file:
        lines=file.readlines() 
        
           
    with open (filepath,"w") as file:
    
        for line in lines:
            if parameter_to_update in line:
                file.write(parameter_to_update+"="+updated_value + "\n")
            else:
                file.write(line)



parser=argparse.ArgumentParser()
parser.add_argument("-f","--filepath",dest="filepath", help="Path to the server configuration file")
parser.add_argument("-p","--parameter_to_update",dest="parameter_to_update", help="Parameter to update")
parser.add_argument("-u","--updated_value",dest="updated_value", help="Updated value for the parameter")
args = parser.parse_args()



update_server_conf(args.filepath,args.parameter_to_update,args.updated_value)