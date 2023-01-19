# مدیریت خطا ها
**خطا ها را میتوان به درستی در shadpy مدیریت کرد، زیرا در shadpy تعریف شده اند برای راحتی شما کاربران عزیز**
```python
from shadapi import exceptions
```
___
## دسته بندی خطاها
**بسته exceptions برای کنترل کردن خطاهایی که ممکن است در طول زمان اجرای برنامه به وجود بیایند،  به وجود آمده است**
```python
from shadapi.exceptions import InvalidInput, TooRequests, ...
```
- NotRegistered
- InvalidInput
- TooRequests
- InvaildAuth
- Repeated
