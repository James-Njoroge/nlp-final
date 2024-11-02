#!/bin/bash

### Create a Bash Script with PBS Directives for Multiple Jobs

### Array of job commands
commands=(
  "python ../nlp/NLPScholar/main.py '../file/path/to/train_config.yaml'"
  "python ../nlp/NLPScholar/main.py '../file/path/to/eval_config.yaml'"
)

### Iterate over each command and create a PBS script
for i in "${!commands[@]}"; do
  script_name="job_$i.pbs"
  output_log="~/pbs/outcomes/job_${i}.o"
  error_log="~/pbs/errors/job_${i}.e"

  cat << EOF > \$script_name
#!/bin/bash
### A name for the job - No spaces allowed
#PBS -N NLP_Job_$i
### Specify the queue or it will be submitted to workq by default
#PBS -q gpu
### Specify how many nodes and how many processors
#PBS -l nodes=1:ppn=5
### Specify the maximum time allowed for the job to run in each node
#PBS -l walltime=72:00:00
### Specify memory limit 4gb
#PBS -l mem=4gb
### Specify a file for the console output - USE a hostname of localhost:
#PBS -o localhost:\$output_log
### Specify a file for the console error output - USE a hostname of localhost:
#PBS -e localhost:\$error_log
### Receive an email when the job begins execution (b), ends (e), and encounters an error (a)
#PBS -m bae
### Specify an email for notifications
#PBS -M jnjoroge@colgate.edu
### Use submission environment, including all shell variables
#PBS -V

### Change directory to the working PBS directory
cd ~/nlp/nlp-midterm/

### Activate the 'nlp' environment
source /local/JupyterHub/etc/profile.d/conda.sh
conda activate nlp



### Run the job command
${commands[$i]}
EOF

  ### Submit the PBS script to the queue
  qsub \$script_name

done
