# Use the "exec" resource type to execute the "pkill" command to kill the process
exec { 'killmenow':
  command => 'pkill -9 killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
