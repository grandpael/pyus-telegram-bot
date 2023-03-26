from settings import *

@dp.message(Command('run'))
async def cmd_pyrun(message: types.Message):

    msd = [message.text[5:]]
    args = " ".join(msd)
    with open("package/pyrun_launch.py", "w", encoding='utf-8') as myfile:
        myfile.write(str(args))
    try:
        r = subprocess.check_output('python package/pyrun_launch.py', shell=True, stderr=subprocess.STDOUT, stdin=False)
        await message.answer(r)
    except subprocess.CalledProcessError as e:
        await message.answer(e.output.decode())