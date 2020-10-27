# 接收函数中间件

中间件跟接收函数类似，甚至可当成接收函数使用，与接收函数不同的是

1. 接收函数主要写具体的功能，而中间件是作为 ctx 预处理
2. 接收函数对返回值没有要求，**而中间件要求返回的还是传入的 ctx，如果返回的类型与传入的 ctx 不符,则会停止调用后面的中间件，也不会将执行对应消息的所有的接收函数**

注册消息中间件的方法和注册接收函数的方法一致, 分别是:

- `bot.friend_context_use`
- `bot.group_context_use`
- `bot.event_context_use`

---

1. 中间件函数可以任意多个，会按先后顺序排队调用
2. 可以用函数方式添加中间件函数，返回值是 Botoy 对象本身

中间件暂时想到用处就是给 ctx 增加一些数据，用于接收函数中调用，主要是用于插件中的接收函数

```python
@bot.group_context_use
def _(ctx: GroupMsg):
    ctx.master = 88888888 # 给群消息ctx添加一个master属性，这可以是你的QQ
    return ctx # 如果不返回ctx，该消息在运行完这个中间件之后，就丢弃了
```

添加了上面的中间件后
在所有群消息接收函数中可以通过 `ctx.master`访问该值, 而不是每次需要时都定义一遍

好友和事件同上

!!!tip

    三类消息 ctx 在传递给接收函数时，会自动添加 <code>ctx._host</code> 和 <code>ctx._port</code> 属性，所以这两个为保留值,
    其他保留属性:<code>_pattern_result</code>
