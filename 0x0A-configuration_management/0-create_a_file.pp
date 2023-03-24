# Create a file named "school" in the "/tmp" directory
file { '/tmp/school':
  # Ensure that the file exists and is a regular file
  ensure  => file,
  # Set the file permission to 0744 (rwxr--r--)
  mode    => '0744',
  # Set the owner of the file to "www-data"
  owner   => 'www-data',
  # Set the group of the file to "www-data"
  group   => 'www-data',
  # Set the content of the file to "I love Puppet"
  content => 'I love Puppet',
}
