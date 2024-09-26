#increase file limits of  holberton user


exec { 'limit increase file_conf':
  command => "sed -i s/'nofile 5'/'nofile 100'/g /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'limit increase fileconf_2':
  command => "sed -i s/'nofile 4'/'nofile 100'/g /etc/security/limits.conf",
  path    => '/bin'
}
