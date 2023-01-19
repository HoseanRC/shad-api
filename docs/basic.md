# شروع سریع
#### چند مرحله سریع تر شروع میکنیم، برای دیدن سرعت و عمکلکرد فریمورک روبیکا پای


## سرعت باورنکردنی شاد پای

1. کتابخانه را با دستور ```pip install -U shadpy``` نصب کنید
2. شناسه معتبر(آث) خود را از [وب شاد](https://web.shad.ir/ "وب شاد") دریافت کنید
3. اگر نحوه به دست آوردن آث را نمیدانید لطفا [آموزش دریافت آث](link) را دنبال کنید 
4. ویرایشگر کد خود را باز کنید و تیکه کد زیر را در آن وارد نمایید
```python
from shadapi import Client

app = Client('MY-AUTH')

@app.handler
async def my_bot(bot, message):
    await message.reply('``Hello`` __from__ **Shad-Api**!')
```
5. لطفا MY-AUTH را با شناسه آث حساب کاربری خود تعویض کنید
6. فایل را به عنوان ```hello.py``` ذخیره کنید
7. فایل پایتونی را با دستور ```python3 hello.py``` اجرا کنید
8. اگر پیام جدیدی دریافت کنید، خواهید دید که روبیکا پای به آن پاسخ داده است

# از API لذت ببرید
###### این فقط یک مرور سریع بود. در چند صفحه بعدی مقدمه، نگاه بسیار عمیق تری به آنچه در بالا انجام دادیم خواهیم داشت.

<p align="center">
    <a href="https://github.com/HoseanRC/shad-api/blob/master/docs/Install-Guide.md">
        صفحه بعدی
    </a>
</p>