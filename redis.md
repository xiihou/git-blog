doc 环境下使用命令：<br>
 <br>
    keys 命令<br>
        ?    匹配一个字符<br>
        *    匹配任意个（包括0个）字符<br>
        []    匹配括号间的任一个字符，可以使用 "-" 符号表示一个范围，如 a[b-d] 可以匹配 "ab","ac","ad"<br>
        \x    匹配字符x，用于转义符号，如果要匹配 "?" 就需要使用 \?<br>
 <br>
    判断一个键值是否存在<br>
        exists key<br>
        如果存在，返回整数类型 1 ，否则返回 0<br>
 <br>
    删除键<br>
        del key [key.....]<br>
        可以删除一个或多个键，返回值是删除的键的个数<br>
        注意：不支持通配符删除<br>
 <br>
    获得键值的数据类型<br>
        type key<br>
        返回值可能是 string(字符串类型) hash(散列类型) list(列表类型) set(集合类型) zset(有序集合类型)<br>
 <br>
 <br>
    赋值与取值<br>
        set key value       赋值<br>
        get key                取值<br>
    <br>
    递增数字<br>
        incr key<br>
        当存储的字符串是整数形式时，redis提供了一个使用的命令 incr 作用是让当前的键值递增，并返回递增后的值<br>
        incr num<br>
        当要操作的键不存在时会默认键值为 0  ，所以第一次递增后的结果是 1 ，当键值不是整数时 redis会提示错误<br>
 <br>
    增加指定的整数<br>
        incrby key increment<br>
        incrby 命令与 incr 命令基本一样，只不过前者可以通过 increment 参数指定一次增加的数值如：<br>
            incrby num 2<br>
            incrby num 3<br>
 <br>
    减少指定的整数<br>
        decr key<br>
        decrby key increment<br>
        desc 命令与incr 命令用法相同，只不过是让键值递减<br>
        decrby 命令与 incrby命令用法相同<br>
 <br>
    增加指定浮点数<br>
        incrbyfloat key increment<br>
        incrbyfloat 命令类似 incrby 命令，差别是前者可以递增一个双精度浮点数，如：<br>
        incrbyfloat num 2.7<br>
        注意： ( 受reids 版本限制，版本需要大于 2.6 版本) <br>
 <br>
    向尾部追加值<br>
        append key value<br>
        作用是向键值的末尾追加 value ，如果键不存在则将改键的值设置为 value，即相当于 set key value。返回值是追加后字符串的长度<br>
        如：append foo " hello word!"<br>
 <br>
    获取字符串长度<br>
        strlen key<br>
        返回键值的长度，如果键不存在则返回0<br>
 <br>
    同时 获得/设置 多个键值<br>
        mget key [key.....]<br>
        mset key value [key value .......]<br>
 <br>
    位操作<br>
        getbit key offset<br>
        setbit key offset value<br>
        bitcount key [strart] [end]<br>
        bitop operation destkey key [key .....]<br>
        一个字节由8个二进制位组成，redis 提供了4个命令直接对二进制位进行操作<br>
        getbit 命令可以获得一个字符串类型键指定位置的二进制位的值（0 或 1），索引从 0 开始，如果需要获取的二进制位的索引超出了键值<br>
            的二进制位的实际长度则默认位值是 0<br>
        setbit 命令可以设置字符串类型键指定位置的二进制位的值，返回值是该位置的旧值，如果需要设置的位置超过了键值的二进制位的长<br>
            度，setbit 命令会自动将中间的二进制位设置为0，同理设置一个不存在的键的指定二进制位的值会自动将其前面的位赋值为 0<br>
        bitcount 命令可以获得字符串类型键中值是1的二进制位个数，可以通过参数来限制统计的字节范围，如我们希望统计前两个字节(即 <br>
            "aa")  命令：bitcount foo 0 1    注意： ( 受reids 版本限制，版本需要大于 2.6 版本) <br>
        bittop 命令可以对多个字符串类型键进行位运算，并将结果存储在destkey参数指定的键中。该命令支持的运算操作有 AND、 OR、  <br>
            XOR、 NOT，<br>
            如我们对bar 和 aar 进行 OR 运算操作： <br>
            set foo1 bar<br>
            set foo2 aar<br>
            bitop OR res foo1 foo2<br>
            get res<br>
            注： ( 受reids 版本限制，版本需要大于 2.6 版本) <br>
        <br>
        <br>
    散列类型<br>
      <br>
    赋值与取值<br>
        hset key field value<br>
        hget key field<br>
        hmset key field value [ field value ...... ]<br>
        hmget key field [ field ...... ]<br>
        hgetall key<br>
        hset 命令用来给字段赋值，而hget命令用来获得字段的值<br>
        hset 命令的方便之处在于不区分插入和更新操作，这意味着修改数据时不用事先判断字段是否存在来决定要执行的是插入操作还是更新操<br>
            作，当执行的是插入操作时， hset 命令返回 1 ，当执行的是更新操作时，hset 命令返回的是 0 ，当键本身不存在时， hset 命令还会<br>
            自动建立他<br>
        hmset 设置多个键值<br>
        hmget 获得多个键值<br>
        hgetall 获取键中所有字段和字段值却不知道键中有哪些字段时使用，返回的结果是字段和字段值组成的列表<br>
 <br>
    判断字段是否存在<br>
        hexists key field<br>
        存在返回 1 ，否则返回 0<br>
    <br>
    当字段不存在时赋值<br>
        hsetnx key field value<br>
        hsetnx 命令与hset 命令类似，区别在于如果字段已经存在，hsetnx 命令将不执行任何操作<br>
        <br>
    增加数字<br>
        hincrby key field increment<br>
        使字段值增加指定的整数<br>
 <br>
    删除字段<br>
        hdel key field [ field .....]<br>
        删除一个或多个字段，返回值是被删除的字段个数<br>
 <br>
    只获取字段名或字段值<br>
        hkeys key<br>
        hvals key<br>
        hkeys 获取所有字段的名字<br>
        hvals 获得键中所有字段的值<br>
 <br>
    获得字段数量<br>
        hlen key<br>
 <br>
 <br>
列表类型<br>
    <br>
    向列表两端增加元素<br>
        lpush key value [ value ....... ]<br>
        rpush key value [ value ....... ]<br>
        lpush 命令用来向列表左边增加元素，返回表示增加元素后列表的长度 <br>
        rpush 命令用来向列表右边增加元素，返回表示增加元素后列表的长度 <br>
        <br>
    从列表两端弹出元素<br>
        lpop key<br>
        rpop key<br>
        lpop 命令可以从列表左边弹出一个元素，lpop 命令执行两步操作，1：将列表左边的元素从列表中移除，2：返回被移除元素值<br>
        rpop 命令可以从列表右边弹出一个元素<br>
 <br>
    获取列表中元素个数<br>
        llen key<br>
        当键不存在时，llen 返回 0<br>
 <br>
    获得列表片段<br>
        lrange key start stop<br>
        获得列表中的某一片段，返回索引从 start 到 stop 之间的所有元素（包括两端的元素） 索引开始为 0<br>
        注：lrange 与很多语言中用来截取数组片段的方法有一点区别是 lrange 返回的值包含最右边的元素<br>
               lrange 命令也支持负索引，表是从右边开始计算序数，如 ' -1 ' 表示最右边第一个元素， ' -2 ' 表示最右边第二个元素，一次类推<br>
 <br>
    删除列表中指定的值<br>
        lrem key count value<br>
        lrem 命令会删除列表中前 count 个值为 value 的元素，返回值是实际删除的元素个数。根据count 值的不同，lrem 命令执行的方式会<br>
            略有差异<br>
            当 count > 0 时，lrem 命令会从列表左边开始删除前 count 个值为 value 的元素<br>
            当 count < 0 时，lrem 命令会从列表右边开始删除前count 个值为 value 的元素<br>
            当 count = 0 时，lrem 命令会删除所有值为value的元素<br>
 <br>
    获得 / 设置 指定索引的元素值<br>
        lindex key index<br>
        lset key index value<br>
        lindex 命令用来返回指定索引的元素，索引从 0 开始 ，如果 index 是负数则表示从右边开始计算的索引，最右边元素的索引是 -1 <br>
        lset 是通过索引操作列表的命令，它会将索引为 index 的元素赋值为 value <br>
 <br>
    只保留列表指定片段<br>
        ltrim key start end<br>
        ltrim 命令可以删除指定索引范围之外的所有元素，其指定列表范围的方法和 lrange 命令相同<br>
        ltrim 命令常和 lpush 命令一起使用来限制列表中元素的数量，比如记录日志时我们希望只保留最近的 100 条日志，则每次加入新元素时<br>
            调用一次ltrim 命令即可；<br>
 <br>
    向列表中插入元素<br>
        linsert key before | after pivot value<br>
        linsert 命令首先会在列表中从左到右查找值为 pivot 的元素，然后根据第二个参数是 before 还是 after 来决定将 value 插入到该元素的<br>
            前面还是后面,如果命令执行成功，返回插入操作完成之后列表的长度。如果没有找到 pivot 返回 -1 如果key 不存在或为空，返回 0<br>
            <br>
    将元素从一个列表转到另一个列表R<br>
        rpoplpush source destination<br>
        rpoplpush 先执行 rpop 命令在执行 lpush 命令。rpoplpush 命令先会从source 列表类型键的右边弹出一个元素，然后将其加入到 destination 列表类型键的左边，并返回这个元素的值，整个过程是原子的<br>
 <br>
 <br>
 <br>
集合类型<br>
    增加删除命令<br>
        sadd key member [ member .... ]<br>
        srem key member [ member .... ]<br>
        sadd 命令用来向集合中增加一个或多个元素，如果键不存在则会自动创建。因为在一个集合中不能有相同的元素，所以如果要加入的元<br>
            素已经存在与集合中就会忽略这个元素。返回值是成功加入的元素数量（忽略的元素不计算在内）<br>
        srem 命令用来从集合中删除一个或多个元素，并返回删除成功的个数<br>
 <br>
    获得集合中的所有元素<br>
        smembers key<br>
        返回集合中的所有元素<br>
 <br>
    判断元素是否在集合中<br>
        sismember key member<br>
        判断一个元素是否在集合中是一个时间复杂度为 0(1) 的操作，无论集合中有多少个元素， sismember 命令始终可以极快的返回结果。当<br>
            值存在时 sismember 命令返回 1 ，当值不存在或者键不存在时返回 0<br>
 <br>
    集合间运算<br>
        sdiff key [ key ...... ]<br>
        sdiff 命令用来对多个集合执行差集运算。集合 A 与集合 B 的差集表示为 A- B ，代表所有属于 A 且不属于 B 的元素构成的集合,即 <br>
            A - B = { x| x∈A  且 x ∈/B }<br>
            <br>
        命令使用方法：<br>
               sadd seta 1 2 3 4 6 7 8<br>
                sadd setb 2 3 4<br>
                sdiff seta setb<br>
        该命令支持同时传入多个键, 计算顺序是先计算 seta 和 setb 在计算结果与 setc 的差集<br>
                sadd setc 2 3 4<br>
                sdiff seta setb setc<br>
        <br>
        sinter key [ key ..... ]<br>
        该命令用来对多个集合执行交集运算。集合 A 与集合 B 的交集表示为 A∩B，代表所有属于 A 且属于 B 的元素构成的集合<br>
            即 A∩B = { x| x∈A  且 x ∈B }<br>
            <br>
            命令使用方法：<br>
                sinter seta setb<br>
                该命令同样支持同时传入多个键<br>
 <br>
        sunion key [ key ...... ]<br>
        该命令用来对多个集合执行并集运算。集合 A 与集合 B的并集表示为 A∪B ，代表所有属于A或所有属于B的元素构成的集合<br>
            即  A∪B = { x| x∈A  或 x ∈B }<br>
            <br>
            命令使用方法：<br>
                sunion seta setb<br>
                该命令同样支持同时传入多个键<br>
 <br>
        获得集合中元素的个数<br>
            scard key<br>
            <br>
        进行集合运算并将结果存储<br>
            sdiffstore destination key [ key ...... ]<br>
            sinterstore destination key [ key ...... ]<br>
            sunionstore destination key [ key ...... ]<br>
            sdiffstore 命令和 sdiff 命令功能一样，唯一的区别就是前者不会直接返回运算的结果，而是将结果存在 destination 键中<br>
            sinterstore 这个命令类似于 sinter 命令，但它将结果保存到 destination 集合，而不是简单地返回结果集。<br>
            sunionstore 这个命令类似于 sunion 命令，但它将结果保存到 destination 集合，而不是简单地返回结果集。<br>
 <br>
        随机获得集合中的元素<br>
            srandmember key [ count ]<br>
            该命令用来随机从集合中获取一个元素<br>
            还可以传递 count 参数来一次随机获得多个元素，根据 count 的正负不同，具体表现也不同<br>
                当count 为正数时，srandmember 会随机获取从集合里获得 count 个不重复的元素。如果 count 的值大于集合中的元素个数，则 <br>
                    srandmember 会返回集合中的全部元素<br>
                当 count 为负数时，srandmember 会随机从集合中获得 |count| 个的元素，这些元素有可能相同<br>
            注：当传递count 参数时，在windows环境下提示命令参数错误<br>
 <br>
        从集合中弹出一个元素<br>
            spop key<br>
            由于集合类型的元素是无序的，所以 spop 命令会从集合中随机选择一个元素弹出，返回值为被移除的随机元素，如果 key 不存在或者 <br>
                key 为空集时，返回 nil<br>
 <br>
 <br>
有序集合类型（sorted set）<br>
        增加元素<br>
            zadd key score member [ score member ...... ]<br>
            zadd 命令用来向有序集合中加入一个元素和该元素的分数，如果该元素已经存在，则会用新的分数替换原有的分数。zadd命令的返回<br>
                值是新加入到集合中的元素个数（不包含之前已经存在的元素）<br>
 <br>
        获得元素的分数<br>
            zscore key member<br>
            <br>
        获得排名在某个范围的元素列表<br>
            zrange key start stop [ withscores ]<br>
            zrevrange key start stop [ withscores ]<br>
            zrange 命令会按照元素分数从小到大的顺序返回索引从 start 到 stop 之间的所有元素（包含两端的元素）。zrange 命令和 lrange 命<br>
                令十分相似，如索引都是从0开始，负数代表从后向前查找（-1 表示最后一个元素）。如果需要同时获得元素的分数的话，可以在 <br>
                 zrange 命令的尾部加上 widthscores 参数<br>
            注：如果两个元素的分数相同，redis会按照字典顺序（即 0<9<A<Z<a<z 这样的顺序）来进行排列。如果元素的值是中文，则取决于<br>
                   中文的编码方式，如图：<br>
                    <br>
            zrevrange 命令和 zrange 的唯一不同在于 zrevrange 是按照元素分数从大到小的顺序给定结果的<br>
           <br>
        获得指定分数范围内的元素<br>
            zrangebyscore key min max [ withscores ] [ limit offset count ]<br>
            该命令按照元素分数从小到大的顺序返回分数在 min 到 max 之间（包含 min 和max 的元素）<br>
            如果希望分数范围不包含端点值，可以在分数前加上 "(" 符号，例如：希望返回80分到100分的的数据，可以包含80分单不包含100分<br>
                命令：zrangebyscore scoreboard 80 (100 widthscores<br>
                <br>
                min 和 max 还支持无穷大，同 zadd 命令一样，-inf 和 +inf 分别表示负无穷大和正无穷大。比如希望得到所有分数高于 80分（不<br>
                包含80分）的人的名单，但是却不知道最高分是多少，这是就可以使用 +inf<br>
                zrangebyscore scoreboard (80 +inf<br>
                <br>
                命令 limit offset count 与 SQL 中的用法基本相同，即在获得的元素列表的基础上向后偏移 offset 个元素并且只获取前count个元<br>
                素<br>
                <br>
                <br>
                zrevrangebyscore 不仅是按照元素分数从大往小的顺序给出结果，而且他的 min 和max 的参数的顺序和 zrangebyscore 命令是相<br>
                反的<br>
                <br>
 <br>
        增加某个元素的分数<br>
            zincrby key increment member<br>
            zincrby 命令可以增加一个元素的分数，返回值是更改后的分数，例如想给peter 加 4 分<br>
               zincrby scoreborder 4 peter<br>
               increment  也可以是负数表示减分<br>
                 zincrby scoreborder -4 peter<br>
            如果指定元素不存在，redis 在执行命令前会先建立它并将他的值赋为0在执行操作        <br>
 <br>
        获得集合中元素的数量<br>
            zcard key<br>
        获得指定分数范围内的元素个数<br>
            zcount key min max<br>
            zcount 命令的 min max 参数的特性与 zrangebyscore 命令中的一样<br>
            <br>
 <br>
        删除一个或多个元素<br>
            zrem key member [ member .... ]<br>
            zrem 命令的返回值是成功删除的元素数量（不包含本来就不存在的元素）<br>
 <br>
        按照排名范围删除元素<br>
            zremrangebyrank key start stop<br>
            按照元素分数从小到大的顺序（即索引 0 表示最小的值）删除在指定排名范围内的所有元素，并返回删除元素的数量<br>
            <br>
 <br>
        按照分数范围删除元素<br>
            zremrangebyscore key min max<br>
            zremrangebyscore 命令删除指定分数范围内的所有元素，参数 min 和 max 的特性和 zrangebyscore 命令中的一样，返回值是删除<br>
                元素的个数<br>
            <br>
 <br>
        获得元素的排名<br>
            zrank key member<br>
            zrevrank key member<br>
            zrank 命令会按照元素分数从小到大的顺序获得指定的元素排名（从 0 开始，即分数最小的元素排名为0）<br>
            <br>
            zrebrank 命令则正好相反，分数最大的元素排名为0<br>
 <br>
        计算有序集合的交集<br>
            zinterstore destination numkeys key [ key ... ] [ weights weight [ weight ... ] ] [ aggregate SUM | MIN | MAX ]<br>
            zinterstore 命令用来计算多个有序集合的交集病将结果存储在 destination 键中（同样以有序集合类型存储），返回值为 destination <br>
                键中元素的个数，destination 键中元素的分数是由 aggregate 参数决定的<br>
            1. 当 aggregate 是 SUM （也就是默认值），destination 键中元素的分数是每个参与计算的集合中该元素分数的和<br>
                <br>
            2.当 aggregate 是 MIN 时，destination 键中元素的分数是参与计算的集合中该元素分数最小值<br>
                <br>
            3.当 aggregate 是 MAX 是，destination 键中元素的分数是参与计算的集合中该元素分数最大值<br>
         <br>
          zinterstore 命令还能通过 weights 参数设置每个集合的权重，每个集合在参与计算时元素的分数会被乘上该集合的权重<br>
            如：<br>
                <br>
 <br>
        计算集合间的并集<br>
            zunionstore <br>
            用法与 zinterstore 命令的用法一样<br>
 <br>
 <br>
事务<br>
        事务的原理是先将属于一个事务的命令发送给redis ，然后再让 redis 依次执行这些命令<br>
        <br>
            <br>
        错误处理<br>
        （1）语法错误。语法错误指命令不存在或者命令参数个数不对。这种情况下，事务中只要有一个命令有语法错误，执行exec命令后redis<br>
                就会直接返回错误，连语法正确的命令也不会执行<br>
                注：redis 2.6.5 之前的版本会忽略有语法错误的命令，然后执行事务中其他语法正确的命令。<br>
        （2）运行错误。运行错误指在命令执行时出现的错误，比如使用散列类型的命令操作集合类型的键，这种错误在实际执行之前redis是无<br>
                法发现的，所以在事务里这样的命令是会被redis接受并执行的，如果事务里的一条命令出现运行错误，事务里其他的命令依然会继<br>
                续执行（包含出错命令之后的命令）<br>
 <br>
        reids的事务没有关系数据库事务提供的回滚功能，为此开发者必须在事务执行出错之后自己收拾剩下的摊子<br>
        <br>
    watch 命令<br>
        watch key [ key ... ]<br>
        监视一个或多个 key ，如果在事务执行之前这个或这些 key 被其他命令所改动，那么事务将被打断，监控一直持续到exec命令<br>
        <br>
 <br>
    unwatch<br>
        取消 watch 命令对所有 key 的监视<br>
 <br>
    <br>
    生存时间<br>
        expire<br>
        expire 命令的使用方法为 expire key seconds ，其中 seconds 参数表示键的生存时间，单位是秒，该参数必须是整数<br>
        <br>
        命令返回 1表示设置成功，返回 0 则表示键不存在或设置失败<br>
 <br>
        如果想知道一个键还有多久会被删除，可以使用 ttl 命令。返回值是键的剩余时间（单位是秒），<br>
        <br>
        如果想取消键的生存时间设置(即将键恢复成为永久的)，可以使用 persist 命令。如果生存时间被成功清除则返回 1 。否则返回 0<br>
        <br>
        <br>
        除了 persist 命令之外，使用 set 、getset 命令为键赋值也同时会清楚键的生存时间<br>
        注： incr 、lpush、hset、zrem 命令均不会影像键的生存时间<br>
 <br>
        精确控制键的生存时间应该使用 pexpire 命令。该命令的单位是毫秒<br>
        可以使用 pttl 命令以毫秒为单位返回键的剩余时间<br>
        另外不太常用命令：expireat 和 pexpireat，该命令第二个参数表示键的生存时间的截至时间，expireat 单位秒 pexpireat 单位毫秒<br>
 <br>
    sort <br>
        该命令可以对列表类型，集合类型，和有序集合类型键进行排序<br>
        列表类型：<br>
        <br>
        <br>
        有序集合类型排序时，会忽略元素的分数，只针对元素的自身的值进行排序<br>
        <br>
        <br>
        除了可以排列数字外，sort 命令还可以通过 alpha 参数实现按照字典顺序排列非数字元素<br>
        <br>
 <br>
        sort 命令的 desc 参数可以实现将元素按照从大到小的顺序排列<br>
        sort 命令还支持 limit 参数来返回指定范围的结果，用法和sql 语句一样 limit offset count ，表示跳过前 offset 个元素并获取之后的<br>
            count 个元素<br>
        <br>
 <br>
        sort 命令 by 参数，默认情况下， sort uid 直接按照 uid 中的值排序，通过 by 参数，可以让 uid 按照其他键的元素来排序<br>
        <br>
        user_level_* 是一个占位符，他先取出 uid 中的值，然后在用这个值来查找相应的键<br>
            比如在对 uid 列表进行排序时， 程序就会先取出 uid 的值 1 、 2 、 3 、 4 ， 然后使用 user_level_1 、 user_level_2 、 user_level_3 <br>
            和   user_level_4 的值作为排序 uid 的权重。<br>
 <br>
        使用 get 选项，可以根据排序的结果来取出相应的键值<br>
        <br>
        <br>
        一个sort 命令中可以有多个 get 参数（而 by 参数只能有一个）<br>
        <br>
 <br>
        默认情况下 sort 命令会直接返回排序结果，如果希望保存排序结果，可以使用 store 参数,保存后键的类型为列表类型<br>