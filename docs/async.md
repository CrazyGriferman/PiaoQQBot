# 使用异步

使用异步，使用 AsyncBotoy 和 AsyncAction 即可。 **暂不稳定**

使用和前面的介绍基本一致，需要注意的是:

- when_connected 和 when_disconnected 注册的钩子函数仍然要求是同步
- **动作语法糖和装饰器都无法使用**, 以后可能考虑兼容
- 中间件和接收函数包括插件中的接收函数是否异步都是可选的，但尽量都使用异步。但中间无论是否异步，都是按顺序执行的
- 与插件管理有关的方法依旧是同步
- close 方法是异步方法
