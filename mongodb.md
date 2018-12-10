成功启动MongoDB后，再打开一个命令行窗口输入mongo，就可以进行数据库的一些操作。<br>
<br>
输入help可以看到基本操作命令：<br>
<br>
show dbs:显示数据库列表  show collections：显示当前数据库中的集合（类似关系数据库中的表）  show users：显示用户<br>
<br>
use <db name>：切换当前数据库，这和MS-SQL里面的意思一样  db.help()：显示数据库操作命令，里面有很多的命令  db.foo.help()：显示集合操作命令，同样有很多的命令，foo指的是当前数据库下，一个叫foo的集合，并非真正意义上的命令  db.foo.find()：对于当前数据库中的foo集合进行数据查找（由于没有条件，会列出所有数据）  db.foo.find( { a : 1 } )：对于当前数据库中的foo集合进行查找，条件是数据中有一个属性叫a，且a的值为1<br>
<br>
MongoDB没有创建数据库的命令，但有类似的命令。<br>
<br>
如：如果你想创建一个“myTest”的数据库，先运行use myTest命令，之后就做一些操作（如：db.createCollection('user')）,这样就可以创建一个名叫“myTest”的数据库。<br>
<br>
数据库常用命令<br>
<br>
1、Help查看命令提示<br>
<br>
 help<br>
<br>
  db.help();<br>
<br>
  db.yourColl.help();<br>
<br>
  db.youColl.find().help();<br>
<br>
  rs.help();<br>
<br>
2、切换/创建数据库<br>
<br>
 use yourDB;  当创建一个集合(table)的时候会自动创建当前数据库<br>
<br>
3、查询所有数据库<br>
<br>
 show dbs;<br>
<br>
4、删除当前使用数据库<br>
<br>
 db.dropDatabase();<br>
<br>
5、从指定主机上克隆数据库<br>
<br>
 db.cloneDatabase(“127.0.0.1”); 将指定机器上的数据库的数据克隆到当前数据库<br>
<br>
6、从指定的机器上复制指定数据库数据到某个数据库<br>
<br>
 db.copyDatabase("mydb", "temp", "127.0.0.1");将本机的mydb的数据复制到temp数据库中<br>
<br>
7、修复当前数据库<br>
<br>
 db.repairDatabase();<br>
<br>
8、查看当前使用的数据库<br>
<br>
 db.getName();<br>
<br>
 db; db和getName方法是一样的效果，都可以查询当前使用的数据库<br>
<br>
9、显示当前db状态<br>
<br>
 db.stats();<br>
<br>
10、当前db版本<br>
<br>
 db.version();<br>
<br>
11、查看当前db的链接机器地址<br>
<br>
 db.getMongo();<br>
<br>
Collection聚集集合<br>
<br>
1、创建一个聚集集合（table）<br>
<br>
 db.createCollection(“collName”, {size: 20, capped: 5, max: 100});<br>
<br>
2、得到指定名称的聚集集合（table）<br>
<br>
 db.getCollection("account");<br>
<br>
3、得到当前db的所有聚集集合<br>
<br>
 db.getCollectionNames();<br>
<br>
4、显示当前db所有聚集索引的状态<br>
<br>
 db.printCollectionStats();<br>
<br>
 用户相关<br>
<br>
1、添加一个用户<br>
<br>
 db.addUser("name");<br>
<br>
 db.addUser("userName", "pwd123", true); 添加用户、设置密码、是否只读<br>
<br>
2、数据库认证、安全模式<br>
<br>
 db.auth("userName", "123123");<br>
<br>
3、显示当前所有用户<br>
<br>
 show users;<br>
<br>
4、删除用户<br>
<br>
 db.removeUser("userName");<br>
<br>
其他<br>
1、查询之前的错误信息<br>
 db.getPrevError();<br>
2、清除错误记录<br>
 db.resetError();<br>
 <br>
查看聚集集合基本信息<br>
1、查看帮助  db.yourColl.help();<br>
2、查询当前集合的数据条数  db.yourColl.count();<br>
3、查看数据空间大小 db.userInfo.dataSize();<br>
4、得到当前聚集集合所在的db db.userInfo.getDB();<br>
5、得到当前聚集的状态 db.userInfo.stats();<br>
6、得到聚集集合总大小 db.userInfo.totalSize();<br>
7、聚集集合储存空间大小 db.userInfo.storageSize();<br>
8、Shard版本信息  db.userInfo.getShardVersion()<br>
9、聚集集合重命名 db.userInfo.renameCollection("users"); 将userInfo重命名为users<br>
10、删除当前聚集集合 db.userInfo.drop();<br>
聚集集合查询<br>
<br>
1、查询所有记录<br>
db.userInfo.find();<br>
相当于：select* from userInfo;<br>
默认每页显示20条记录，当显示不下的情况下，可以用it迭代命令查询下一页数据。注意：键入it命令不能带“；”<br>
但是你可以设置每页显示数据的大小，用DBQuery.shellBatchSize= 50;这样每页就显示50条记录了。<br>
 <br>
2、查询去掉后的当前聚集集合中的某列的重复数据<br>
db.userInfo.distinct("name");<br>
会过滤掉name中的相同数据<br>
相当于：select distict name from userInfo;<br>
 <br>
3、查询age = 22的记录<br>
db.userInfo.find({"age": 22});<br>
相当于： select * from userInfo where age = 22;<br>
 <br>
4、查询age > 22的记录<br>
db.userInfo.find({age: {$gt: 22}});<br>
相当于：select * from userInfo where age >22;<br>
 <br>
5、查询age < 22的记录<br>
db.userInfo.find({age: {$lt: 22}});<br>
相当于：select * from userInfo where age <22;<br>
 <br>
6、查询age >= 25的记录<br>
db.userInfo.find({age: {$gte: 25}});<br>
相当于：select * from userInfo where age >= 25;<br>
 <br>
7、查询age <= 25的记录<br>
db.userInfo.find({age: {$lte: 25}});<br>
 <br>
8、查询age >= 23 并且 age <= 26<br>
db.userInfo.find({age: {$gte: 23, $lte: 26}});<br>
 <br>
9、查询name中包含 mongo的数据<br>
db.userInfo.find({name: /mongo/});<br>
//相当于%%<br>
select * from userInfo where name like ‘%mongo%’;<br>
 <br>
10、查询name中以mongo开头的<br>
db.userInfo.find({name: /^mongo/});<br>
select * from userInfo where name like ‘mongo%’;<br>
 <br>
11、查询指定列name、age数据<br>
db.userInfo.find({}, {name: 1, age: 1});<br>
相当于：select name, age from userInfo;<br>
当然name也可以用true或false,当用ture的情况下河name:1效果一样，如果用false就是排除name，显示name以外的列信息。<br>
 <br>
12、查询指定列name、age数据, age > 25<br>
db.userInfo.find({age: {$gt: 25}}, {name: 1, age: 1});<br>
相当于：select name, age from userInfo where age >25;<br>
 <br>
13、按照年龄排序<br>
升序：db.userInfo.find().sort({age: 1});<br>
降序：db.userInfo.find().sort({age: -1});<br>
 <br>
14、查询name = zhangsan, age = 22的数据<br>
db.userInfo.find({name: 'zhangsan', age: 22});<br>
相当于：select * from userInfo where name = ‘zhangsan’ and age = ‘22’;<br>
 <br>
15、查询前5条数据<br>
db.userInfo.find().limit(5);<br>
相当于：selecttop 5 * from userInfo;<br>
 <br>
16、查询10条以后的数据<br>
db.userInfo.find().skip(10);<br>
相当于：select * from userInfo where id not in (<br>
selecttop 10 * from userInfo<br>
);<br>
 <br>
17、查询在5-10之间的数据<br>
db.userInfo.find().limit(10).skip(5);<br>
可用于分页，limit是pageSize，skip是第几页*pageSize<br>
 <br>
18、or与 查询<br>
db.userInfo.find({$or: [{age: 22}, {age: 25}]});<br>
相当于：select * from userInfo where age = 22 or age = 25;<br>
 <br>
19、查询第一条数据<br>
db.userInfo.findOne();<br>
相当于：selecttop 1 * from userInfo;<br>
db.userInfo.find().limit(1);<br>
 <br>
20、查询某个结果集的记录条数<br>
db.userInfo.find({age: {$gte: 25}}).count();<br>
相当于：select count(*) from userInfo where age >= 20;<br>
 <br>
21、按照某列进行排序<br>
db.userInfo.find({sex: {$exists: true}}).count();<br>
相当于：select count(sex) from userInfo;<br>
索引<br>
<br>
1、创建索引<br>
db.userInfo.ensureIndex({name: 1});<br>
db.userInfo.ensureIndex({name: 1, ts: -1});<br>
 <br>
2、查询当前聚集集合所有索引<br>
db.userInfo.getIndexes();<br>
 <br>
3、查看总索引记录大小<br>
db.userInfo.totalIndexSize();<br>
 <br>
4、读取当前集合的所有index信息<br>
db.users.reIndex();<br>
 <br>
5、删除指定索引<br>
db.users.dropIndex("name_1");<br>
 <br>
6、删除所有索引索引<br>
db.users.dropIndexes();<br>
 修改、添加、删除集合数据<br>
<br>
1、添加<br>
db.users.save({name: ‘zhangsan’, age: 25, sex: true});<br>
添加的数据的数据列，没有固定，根据添加的数据为准<br>
 <br>
2、修改<br>
db.users.update({age: 25}, {$set: {name: 'changeName'}}, false, true);<br>
相当于：update users set name = ‘changeName’ where age = 25;<br>
 <br>
db.users.update({name: 'Lisi'}, {$inc: {age: 50}}, false, true);<br>
相当于：update users set age = age + 50 where name = ‘Lisi’;<br>
 <br>
db.users.update({name: 'Lisi'}, {$inc: {age: 50}, $set: {name: 'hoho'}}, false, true);<br>
相当于：update users set age = age + 50, name = ‘hoho’ where name = ‘Lisi’;<br>
 <br>
3、删除<br>
db.users.remove({age: 132});<br>
 <br>
4、查询修改删除<br>
db.users.findAndModify({<br>
    query: {age: {$gte: 25}}, <br>
    sort: {age: -1}, <br>
    update: {$set: {name: 'a2'}, $inc: {age: 2}},<br>
    remove: true<br>
});<br>
 <br>
db.runCommand({ findandmodify : "users", <br>
    query: {age: {$gte: 25}}, <br>
    sort: {age: -1}, <br>
    update: {$set: {name: 'a2'}, $inc: {age: 2}},<br>
    remove: true<br>
});<br>
update 或 remove 其中一个是必须的参数; 其他参数可选。<br>
<br>
参数<br>
<br>
详解<br>
<br>
默认值<br>
<br>
query<br>
<br>
查询过滤条件<br>
<br>
{}<br>
<br>
sort<br>
<br>
如果多个文档符合查询过滤条件，将以该参数指定的排列方式选择出排在首位的对象，该对象将被操作<br>
<br>
{}<br>
<br>
remove<br>
<br>
若为true，被选中对象将在返回前被删除<br>
<br>
N/A<br>
<br>
update<br>
<br>
一个 修改器对象<br>
<br>
N/A<br>
<br>
new<br>
<br>
若为true，将返回修改后的对象而不是原始对象。在删除操作中，该参数被忽略。<br>
<br>
false<br>
<br>
fields<br>
<br>
参见Retrieving a Subset of Fields (1.5.0+)<br>
<br>
All fields<br>
<br>
upsert<br>
<br>
创建新对象若查询结果为空。 示例 (1.5.4+)<br>
<br>
false<br>
<br>
语句块操作<br>
<br>
1、简单Hello World<br>
print("Hello World!");<br>
这种写法调用了print函数，和直接写入"Hello World!"的效果是一样的；<br>
 <br>
2、将一个对象转换成json<br>
tojson(new Object());<br>
tojson(new Object('a'));<br>
 <br>
3、循环添加数据<br>
> for (var i = 0; i < 30; i++) {<br>
... db.users.save({name: "u_" + i, age: 22 + i, sex: i % 2});<br>
... };<br>
这样就循环添加了30条数据，同样也可以省略括号的写法<br>
> for (var i = 0; i < 30; i++) db.users.save({name: "u_" + i, age: 22 + i, sex: i % 2});<br>
也是可以的，当你用db.users.find()查询的时候，显示多条数据而无法一页显示的情况下，可以用it查看下一页的信息；<br>
 <br>
4、find 游标查询<br>
>var cursor = db.users.find();<br>
> while (cursor.hasNext()) { <br>
    printjson(cursor.next()); <br>
}<br>
这样就查询所有的users信息，同样可以这样写<br>
var cursor = db.users.find();<br>
while (cursor.hasNext()) { printjson(cursor.next); }<br>
同样可以省略{}号<br>
 <br>
5、forEach迭代循环<br>
db.users.find().forEach(printjson);<br>
forEach中必须传递一个函数来处理每条迭代的数据信息<br>
 <br>
6、将find游标当数组处理<br>
var cursor = db.users.find();<br>
cursor[4];<br>
取得下标索引为4的那条数据<br>
既然可以当做数组处理，那么就可以获得它的长度：cursor.length();或者cursor.count();<br>
那样我们也可以用循环显示数据<br>
for (var i = 0, len = c.length(); i < len; i++) printjson(c[i]);<br>
 <br>
7、将find游标转换成数组<br>
> var arr = db.users.find().toArray();<br>
> printjson(arr[2]);<br>
用toArray方法将其转换为数组<br>
 <br>
8、定制我们自己的查询结果<br>
只显示age <= 28的并且只显示age这列数据<br>
db.users.find({age: {$lte: 28}}, {age: 1}).forEach(printjson);<br>
db.users.find({age: {$lte: 28}}, {age: true}).forEach(printjson);<br>
排除age的列<br>
db.users.find({age: {$lte: 28}}, {age: false}).forEach(printjson);<br>
 <br>
9、forEach传递函数显示信息<br>
db.things.find({x:4}).forEach(function(x) {print(tojson(x));});<br>