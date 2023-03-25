from settings import *

@dp.message(Command('pyrun'))
async def cmd_pyrun(message: types.Message):

    args = " ".join(message.text.split()[1:])
    with open("package/pyrun_launch.py", "w", encoding='utf-8') as myfile:
        myfile.write(str(args))

    try:
        r = subprocess.check_output('python package/pyrun_launch.py', shell=True, stderr=subprocess.STDOUT, stdin=False)
        await message.answer(r)
    except subprocess.CalledProcessError as e:
        print(e.output)
        await message.answer(f'error\n {e.output}')