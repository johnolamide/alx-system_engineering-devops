# This Puppet manifest configures ssh configuration file

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "
    Host 54.210.42.244
      User ubuntu
      IdentifyFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
