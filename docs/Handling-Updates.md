# مدیریت به روز رسانی ها
___
## تعریف به روزرسانی
به‌روزرسانی‌ها رویدادهایی هستند که در اکانت شاد شما اتفاق می‌افتند (پیام‌های دریافتی، عضویت اعضای جدید، فشار دادن دکمه‌های ربات و غیره) که به منظور اطلاع شما از وضعیت جدیدی که تغییر کرده است، می‌باشد. این به روز رسانی ها با ثبت یک یا چند عملکرد برگشت به تماس در برنامه شما با استفاده از Handlers انجام می شود.

هر کنترل کننده با یک رویداد خاص سروکار دارد و به محض اینکه یک به روز رسانی منطبق از شاد دریافت شود، تابع callback ثبت شده شما توسط فریمورک فراخوانی می شود و بدنه آن اجرا می شود.

## استفاده از دکوراتورها
زیباترین راه برای ثبت یک کنترل کننده پیام، استفاده از دکوراتور ()handler است:
```python
from shadapi import Client

app = Client('MY-AUTH')

@app.handler
async def my_bot(bot, message):
    await message.reply('``Hello`` __from__ **Shad-Api**!')
```

<p align="center">
    <a href="https://github.com/HoseanRC/shad-api/blob/master/docs/Error-Handling.md">
        صفحه بعدی
    </a>
  •
  <a href="https://github.com/HoseanRC/shad-api/blob/master/docs/Authorization.md">
        صفحه قبلی
    </a>
</p>
