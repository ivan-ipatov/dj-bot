from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com">
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200;400;600&display=swap" rel="stylesheet">
  <title>Чат-бот</title>
</head>

<body>
  <div class="grid h-screen place-content-center font-[Manrope]">
    <h1 class="font-black text-[35px] mb-4">Я в порядке</h1>
    <a href="https://t.me/rtf_dj_bot" target="_blank" class="text-center bg-blue-400 py-3 rounded-full text-white">Написать боту</a>
  </div>

</body>

</html>
    '''


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
