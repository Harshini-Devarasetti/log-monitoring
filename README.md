# log-monitoring
Install new modules- python -m pip install pandas
start the utility from cmd- python ReportUtility.py

LANE monitors the server at startup and in real-time for any errors or warnings with our advanced log file analyzer.
LANE scans log files and will generate a comprehensive report on the spot.
Keeps track of all critical errors and warnings, so that swift action can be taken to prevent any future issues.
Notifies the user with a summary of all the errors, warnings, and other critical information at that point of time.
LANE has comprehensive search feature to get detailed summaries of any sofwtare or issues quickly and accurately.

Configurations like root directory path, smtp server settings, Email address are maintained in application.yml file which makes cloud deployable through UCD.
We have used regex for pattern matching, pandas to create the structural representation of information using dataframe, smtp server for notifications.
