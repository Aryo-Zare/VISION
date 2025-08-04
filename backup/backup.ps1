
# latitude


# =========================================================================
# === Define Variables for your Robocopy Command ===
# =========================================================================

# The source folder you want to back up
$sourceDir = "U:\home_cage\backup\test_transfer"

# The destination folder for the backup
# (The destination drive is a WebDAV share mapped to L:)
$destDir = "L:\P087\test"

# Get the current date in 'YYYY-MM-DD' format for the log file
$currentDate = Get-Date -f 'yyyy-MM-dd'

# Construct the full path for the log file
$logPath = "U:\home_cage\backup\log_backup_$currentDate.txt"


# =========================================================================
# === The Main Robocopy Command ===
# =========================================================================

# Ensure the log file directory exists before the command runs
# This prevents an error if the 'backup' folder doesn't exist
$logDir = Split-Path -Path $logPath -Parent
if (-not (Test-Path -Path $logDir)) {
    New-Item -Path $logDir -ItemType Directory | Out-Null
}


# Execute the robocopy command using the defined variables
robocopy $sourceDir $destDir /E /Z /MT:8 /R:5 /W:10 /ETA /LOG+:$logPath


# ___________________________________________________________________________

# cage_2_batch_1
robocopy "D:\" "L:\P087\P087 TM-02\tracking_cage_2_batch_1" /E /Z /MT:8 /R:5 /W:10 /ETA /tee /LOG:"C:\Users\User\Documents\log_backup_$(Get-Date -f 'yyyy-MM-dd').txt"

# cage_3_batch_1
robocopy "D:\" "L:\P087\P087 TM-03\tracking_cage_3_batch_1" /E /Z /MT:8 /R:5 /W:10 /ETA /tee /LOG:"C:\Users\User\Documents\log_backup_$(Get-Date -f 'yyyy-MM-dd').txt"

# cage_4_batch_1
robocopy "D:\" "L:\P087\P087 TM-04\tracking_cage_4_batch_1" /E /Z /MT:8 /R:5 /W:10 /ETA /tee /LOG:"C:\Users\User\Documents\log_backup_$(Get-Date -f 'yyyy-MM-dd').txt"
