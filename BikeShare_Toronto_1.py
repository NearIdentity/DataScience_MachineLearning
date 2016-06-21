#!/usr/bin/python

from os import path, getcwd
from numpy import genfromtxt
from operator import itemgetter

trip_data_file="HackBikeShareTO-Trips.csv"
num_top=10


if __name__=="__main__":
	print "# Diagnostic: Seeking \'"+getcwd()+'/'+trip_data_file+"\'..."
	if(path.exists(getcwd()+'/'+trip_data_file)):
		print "# Diagnostic: File \'"+getcwd()+'/'+trip_data_file+"\' found"
		data=genfromtxt(getcwd()+'/'+trip_data_file, dtype=int, delimiter=',', skip_header=1, usecols=(4,7))
		data_str=genfromtxt(getcwd()+'/'+trip_data_file, dtype=str, delimiter=',', skip_header=1, usecols=(3,6))
		#data=data[0:1000,:]
		print "# Diagnostic: File \'"+getcwd()+'/'+trip_data_file+"\' loaded"
		num_data=len(data[:,0])
		print str("# Diagnostic: num_data = %d" %num_data)
		trip_counts={}
		for i in range(num_data):
			key=(data[i,0],data[i,1])
			###key=(data_str[i,0],data_str[i,1])
			if not(key in trip_counts.keys()):
				trip_counts.update({key:1})
			else:
				trip_counts[key]+=1
		print str("# Diagnostic: sum(trip_counts.values()) = %d\n" %sum(trip_counts.values()))
		trip_counts_sorted=sorted(trip_counts.items(),key=itemgetter(1),reverse=True)
		buffer_count=0
		output_file=open("CycleApp_TripCountsSorted.csv",'w')
		output_file.write("Start_Code,End_Code,Count\n")
		for top_item in trip_counts_sorted:
			buffer_count+=1
			###print top_item
			###print str("%i,%i,%i" %(top_item[0][0],top_item[0][1],top_item[1]))
			###if(buffer_count==num_top):
			###	break
			if(buffer_count<=10):
				print str("%i,%i,%i" %(top_item[0][0],top_item[0][1],top_item[1]))
			output_file.write(str("%i,%i,%i\n" %(top_item[0][0],top_item[0][1],top_item[1])))
		output_file.close()
			
	else:
		raise IOError("File \'"+getcwd()+'/'+trip_data_file+"\' not found")
		
			
				
	
