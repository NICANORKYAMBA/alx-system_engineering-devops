# Use the "package" resource type to manage the installation of the Flask package
package { 'flask':
  # Ensure that Flask version 2.1.0 is installed
  ensure   => '2.1.0',
  # Use pip3 as the package provider to install the package
  provider => 'pip3',
}
