# python+uiautomator2 完成控制手机<br>
## 一 环境搭建<br>
+ 安装 uiautomator2
   - pip install uiautomator2
   - 如果你需要用到截图，安装pillow
   - pip install pillow
+ 手机USB线与电脑连接，将关联的守护进程部署到设备电脑连接上一个手机或多个手机，确保adb已经添加到环境变量中，执行下面的命令会自动安装本库所需要的设备端程序：uiautomator-server，atx-agent，openstf / minicap，openstf / minitouch
   - #### init就是所有USB连接电脑的手机上都安装uiautomator2
   - python -m uiautomator2 init
   - #### 指定手机安装uiautomator2， 用 --mirror
   - python -m uiautomator2 init --mirror --serial {设备的serial}
   - 查看设备的serial 在CMD 命令行 adb devices

## 二 设备连接方法，有两种
   + 通过WiFi，假设设备IP 192.168.5.4和您的PC在同一网络中
      - `d = u2.connect('192.168.5.4') # alias for u2.connect_wifi('192.168.5.4')`
   + 通过USB， 假设设备序列是123456789F（见adb devices）
      - `d = u2.connect('123456789F') # alias for u2.connect_usb('123456789F')`
   + 需要设备曾经使用 python -m uiautomator2 init 初始化过

## 三 检查并维持设备端守护进程处于运行状态
&nbsp;&nbsp;&nbsp;`d.healthcheck()`

## 四 安装应用
&nbsp;&nbsp;&nbsp;`d.app_install（' http://some-domain.com/some.apk '）`安装应用，只能从URL安装

## 五 启动应用
&nbsp;&nbsp;&nbsp;`d.app_start（“ com.example.hello_world ”）＃ start包名称`

## 六 停止应用
&nbsp;&nbsp;&nbsp;`d.app_stop（ “ com.example.hello_world ”）`＃相当于`am force-stop`，因此你可能丢失数据 <br>
&nbsp;&nbsp;&nbsp;`d.app_clear（ ' com.example.hello_world '）`＃相当于`pm clear`

## 七 推送和拉取文件
   + 把文件推送到设备
      - `d.push("foo.txt", "/sdcard/")`# push to a folder
      - `d.push("foo.txt", "/sdcard/")`# push and rename
      - `d.push("foo.txt", "/sdcard/")`# push fileobj
      - `with open("foo.txt", 'rb') as f:`<br>
               `d.push(f, "/sdcard/")`
      - `d.push("foo.sh", "/data/local/tmp/", mode=0o755)`# push and change file access mode

   + 从设备中提取文件
      - #### FileNotFoundError will raise if the file is not found on the device
      - `d.pull("/sdcard/tmp.txt", "tmp.txt")`
      - `d.pull("/sdcard/some-file-not-exists.txt", "tmp.txt")`
   
   + 跳过弹窗，禁止弹窗
      - `d.disable_popups（） ＃自动跳过弹出窗口`
      - `d.disable_popups（false）＃禁用自动跳过弹出窗口`

## 八 Session
   ### Session represent an app lifestyle. 可用于启动应用，检测应用崩溃
   + 启动应用
      - `sess = d.session（“ com.netease.cloudmusic ”）`
   + Attach to the running app
      - `sess = d.session（“ com.netease.cloudmusic ”，attach = True）`
   + 检测应用崩溃
      - `# When app is still running`
      - `sess(text="Music").click() # operation goes normal`
      - `# If app crash or quit`
      - `sess(text="Music").click() # raise SessionBrokenError`
      - `# other function calls under session will raise SessionBrokenError too`

## 九 检索设备信息
   + 获取基本信息
      - `d.info`
      - `d.window_size()`
      - `d.serial`

## 十 关键事件
   + 打开/关闭屏幕
      - `d.screen_on（）＃打开屏幕 `
      - `d.screen_off（）＃关闭屏幕`
   + 获取当前屏幕状态
      - `d.info.get（' screenOn '）＃ require Android> = 4.4`
   + Home / Back 按键操作
      - `d.press("home") # press the home key, with key name`
      - `d.press("back") # press the back key, with key name`
      - `d.press(0x07, 0x02) # press keycode 0x07('0') with META ALT(0x02)`
      - 目前支持这些密钥名称(home,back,left,right,up,down,center,menu,search,enter,delete ( or del),recent (recent apps),volume_up,volume_down,volume_mute,camera,power)
   + 解锁屏幕
      - `d.unlock()`
      - `# This is equivalent to`
      - `# 1. launch activity: com.github.uiautomator.ACTION_IDENTIFY`
      - `# 2. press the "home" key`

## 十一 手势与设备的交互
   + 点击屏幕
      - `d.click（x，y）`
   + 双击
      - `d.double_click（x，y）`
      - `d.double_click（X，Y，0.1）＃默认之间的两个点击持续时间为0.1秒`
   + 长按一下屏幕
      - `d.long_click（x，y）`
      - `d.long_click（X，Y，0.5）＃长按0.5秒（默认）`
   + Swipe 滑动
      - `d.swipe(sx, sy, ex, ey)`
      - `d.swipe(sx, sy, ex, ey, 0.5) # swipe for 0.5s(default)`
   + 拖动
      - `d.drag(sx, sy, ex, ey)`
      - `d.drag(sx, sy, ex, ey, 0.5) # Drag for 0.5s(default)`
   + 滑动点   多用于九宫格解锁，提前获取到每个点的相对坐标（这里支持百分比）
      - `# swipe from point(x0, y0) to point(x1, y1) then to point(x2, y2)`
      - `# time will speed 0.2s bwtween two points`
      - `d.swipe((x0, y0), (x1, y1), (x2, y2), 0.2)`
## 十二 屏幕相关的
   + 检索/设置设备方向     --可能的方向如下
      - `# 检索方向。输出可以是 "natural" or "left" or "right" or "upsidedown"`
      - `orientation = d.orientation`
      - `# WARNING: not pass testing in my TT-M1`
      - `# set orientation and freeze rotation.`
      - `# notes: setting "upsidedown" requires Android>=4.3.`
      - `d.set_orientation('l') # or "left"`
      - `d.set_orientation("l") # or "left"`
      - `d.set_orientation("r") # or "right"`
      - `d.set_orientation("n") # or "natural"`
   + Freeze/Un-freeze rotation
      - `# freeze rotation`
      - `d.freeze_rotation()`
      - `# un-freeze rotation`
      - `d.freeze_rotation(False)`
   + 截图
      ```
         # 截取并保存到计算机上的文件，需要Android> = 4.2。
         d.screenshot("home.jpg")
         
         # 得到PIL.Image格式的图像. 但你必须先安装pillow
         image = d.screenshot() # default format="pillow"
         image.save("home.jpg") # or home.png. Currently, 只支持png and jpg格式的图像
         
         # 得到OpenCV的格式图像。当然，你需要numpy和cv2安装第一个
         import cv2
         image = d.screenshot(format='opencv')
         cv2.imwrite('home.jpg', image)
         
         # 获取原始JPEG数据
         imagebin = d.screenshot(format='raw')
         open("some.jpg", "wb").write(imagebin)
      ```
   + Dump UI hierarchy
      - `# get the UI hierarchy dump content (unicoded).`
      - `xml = d.dump_hierarchy()`
   + 打开通知或快速设置
      - `d.open_notification（）`
      - `d.open_quick_settings（）`
## 十三 选择
   + Selector是一种在当前窗口中标识特定UI对象的便捷机制。
   ```
   # 选择文本为'Clock'的对象，其className为'android.widget.TextView'd 
   d(text='Clock', className='android.widget.TextView')
   ```
   + 选择器支持以下参数。有关详细信息，请参阅[UiSelector Java文档](https://github.com/openatx/uiautomator2)。
   + text，textContains，textMatches，textStartsWith
   + className， classNameMatches
   + description，descriptionContains，descriptionMatches，descriptionStartsWith
   + checkable，checked，clickable，longClickable
   + scrollable，enabled，focusable，focused，selected
   + packageName， packageNameMatches
   + resourceId， resourceIdMatches
   + index， instance
## 十四 Children and siblings
   + children
      - `# get the children or grandchildren`
      - `d(className="android.widget.ListView").child(text="Bluetooth")`
   + siblings
      - `# get siblings`
      - `d(text="Google").sibling(className="android.widget.ImageView")`
   + children by text or description or instance
      ```
         # get the child matching the condition className="android.widget.LinearLayout"
         # and also its children or grandchildren with text "Bluetooth"
         d(className="android.widget.ListView", resourceId="android:id/list") \
         .child_by_text("Bluetooth", className="android.widget.LinearLayout")
         
         # 通过允许滚动搜索来获取子项
         d(className="android.widget.ListView", resourceId="android:id/list") \
         .child_by_text(
            "Bluetooth",
            allow_scroll_search=True,
            className="android.widget.LinearLayout"
         )
      ```
   + child_by_description is to find children whose grandchildren have the specified description, other parameters being similar to child_by_text.
   + child_by_instance是在子层次结构中的任何位置找到具有子UI元素的子元素，该元素位于指定的实例中。它在可见视图上执行而无需滚动.
   + UiScrollable，getChildByDescription，getChildByText，getChildByInstance
   + UiCollection，getChildByDescription，getChildByText，getChildByInstance
   + 获取/设置/清除可编辑字段的文本（例如，EditText小部件）
   ```
      d（text = “ Settings ”）.get_text（）   # get widget text 
      d（text = “ Settings ”）.set_text（“ My text ... ”）   ＃设置文本 
      d（text = “ Settings ”）.clear_text（ ）   ＃清除文字
   ```
   + 获取Widget中心点
      - `x, y = d(text="Settings").center()`
## 十五 对选定的UI对象执行单击操作
   + 执行单击特定对象
      ```
         # 单击特定ui对象的中心
         d(text="Settings").click()
         # wait元素最多显示10秒然后单击 
         d(text="Settings").click(timeout=10)
         # 请在10秒时点击，默认的超时0
         clicked = d(text='Skip').click_exists(timeout=10.0)
         # 点击直到元素不见了，返回布尔
         is_gone = d(text="Skip").click_gone(maxretry=10, interval=1.0) # maxretry default 10, interval default 1.0
      ```
   + 长按特定的UI对象
      - `# 长按特定UI对象的中心`
      - `d(text="Settings").long_click()`
## 十六 特定UI对象的手势操作
   + 将UI对象拖向另一个点或另一个UI对象
   ```
      # notes : Android<4.3不能使用drag.
      # 0.5S后，将UI对象拖动到屏幕点（x，y）
      d(text="Settings").drag_to(x, y, duration=0.5)
      # drag the UI object to (the center position of) another UI object, in 0.25 second
      d(text="Settings").drag_to(text="Clock", duration=0.25)
   ```
   + 两点手势操作，从一个点到另一个点
      - `d(text="Settings").gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))`
   + 特定UI对象上的两点手势
      ### 支持两种手势
      - In，从边缘到中心
      - Out，从中心到边缘
      ```
         # notes : pinch can not be set until Android 4.3.
         # 从边缘到中心. here is "In" not "in"
         d(text="Settings").pinch_in(percent=100, steps=10)
         # 从中心到边缘
         d(text="Settings").pinch_out()
      ```
      - 等到特定UI出现或消失
      ```
         # 一直等到UI对象出现
         d(text="Settings").wait(timeout=3.0) # return bool
         # 一直等到UI对象消失
         d(text="Settings").wait_gone(timeout=1.0)
      ```
      ### 默认超时为20秒。有关详细信息，请参阅全局设置
## 十七 对特定的ui对象执行fling（可滚动）
   #### 可能的属性
   + horiz 要么 vert
   + forward或backward或toBeginning或toEnd
   ```
      # fling forward(default) vertically(default) 
      d(scrollable=True).fling()
      # fling forward horizontally
      d(scrollable=True).fling.horiz.forward()
      # fling backward vertically
      d(scrollable=True).fling.vert.backward()
      # fling to beginning horizontally
      d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
      # fling to end vertically
      d(scrollable=True).fling.toEnd()
   ```
## 十八 在特定的ui对象上执行Scroll（可滚动））
   ### Possible properties
   + horiz or vert
   + forward or backward or toBeginning or toEnd, or to
   ```
      # scroll forward(default) vertically(default)
      d(scrollable=True).scroll(steps=10)
      # scroll forward horizontally
      d(scrollable=True).scroll.horiz.forward(steps=100)
      # scroll backward vertically
      d(scrollable=True).scroll.vert.backward()
      # scroll to beginning horizontally
      d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)
      # scroll to end vertically
      d(scrollable=True).scroll.toEnd()
      # scroll forward vertically until specific ui object appears
      d(scrollable=True).scroll.to(text="Security")
   ```
## 十九 Watcher
   #### 当selector找不到匹配项时，您可以注册watchers 以执行某些操作。
   + 注册watchers
      - 当selector找不到匹配项时，uiautomator2将运行所有注册的watcher。
   + 条件匹配时单击目标
      ```
         d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .click(text="Force Close")
         # d.watcher(name) ## creates a new named watcher.
         #  .when(condition)  ## the UiSelector condition(条件) of the watcher.
         #  .click(target)  ## 对目标UiSelector执行单击操作
      ```
   + 关于点击还有一个技巧。您可以使用不带参数的click。
      ```
         d.watcher("ALERT").when(text="OK").click()
         # Same as
         d.watcher("ALERT").when(text="OK").click(text="OK")
      ```
   + Press key when a condition becomes true
      ```
         d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .press("back", "home")
         # d.watcher(name) ## creates a new named watcher.
         #  .when(condition)  ## the UiSelector condition of the watcher.
         #  .press(<keyname>, ..., <keyname>.()  ## 按顺序依次按键
      ```
   + 检查命名的watcher是否被触发
      ```
         d.watcher("watcher_name").triggered
         # 在指定的watcher触发的情况下为true，否则为false
      ```
   + 删除已命名的watcher<br>
      `d.watcher("watcher_name").remove()`
   + 列出所有watcher<br>
      `d.watchers`
   + 检查是否有任何条件触发的watcher
      ```
      d.watchers.triggered
      #  true in case of any watcher triggered
      ```
   + 重置reset所有触发的watcher
      ```
      # reset all triggered watchers, after that, d.watchers.triggered will be false.
      d.watchers.reset()
      ```
   + 强制运行所有watcher<br>
      `d.watchers.run()`
   + 页面更新时运行所有watcher。 通常可以用来自动点击权限确认框，或者自动安装
      ```
         d.watcher("OK").when(text="OK").click(text="OK")
         # enable auto trigger watchers
         d.watchers.watched = True
         
         # disable auto trigger watchers
         d.watchers.watched = False
         
         # get current trigger watchers status
         assert d.watchers.watched == False
      ```
## 二十 全局设置
   ```
      # set delay 1.5s after each UI click and click
      d.click_post_delay = 1.5 # default no delay
      
      # set default element wait timeout (seconds)
      d.wait_timeout = 30.0 # default 20.0
   ```
   #### UiAutomator中的超时设置(隐藏方法)
   ```
      d.jsonrpc.getConfigurator()
      d.jsonrpc.setConfigurator({"waitForIdleTimeout": 100})
   ```
## 二十一 输入法
   #### 这种方法通常用于不知道控件的情况下的输入。第一步需要切换输入法，然后发送ADB广播命令，具体使用方法如下
   ```
      d.set_fastinput_ime(True) # 切换成FastInputIME输入法
      d.send_keys("你好123abcEFG") # adb广播输入
      d.clear_text() # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
      d.set_fastinput_ime(False) # 切换成正常的输入法
   ```

## 二十二 Toast
   + 在手机的屏幕上显示Toast
      - `d.toast.show("Hello world")`
      - `d.toast.show("Hello world", 1.0) # 显示 1.0s, 默认 1.0s`
   + 获取 Toast
      ```
         # [Args]
         # 5.0: max wait timeout. Default 10.0
         # 10.0: cache time. return cache toast if already toast already show up in recent 10 seconds. Default 10.0 (Maybe change in the furture)
         # "default message": return if no toast finally get. Default None
         d.toast.get_message(5.0, 10.0, "default message")
         
         # common usage
         assert "Short message" in d.toast.get_message(5.0, default="")
         
         # clear cached toast
         d.toast.reset()
         # Now d.toast.get_message(0) is None
      ```
## 二十三 XPath
   ```
      # wait exists 10s
      d.xpath("//android.widget.TextView").wait(10.0)
      # find and click
      d.xpath("//*[@content-desc='分享']").click()
      # get all text-view text, attrib and center point
      for elem in d.xpath("//android.widget.TextView").all():
         print("Text:", elem.text)
         # Dictionary eg: 
         # {'index': '1', 'text': '999+', 'resource-id': 'com.netease.cloudmusic:id/qb', 'package': 'com.netease.cloudmusic', 'content-desc': '', 'checkable': 'false', 'checked': 'false', 'clickable': 'false', 'enabled': 'true', 'focusable': 'false', 'focused': 'false','scrollable': 'false', 'long-clickable': 'false', 'password': 'false', 'selected': 'false', 'visible-to-user': 'true', 'bounds': '[661,1444][718,1478]'}
         print("Attrib:", elem.attrib)
         # Coordinate eg: (100, 200)
         print("Position:", elem.center())
   ```
