import subprocess
# import tests.mainapp.tests_main_smoke

# print('Hello')
# subprocess.Popen(tests_main_smoke)

subprocess.Popen(['python3', 'tests/mainapp/tests_main_smoke.py'], stdout=subprocess.PIPE)