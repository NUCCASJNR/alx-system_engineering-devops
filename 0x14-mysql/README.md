## 0x14-mysql

## replica config

##on source server

```bash
CREATE USER '<replication_user>'@'<replication_server>' IDENTIFIED BY '<password>';
GRANT REPLICATION SLAVE ON *.* TO '<replication_user>'@'<replication_server>';
FLUSH PRIVILEGES;
```

## on replica server

```bash
STOP SLAVE;
CHANGE MASTER TO
  MASTER_HOST = '<source_server>',
  MASTER_PORT = <source_port>,
  MASTER_USER = '<replication_user>',
  MASTER_PASSWORD = '<password>',
  MASTER_LOG_FILE = '<log_bin_filename>',
  MASTER_LOG_POS = <log_bin_position>;
START SLAVE;
```
## verify

```bash
SHOW SLAVE STATUS\G
```
