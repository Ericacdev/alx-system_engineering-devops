#increase file limits of  holberton user


exec { 'limit increase file1':
  command => 'sed -i s/'nofile 5'/'nofile 100'/g /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'limit increase file2':
  command => 'sed -i s/'nofile 4'/'nofile 100'/g /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
