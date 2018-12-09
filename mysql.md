#mysql
Windows服务<br>
启动MySQL<br>
* netstartmysql<br>
创建Windows服务<br>
* sccreatemysqlbinPath=mysqld_bin_path(注意：等号与值之间有空格)<br>
连接与断开服务器<br>
mysql-h地址-P端口-u用户名-p密码<br>
SHOWPROCESSLIST显示哪些线程正在运行<br>
SHOWVARIABLES显示系统变量信息<br>
数据库操作<br>
查看当前数据库<br>
* SELECTDATABASE();<br>
显示当前时间、用户名、数据库版本<br>
* SELECTnow(),user(),version();<br>
创建库<br>
* CREATEDATABASE[IFNOTEXISTS]数据库名数据库选项<br>
* 数据库选项：<br>
* * CHARACTERSETcharset_name<br>
* * COLLATEcollation_name<br>
查看已有库<br>
* SHOWDATABASES[LIKE'PATTERN']<br>
查看当前库信息<br>
* SHOWCREATEDATABASE数据库名<br>
修改库的选项信息<br>
* ALTERDATABASE库名选项信息<br>
删除库<br>
* DROPDATABASE[IFEXISTS]数据库名<br>
* * 同时删除该数据库相关的目录及其目录内容<br>
表的操作<br>
创建表<br>
* CREATE[TEMPORARY]TABLE[IFNOTEXISTS][库名.]表名(表的结构定义)[表选项]<br>
* * 每个字段必须有数据类型<br>
* * 最后一个字段后不能有逗号<br>
* * TEMPORARY临时表，会话结束时表自动消失<br>
* * 对于字段的定义：<br>
* * * 字段名数据类型[NOTNULL|NULL][DEFAULTdefault_value][AUTO_INCREMENT][UNIQUE[KEY]|[PRIMARY]KEY][COMMENT'string']<br>
表选项<br>
* 字符集<br>
* * CHARSET=charset_name<br>
* * 如果表没有设定，则使用数据库字符集<br>
* 存储引擎<br>
* * ENGINE=engine_name<br>
* * 表在管理数据时采用的不同的数据结构，结构不同会导致处理方式、提供的特性操作等不同<br>
* * 常见的引擎：InnoDBMyISAMMemoryHeapBDBMergeExampleCSVMaxDBArchive<br>
* * 不同的引擎在保存表的结构和数据时采用不同的方式<br>
* * MyISAM表文件含义：.frm表定义，.MYD表数据，.MYI表索引<br>
* * InnoDB表文件含义：.frm表定义，表空间数据和日志文件<br>
* * SHOWENGINES显示存储引擎的状态信息<br>
* * SHOWENGINE引擎名{LOGS|STATUS}显示存储引擎的日志或状态信息<br>
* 自增起始数<br>
* * AUTO_INCREMENT=行数<br>
* 数据文件目录<br>
* * DATADIRECTORY='目录'<br>
* 索引文件目录<br>
* * INDEXDIRECTORY='目录'<br>
* 表注释<br>
* * COMMENT='string'<br>
* 分区选项<br>
* * PARTITIONBY...(详细见手册)<br>
查看所有表<br>
* SHOWTABLES[LIKE'pattern']<br>
* SHOWTABLESFROM表名<br>
查看表机构<br>
* SHOWCREATETABLE表名（信息更详细）<br>
* DESC表名DESCRIBE表名EXPLAIN表名SHOWCOLUMNSFROM表名[LIKE'PATTERN']<br>
* SHOWTABLESTATUS[FROMdb_name][LIKE'pattern']<br>
修改表<br>
* 修改表本身的选项<br>
* * ALTERTABLE表名表的选项<br>
* * eg:ALTERTABLE表名ENGINE=MYISAM;<br>
* 对表进行重命名<br>
* * RENAMETABLE原表名TO新表名<br>
* * RENAMETABLE原表名TO库名.表名（可将表移动到另一个数据库）<br>
* * RENAME可以交换两个表名<br>
* 修改表的字段机构（13.1.2.ALTERTABLE语法）<br>
* * ALTERTABLE表名操作名<br>
* * 操作名<br>
* * * ADD[COLUMN]字段定义* * 增加字段<br>
* * * * AFTER字段名* * 表示增加在该字段名后面<br>
* * * * FIRST* * * * 表示增加在第一个<br>
* * * ADDPRIMARYKEY(字段名)* 创建主键<br>
* * * ADDUNIQUE[索引名](字段名)创建唯一索引<br>
* * * ADDINDEX[索引名](字段名)创建普通索引<br>
* * * DROP[COLUMN]字段名* 删除字段<br>
* * * MODIFY[COLUMN]字段名字段属性* 支持对字段属性进行修改，不能修改字段名(所有原有属性也需写上)<br>
* * * CHANGE[COLUMN]原字段名新字段名字段属性* 支持对字段名修改<br>
* * * DROPPRIMARYKEY* 删除主键(删除主键前需删除其AUTO_INCREMENT属性)<br>
* * * DROPINDEX索引名删除索引<br>
* * * DROPFOREIGNKEY外键* 删除外键<br>
删除表<br>
* DROPTABLE[IFEXISTS]表名...<br>
清空表数据<br>
* TRUNCATE[TABLE]表名<br>
复制表结构<br>
* CREATETABLE表名LIKE要复制的表名<br>
复制表结构和数据<br>
* CREATETABLE表名[AS]SELECTFROM要复制的表名<br>
检查表是否有错误<br>
* CHECKTABLEtbl_name[,tbl_name]...[option]...<br>
优化表<br>
* OPTIMIZE[LOCAL|NO_WRITE_TO_BINLOG]TABLEtbl_name[,tbl_name]...<br>
修复表<br>
* REPAIR[LOCAL|NO_WRITE_TO_BINLOG]TABLEtbl_name[,tbl_name]...[QUICK][EXTENDED][USE_FRM]<br>
分析表<br>
* ANALYZE[LOCAL|NO_WRITE_TO_BINLOG]TABLEtbl_name[,tbl_name]...<br>
数据操作<br>
增<br>
* INSERT[INTO]表名[(字段列表)]VALUES(值列表)[,(值列表),...]<br>
* * 如果要插入的值列表包含所有字段并且顺序一致，则可以省略字段列表。<br>
* * 可同时插入多条数据记录！<br>
* * REPLACE与INSERT完全一样，可互换。<br>
* INSERT[INTO]表名SET字段名=值[,字段名=值,...]<br>
查<br>
* SELECT字段列表FROM表名[其他子句]<br>
* * 可来自多个表的多个字段<br>
* * 其他子句可以不使用<br>
* * 字段列表可以用代替，表示所有字段<br>
删<br>
* DELETEFROM表名[删除条件子句]<br>
* * 没有条件子句，则会删除全部<br>
改<br>
* UPDATE表名SET字段名=新值[,字段名=新值][更新条件]<br>
字符集编码<br>
MySQL、数据库、表、字段均可设置编码<br>
数据编码与客户端编码不需一致<br>
SHOWVARIABLESLIKE'character_set_%'* 查看所有字符集编码项<br>
* character_set_client* * 客户端向服务器发送数据时使用的编码<br>
* character_set_results* 服务器端将结果返回给客户端所使用的编码<br>
* character_set_connection* 连接层编码<br>
SET变量名=变量值<br>
* SETcharacter_set_client=gbk;<br>
* SETcharacter_set_results=gbk;<br>
* SETcharacter_set_connection=gbk;<br>
SETNAMESGBK;相当于完成以上三个设置<br>
校对集<br>
* 校对集用以排序<br>
* SHOWCHARACTERSET[LIKE'pattern']SHOWCHARSET[LIKE'pattern']查看所有字符集<br>
* SHOWCOLLATION[LIKE'pattern']* 查看所有校对集<br>
* CHARSET字符集编码* 设置字符集编码<br>
* COLLATE校对集编码* 设置校对集编码<br>
数据类型（列类型）<br>
1.数值类型<br>
a.整型<br>
* 类型* * 字节* 范围（有符号位）<br>
* tinyint* 1字节* -128~127* 无符号位：0~255<br>
* smallint* 2字节* -32768~32767<br>
* mediumint3字节* -8388608~8388607<br>
* int* * 4字节<br>
* bigint* 8字节<br>
* int(M)M表示总位数<br>
* -默认存在符号位，unsigned属性修改<br>
* -显示宽度，如果某个数不够定义字段时设置的位数，则前面以0补填，zerofill属性修改<br>
* * 例：int(5)插入一个数'123'，补填后为'00123'<br>
* -在满足要求的情况下，越小越好。<br>
* -1表示bool值真，0表示bool值假。MySQL没有布尔类型，通过整型0和1表示。常用tinyint(1)表示布尔型。<br>
b.浮点型<br>
* 类型* * * 字节* 范围<br>
* float(单精度)* 4字节<br>
* double(双精度)* 8字节<br>
* 浮点型既支持符号位unsigned属性，也支持显示宽度zerofill属性。<br>
* * 不同于整型，前后均会补填0.<br>
* 定义浮点型时，需指定总位数和小数位数。<br>
* * float(M,D)* double(M,D)<br>
* * M表示总位数，D表示小数位数。<br>
* * M和D的大小会决定浮点数的范围。不同于整型的固定范围。<br>
* * M既表示总位数（不包括小数点和正负号），也表示显示宽度（所有显示符号均包括）。<br>
* * 支持科学计数法表示。<br>
* * 浮点数表示近似值。<br>
c.定点数<br>
* decimal可变长度<br>
* decimal(M,D)M也表示总位数，D表示小数位数。<br>
* 保存一个精确的数值，不会发生数据的改变，不同于浮点数的四舍五入。<br>
* 将浮点数转换为字符串来保存，每9位数字保存为4个字节。<br>
2.字符串类型<br>
a.char,varchar<br>
* char* 定长字符串，速度快，但浪费空间<br>
* varchar变长字符串，速度慢，但节省空间<br>
* M表示能存储的最大长度，此长度是字符数，非字节数。<br>
* 不同的编码，所占用的空间不同。<br>
* char,最多255个字符，与编码无关。<br>
* varchar,最多65535字符，与编码有关。<br>
* 一条有效记录最大不能超过65535个字节。<br>
* * utf8最大为21844个字符，gbk最大为32766个字符，latin1最大为65532个字符<br>
* varchar是变长的，需要利用存储空间保存varchar的长度，如果数据小于255个字节，则采用一个字节来保存长度，反之需要两个字节来保存。<br>
* varchar的最大有效长度由最大行大小和使用的字符集确定。<br>
* 最大有效长度是65532字节，因为在varchar存字符串时，第一个字节是空的，不存在任何数据，然后还需两个字节来存放字符串的长度，所以有效长度是64432-1-2=65532字节。<br>
* 例：若一个表定义为CREATETABLEtb(c1int,c2char(30),c3varchar(N))charset=utf8;问N的最大值是多少？答：(65535-1-2-4-303)3<br>
b.blob,text<br>
* blob二进制字符串（字节字符串）<br>
* * tinyblob,blob,mediumblob,longblob<br>
* text非二进制字符串（字符字符串）<br>
* * tinytext,text,mediumtext,longtext<br>
* text在定义时，不需要定义长度，也不会计算总长度。<br>
* text类型在定义时，不可给default值<br>
c.binary,varbinary<br>
* 类似于char和varchar，用于保存二进制字符串，也就是保存字节字符串而非字符字符串。<br>
* char,varchar,text对应binary,varbinary,blob.<br>
3.日期时间类型<br>
* 一般用整型保存时间戳，因为PHP可以很方便的将时间戳进行格式化。<br>
* datetime* 8字节* 日期及时间* 1000-01-0100:00:00到9999-12-3123:59:59<br>
* date* * 3字节* 日期* * 1000-01-01到9999-12-31<br>
* timestamp4字节* 时间戳* * 19700101000000到2038-01-1903:14:07<br>
* time* * 3字节* 时间* * -838:59:59到838:59:59<br>
* year* * 1字节* 年份* * 1901-2155<br>
datetime* YYYY-MM-DDhh:mm:ss<br>
timestampYY-MM-DDhh:mm:ss<br>
* * * YYYYMMDDhhmmss<br>
* * * YYMMDDhhmmss<br>
* * * YYYYMMDDhhmmss<br>
* * * YYMMDDhhmmss<br>
date* * YYYY-MM-DD<br>
* * * YY-MM-DD<br>
* * * YYYYMMDD<br>
* * * YYMMDD<br>
* * * YYYYMMDD<br>
* * * YYMMDD<br>
time* * hh:mm:ss<br>
* * * hhmmss<br>
* * * hhmmss<br>
year* * YYYY<br>
* * * YY<br>
* * * YYYY<br>
* * * YY<br>
4.枚举和集合<br>
枚举(enum)<br>
enum(val1,val2,val3...)<br>
* 在已知的值中进行单选。最大数量为65535.<br>
* 枚举值在保存时，以2个字节的整型(smallint)保存。每个枚举值，按保存的位置顺序，从1开始逐一递增。<br>
* 表现为字符串类型，存储却是整型。<br>
* NULL值的索引是NULL。<br>
* 空字符串错误值的索引值是0。<br>
集合（set）<br>
set(val1,val2,val3...)<br>
* createtabletab(genderset('男','女','无'));<br>
* insertintotabvalues('男,女');<br>
* 最多可以有64个不同的成员。以bigint存储，共8个字节。采取位运算的形式。<br>
* 当创建表时，SET成员值的尾部空格将自动被删除。<br>
选择类型<br>
PHP角度<br>
1.功能满足<br>
2.存储空间尽量小，处理效率更高<br>
3.考虑兼容问题<br>
IP存储<br>
1.只需存储，可用字符串<br>
2.如果需计算，查找等，可存储为4个字节的无符号int，即unsigned<br>
* 1)PHP函数转换<br>
* * ip2long可转换为整型，但会出现携带符号问题。需格式化为无符号的整型。<br>
* * 利用sprintf函数格式化字符串<br>
* * sprintf("%u",ip2long('192.168.3.134'));<br>
* * 然后用long2ip将整型转回IP字符串<br>
* 2)MySQL函数转换(无符号整型，UNSIGNED)<br>
* * INET_ATON('127.0.0.1')将IP转为整型<br>
* * INET_NTOA(2130706433)将整型转为IP<br>
列属性（列约束）<br>
1.PRIMARY主键<br>
* -能唯一标识记录的字段，可以作为主键。<br>
* -一个表只能有一个主键。<br>
* -主键具有唯一性。<br>
* -声明字段时，用primarykey标识。<br>
* * 也可以在字段列表之后声明<br>
* * * 例：createtabletab(idint,stuvarchar(10),primarykey(id));<br>
* -主键字段的值不能为null。<br>
* -主键可以由多个字段共同组成。此时需要在字段列表后声明的方法。<br>
* * 例：createtabletab(idint,stuvarchar(10),ageint,primarykey(stu,age));<br>
2.UNIQUE唯一索引（唯一约束）<br>
* 使得某字段的值也不能重复。<br>
3.NULL约束<br>
* null不是数据类型，是列的一个属性。<br>
* 表示当前列是否可以为null，表示什么都没有。<br>
* null,允许为空。默认。<br>
* notnull,不允许为空。<br>
* insertintotabvalues(null,'val');<br>
* * 此时表示将第一个字段的值设为null,取决于该字段是否允许为null<br>
4.DEFAULT默认值属性<br>
* 当前字段的默认值。<br>
* insertintotabvalues(default,'val');* 此时表示强制使用默认值。<br>
* createtabletab(add_timetimestampdefaultcurrent_timestamp);<br>
* * 表示将当前时间的时间戳设为默认值。<br>
* * current_date,current_time<br>
5.AUTO_INCREMENT自动增长约束<br>
* 自动增长必须为索引（主键或unique）<br>
* 只能存在一个字段为自动增长。<br>
* 默认为1开始自动增长。可以通过表属性auto_increment=x进行设置，或altertabletblauto_increment=x;<br>
6.COMMENT注释<br>
* 例：createtabletab(idint)comment'注释内容';<br>
7.FOREIGNKEY外键约束<br>
* 用于限制主表与从表数据完整性。<br>
* altertablet1addconstraint`t1_t2_fk`foreignkey(t1_id)referencest2(id);<br>
* * 将表t1的t1_id外键关联到表t2的id字段。<br>
* * 每个外键都有一个名字，可以通过constraint指定<br>
* 存在外键的表，称之为从表（子表），外键指向的表，称之为主表（父表）。<br>
* 作用：保持数据一致性，完整性，主要目的是控制存储在外键表（从表）中的数据。<br>
* MySQL中，可以对InnoDB引擎使用外键约束：<br>
* 语法：<br>
* foreignkey(外键字段）references主表名(关联字段)[主表记录删除时的动作][主表记录更新时的动作]<br>
* 此时需要检测一个从表的外键需要约束为主表的已存在的值。外键在没有关联的情况下，可以设置为null.前提是该外键列，没有notnull。<br>
* 可以不指定主表记录更改或更新时的动作，那么此时主表的操作被拒绝。<br>
* 如果指定了onupdate或ondelete：在删除或更新时，有如下几个操作可以选择：<br>
* 1.cascade，级联操作。主表数据被更新（主键值更新），从表也被更新（外键值更新）。主表记录被删除，从表相关记录也被删除。<br>
* 2.setnull，设置为null。主表数据被更新（主键值更新），从表的外键被设置为null。主表记录被删除，从表相关记录外键被设置成null。但注意，要求该外键列，没有notnull属性约束。<br>
* 3.restrict，拒绝父表删除和更新。<br>
* 注意，外键只被InnoDB存储引擎所支持。其他引擎是不支持的。<br>
建表规范<br>
* NormalFormat,NF<br>
* * -每个表保存一个实体信息<br>
* * -每个具有一个ID字段作为主键<br>
* * -ID主键+原子表<br>
* 1NF,第一范式<br>
* * 字段不能再分，就满足第一范式。<br>
* 2NF,第二范式<br>
* * 满足第一范式的前提下，不能出现部分依赖。<br>
* * 消除符合主键就可以避免部分依赖。增加单列关键字。<br>
* 3NF,第三范式<br>
* * 满足第二范式的前提下，不能出现传递依赖。<br>
* * 某个字段依赖于主键，而有其他字段依赖于该字段。这就是传递依赖。<br>
* * 将一个实体信息的数据放在一个表内实现。<br>
SELECT<br>
SELECT[ALL|DISTINCT]select_exprFROM-* WHERE-* GROUPBY[合计函数]-* HAVING-* ORDERBY-* LIMIT<br>
a.select_expr<br>
* 可以用表示所有字段。<br>
* * selectfromtb;<br>
* 可以使用表达式（计算公式、函数调用、字段也是个表达式）<br>
* * selectstu,29+25,now()fromtb;<br>
* 可以为每个列使用别名。适用于简化列标识，避免多个列标识符重复。<br>
* * -使用as关键字，也可省略as.<br>
* * selectstu+10asadd10fromtb;<br>
b.FROM子句<br>
* 用于标识查询来源。<br>
* 可以为表起别名。使用as关键字。<br>
* * SELECTFROMtb1AStt,tb2ASbb;<br>
* from子句后，可以同时出现多个表。<br>
* * 多个表会横向叠加到一起，而数据会形成一个笛卡尔积。<br>
* * SELECTFROMtb1,tb2;<br>
* 向优化符提示如何选择索引<br>
* * USEINDEX、IGNOREINDEX、FORCEINDEX<br>
* * SELECTFROMtable1USEINDEX(key1,key2)WHEREkey1=1ANDkey2=2ANDkey3=3;<br>
* * SELECTFROMtable1IGNOREINDEX(key3)WHEREkey1=1ANDkey2=2ANDkey3=3;<br>
c.WHERE子句<br>
* 从from获得的数据源中进行筛选。<br>
* 整型1表示真，0表示假。<br>
* 表达式由运算符和运算数组成。<br>
* * 运算数：变量（字段）、值、函数返回值<br>
* * 运算符：<br>
* * * =,<=* ,<* ,!=,<=,<,* =,* ,!,&&,||,<br>
* * * in(not)null,(not)like,(not)in,(not)betweenand,is(not),and,or,not,xor<br>
* * * isisnot加上turefalseunknown，检验某个值的真假<br>
* * * <=* 与<* 功能相同，<=* 可用于null比较<br>
d.GROUPBY子句,分组子句<br>
* GROUPBY字段别名[排序方式]<br>
* 分组后会进行排序。升序：ASC，降序：DESC<br>
* 以下[合计函数]需配合GROUPBY使用：<br>
* count返回不同的非NULL值数目count()、count(字段)<br>
* sum求和<br>
* max求最大值<br>
* min求最小值<br>
* avg求平均值<br>
* group_concat返回带有来自一个组的连接的非NULL值的字符串结果。组内字符串连接。<br>
e.HAVING子句，条件子句<br>
* 与where功能、用法相同，执行时机不同。<br>
* where在开始时执行检测数据，对原数据进行过滤。<br>
* having对筛选出的结果再次进行过滤。<br>
* having字段必须是查询出来的，where字段必须是数据表存在的。<br>
* where不可以使用字段的别名，having可以。因为执行WHERE代码时，可能尚未确定列值。<br>
* where不可以使用合计函数。一般需用合计函数才会用having<br>
* SQL标准要求HAVING必须引用GROUPBY子句中的列或用于合计函数中的列。<br>
f.ORDERBY子句，排序子句<br>
* orderby排序字段别名排序方式[,排序字段别名排序方式]...<br>
* 升序：ASC，降序：DESC<br>
* 支持多个字段的排序。<br>
g.LIMIT子句，限制结果数量子句<br>
* 仅对处理好的结果进行数量限制。将处理好的结果的看作是一个集合，按照记录出现的顺序，索引从0开始。<br>
* limit起始位置,获取条数<br>
* 省略第一个参数，表示从索引0开始。limit获取条数<br>
h.DISTINCT,ALL选项<br>
* distinct去除重复记录<br>
* 默认为all,全部记录<br>
UNION<br>
* 将多个select查询的结果组合成一个结果集合。<br>
* SELECT...UNION[ALL|DISTINCT]SELECT...<br>
* 默认DISTINCT方式，即所有返回的行都是唯一的<br>
* 建议，对每个SELECT查询加上小括号包裹。<br>
* ORDERBY排序时，需加上LIMIT进行结合。<br>
* 需要各select查询的字段数量一样。<br>
* 每个select查询的字段列表(数量、类型)应一致，因为结果中的字段名以第一条select语句为准。<br>
子查询<br>
* -子查询需用括号包裹。<br>
from型<br>
* from后要求是一个表，必须给子查询结果取个别名。<br>
* -简化每个查询内的条件。<br>
* -from型需将结果生成一个临时表格，可用以原表的锁定的释放。<br>
* -子查询返回一个表，表型子查询。<br>
* selectfrom(selectfromtbwhereid* 0)assubfromwhereid* 1;<br>
where型<br>
* -子查询返回一个值，标量子查询。<br>
* -不需要给子查询取别名。<br>
* -where子查询内的表，不能直接用以更新。<br>
* selectfromtbwheremoney=(selectmax(money)fromtb);<br>
* 列子查询<br>
* * 如果子查询结果返回的是一列。<br>
* * 使用in或notin完成查询<br>
* * exists和notexists条件<br>
* * * 如果子查询返回数据，则返回1或0。常用于判断条件。<br>
* * * selectcolumn1fromt1whereexists(selectfromt2);<br>
* 行子查询<br>
* * 查询条件是一个行。<br>
* * selectfromt1where(id,gender)in(selectid,genderfromt2);<br>
* * 行构造符：(col1,col2,...)或ROW(col1,col2,...)<br>
* * 行构造符通常用于与对能返回两个或两个以上列的子查询进行比较。<br>
* 特殊运算符<br>
* !=all()* 相当于notin<br>
* =some()* 相当于in。any是some的别名<br>
* !=some()不等同于notin，不等于其中某一个。<br>
* all,some可以配合其他运算符一起使用。<br>
连接查询(join)<br>
* 将多个表的字段进行连接，可以指定连接条件。<br>
内连接(innerjoin)<br>
* -默认就是内连接，可省略inner。<br>
* -只有数据存在时才能发送连接。即连接结果不能出现空行。<br>
* on表示连接条件。其条件表达式与where类似。也可以省略条件（表示条件永远为真）<br>
* 也可用where表示连接条件。<br>
* 还有using,但需字段名相同。using(字段名)<br>
* 交叉连接crossjoin<br>
* * 即，没有条件的内连接。<br>
* * selectfromtb1crossjointb2;<br>
外连接(outerjoin)<br>
* -如果数据不存在，也会出现在连接结果中。<br>
* 左外连接leftjoin<br>
* * 如果数据不存在，左表记录会出现，而右表为null填充<br>
* 右外连接rightjoin<br>
* * 如果数据不存在，右表记录会出现，而左表为null填充<br>
自然连接(naturaljoin)<br>
* 自动判断连接条件完成连接。<br>
* 相当于省略了using，会自动查找相同字段名。<br>
* naturaljoin<br>
* naturalleftjoin<br>
* naturalrightjoin<br>
selectinfo.id,info.name,info.stu_num,extra_info.hobby,extra_info.sexfrominfo,extra_infowhereinfo.stu_num=extra_info.stu_id;<br>
导入导出<br>
selectintooutfile文件地址[控制格式]from表名;* 导出表数据<br>
loaddata[local]infile文件地址[replace|ignore]intotable表名[控制格式];导入数据<br>
* 生成的数据默认的分隔符是制表符<br>
* local未指定，则数据文件必须在服务器上<br>
* replace和ignore关键词控制对现有的唯一键记录的重复的处理<br>
控制格式<br>
fields控制字段格式<br>
默认：fieldsterminatedby'\t'enclosedby''escapedby'\\'<br>
* terminatedby'string'终止<br>
* enclosedby'char'* 包裹<br>
* escapedby'char'* * 转义<br>
* 示例：<br>
* * SELECTa,b,a+bINTOOUTFILE'tmpresult.text'<br>
* * FIELDSTERMINATEDBY','OPTIONALLYENCLOSEDBY'"'<br>
* * LINESTERMINATEDBY'\n'<br>
* * FROMtest_table;<br>
lines控制行格式<br>
默认：linesterminatedby'\n'<br>
* terminatedby'string'终止<br>
INSERT<br>
select语句获得的数据可以用insert插入。<br>
可以省略对列的指定，要求values()括号内，提供给了按照列顺序出现的所有字段的值。<br>
* 或者使用set语法。<br>
* INSERTINTOtbl_nameSETfield=value,...；<br>
可以一次性使用多个值，采用(),(),();的形式。<br>
* INSERTINTOtbl_nameVALUES(),(),();<br>
可以在列值指定时，使用表达式。<br>
* INSERTINTOtbl_nameVALUES(field_value,10+10,now());<br>
可以使用一个特殊值DEFAULT，表示该列使用默认值。<br>
* INSERTINTOtbl_nameVALUES(field_value,DEFAULT);<br>
可以通过一个查询的结果，作为需要插入的值。<br>
* INSERTINTOtbl_nameSELECT...;<br>
可以指定在插入的值出现主键（或唯一索引）冲突时，更新其他非主键列的信息。<br>
* INSERTINTOtbl_nameVALUESSETSELECTONDUPLICATEKEYUPDATE字段=值,…;<br>
DELETE<br>
DELETEFROMtbl_name[WHEREwhere_definition][ORDERBY...][LIMITrow_count]<br>
按照条件删除。where<br>
指定删除的最多记录数。limit<br>
可以通过排序条件删除。orderby+limit<br>
支持多表删除，使用类似连接语法。<br>
deletefrom需要删除数据多表1，表2using表连接操作条件。<br>
TRUNCATE<br>
TRUNCATE[TABLE]tbl_name<br>
清空数据<br>
删除重建表<br>
区别：<br>
1，truncate是删除表再创建，delete是逐条删除<br>
2，truncate重置auto_increment的值。而delete不会<br>
3，truncate不知道删除了几条，而delete知道。<br>
4，当被用于带分区的表时，truncate会保留分区<br>
备份与还原<br>
备份，将数据的结构与表内数据保存起来。<br>
利用mysqldump指令完成。<br>
导出<br>
mysqldump[options]db_name[tables]<br>
mysqldump[options]-databaseDB1[DB2DB3...]<br>
mysqldump[options]alldatabase<br>
1.导出一张表<br>
　　mysqldump-u用户名-p密码库名表名* 文件名(D:a.sql)<br>
2.导出多张表<br>
　　mysqldump-u用户名-p密码库名表1表2表3* 文件名(D:a.sql)<br>
3.导出所有表<br>
　　mysqldump-u用户名-p密码库名* 文件名(D:a.sql)<br>
4.导出一个库<br>
　　mysqldump-u用户名-p密码lock-all-tablesdatabase库名* 文件名(D:a.sql)<br>
可以-w携带WHERE条件<br>
导入<br>
1.在登录mysql的情况下：<br>
　　source备份文件<br>
2.在不登录的情况下<br>
　　mysql-u用户名-p密码库名<备份文件<br>
视图<br>
什么是视图：<br>
* 视图是一个虚拟表，其内容由查询定义。同真实的表一样，视图包含一系列带有名称的列和行数据。但是，视图并不在数据库中以存储的数据值集形式存在。行和列数据来自由定义视图的查询所引用的表，并且在引用视图时动态生成。<br>
* 视图具有表结构文件，但不存在数据文件。<br>
* 对其中所引用的基础表来说，视图的作用类似于筛选。定义视图的筛选可以来自当前或其它数据库的一个或多个表，或者其它视图。通过视图进行查询没有任何限制，通过它们进行数据修改时的限制也很少。<br>
* 视图是存储在数据库中的查询的sql语句，它主要出于两种原因：安全原因，视图可以隐藏一些数据，如：社会保险基金表，可以用视图只显示姓名，地址，而不显示社会保险号和工资数等，另一原因是可使复杂的查询易于理解和使用。<br>
创建视图<br>
CREATE[ORREPLACE][ALGORITHM={UNDEFINED|MERGE|TEMPTABLE}]VIEWview_name[(column_list)]ASselect_statement<br>
* -视图名必须唯一，同时不能与表重名。<br>
* -视图可以使用select语句查询到的列名，也可以自己指定相应的列名。<br>
* -可以指定视图执行的算法，通过ALGORITHM指定。<br>
* -column_list如果存在，则数目必须等于SELECT语句检索的列数<br>
查看结构<br>
* SHOWCREATEVIEWview_name<br>
删除视图<br>
* -删除视图后，数据依然存在。<br>
* -可同时删除多个视图。<br>
* DROPVIEW[IFEXISTS]view_name...<br>
修改视图结构<br>
* -一般不修改视图，因为不是所有的更新视图都会映射到表上。<br>
* ALTERVIEWview_name[(column_list)]ASselect_statement<br>
视图作用<br>
* 1.简化业务逻辑<br>
* 2.对客户端隐藏真实的表结构<br>
视图算法(ALGORITHM)<br>
* MERGE* 合并<br>
* * 将视图的查询语句，与外部查询需要先合并再执行！<br>
* TEMPTABLE临时表<br>
* * 将视图执行完毕后，形成临时表，再做外层查询！<br>
* UNDEFINED未定义(默认)，指的是MySQL自主去选择相应的算法。<br>
事务(transaction)<br>
事务是指逻辑上的一组操作，组成这组操作的各个单元，要不全成功要不全失败。<br>
* -支持连续SQL的集体成功或集体撤销。<br>
* -事务是数据库在数据晚自习方面的一个功能。<br>
* -需要利用InnoDB或BDB存储引擎，对自动提交的特性支持完成。<br>
* -InnoDB被称为事务安全型引擎。<br>
事务开启<br>
* STARTTRANSACTION;或者BEGIN;<br>
* 开启事务后，所有被执行的SQL语句均被认作当前事务内的SQL语句。<br>
事务提交<br>
* COMMIT;<br>
事务回滚<br>
* ROLLBACK;<br>
* 如果部分操作发生问题，映射到事务开启前。<br>
事务的特性<br>
* 1.原子性（Atomicity）<br>
* * 事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。<br>
* 2.一致性（Consistency）<br>
* * 事务前后数据的完整性必须保持一致。<br>
* * -事务开始和结束时，外部数据一致<br>
* * -在整个事务过程中，操作是连续的<br>
* 3.隔离性（Isolation）<br>
* * 多个用户并发访问数据库时，一个用户的事务不能被其它用户的事物所干扰，多个并发事务之间的数据要相互隔离。<br>
* 4.持久性（Durability）<br>
* * 一个事务一旦被提交，它对数据库中的数据改变就是永久性的。<br>
事务的实现<br>
* 1.要求是事务支持的表类型<br>
* 2.执行一组相关的操作前开启事务<br>
* 3.整组操作完成后，都成功，则提交；如果存在失败，选择回滚，则会回到事务开始的备份点。<br>
事务的原理<br>
* 利用InnoDB的自动提交(autocommit)特性完成。<br>
* 普通的MySQL执行语句后，当前的数据提交操作均可被其他客户端可见。<br>
* 而事务是暂时关闭“自动提交”机制，需要commit提交持久化数据操作。<br>
注意<br>
* 1.数据定义语言（DDL）语句不能被回滚，比如创建或取消数据库的语句，和创建、取消或更改表或存储的子程序的语句。<br>
* 2.事务不能被嵌套<br>
保存点<br>
* SAVEPOINT保存点名称设置一个事务保存点<br>
* ROLLBACKTOSAVEPOINT保存点名称回滚到保存点<br>
* RELEASESAVEPOINT保存点名称删除保存点<br>
InnoDB自动提交特性设置<br>
* SETautocommit=0|1;0表示关闭自动提交，1表示开启自动提交。<br>
* -如果关闭了，那普通操作的结果对其他客户端也不可见，需要commit提交后才能持久化数据操作。<br>
* -也可以关闭自动提交来开启事务。但与STARTTRANSACTION不同的是，<br>
* * SETautocommit是永久改变服务器的设置，直到下次再次修改该设置。(针对当前连接)<br>
* * 而STARTTRANSACTION记录开启前的状态，而一旦事务提交或回滚后就需要再次开启事务。(针对当前事务)<br>
锁表<br>
表锁定只用于防止其它客户端进行不正当地读取和写入<br>
MyISAM支持表锁，InnoDB支持行锁<br>
锁定<br>
* LOCKTABLEStbl_name[ASalias]<br>
解锁<br>
* UNLOCKTABLES<br>
触发器<br>
* 触发程序是与表有关的命名数据库对象，当该表出现特定事件时，将激活该对象<br>
* 监听：记录的增加、修改、删除。<br>
创建触发器<br>
CREATETRIGGERtrigger_nametrigger_timetrigger_eventONtbl_nameFOREACHROWtrigger_stmt<br>
* 参数：<br>
* trigger_time是触发程序的动作时间。它可以是before或after，以指明触发程序是在激活它的语句之前或之后触发。<br>
* trigger_event指明了激活触发程序的语句的类型<br>
* * INSERT：将新行插入表时激活触发程序<br>
* * UPDATE：更改某一行时激活触发程序<br>
* * DELETE：从表中删除某一行时激活触发程序<br>
* tbl_name：监听的表，必须是永久性的表，不能将触发程序与TEMPORARY表或视图关联起来。<br>
* trigger_stmt：当触发程序激活时执行的语句。执行多个语句，可使用BEGIN...END复合语句结构<br>
删除<br>
DROPTRIGGER[schema_name.]trigger_name<br>
可以使用old和new代替旧的和新的数据<br>
* 更新操作，更新前是old，更新后是new.<br>
* 删除操作，只有old.<br>
* 增加操作，只有new.<br>
注意<br>
* 1.对于具有相同触发程序动作时间和事件的给定表，不能有两个触发程序。<br>
字符连接函数<br>
concat(str1,str2,...])<br>
concat_ws(separator,str1,str2,...)<br>
分支语句<br>
if条件then<br>
* 执行语句<br>
elseif条件then<br>
* 执行语句<br>
else<br>
* 执行语句<br>
endif;<br>
修改最外层语句结束符<br>
delimiter自定义结束符号<br>
* SQL语句<br>
自定义结束符号<br>
delimiter;* 修改回原来的分号<br>
语句块包裹<br>
begin<br>
* 语句块<br>
end<br>
特殊的执行<br>
1.只要添加记录，就会触发程序。<br>
2.Insertintoonduplicatekeyupdate语法会触发：<br>
* 如果没有重复记录，会触发beforeinsert,afterinsert;<br>
* 如果有重复记录并更新，会触发beforeinsert,beforeupdate,afterupdate;<br>
* 如果有重复记录但是没有发生更新，则触发beforeinsert,beforeupdate<br>
3.Replace语法如果有记录，则执行beforeinsert,beforedelete,afterdelete,afterinsert<br>
SQL编程<br>
局部变量<br>
变量声明<br>
* declarevar_name[,...]type[defaultvalue]<br>
* 这个语句被用来声明局部变量。要给变量提供一个默认值，请包含一个default子句。值可以被指定为一个表达式，不需要为一个常数。如果没有default子句，初始值为null。<br>
赋值<br>
* 使用set和selectinto语句为变量赋值。<br>
* -注意：在函数内是可以使用全局变量（用户自定义的变量）<br>
全局变量<br>
定义、赋值<br>
set语句可以定义并为变量赋值。<br>
set@var=value;<br>
也可以使用selectinto语句为变量初始化并赋值。这样要求select语句只能返回一行，但是可以是多个字段，就意味着同时为多个变量进行赋值，变量的数量需要与查询的列数一致。<br>
还可以把赋值语句看作一个表达式，通过select执行完成。此时为了避免=被当作关系运算符看待，使用:=代替。（set语句可以使用=和:=）。<br>
select@var:=20;<br>
select@v1:=id,@v2=namefromt1limit1;<br>
selectfromtbl_namewhere@var:=30;<br>
selectinto可以将表中查询获得的数据赋给变量。<br>
* -|selectmax(height)into@max_heightfromtb;<br>
自定义变量名<br>
为了避免select语句中，用户自定义的变量与系统标识符（通常是字段名）冲突，用户自定义变量在变量名前使用@作为开始符号。<br>
@var=10;<br>
* -变量被定义后，在整个会话周期都有效（登录到退出）<br>
控制结构<br>
if语句<br>
ifsearch_conditionthen<br>
* statement_list<br>
[elseifsearch_conditionthen<br>
* statement_list]<br>
...<br>
[else<br>
* statement_list]<br>
endif;<br>
case语句<br>
CASEvalueWHEN[compare-value]THENresult<br>
[WHEN[compare-value]THENresult...]<br>
[ELSEresult]<br>
END<br>
while循环<br>
[begin_label:]whilesearch_conditiondo<br>
* statement_list<br>
endwhile[end_label];<br>
-如果需要在循环内提前终止while循环，则需要使用标签；标签需要成对出现。<br>
* 退出循环<br>
* * 退出整个循环leave<br>
* * 退出当前循环iterate<br>
* * 通过退出的标签决定退出哪个循环<br>
内置函数<br>
数值函数<br>
abs(x)* * 绝对值abs(-10.9)=10<br>
format(x,d)* 格式化千分位数值format(1234567.456,2)=1,234,567.46<br>
ceil(x)* * 向上取整ceil(10.1)=11<br>
floor(x)* * 向下取整floor(10.1)=10<br>
round(x)* * 四舍五入去整<br>
mod(m,n)* * m%nmmodn求余10%3=1<br>
pi()* * * 获得圆周率<br>
pow(m,n)* * m^n<br>
sqrt(x)* * 算术平方根<br>
rand()* * 随机数<br>
truncate(x,d)截取d位小数<br>
时间日期函数<br>
now(),current_timestamp();* 当前日期时间<br>
current_date();* * * * 当前日期<br>
current_time();* * * * 当前时间<br>
date('yyyy-mm-ddhh:ii:ss');* 获取日期部分<br>
time('yyyy-mm-ddhh:ii:ss');* 获取时间部分<br>
date_format('yyyy-mm-ddhh:ii:ss','%d%y%a%d%m%b%j');格式化时间<br>
unix_timestamp();* * * * 获得unix时间戳<br>
from_unixtime();* * * * 从时间戳获得时间<br>
字符串函数<br>
length(string)* * string长度，字节<br>
char_length(string)* string的字符个数<br>
substring(str,position[,length])* 从str的position开始,取length个字符<br>
replace(str,search_str,replace_str)* 在str中用replace_str替换search_str<br>
instr(string,substring)* 返回substring首次在string中出现的位置<br>
concat(string[,...])* 连接字串<br>
charset(str)* * * 返回字串字符集<br>
lcase(string)* * * 转换成小写<br>
left(string,length)* 从string2中的左边起取length个字符<br>
load_file(file_name)* 从文件读取内容<br>
locate(substring,string[,start_position])同instr,但可指定开始位置<br>
lpad(string,length,pad)* 重复用pad加在string开头,直到字串长度为length<br>
ltrim(string)* * * 去除前端空格<br>
repeat(string,count)* 重复count次<br>
rpad(string,length,pad)在str后用pad补充,直到长度为length<br>
rtrim(string)* * * 去除后端空格<br>
strcmp(string1,string2)* 逐字符比较两字串大小<br>
流程函数<br>
casewhen[condition]thenresult[when[condition]thenresult...][elseresult]end多分支<br>
if(expr1,expr2,expr3)双分支。<br>
聚合函数<br>
count()<br>
sum();<br>
max();<br>
min();<br>
avg();<br>
group_concat()<br>
其他常用函数<br>
md5();<br>
default();<br>
存储函数，自定义函数<br>
新建<br>
* CREATEFUNCTIONfunction_name(参数列表)RETURNS返回值类型<br>
* * 函数体<br>
* -函数名，应该合法的标识符，并且不应该与已有的关键字冲突。<br>
* -一个函数应该属于某个数据库，可以使用db_name.funciton_name的形式执行当前函数所属数据库，否则为当前数据库。<br>
* -参数部分，由"参数名"和"参数类型"组成。多个参数用逗号隔开。<br>
* -函数体由多条可用的mysql语句，流程控制，变量声明等语句构成。<br>
* -多条语句应该使用begin...end语句块包含。<br>
* -一定要有return返回值语句。<br>
删除<br>
* DROPFUNCTION[IFEXISTS]function_name;<br>
查看<br>
* SHOWFUNCTIONSTATUSLIKE'partten'<br>
* SHOWCREATEFUNCTIONfunction_name;<br>
修改<br>
* ALTERFUNCTIONfunction_name函数选项<br>
存储过程，自定义功能<br>
定义<br>
存储存储过程是一段代码（过程），存储在数据库中的sql组成。<br>
一个存储过程通常用于完成一段业务逻辑，例如报名，交班费，订单入库等。<br>
而一个函数通常专注与某个功能，视为其他程序服务的，需要在其他语句中调用函数才可以，而存储过程不能被其他调用，是自己执行通过call执行。<br>
创建<br>
CREATEPROCEDUREsp_name(参数列表)<br>
* 过程体<br>
参数列表：不同于函数的参数列表，需要指明参数类型<br>
IN，表示输入型<br>
OUT，表示输出型<br>
INOUT，表示混合型<br>
注意，没有返回值。<br>
存储过程<br>
存储过程是一段可执行性代码的集合。相比函数，更偏向于业务逻辑。<br>
调用：CALL过程名<br>
注意<br>
-没有返回值。<br>
-只能单独调用，不可夹杂在其他语句中<br>
参数<br>
IN|OUT|INOUT参数名数据类型<br>
IN* 输入：在调用过程中，将数据输入到过程体内部的参数<br>
OUT* 输出：在调用过程中，将过程体处理完的结果返回到客户端<br>
INOUT输入输出：既可输入，也可输出<br>
语法<br>
CREATEPROCEDURE过程名(参数列表)<br>
BEGIN<br>
* 过程体<br>
END<br>
用户和权限管理<br>
root密码重置<br>
1.停止MySQL服务<br>
2.[Linux]usrlocalmysqlbinsafe_mysqldskip-grant-tables&<br>
* [Windows]mysqldskip-grant-tables<br>
3.usemysql;<br>
4.UPDATE`user`SETPASSWORD=PASSWORD("密码")WHERE`user`="root";<br>
5.FLUSHPRIVILEGES;<br>
用户信息表：mysql.user<br>
刷新权限<br>
FLUSHPRIVILEGES;<br>
增加用户<br>
CREATEUSER用户名IDENTIFIEDBY[PASSWORD]密码(字符串)<br>
* -必须拥有mysql数据库的全局CREATEUSER权限，或拥有INSERT权限。<br>
* -只能创建用户，不能赋予权限。<br>
* -用户名，注意引号：如'user_name'@'192.168.1.1'<br>
* -密码也需引号，纯数字密码也要加引号<br>
* -要在纯文本中指定密码，需忽略PASSWORD关键词。要把密码指定为由PASSWORD()函数返回的混编值，需包含关键字PASSWORD<br>
重命名用户<br>
RENAMEUSERold_userTOnew_user<br>
设置密码<br>
SETPASSWORD=PASSWORD('密码')为当前用户设置密码<br>
SETPASSWORDFOR用户名=PASSWORD('密码')为指定用户设置密码<br>
删除用户<br>
DROPUSER用户名<br>
分配权限添加用户<br>
GRANT权限列表ON表名TO用户名[IDENTIFIEDBY[PASSWORD]'password']<br>
* -allprivileges表示所有权限<br>
* -.表示所有库的所有表<br>
* -库名.表名表示某库下面的某表<br>
* GRANTALLPRIVILEGESON`pms`.TO'pms'@'%'IDENTIFIEDBY'pms0817';<br>
查看权限<br>
SHOWGRANTSFOR用户名<br>
* 查看当前用户权限<br>
* SHOWGRANTS;或SHOWGRANTSFORCURRENT_USER;或SHOWGRANTSFORCURRENT_USER();<br>
撤消权限<br>
REVOKE权限列表ON表名FROM用户名<br>
REVOKEALLPRIVILEGES,GRANTOPTIONFROM用户名* 撤销所有权限<br>
权限层级<br>
要使用GRANT或REVOKE，您必须拥有GRANTOPTION权限，并且您必须用于您正在授予或撤销的权限。<br>
全局层级：全局权限适用于一个给定服务器中的所有数据库，mysql.user<br>
* GRANTALLON.和REVOKEALLON.只授予和撤销全局权限。<br>
数据库层级：数据库权限适用于一个给定数据库中的所有目标，mysql.db,mysql.host<br>
* GRANTALLONdb_name.和REVOKEALLONdb_name.只授予和撤销数据库权限。<br>
表层级：表权限适用于一个给定表中的所有列，mysql.talbes_priv<br>
* GRANTALLONdb_name.tbl_name和REVOKEALLONdb_name.tbl_name只授予和撤销表权限。<br>
列层级：列权限适用于一个给定表中的单一列，mysql.columns_priv<br>
* 当使用REVOKE时，您必须指定与被授权列相同的列。<br>
权限列表<br>
ALL[PRIVILEGES]* 设置除GRANTOPTION之外的所有简单权限<br>
ALTER* 允许使用ALTERTABLE<br>
ALTERROUTINE* 更改或取消已存储的子程序<br>
CREATE允许使用CREATETABLE<br>
CREATEROUTINE创建已存储的子程序<br>
CREATETEMPORARYTABLES* 允许使用CREATETEMPORARYTABLE<br>
CREATEUSER* 允许使用CREATEUSER,DROPUSER,RENAMEUSER和REVOKEALLPRIVILEGES。<br>
CREATEVIEW* 允许使用CREATEVIEW<br>
DELETE允许使用DELETE<br>
DROP* 允许使用DROPTABLE<br>
EXECUTE* 允许用户运行已存储的子程序<br>
FILE* 允许使用SELECT...INTOOUTFILE和LOADDATAINFILE<br>
INDEX* 允许使用CREATEINDEX和DROPINDEX<br>
INSERT允许使用INSERT<br>
LOCKTABLES* 允许对您拥有SELECT权限的表使用LOCKTABLES<br>
PROCESS* 允许使用SHOWFULLPROCESSLIST<br>
REFERENCES未被实施<br>
RELOAD允许使用FLUSH<br>
REPLICATIONCLIENT允许用户询问从属服务器或主服务器的地址<br>
REPLICATIONSLAVE* 用于复制型从属服务器（从主服务器中读取二进制日志事件）<br>
SELECT允许使用SELECT<br>
SHOWDATABASES显示所有数据库<br>
SHOWVIEW* 允许使用SHOWCREATEVIEW<br>
SHUTDOWN* 允许使用mysqladminshutdown<br>
SUPER* 允许使用CHANGEMASTER,KILL,PURGEMASTERLOGS和SETGLOBAL语句，mysqladmindebug命令；允许您连接（一次），即使已达到max_connections。<br>
UPDATE允许使用UPDATE<br>
USAGE* “无权限”的同义词<br>
GRANTOPTION* 允许授予权限<br>
表维护<br>
分析和存储表的关键字分布<br>
ANALYZE[LOCAL|NO_WRITE_TO_BINLOG]TABLE表名...<br>
检查一个或多个表是否有错误<br>
CHECKTABLEtbl_name[,tbl_name]...[option]...<br>
option={QUICK|FAST|MEDIUM|EXTENDED|CHANGED}<br>
整理数据文件的碎片<br>
OPTIMIZE[LOCAL|NO_WRITE_TO_BINLOG]TABLEtbl_name[,tbl_name]...<br>
杂项<br>
1.可用反引号（`）为标识符（库名、表名、字段名、索引、别名）包裹，以避免与关键字重名！中文也可以作为标识符！<br>
2.每个库目录存在一个保存当前数据库的选项文件db.opt。<br>
3.注释：<br>
* 单行注释#注释内容<br>
* 多行注释注释内容<br>
* 单行注释注释内容* (标准SQL注释风格，要求双破折号后加一空格符（空格、TAB、换行等）)<br>
4.模式通配符：<br>
* _任意单个字符<br>
* %任意多个字符，甚至包括零字符<br>
* 单引号需要进行转义\'<br>
5.CMD命令行内的语句结束符可以为";","\G","\g"，仅影响显示结果。其他地方还是用分号结束。delimiter可修改当前对话的语句结束符。<br>
6.SQL对大小写不敏感<br>
7.清除已有语句：\c<br>