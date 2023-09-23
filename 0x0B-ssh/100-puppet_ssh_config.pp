# This Puppet manifest configures ssh configuration file

file { '~/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "
    Host *
      IdentifyFile ~/.ssh/school
      PasswordAuthentication no
  ",
}

