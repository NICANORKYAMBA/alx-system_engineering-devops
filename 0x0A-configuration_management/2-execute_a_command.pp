# Use the "exec" resource type to execute the "pkill" command to kill the process
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  # Set the "refreshonly" parameter to true to ensure that the command is only executed when triggered by another resource
  refreshonly => true,
}
