#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define variables
jobname = 'plymaler_BLAST'
queue = 'med16core'
prefix = jobname
num_nodes = 1
num_processors = 1
wall = 3 # this is in hours

# This section prints the header/required info for the PBS script
# use a print statement for each line
print('#PBS -N', jobname) # job name
print('#PBS -q', queue) # which queue to use; check with qstat -q # use comma because do want space
print('#PBS -j oe') # join the STDOUT and STDERR into a single job output file
print('#PBS -o', prefix + '.' + '$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(num_nodes) + ':ppn=' + str(num_processors)) # how many resources to ask for (nodes = num nodes, ppn = num processors)
# print('#PBS -l walltime=1:00:00') # set the walltime (default to 1 hr) - must not exceed queue max
print('#PBS -l walltime=' + str(wall) + ':00:00') # use plus because don't want space; use str(wall) becuase wall is an integer
print() #add new line by putting empty print statement because print statement ends in newline

# cd into working directory (where executing script from)
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
# or print code chunk bracketed with '''
print(
'''   
# load modules
module purge
module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0
'''
)
print()

# commands for this job
print('# insert commands here')


# perl -pwe 's/\r/\n/' write_razor_pbs_class.py > z; mv z write_razor_pbs_class.py #to change MS-DOS \r carriage return to \n line breaks