import sys

sys.path.append("C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/SAXS_Assist/src")

# from saxs_assistant.runner import run_analysis


# Use your package here
from saxs_assistant.runner import prepare_dataframe

prepare_dataframe(
    folder_path="C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/profiles",
    angular_unit="1/A",
)


# to run
# & "C:\Users\Cesar\Box\Sync files\SAXS project\Manuscript\SAXS_Assist\.venv\Scripts\python.exe" "C:\Users\Cesar\Box\Sync files\SAXS project\Manuscript\SAXS_Assist\general_test.py"

#if do PS

#python general_test.py
#to know if in powershell
#echo $PSVersionTable