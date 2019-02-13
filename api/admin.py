from django.contrib import admin
from .models import User, Budget, WasteBook, Category1, Category2, Config


class UserAdmin(admin.ModelAdmin):
    # 显示的列
    fields = ('nickname', 'mobile', 'username', 'email')


class BudgetAdmin(admin.ModelAdmin):
    pass


class WasteBookAdmin(admin.ModelAdmin):
    pass


class Category1Admin(admin.ModelAdmin):
    pass


class Category2Admin(admin.ModelAdmin):
    pass


class ConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(WasteBook, WasteBookAdmin)
admin.site.register(Category1, Category1Admin)
admin.site.register(Category2, Category2Admin)
admin.site.register(Config, ConfigAdmin)


