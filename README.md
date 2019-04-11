# rsync-linux-home

A simple script to make backups of your linux home.

## Usage
1. Configure UUID of destination partition into `rsync-linux-home.py`:
    ```
    DRIVE_UUID="<set here your UUID Partition>"
    ```

2. Configure which folders to include and which to exclude, changing arrays `INCLUDES`/`EXCLUDES` into `rsync-linux-home.py`:
    ```
    INCLUDES = [...]
    EXCLUDES = [...]
    ```

3. Make the script executable
    ```
    chmod +x rsync-linux-home.py
    ```

4. Launch the script to perform the backup
    ```
    ./rsync-linux-home.py
    ```

## License
GPLv3